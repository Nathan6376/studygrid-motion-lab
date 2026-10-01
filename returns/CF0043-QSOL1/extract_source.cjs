const fs=require('fs'),crypto=require('crypto');
const B=require('/opt/codex/runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/lib/transform/babelBundle.js');
const input=process.argv[2],out=process.argv[3]||'studygrid-sol-audit';
const html=fs.readFileSync(input,'utf8');fs.mkdirSync(out,{recursive:true});
const lineAt=o=>html.slice(0,o).split('\n').length;
const functions=[],handlers=[],routes=[],stateWrites=[],selectionCalls=[],scripts=[];
for(const m of html.matchAll(/<script\b([^>]*)>([\s\S]*?)<\/script>/gi)){
 if(/application\/json/.test(m[1]))continue;
 const code=m[2],offset=m.index+m[0].indexOf(code),baseLine=lineAt(offset)-1;
 const ast=B.babelParse(code,'audit.js',false);scripts.push({line:baseLine+1,bytes:Buffer.byteLength(code),parsed:true});
 const sn=n=>code.slice(n.start,n.end),ln=n=>baseLine+n.loc.start.line;
 function name(p){const n=p.node;if(n.id?.name)return n.id.name;if(p.parentPath?.isVariableDeclarator())return sn(p.parentPath.node.id);if(p.parentPath?.isAssignmentExpression())return sn(p.parentPath.node.left);if(p.parentPath?.isObjectProperty()||p.parentPath?.isObjectMethod())return sn(p.parentPath.node.key);return '(anonymous)';}
 function owner(p){let q=p.findParent(x=>x.isFunction()&&name(x)!=='(anonymous)');return q?name(q):'(script)';}
 B.traverse(ast,{
  Function(p){const n=p.node;if(n.type==='FunctionDeclaration'||p.parentPath?.isAssignmentExpression()||p.parentPath?.isVariableDeclarator()||n.type==='ObjectMethod')functions.push({name:name(p),line:ln(n),endLine:baseLine+n.loc.end.line,parent:owner(p),code:sn(n)});},
  'CallExpression|OptionalCallExpression'(p){const n=p.node,c=sn(n.callee),record={line:ln(n),owner:owner(p),callee:c,code:sn(n)};
    if(/\.addEventListener$/.test(c)){
      const callback=n.arguments[1],calls=[],writes=[];function scan(x){if(!x||typeof x!=='object')return;if(['CallExpression','OptionalCallExpression'].includes(x.type))calls.push(sn(x));if(x.type==='AssignmentExpression')writes.push(sn(x));for(const [k,v] of Object.entries(x)){if(['loc','extra','start','end'].includes(k))continue;if(Array.isArray(v))v.forEach(scan);else if(v&&typeof v==='object')scan(v);}}
      scan(callback);const scope=p.findParent(q=>q.isCallExpression()&&/\.forEach$/.test(sn(q.node.callee)));const bindingScope=scope?sn(scope.node.callee):c;handlers.push({...record,bindingScope,event:n.arguments[0]?.value||sn(n.arguments[0]),target:sn(n.callee.object),callback:callback?sn(callback):'',calls,writes});
    }
    if(c==='nav'||/^(?:history\.(?:pushState|replaceState)|location\.(?:assign|replace))$/.test(c))routes.push(record);
    if(/\.(?:setPointerCapture|releasePointerCapture|getSelection|removeAllRanges)$/.test(c))selectionCalls.push(record);
  },
  AssignmentExpression(p){const n=p.node,left=sn(n.left);if(/^state\.|^sgR6\.|location\.hash|\.style\.(cursor|userSelect|pointerEvents|touchAction)|\.dataset\.(mode|theme)/.test(left))stateWrites.push({line:ln(n),owner:owner(p),target:left,code:sn(n)});}
 });
}
const controls=[];
for(const m of html.matchAll(/<(button|a|input|select|textarea|summary|dialog|form)\b([^>]*?)>/gi)){
 const tag=m[1].toLowerCase();const attributes=m[2];const closing=html.indexOf(`</${tag}>`,m.index+m[0].length);let body=tag==='input'?'':(closing>=0?html.slice(m.index+m[0].length,closing):'');
 const attr={};for(const a of attributes.matchAll(/([\w:-]+)(?:="([\s\S]*?)"|='([\s\S]*?)'|=([^\s>]+))?/g))attr[a[1]]=a[2]??a[3]??a[4]??true;
 const line=lineAt(m.index);const enclosing=functions.filter(f=>f.line<=line&&f.endLine>=line).sort((a,b)=>(a.endLine-a.line)-(b.endLine-b.line))[0];
 controls.push({line,tag,id:attr.id||null,attributes:attr,label:body.replace(/<[^>]*>/g,' ').replace(/\s+/g,' ').trim(),owner:enclosing?.name||'(static or inline template)',raw:m[0]});
}
const css=[];for(const m of html.matchAll(/([^{}]+)\{([^{}]*\b(?:cursor|user-select|pointer-events|touch-action|-webkit-user-select)[^{}]*)\}/g))css.push({line:lineAt(m.index),selector:m[1].trim().slice(-400),declarations:m[2]});
const registryMatch=html.match(/<script[^>]*id="studygridComponentRegistry"[^>]*>([\s\S]*?)<\/script>/);
const registry=registryMatch?JSON.parse(registryMatch[1]):null;
const manifest={sourceFile:input,sha256:crypto.createHash('sha256').update(html).digest('hex'),bytes:Buffer.byteLength(html),lines:html.split('\n').length,APP_VERSION:html.match(/APP_VERSION\s*=\s*['"]([^'"]+)/)?.[1],scripts,counts:{functions:functions.length,handlers:handlers.length,routeCalls:routes.length,controls:controls.length,cssRules:css.length,registryEntries:registry?.entries?.length},scope:'Static exhaustive parse; declarations include replaced legacy functions; runtime/device reproduction not performed.'};
for(const [name,data] of Object.entries({manifest,functions,handlers,routes,stateWrites,selectionCalls,controls,cursorCSS:css,registry}))fs.writeFileSync(`${out}/${name}.json`,JSON.stringify(data,null,2)+'\n');
console.log(JSON.stringify(manifest,null,2));
