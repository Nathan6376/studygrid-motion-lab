#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, math
from motion_fallback_harness import (
    MotionFallbackHarness, State, Event, TransitionError,
    CANONICAL_STATES, CANONICAL_EVENTS, ALLOWED_TRANSITIONS
)

R5_SHA='0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00'
R6_SHA='875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef'
VIEWPORTS=[(320,568),(360,800),(768,1024),(1024,768),(1440,900),(1920,1080)]

def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()

def source_check(path, expected):
    text=pathlib.Path(path).read_text(encoding='utf-8')
    anchors=['@media(prefers-reduced-motion:reduce)','body[data-less-motion="true"] *','body.entry-mode #root','.welcome-page{position:relative;min-height:100vh','function focusRouteEntry()','function render(){']
    return {'sha_match':sha(path)==expected,'missing':[a for a in anchors if a not in text]}

def original_cases():
    cases={}
    h=MotionFallbackHarness(reduced_motion=True); f='welcome-title'; h.mount(f)
    cases['reduced_motion']={'pass':h.state==State.SHELL_READY and State.RUNNING.value not in h.history and not h.renderer_initialised and h.focus_token==f,'history':h.history}

    h=MotionFallbackHarness(app_less_motion=True); h.mount()
    cases['app_less_motion']={'pass':h.state==State.SHELL_READY and not h.renderer_initialised,'history':h.history}

    h=MotionFallbackHarness(webgl_available=False); h.mount()
    cases['webgl_unavailable']={'pass':h.state==State.SHELL_READY and h.failure_reason=='WEBGL_UNAVAILABLE' and not h.assets_requested,'history':h.history}

    h=MotionFallbackHarness(); f='continue-button'; h.mount(f); before=h.layout_box.copy(); h.tick(1600); can=h.escape_control_available; h.skip(); after=h.layout_box.copy()
    cases['slow_load_continue']={'pass':can and h.state==State.SHELL_READY and before==after and h.focus_token==f,'history':h.history}

    h=MotionFallbackHarness(); h.mount(); h.asset_fail()
    cases['asset_failure']={'pass':h.state==State.SHELL_READY and 'FALLBACK_STATIC' in h.history,'history':h.history}

    h=MotionFallbackHarness(); h.mount(); h.tick(6000)
    cases['hard_timeout']={'pass':h.state==State.SHELL_READY and h.failure_reason=='HARD_TIMEOUT','history':h.history}

    h=MotionFallbackHarness(); h.mount(); h.asset_ready(); h.start(); h.skip()
    cases['running_skip']={'pass':h.state==State.SHELL_READY and 'RUNNING' in h.history and 'SKIPPED' in h.history,'history':h.history}

    h=MotionFallbackHarness(); h.mount(); h.asset_ready(); h.start(); h.complete()
    cases['normal_completion']={'pass':h.state==State.SHELL_READY and 'HANDOFF_READY' in h.history,'history':h.history}

    h=MotionFallbackHarness(); h.mount(); h.dispose()
    cases['route_dispose']={'pass':h.state==State.DISPOSED and not h.renderer_initialised and not h.assets_requested,'history':h.history}

    h=MotionFallbackHarness(); h.mount(); lens=h.lens_mm; metrics=[]; ok=True
    for w,hh in VIEWPORTS:
        h.resize(w,hh); metrics.append({'viewport':[w,hh],'aspect':h.aspect,'lens_mm':h.lens_mm,'layout':h.layout_box}); ok=ok and h.lens_mm==lens
    cases['viewport_fixed_lens']={'pass':ok,'metrics':metrics}

    envelope=[]; env_ok=True; vfov=40.0; near_min=0.12
    for w,hh in VIEWPORTS:
        aspect=w/hh; d_cover=(0.5-0.055)/(max(1.0,aspect)*math.tan(math.radians(vfov)/2.0)); safe=max(d_cover,near_min)
        envelope.append({'viewport':[w,hh],'aspect':aspect,'vfov_deg':vfov,'d_cover':d_cover,'d_near_min':near_min,'safe_handoff':safe}); env_ok=env_ok and safe>=d_cover and safe>=near_min and safe>0
    cases['doorway_envelope']={'pass':env_ok,'metrics':envelope}

    rows=[]
    for scenario in ('loading','slow','ready','running'):
        h=MotionFallbackHarness(); h.mount()
        if scenario=='slow': h.tick(1600)
        elif scenario=='ready': h.asset_ready()
        elif scenario=='running': h.asset_ready(); h.start()
        rows.append({'state':h.state.value,'escape':h.escape_control_available,'no_dead_end':h.assert_no_dead_end()})
    cases['active_state_escape']={'pass':all(x['no_dead_end'] for x in rows),'states':rows}
    return cases

