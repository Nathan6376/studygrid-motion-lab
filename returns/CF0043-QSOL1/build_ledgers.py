import json, re
from pathlib import Path
p = Path(__file__).parent
def read(name): return json.loads((p/(name+'.json')).read_text())
functions, handlers, controls = read('functions'), read('handlers'), read('controls')
# Exact replacement definitions; wrappers retaining base are deliberately not excluded.
replaced = {'renderWelcome':3396, 'renderAddClass':3405, 'renderTree':3052,
            'renderTreeTopicDetail':3060, 'renderQuestionSession':3103,
            'startSession':3084, 'startAssessmentSession':3091,
            'commitAttempt':3116, 'finishSession':3122, 'sgR6PaintSources':3390,
            'courseHead':3409}
def status(owner, line):
    if owner in replaced and line < replaced[owner]: return 'SUPERSEDED_DEFINITION'
    if owner == 'renderInstructorWorkspace' and 2954 <= line <= 2957:
        return 'LEGACY_TOUR_LAUNCHER_REMOVED_BY_FINAL_WRAPPER'
    return 'SOURCE_DECLARATION__RUNTIME_VISIBILITY_NOT_ASSERTED'
def enclosing(line):
    matches=[f for f in functions if f['line'] <= line <= f['endLine']]
    return min(matches,key=lambda f:f['endLine']-f['line']) if matches else None
def scope(owner,line):
    if owner in ['renderWelcome']: return '/welcome'
    if owner in ['renderAddClass','sgR6CourseAssist']: return '/courses/add'
    if owner=='renderCourses': return '/courses'
    if owner=='renderFirstStart': return '/start'
    if 'Tour' in owner or owner in ['tourVisualMarkup','bindTourDemo']: return '/tour or /tour/instructor; index-local'
    if owner=='renderAccess': return '/access/login or signup'
    if 'Professor' in owner or 'QB15' in owner: return '/workspace/instructor; local fixture'
    if 'Instructor' in owner or 'sgR6' in owner or 'StudySet' in owner: return '/workspace/instructor/class/id/tab; local fixture'
    if 'Profile' in owner: return '/profile subroute'
    if 'Inventory' in owner or owner in ['appearanceButton','equipAppearance']: return '/profile/inventory'
    if owner=='renderPlan': return '/plan'
    if 'Scenario' in owner or owner=='renderDebrief': return '/course/id/scenario or Study activity'
    if 'ClassNote' in owner or 'Companion' in owner or 'SourceLayers' in owner: return '/course/id/notes/note or Study'
    if owner in ['renderSources','lessonMarkup','bindLessonUi']: return '/course/id/sources/mode'
    if 'Tree' in owner: return '/course/id/tree/topic'
    if 'Session' in owner or owner in ['renderFeedback','showConfidenceInPlace','renderNeutralSubmittedState']: return '/course/id/study; session-local'
    if 'Local' in owner: return '/course/local-id/overview|material|study'
    if 'Study' in owner: return '/course/id/study/purpose|topic'
    if 'Report' in owner or owner=='(static or inline template)' and line<1213: return 'global shell/feedback/annotation; see exact ID and handler'
    return 'inherited route/local surface; see exact owner and callback source'
for i,h in enumerate(handlers,1):
    h['audit_id']=f'H{i:04d}'
    h['definition_status']=status(h['owner'],h['line'])
    h['visible_route_state']=scope(h['owner'],h['line'])
    h['actual_destination_or_mutation']='Exact callback, calls and writes below; function-name callback resolves in functions.json.'
for i,c in enumerate(controls,1):
    c['audit_id']=f'C{i:04d}'
    c['definition_status']=status(c['owner'],c['line'])
    c['visible_route_state']=scope(c['owner'],c['line'])
    tokens=[]
    if isinstance(c['id'],str): tokens.append(c['id'])
    tokens += [k for k in c['attributes'] if k.startswith('data-')]
    candidates=[h for h in handlers if any(t in h['target']+' '+h.get('bindingScope','') for t in tokens)]
    c['handler_candidates']=[h['audit_id'] for h in candidates]
    c['binding_evidence_limit']='Selector-token association only; use scope/owner and supersession. Not a live DOM match.'
    c['actual_destination_or_mutation']={'href':c['attributes'].get('href'),
        'type':c['attributes'].get('type'), 'name':c['attributes'].get('name'),
        'event_callbacks':[{'id':h['audit_id'],'line':h['line'],'event':h['event'],
                           'owner':h['owner'],'callback':h['callback']} for h in candidates]}
    f=enclosing(c['line'])
    c['owner_source_reference']={'name':f['name'],'line':f['line'],'endLine':f['endLine']} if f else None
    c['review_findings']=[f for token,f in [('data-theme-choice','F08'),('data-prof-colour','F03'),
        ('data-prof-label','F03'),('data-prof-resolve','F04/F11'),('data-note-read','F11'),
        ('data-all-instructor-classes','F02'),('seeTree','F10'),('localClassName','F09')]
        if token in c['raw']]
    # Forms and template scopes can legitimately have long body text. Keep exact raw label;
    # also provide a scan label without replacing the evidence.
    c['scan_label']=c['label'][:240]
supplement = read('role-controls') if (p/'role-controls.json').exists() else []
(p/'control-ledger.json').write_text(json.dumps(controls+supplement,indent=2)+'\n')
(p/'handler-ledger.json').write_text(json.dumps(handlers,indent=2)+'\n')
assert len(controls)==553 and len(handlers)==355
print('Ledger coverage:',len(controls),'controls;',len(handlers),'handlers')
