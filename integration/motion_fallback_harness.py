#!/usr/bin/env python3
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Tuple

class State(str, Enum):
    NEW='NEW'; MOUNTED='MOUNTED'; REDUCED_MOTION='REDUCED_MOTION'
    LOADING='LOADING'; SLOW_LOAD='SLOW_LOAD'; READY='READY'; RUNNING='RUNNING'
    FAILED='FAILED'; FALLBACK_STATIC='FALLBACK_STATIC'; SKIPPED='SKIPPED'
    HANDOFF_READY='HANDOFF_READY'; SHELL_READY='SHELL_READY'; DISPOSED='DISPOSED'

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
    renderer_initialised: bool=False
    assets_requested: bool=False
    focus_token: Optional[str]=None
    failure_reason: Optional[str]=None

    def _set(self, state: State):
        self.state=state
        self.history.append(state.value)

    @property
    def aspect(self):
        w,h=self.viewport
        return w/h

    @property
    def layout_box(self):
        return {'width':self.viewport[0],'height':self.viewport[1],'min_height':'100vh'}

    @property
    def escape_control_available(self):
        return self.state in {State.MOUNTED,State.LOADING,State.SLOW_LOAD,State.READY,State.RUNNING}

    @property
    def shell_ready(self):
        return self.state==State.SHELL_READY

    def mount(self, focus_token='existing-welcome-focus'):
        if self.state != State.NEW:
            raise RuntimeError('mount must start from NEW')
        self.focus_token=focus_token
        self._set(State.MOUNTED)
        if self.reduced_motion or self.app_less_motion:
            self._set(State.REDUCED_MOTION)
            self._set(State.FALLBACK_STATIC)
            self._set(State.SHELL_READY)
            return
        if not self.webgl_available:
            self.failure_reason='WEBGL_UNAVAILABLE'
            self._set(State.FAILED)
            self._set(State.FALLBACK_STATIC)
            self._set(State.SHELL_READY)
            return
        self.renderer_initialised=True
        self.assets_requested=True
        self._set(State.LOADING)

    def tick(self, elapsed_ms:int):
        if self.state==State.LOADING and elapsed_ms>=self.slow_threshold_ms:
            self._set(State.SLOW_LOAD)
        if self.state in {State.LOADING,State.SLOW_LOAD} and elapsed_ms>=self.hard_timeout_ms:
            self.asset_fail('HARD_TIMEOUT')

    def asset_ready(self):
        if self.state not in {State.LOADING,State.SLOW_LOAD}:
            raise RuntimeError('assets not awaited')
        self._set(State.READY)

    def asset_fail(self, reason='ASSET_FAILURE'):
        if self.state in {State.DISPOSED,State.SHELL_READY}:
            return
        self.failure_reason=reason
        self._set(State.FAILED)
        self._set(State.FALLBACK_STATIC)
        self._set(State.SHELL_READY)

    def start(self):
        if self.state!=State.READY:
            raise RuntimeError('start requires READY')
        self._set(State.RUNNING)

    def skip(self, reason='USER_CONTINUE'):
        if self.state in {State.DISPOSED,State.SHELL_READY}:
            return
        self._set(State.SKIPPED)
        self._set(State.SHELL_READY)

    def complete(self):
        if self.state!=State.RUNNING:
            raise RuntimeError('complete requires RUNNING')
        self._set(State.HANDOFF_READY)
        self._set(State.SHELL_READY)

    def resize(self,width:int,height:int):
        if width<=0 or height<=0:
            raise ValueError('positive viewport required')
        self.viewport=(width,height)
        # lens_mm deliberately unchanged; aspect derives from host box.

    def dispose(self):
        self.renderer_initialised=False
        self.assets_requested=False
        self._set(State.DISPOSED)

    def assert_no_dead_end(self):
        if self.state==State.DISPOSED:
            return True
        return self.shell_ready or self.escape_control_available
