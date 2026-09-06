"""Inventário estático do PBIP do Atlas. Não executa DAX, M ou consultas remotas.

Parser limitado ao TMDL deste projeto: preserva expressões e locators; não é
substituto do serializer TOM. Usa somente a biblioteca padrão do Python.
"""
from pathlib import Path
import re, json, hashlib, textwrap, unicodedata

ROOT = Path(__file__).resolve().parents[1]
MODEL = next((ROOT / 'powerbi').glob('*.SemanticModel'))
REPORT = next((ROOT / 'powerbi').glob('*.Report'))

def read(p):
    return p.read_text(encoding='utf-8-sig')

def rel(p):
    return p.relative_to(ROOT).as_posix()

def slug(s):
    s = s.replace('%', ' percentual ').replace('+', ' mais ').replace('&', ' e ')
    return re.sub(r'[^a-z0-9]+', '_', unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()).strip('_')

def unquote(s):
    s = s.strip()
    return s[1:-1].replace("''", "'") if s.startswith("'") and s.endswith("'") else s

def no_comments(s, mask_strings=False):
    # Preserve quoted identifiers; recognize escaped quotes before comment tokens.
    token = re.compile(r'"(?:[^"\n]|"")*"|\'(?:[^\']|\'\')*\'|/\*[\s\S]*?\*/|//[^\n]*|--[^\n]*')
    def sub(m):
        t = m.group()
        if t.startswith(('/*','//','--')) or (mask_strings and t.startswith('"')):
            return ''.join('\n' if c == '\n' else ' ' for c in t)
        return t
    return token.sub(sub, s)

def props(lines, indent):
    d = {}
    for line in lines:
        if not line.startswith('\t'*indent) or line.startswith('\t'*(indent+1)):
            continue
        s = line.strip()
        m = re.match(r'(\w+):\s*(.*)', s)
        if m:
            d[m[1]] = m[2]
        elif s in ('isHidden', 'isKey', 'excludeFromModelRefresh'):
            d[s] = True
    return d

def expression(lines, header_index, indent):
    initial = lines[header_index].split('=',1)[1].strip() if '=' in lines[header_index] else ''
    out = []
    if initial == '```':
        for line in lines[header_index+1:]:
            if line.strip() == '```':
                break
            out.append(line)
    else:
        if initial:
            out.append('\t'*(indent+2)+initial)
        for line in lines[header_index+1:]:
            if line.strip() and len(line)-len(line.lstrip('\t')) <= indent+1:
                break
            out.append(line)
    return textwrap.dedent('\n'.join(out)).strip('\n')

def parse_table(path):
    lines = read(path).splitlines()
    name = unquote(lines[0][6:])
    starts = [(i,m) for i,l in enumerate(lines) if (m:=re.match(r'^\t(measure|column|partition|hierarchy) (\'(?:[^\']|\'\')*\'|[^=]+?)(?:\s*=\s*(.*))?$',l))]
    table = {'name':name, 'source':rel(path), 'properties':props(lines[:starts[0][0]] if starts else lines,1), 'columns':[], 'measures':[], 'partitions':[], 'hierarchies':[]}
    for n,(i,m) in enumerate(starts):
        end = starts[n+1][0] if n+1<len(starts) else len(lines)
        block = lines[i:end]
        desc=[]; k=i-1
        while k>=0 and lines[k].startswith('\t///'):
            desc.insert(0,lines[k][4:].lstrip()); k-=1
        obj={'name':unquote(m[2]),'line':i+1,'description':'\n'.join(desc) or None,'properties':props(block,2)}
        if m[1] in ('measure','column') and m[3] is not None:
            obj['expression']=expression(block,0,1)
        for pi, pl in enumerate(block):
            pm = re.match(r'^\t\t(formatStringDefinition|detailRowsDefinition)\s*=', pl)
            if pm:
                obj.setdefault('expression_properties',{})[pm[1]]=expression(block,pi,2)
        if m[1]=='partition':
            obj['kind']=m[3]
            si=next((j for j,l in enumerate(block) if re.match(r'^\t\tsource\s*=',l)),None)
            obj['expression']=expression(block,si,2) if si is not None else None
            obj['source_line']=i+si+1 if si is not None else None
        if m[1]=='hierarchy':
            obj['definition']='\n'.join(block).rstrip()
        table[{'column':'columns','measure':'measures','partition':'partitions','hierarchy':'hierarchies'}[m[1]]].append(obj)
    return table

def walk(x, path='$'):
    yield path,x
    if isinstance(x,dict):
        for k,v in x.items(): yield from walk(v,path+'/'+k)
    elif isinstance(x,list):
        for i,v in enumerate(x): yield from walk(v,path+'/'+str(i))

