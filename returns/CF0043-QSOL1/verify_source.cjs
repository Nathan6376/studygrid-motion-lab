// Uses exact extracted source functions in isolated stubs, not a browser/device.
const fs=require('fs'), vm=require('vm'), assert=require('assert'), crypto=require('crypto');
const dir=__dirname, f=JSON.parse(fs.readFileSync(dir+'/functions.json'));
const source=process.argv[2];const bytes=fs.readFileSync(source);
assert.equal(crypto.createHash('sha256').update(bytes).digest('hex'),'48b16df1c05b1a62cf7af174d3a48b3609ae79c2b39edfbe8c6046cbe48c46cf');
assert.equal(bytes.length,996820);
const code=name=>{const matches=f.filter(x=>x.name===name);assert.equal(matches.length,1,name);return matches[0].code};
const cls={add(){},remove(){},contains(){return false}};
const element={classList:cls,setAttribute(){},removeAttribute(){},dataset:{},width:1,height:1,getContext(){return {clearRect(){}}},focus(){}};
const doc={getElementById(){return element},querySelectorAll(){return []}};
const ctx={document:doc,reportMarkState:{drawing:true,points:[1],bounds:{},items:[],areas:[],mode:'circle'},reportCirclePointer:7,reportTwoFingerLastY:10,
reportSelectionReviewMode:false,reportSelectionReviewReturnFocus:null,pendingReportSelection:null,
closeSiteReports(){},openSiteReports(){},renderReportSelectionChip(){},resizeReportMarkCanvas(){},updateReportItemModeLabel(){},showToast(){},setTimeout(){}};
vm.createContext(ctx);
vm.runInContext(['clearReportMarkCanvas','clearReportTarget','setReportMarkMode','closeReportMarking','openReportMarking'].map(code).join('\n'),ctx);
vm.runInContext('closeReportMarking(true);openReportMarking();setReportMarkMode("circle")',ctx);
assert.equal(ctx.reportMarkState.drawing,true);assert.equal(ctx.reportCirclePointer,7);assert.equal(ctx.reportTwoFingerLastY,10);
assert.equal(ctx.reportMarkState.points.length,0);
const q=[], seen=[], range={startContainer:{isConnected:true}};
const a={document:doc,window:{getSelection(){return {removeAllRanges(){}}}},pendingStudySelection:{quote:'selection'},
annotationSelectionTimer:null,lastStudyRange:range,lastStudySurfaceId:'surface-a',clearTimeout(){},
setTimeout(fn){q.push(fn);return q.length},cacheAnnotationRange(){return {range,sid:'surface-a'}},
currentAnnotationRange(){return null},showAnnotationPopover(r,sid){seen.push({r,sid})}};
vm.createContext(a);vm.runInContext(code('closeAnnotationPopover')+'\n'+code('captureAnnotationSelection'),a);
vm.runInContext('captureAnnotationSelection(80);closeAnnotationPopover()',a);
assert.equal(a.pendingStudySelection,null);assert.equal(q.length,1);q[0]();assert.equal(seen.length,1);assert.equal(seen[0].sid,'surface-a');
const manifest=JSON.parse(fs.readFileSync(dir+'/manifest.json'));
assert.equal(manifest.scripts.length,4);assert(manifest.scripts.every(x=>x.parsed));
const checks={sourceSha256:manifest.sha256,bytes:bytes.length,executableScriptParses:4,
checks:[{name:'Source identity preserved',result:'PASS'},
{name:'Report close/open exact functions leave drawing/pointer/centroid when native finish event absent',result:'CONFIRMED_SOURCE_STATE',browserReproduction:false},
{name:'Annotation cached delayed callback survives exact close function with connected source range',result:'CONFIRMED_SOURCE_STATE',browserReproduction:false}],
limits:'DOM is stubbed; no native event dispatch, pointer capture delivery, CSS geometry, Safari/iPad, screen reader, theme hit-test or runtime acceptance is verified.'};
fs.writeFileSync(dir+'/verification.json',JSON.stringify(checks,null,2)+'\n');console.log(JSON.stringify(checks,null,2));
