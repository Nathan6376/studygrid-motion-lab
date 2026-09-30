#!/usr/bin/env python3
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple

class State(str, Enum):
    NEW='NEW'; MOUNTED='MOUNTED'; REDUCED_MOTION='REDUCED_MOTION'
    LOADING='LOADING'; SLOW_LOAD='SLOW_LOAD'; READY='READY'; RUNNING='RUNNING'
    FAILED='FAILED'; FALLBACK_STATIC='FALLBACK_STATIC'; SKIPPED='SKIPPED'
    HANDOFF_READY='HANDOFF_READY'; SHELL_READY='SHELL_READY'; DISPOSED='DISPOSED'

class Event(str, Enum):
    MOUNT='MOUNT'
    REDUCED_MOTION_SELECTED='REDUCED_MOTION_SELECTED'
    CAPABILITY_FAILURE='CAPABILITY_FAILURE'
    LOAD_BEGIN='LOAD_BEGIN'
    SLOW_LOAD_THRESHOLD='SLOW_LOAD_THRESHOLD'
    ASSETS_READY='ASSETS_READY'
    FAILURE='FAILURE'
    START='START'
    SKIP='SKIP'
    COMPLETE='COMPLETE'
    FALLBACK='FALLBACK'
    SHELL_HANDOFF='SHELL_HANDOFF'
    DISPOSE='DISPOSE'

class TransitionError(RuntimeError):
    pass

CANONICAL_STATES=tuple(s.value for s in State)
CANONICAL_EVENTS=tuple(e.value for e in Event)

_TRANSITION_ROWS = (
    ((State.NEW,), Event.MOUNT, State.MOUNTED),
    ((State.MOUNTED,), Event.REDUCED_MOTION_SELECTED, State.REDUCED_MOTION),
    ((State.MOUNTED,), Event.CAPABILITY_FAILURE, State.FAILED),
    ((State.MOUNTED,), Event.LOAD_BEGIN, State.LOADING),
    ((State.LOADING,), Event.SLOW_LOAD_THRESHOLD, State.SLOW_LOAD),
    ((State.LOADING,State.SLOW_LOAD), Event.ASSETS_READY, State.READY),
    ((State.LOADING,State.SLOW_LOAD,State.READY,State.RUNNING), Event.FAILURE, State.FAILED),
    ((State.READY,), Event.START, State.RUNNING),
    ((State.LOADING,State.SLOW_LOAD,State.READY,State.RUNNING), Event.SKIP, State.SKIPPED),
    ((State.RUNNING,), Event.COMPLETE, State.HANDOFF_READY),
    ((State.REDUCED_MOTION,State.FAILED), Event.FALLBACK, State.FALLBACK_STATIC),
    ((State.FALLBACK_STATIC,State.SKIPPED,State.HANDOFF_READY), Event.SHELL_HANDOFF, State.SHELL_READY),
    ((State.MOUNTED,State.REDUCED_MOTION,State.LOADING,State.SLOW_LOAD,State.READY,State.RUNNING,
      State.FAILED,State.FALLBACK_STATIC,State.SKIPPED,State.HANDOFF_READY,State.SHELL_READY),
     Event.DISPOSE, State.DISPOSED),
)

ALLOWED_TRANSITIONS: Dict[Tuple[State,Event],State] = {
    (source,event): target
    for sources,event,target in _TRANSITION_ROWS
    for source in sources
}

@dataclass
class MotionFallbackHarness:
    viewport: Tuple[int,int]=(1440,900)
    lens_mm: float=50.0
    reduced_motion: bool=False
    app_less_motion: bool=False
    webgl_available: bool=True
    slow_threshold_ms: int=1500
    hard_timeout_ms: int=5000
    state: State=State.NEW
    history: List[str]=field(default_factory=list)
    event_history: List[str]=field(default_factory=list)
    renderer_initialised: bool=False
    assets_requested: bool=False
    focus_token: Optional[str]=None
    failure_reason: Optional[str]=None

    def _transition(self, event: Event, target: Optional[State]=None):
        key=(self.state,event)
        expected=ALLOWED_TRANSITIONS.get(key)
        if expected is None:
            raise TransitionError(f'invalid transition: {self.state.value} --{event.value}--> ?')
        if target is not None and target != expected:
            raise TransitionError(
                f'target mismatch: {self.state.value} --{event.value}--> '
                f'{target.value}, expected {expected.value}'
            )
        self.state=expected
        self.event_history.append(event.value)
        self.history.append(expected.value)
        return expected

    @property
    def aspect(self):
        w,h=self.viewport
        return w/h

    @property
    def layout_box(self):
        return {'width':self.viewport[0],'height':self.viewport[1],'min_height':'100vh'}

    @property
    def escape_control_available(self):
        return self.state in {State.LOADING,State.SLOW_LOAD,State.READY,State.RUNNING}

    @property
    def shell_ready(self):
        return self.state==State.SHELL_READY

    def _fallback_to_shell(self):
        self._transition(Event.FALLBACK)
        self._transition(Event.SHELL_HANDOFF)

    def mount(self, focus_token='existing-welcome-focus'):
        if self.state != State.NEW:
            raise TransitionError('mount must start from NEW')
        self.focus_token=focus_token
        self._transition(Event.MOUNT)
        if self.reduced_motion or self.app_less_motion:
            self._transition(Event.REDUCED_MOTION_SELECTED)
            self._fallback_to_shell()
            return
        if not self.webgl_available:
            self.failure_reason='WEBGL_UNAVAILABLE'
            self._transition(Event.CAPABILITY_FAILURE)
            self._fallback_to_shell()
            return
        self.renderer_initialised=True
        self.assets_requested=True
        self._transition(Event.LOAD_BEGIN)

    def tick(self, elapsed_ms:int):
        if self.state==State.LOADING and elapsed_ms>=self.slow_threshold_ms:
            self._transition(Event.SLOW_LOAD_THRESHOLD)
        if self.state in {State.LOADING,State.SLOW_LOAD} and elapsed_ms>=self.hard_timeout_ms:
            self.fail('HARD_TIMEOUT')

    def asset_ready(self):
        self._transition(Event.ASSETS_READY)

    def fail(self, reason='RUNTIME_FAILURE'):
        if self.state in {State.DISPOSED,State.SHELL_READY}:
            return
        self.failure_reason=reason
        self._transition(Event.FAILURE)
        self._fallback_to_shell()

    def asset_fail(self, reason='ASSET_FAILURE'):
        self.fail(reason)

    def start(self):
        self._transition(Event.START)

    def skip(self, reason='USER_CONTINUE'):
        if self.state in {State.DISPOSED,State.SHELL_READY}:
            return
        self._transition(Event.SKIP)
        self._transition(Event.SHELL_HANDOFF)

    def complete(self):
        self._transition(Event.COMPLETE)
        self._transition(Event.SHELL_HANDOFF)

    def resize(self,width:int,height:int):
        if width<=0 or height<=0:
            raise ValueError('positive viewport required')
        self.viewport=(width,height)
        # lens_mm deliberately unchanged; aspect derives from host box.

    def dispose(self):
        if self.state==State.DISPOSED:
            return
        self._transition(Event.DISPOSE)
        self.renderer_initialised=False
        self.assets_requested=False

    def assert_no_dead_end(self):
        if self.state==State.DISPOSED:
            return True
        return self.shell_ready or self.escape_control_available
