#!/usr/bin/env python3
import argparse, hashlib, json, pathlib

EXPECTED = {
  "r5": {
    "sha256": "0fee828511bdccd373fdc0625c0ea9f894485a57f6e6cbceff74e2652ec34d00",
    "required": [
      'id="root"', 'body.entry-mode .topbar', 'body.entry-mode #root',
      '.welcome-page{position:relative;min-height:100vh',
      '.welcome-shell{width:min(780px,100%)', 'function setEntryMode(r)',
      'function focusRouteEntry()', 'function render(){',
      'function handleRouteHistoryChange()',
      "const APP_VERSION='v7.15-cf0032-integrated-batch4-8-cf0039-r5';"
    ],
    "forbidden_r6_only": ['.r6-welcome-grid{', 'renderWelcome=function()']
  },
  "r6": {
    "sha256": "875a81262d80cf33ceb32545ff20c1cbc03ae91db34c66a3a8a679f93f0314ef",
    "required": [
      'id="root"', 'body.entry-mode .topbar', 'body.entry-mode #root',
      '.welcome-page{position:relative;min-height:100vh',
      '.welcome-shell{width:min(780px,100%)', 'function setEntryMode(r)',
      'function focusRouteEntry()', 'function render(){',
      'function handleRouteHistoryChange()', '.r6-welcome-grid{',
      'renderWelcome=function()',
      "const APP_VERSION='v7.16-cf0032-integrated-batch4-8-cf0039-r6';"
    ]
  }
}

def inspect(path, key):
    raw = pathlib.Path(path).read_bytes()
    text = raw.decode('utf-8')
    digest = hashlib.sha256(raw).hexdigest()
    problems = []
    if digest != EXPECTED[key]['sha256']:
        problems.append({'code':'SOURCE_DIGEST_MISMATCH','expected':EXPECTED[key]['sha256'],'actual':digest})
    for token in EXPECTED[key]['required']:
        if token not in text:
            problems.append({'code':'ANCHOR_MISSING','token':token})
    for token in EXPECTED[key].get('forbidden_r6_only',[]):
        if token in text:
            problems.append({'code':'UNEXPECTED_R6_OVERRIDE_IN_R5','token':token})
    return {'path':str(path),'sha256':digest,'bytes':len(raw),'problems':problems}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--r5', required=True)
    ap.add_argument('--r6', required=True)
    args=ap.parse_args()
    result={'schema':'studygrid.qb9.seam_verification.v1','r5':inspect(args.r5,'r5'),'r6':inspect(args.r6,'r6')}
    result['status']='PASS' if not result['r5']['problems'] and not result['r6']['problems'] else 'FAIL'
    print(json.dumps(result,indent=2))
    return 0 if result['status']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