def report_refs(x):
    refs=[]
    aliases={}
    for _,v in walk(x):
        if isinstance(v,dict) and isinstance(v.get('From'),list):
            for item in v['From']:
                if 'Name' in item and 'Entity' in item:
                    aliases.setdefault(item['Name'],set()).add(item['Entity'])
    for p,v in walk(x):
        if isinstance(v,dict):
            for kind in ('Measure','Column'):
                if kind in v and isinstance(v[kind],dict):
                    a=v[kind]; sr=a.get('Expression',{}).get('SourceRef',{})
                    candidates=aliases.get(sr.get('Source'),set())
                    entity=sr.get('Entity') or (next(iter(candidates)) if len(candidates)==1 else None)
                    refs.append({'kind':kind,'table':entity,'property':a.get('Property'),'locator':p+'/'+kind})
    return refs

def extract():
    tables=[parse_table(p) for p in sorted((MODEL/'definition/tables').glob('*.tmdl'))]
    for t in tables:
        for m in t['measures']:
            m['id']='bi_'+slug(m['name'])
            m['table']=t['name']; m['source']=t['source']
    measures=[m for t in tables for m in t['measures']]
    names={m['name']:m['id'] for m in measures}
    colref=re.compile(r"(?:'((?:[^']|'')+)'|([\w]+))\s*\[((?:[^\]]|\]\])+?)\]")
    for m in measures:
        active=no_comments(m.get('expression',''),True)
        table_scope=re.sub(r'\[(?:[^\]]|\]\])+?\]','',active)
        m['table_dependencies']=sorted(t['name'] for t in tables if re.search(r"(?<![\w])"+re.escape(t['name'])+r"(?![\w])",table_scope))
        m['column_dependencies']=[]
        m['measure_dependencies']=[]
        for match in colref.finditer(active):
            t=(match[1] or match[2]).replace("''", "'"); c=match[3].replace(']]',']')
            if t==m['table'] and c in names:
                m['measure_dependencies'].append(names[c])
            else:
                m['column_dependencies'].append({'table':t,'column':c})
        leftovers=colref.sub('',active)
        m['unresolved_bracket_references']=[]
        for ref in re.findall(r'\[([^\]]+)\]',leftovers):
            if ref in names: m['measure_dependencies'].append(names[ref])
            else: m['unresolved_bracket_references'].append(ref)
        m['measure_dependencies']=sorted(set(m['measure_dependencies']))
        m['column_dependencies']=list({(c['table'],c['column']):c for c in m['column_dependencies']}.values())
        m['context_functions']=sorted(set(re.findall(r'\b(CALCULATE|REMOVEFILTERS|ALL|ALLSELECTED|ALLEXCEPT|USERELATIONSHIP|CROSSFILTER|TREATAS|TODAY|NOW|SELECTEDVALUE|ISINSCOPE|DATESYTD|DATEADD)\s*\(',active,re.I)))
    rp=MODEL/'definition/relationships.tmdl'; rl=read(rp).splitlines()
    starts=[i for i,l in enumerate(rl) if l.startswith('relationship ')]
    relationships=[]
    for j,i in enumerate(starts):
        relationships.append({'name':rl[i][13:],'source':rel(rp),'line':i+1,'properties':props(rl[i:starts[j+1] if j+1<len(starts) else len(rl)],1)})
    pages=[]
    for p in sorted((REPORT/'definition/pages').glob('*/page.json')):
        raw=json.loads(read(p)); visuals=[]
        for vp in sorted((p.parent/'visuals').glob('*/visual.json')):
            v=json.loads(read(vp))
            visuals.append({'id':v['name'],'type':v.get('visual',{}).get('visualType'),'source':rel(vp),'refs':report_refs(v),'filterConfig':v.get('filterConfig'),'query':v.get('visual',{}).get('query'),'title_properties':v.get('visual',{}).get('visualContainerObjects',{}).get('title'),'isHidden':v.get('isHidden')})
        pages.append({'id':raw['name'],'title':raw['displayName'],'source':rel(p),'visibility':raw.get('visibility'),'filterConfig':raw.get('filterConfig'),'visuals':visuals})
    roles=[]
    for p in sorted((MODEL/'definition/roles').glob('*.tmdl')):
        roles.append({'source':rel(p),'definition':read(p)})
    files=[p for p in (ROOT/'powerbi').rglob('*') if p.is_file() and '.pbi' not in p.parts]
    return {'tables':tables,'measures':measures,'relationships':relationships,'pages':pages,'roles':roles,'manifest':[{'path':rel(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(files)]}

if __name__ == '__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('--output',required=True)
    args=ap.parse_args(); data=extract()
    Path(args.output).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'tables':len(data['tables']),'columns':sum(len(t['columns']) for t in data['tables']),'measures':len(data['measures']),'relationships':len(data['relationships']),'pages':len(data['pages']),'visuals':sum(len(p['visuals']) for p in data['pages'])}))