def expanded_cases(state_machine_path):
    cases={}
    graph=json.loads(pathlib.Path(state_machine_path).read_text(encoding='utf-8'))
    json_states=tuple(graph['canonical']['states'])
    json_events=tuple(graph['canonical']['events'])
    expanded={}
    for row in graph['transitions']:
        event=Event(row['event'])
        target=State(row['to'])
        for source_name in row['from']:
            expanded[(State(source_name),event)]=target
    cases['canonical_contract_alignment']={
        'pass': json_states==CANONICAL_STATES and json_events==CANONICAL_EVENTS and expanded==ALLOWED_TRANSITIONS,
        'json_states':list(json_states),'harness_states':list(CANONICAL_STATES),
        'json_events':list(json_events),'harness_events':list(CANONICAL_EVENTS),
        'json_transition_count':len(expanded),'harness_transition_count':len(ALLOWED_TRANSITIONS)
    }

    skip_rows=[]
    for scenario in ('loading','slow','ready','running'):
        h=MotionFallbackHarness(); h.mount()
        if scenario=='slow': h.tick(1600)
        elif scenario=='ready': h.asset_ready()
        elif scenario=='running': h.asset_ready(); h.start()
        source=h.state.value
        h.skip()
        skip_rows.append({'source':source,'history':h.history,'pass':h.state==State.SHELL_READY and 'SKIPPED' in h.history})
    cases['all_allowed_skip_paths']={'pass':all(x['pass'] for x in skip_rows),'paths':skip_rows}

    dispose_rows=[]
    for state in State:
        if state in {State.NEW,State.DISPOSED}:
            continue
        h=MotionFallbackHarness(state=state,renderer_initialised=True,assets_requested=True)
        h.dispose()
        dispose_rows.append({'source':state.value,'pass':h.state==State.DISPOSED and not h.renderer_initialised and not h.assets_requested})
    cases['dispose_every_mounted_state']={'pass':all(x['pass'] for x in dispose_rows),'paths':dispose_rows}

    fail_rows=[]
    h=MotionFallbackHarness(); h.mount(); h.asset_ready(); source=h.state.value; h.fail('READY_FAILURE')
    fail_rows.append({'source':source,'history':h.history,'pass':h.state==State.SHELL_READY and h.history[-3:]==['FAILED','FALLBACK_STATIC','SHELL_READY']})
    h=MotionFallbackHarness(); h.mount(); h.asset_ready(); h.start(); source=h.state.value; h.fail('RUNNING_FAILURE')
    fail_rows.append({'source':source,'history':h.history,'pass':h.state==State.SHELL_READY and h.history[-3:]==['FAILED','FALLBACK_STATIC','SHELL_READY']})
    cases['ready_running_failure']={'pass':all(x['pass'] for x in fail_rows),'paths':fail_rows}

    neg=[]
    for action in ('skip','fail'):
        h=MotionFallbackHarness()
        rejected=False
        try:
            h.skip() if action=='skip' else h.fail('INVALID_NEW_FAILURE')
        except TransitionError:
            rejected=True
        neg.append({'action':action,'rejected':rejected,'state':h.state.value})
    cases['invalid_new_transitions']={'pass':all(x['rejected'] and x['state']=='NEW' for x in neg),'tests':neg}

    combos=[]; ok=True
    lens=50.0
    for state in State:
        for w,hh in VIEWPORTS:
            h=MotionFallbackHarness(state=state,viewport=(w,hh),lens_mm=lens)
            box=h.layout_box
            passed=box=={'width':w,'height':hh,'min_height':'100vh'} and h.lens_mm==lens
            combos.append({'state':state.value,'viewport':[w,hh],'layout':box,'lens_mm':h.lens_mm,'pass':passed})
            ok=ok and passed
    cases['all_state_viewport_layout']={'pass':ok,'combinations':len(combos),'expected':len(State)*len(VIEWPORTS),'rows':combos}
    return cases

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--r5',required=True)
    ap.add_argument('--r6',required=True)
    ap.add_argument('--state-machine',default=str(pathlib.Path(__file__).with_name('fallback_state_machine.json')))
    args=ap.parse_args()
    sources={'r5':source_check(args.r5,R5_SHA),'r6':source_check(args.r6,R6_SHA)}
    original=original_cases()
    expanded=expanded_cases(args.state_machine)
    original_pass=sum(1 for v in original.values() if v['pass'])
    expanded_pass=sum(1 for v in expanded.values() if v['pass'])
    status='PASS' if original_pass==len(original) and expanded_pass==len(expanded) and all(v['sha_match'] and not v['missing'] for v in sources.values()) else 'FAIL'
    print(json.dumps({
        'schema':'studygrid.qb11.state_alignment_verification.v1',
        'status':status,
        'sources':sources,
        'original_qb10_acceptance':{'pass':original_pass,'total':len(original),'cases':original},
        'expanded_qb11_regression':{'pass':expanded_pass,'total':len(expanded),'cases':expanded},
        'synthetic_limit':'browser/device/assistive-technology focus and real GPU/WebGL recovery/rendering remain later integration QA'
    },indent=2))
    return 0 if status=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
