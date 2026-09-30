from copy import deepcopy
from stuart_qs11_professor_home_oracles import *

passed = 0

def ok(fn, *args, **kwargs):
    global passed
    fn(*args, **kwargs)
    passed += 1

def rejects(fn, *args, **kwargs):
    global passed
    try:
        fn(*args, **kwargs)
    except OracleFailure:
        passed += 1
        return
    raise AssertionError(f"expected rejection: {fn.__name__}")

courses = [
    {"id":"c1","name":"Police Foundations","code":"PFP207","section":"A","student_count":58,"open_question_count":4,"colour":"green","label":"Core"},
    {"id":"c2","name":"Criminology","code":"CRIM150","section":"B","student_count":54,"open_question_count":2,"colour":"green","label":"Core"},
    {"id":"c3","name":"Provincial Statutes","code":"PFP156","section":"A","student_count":51,"open_question_count":3,"colour":"blue","label":"Core"},
    {"id":"c4","name":"Psychology","code":"PSYC224","section":"WWA","student_count":49,"open_question_count":1,"colour":"blue","label":"Elective"},
    {"id":"c5","name":"Writing","code":"WRIT200","section":"C","student_count":61,"open_question_count":0,"colour":"amber","label":"Elective"},
    {"id":"c6","name":"Community","code":"CORE100","section":"D","student_count":53,"open_question_count":5,"colour":"amber","label":"Elective"},
]

ok(verify_gate_catalogue)
ok(verify_scale, courses)
ok(verify_explicit_class_identity, courses)
ok(verify_colour_not_sole_identifier, courses)
rejects(verify_scale, courses[:2])
amb = deepcopy(courses); amb[1].update(name=amb[0]["name"], code=amb[0]["code"], section=amb[0]["section"])
rejects(verify_colour_not_sole_identifier, amb)

today = [{"id":"t1","confirmed":True,"course_id":"c1","starts_at":"2026-09-30T19:00"}]
ok(verify_today, today)
rejects(verify_today, [{**today[0],"confirmed":False}])
context={"location_hash":"#professor-home","selected_class_id":None,"workspace_view":"professor_home"}
ok(verify_no_auto_navigation, context, dict(context))
rejects(verify_no_auto_navigation, context, {**context,"selected_class_id":"c1"})

live=[{"id":"a1","actionable":True,"resolved":False,"reason":"Question waiting"}]
history=[{"id":"a1","resolved":True,"status":"resolved"}]
ok(verify_attention_live, live)
rejects(verify_attention_live, [{"id":"a1","actionable":True,"resolved":True,"reason":"bad"}])
ok(verify_attention_resolution, live, [], history, "a1")
ok(verify_all_resolved, [], history)

reordered=list(reversed(deepcopy(courses)))
ok(verify_transparent_organization, courses, reordered)
risk=deepcopy(reordered); risk[0]["risk_score"]=9
rejects(verify_transparent_organization, courses, risk)
by_name=sorted(courses,key=lambda c:c["name"].casefold())
by_code=sorted(courses,key=lambda c:c["code"].casefold())
ok(verify_sort, by_name, "name")
ok(verify_sort, by_code, "code")
rejects(verify_sort, list(reversed(by_name)), "name")

drill={"selected_class_id":"c1","workspace_tabs":["Overview","Assessments","Questions","Students","Sources"],"professor_home_replaced_workspace":False}
ok(verify_selected_class_drill, drill, "c1")
rejects(verify_selected_class_drill, {**drill,"professor_home_replaced_workspace":True}, "c1")

revs={k:"assessment-r3" for k in ("assessment_desk","instructor_summary","student_timeline","delivery_plan")}
ok(verify_shared_assessment_revision, revs)
bad_revs=dict(revs); bad_revs["student_timeline"]="assessment-r2"
rejects(verify_shared_assessment_revision, bad_revs)

sources=[{"section_id":"s","source_revision_id":"r","source_block_id":"b","display_locator":"p.4"}]
ok(verify_source_identity, sources)
rejects(verify_source_identity, [{**sources[0],"display_locator":""}])

before={"revision":"r2","title":"Quiz"}
stale={"ok":False,"state":"stale_revision","error":{"code":"STALE_REVISION"}}
unauth={"ok":False,"state":"unauthorized","error":{"code":"UNAUTHORIZED"}}
ok(verify_stale_no_mutation, before, stale, deepcopy(before))
rejects(verify_stale_no_mutation, before, stale, {**before,"title":"mutated"})
ok(verify_unauthorized_no_mutation, before, unauth, deepcopy(before))
rejects(verify_unauthorized_no_mutation, before, unauth, {**before,"title":"mutated"})

states={s:{"state":s} for s in ("ready","loading","empty","error","stale_revision","unauthorized")}
ok(verify_deterministic_states, states, deepcopy(states))
bad_states=deepcopy(states); bad_states["empty"]={"state":"ready"}
rejects(verify_deterministic_states, states, bad_states)

ok(verify_focus, "r6StudentSort", "r6StudentSort")
ok(verify_focus, "r6StudentFilter", "r6StudentFilter")
ok(verify_focus, "r6TaskCanvas", "r6TaskCanvas")
ok(verify_focus, "r6InspectPolicy", "r6InspectPolicy")

resp={"duplicate_ids":0,"horizontal_overflow_px":0,"professor_home_visible":True,"class_library_visible":True}
ok(verify_responsive, resp)
rejects(verify_responsive, {**resp,"horizontal_overflow_px":12})
home={"full_roster_rows_rendered":0,"organization_controls_visible":True}
ok(verify_home_bounded_summary, home)
rejects(verify_home_bounded_summary, {**home,"full_roster_rows_rendered":326})

assert passed == 39, passed
print("39/39 PASS")
