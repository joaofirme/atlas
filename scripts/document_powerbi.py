"""Gera a primeira documentação estática. Recusa sobrescrever arquivos existentes.

Uso: python scripts/document_powerbi.py
Não instala dependências, valida modelos nem conecta ao Power BI/Redshift.
Para futuras ingestões, comparar a extração com os contratos já enriquecidos.
"""
from ingest_powerbi import *
import os
from collections import Counter

DATE='2026-09-06'
INGESTION='docs/ingestoes/2026-09-06-modelo-corporativo'
DATA=extract()
TABLES={t['name']:t for t in DATA['tables']}
MEASURES={m['id']:m for m in DATA['measures']}
BYNAME={m['name']:m for m in DATA['measures']}
CAT=[]

def scalar(x):
    return json.dumps(x,ensure_ascii=False)

def yaml(x,depth=0):
    pad='  '*depth
    if isinstance(x,dict):
        out=[]
        for k,v in x.items():
            if isinstance(v,(dict,list)) and v:
                out.append(pad+k+':\n'+yaml(v,depth+1))
            elif isinstance(v,str) and '\n' in v:
                out.append(pad+k+': |2-\n'+'\n'.join('  '*(depth+1)+l for l in v.splitlines()))
            else: out.append(pad+k+': '+scalar(v))
        return '\n'.join(out)
    return '\n'.join(pad+'-\n'+yaml(v,depth+1) if isinstance(v,(dict,list)) else pad+'- '+scalar(v) for v in x)

def write(path,content):
    p=ROOT/path
    if p.exists(): raise FileExistsError(f'Revisar antes de sobrescrever: {path}')
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content.rstrip()+'\n',encoding='utf-8')

def link(label,path,frompath):
    return '['+str(label).replace('[','').replace(']','')+'](<'+os.path.relpath(ROOT/path,(ROOT/frompath).parent).replace('\\','/')+'>)'

def meta(id,title,type,domain,source,locator='arquivo completo'):
    return dict(schema_version=1,id=id,title=title,type=type,domain=domain,status='draft',version='0.1.0',owners=dict(business=None,technical=None),created_at=DATE,updated_at=DATE,sources=[dict(reference=source,locator=locator,accessed_at=DATE)],validation=dict(reviewed_by=None,reviewed_at=None,evidence=['Extração estática dos arquivos PBIP/TMDL; nenhuma execução de DAX/M ou consulta aos dados.']),pending=['Confirmar responsável de negócio e responsável técnico.','Revisar semântica com a área e validar resultados no modelo em execução.'])

def register(path,d):
    CAT.append(dict(id=d['id'],title=d['title'],type=d['type'],domain=d['domain'],status=d['status'],path=path))

def ydoc(path,d):
    write(path,yaml(d));register(path,d)

def mdoc(path,d,sections):
    text='---\n'+yaml(d)+'\n---\n\n# '+d['title']+'\n'
    for title,body in sections:
        text+='\n## '+title+'\n\n'+body+'\n'
    write(path,text);register(path,d)

def domain(t):
    if 'PlanProd' in t: return 'operacoes'
    if 'Logistica' in t: return 'logistica'
    if t.startswith(('d','f')): return 'comercial'
    return 'corporativo'

def metric_domain(m):
    f=m['properties'].get('displayFolder','')
    return 'financeiro' if f=='03 Financeiro' else 'logistica' if f=='04 Logística' else 'corporativo' if f in ('00 Auxiliares','Bi_novo') else 'comercial'

def mpath(m): return f"metrics/{metric_domain(m)}/{m['id']}.yaml"
def tpath(t): return f"data_products/{domain(t['name'])}/tabela_{slug(t['name'])}.md"
def esc(x): return str(x if x is not None else 'Pendente').replace('|','\\|').replace('\n','<br>')

# Explicações da implementação; descrições originais são preservadas separadamente.
DEFS={
'03 RSL':'Diferença entre faturamento e devolução total, conforme a implementação DAX. A expansão tributária da sigla deve ser confirmada na origem.',
'06 RL':'Soma dos máximos de ledger_net_subtotal por companhia e Ano0Mes. Não é uma simples soma de receita nem uma dedução explícita de tributos no DAX.',
'07 Preço Médio':'Razão entre RSL e unidades faturadas. A descrição original menciona faturamento, mas o numerador ativo é RSL.',
'05 Programado':'Total a faturar com data programada estritamente posterior a TODAY(). A descrição original usa maior ou igual.',
'00 Devolução':'Soma de receita de devoluções cujo depósito é diferente de 52, com adição de zero. Restrições por tipo fiscal e prefixo de SKU não estão ativas nesta medida.',
'01 Refaturamento':'Soma de receita de devoluções no depósito 52, com adição de zero. Confirmar o significado fiscal e os tratamentos upstream.',
'00 Faturamento':'Soma de receita para vendas faturadas ou parcialmente faturadas, usando a relação de data de movimento. Desconto de IPI/ST é declarado na descrição, não calculado explicitamente aqui.',
'08 Faturamento Bruto':'Soma de receita_bruta para vendas faturadas ou parcialmente faturadas, usando a relação de data de movimento.',
'09 Receita Bruta':'Faturamento bruto menos a medida Devolução_Bruta; esta última referencia a devolução total do modelo.',
'05 Devolução_Bruta':'Alias de Devolução Total na implementação ativa; não soma a coluna receita_bruta de devoluções.',
'00 Financeiro':'Parcela de Aberto: FARMAX pelo departamento FINANCEIRO; SANAVITA pelos bloqueios SERASA, TRAVA.FINANCEIRO, PEND.FINANCEIRA e TRAVA.LIMITE.CREDITO.',
'06 Ret.-Limit.créd.exc.':'Parcela de Financeiro com bloqueio Z5 em FARMAX ou TRAVA.LIMITE.CREDITO em SANAVITA.',
'02 Cancelado':'FARMAX: venda fora do depósito 52 com motivo de rejeição preenchido, por data de cancelamento. SANAVITA: venda CANCELADO, por data de pedido.',
'00 Logística':'Parcela de Aberto no departamento LOGISTICA mais Valor Logistica da tabela calculada tLogistica e CS.',
'00 Customer Service':'Parcela de Aberto no departamento CUSTOMER SERVICE mais Valor CS da tabela calculada tLogistica e CS.',
'06 Valor Entregue':'Faturamento na base selecionada com data de entrega preenchida e até TODAY(); a métrica mantém a data de movimento do faturamento.',
'07 Valor Em Transito':'Subtotal de pedidos de venda faturados/parciais com nota fiscal, entrega vazia ou futura e pedido a até 90 dias da maior data de pedido global.',
'10 Carteira Inicial':'Soma do subtotal do snapshot data_carteira no primeiro dia do mês da maior data selecionada; remove filtros de dTempo.',
'Faturamento Selecionado':'Seleciona faturamento bruto quando Base Receita é Receita Bruta; nos demais casos seleciona Faturamento.',
'Receita Selecionada':'Seleciona Receita Bruta quando Base Receita é Receita Bruta; nos demais casos seleciona RSL.',
'Devolução Selecionada':'Retorna Devolução Total em ambas as opções de Base Receita.',
'Meta RB':'Retorna o texto hífen; não contém uma meta numérica de receita bruta.',
'% Meta RB':'Retorna o texto hífen; não contém um percentual de atingimento de receita bruta.',
'07 Preço Médio Bruto':'Receita Bruta dividida por Unidades Faturadas, com resultado alternativo zero.',
'Meta RSL Exibição':'Meta RSL escalada por mil, com regras de ausência de movimento e indisponibilidade de meta por base e nível da matriz.',
'% Meta Exibição':'RSL dividido por Meta RSL, com regras de exibição que retornam zero para contextos sem meta e branco para linhas sem movimento.',
'Linha Matriz Possui Movimento':'Flag que retorna 1 quando a soma dos valores absolutos de vendas, receita, aberto, programado, faturamento e devolução é diferente de zero; caso contrário retorna branco.',
}

def metric_kind(m):
    n=m['name'];f=m['properties'].get('displayFolder','')
    if 'HTML' in n:return 'renderizacao_html'
    if n in ('Meta RB','% Meta RB'):return 'placeholder_textual'
    if f=='00 Auxiliares' or n.startswith(('Cor ','Label ','Legenda ','Aux ')) or n in ('Matriz RSL > Meta','RSL > Meta','RSL Abaixo','RSL Acima','Linha Matriz Possui Movimento'):return 'auxiliar_visual'
    if 'Matriz' in n or 'Exibição' in n:return 'medida_de_exibicao'
    if 'Selecionad' in n:return 'seletor_de_metrica'
    return 'indicador'

def physical(t):
    out=[]
    for p in t['partitions']:
        e=no_comments(p.get('expression') or '')
        if 'AmazonRedshift.Database' in e:
            nav=re.findall(r'\[Name="([^"]+)"\]',e)
            sql=re.findall(r'(?i)\b(?:from|join)\s+([a-z_]+\.[a-z_]+)',e)
            out.append(dict(engine='Amazon Redshift',database='farmax_prod',objects=sorted(set(sql or ['.'.join(nav)])),source_locator=f"{t['source']}:{p['source_line']}"))
        elif 'PowerPlatform.Dataflows' in e:
            out.append(dict(engine='Power Platform Dataflow',entities=re.findall(r'entity="([^"]+)"',e),upstream=None,source_locator=f"{t['source']}:{p['source_line']}"))
        else:out.append(dict(engine='DAX calculado' if p['kind']=='calculated' else 'Power Query local',upstream=None,source_locator=f"{t['source']}:{p['source_line']}"))
    return out

def closure(mid,seen=None):
    seen=set() if seen is None else seen
    if mid in seen:return seen
    seen.add(mid)
    for dep in MEASURES[mid]['measure_dependencies']:closure(dep,seen)
    return seen

missing_columns=[]
for m in DATA['measures']:
    title=re.sub(r'^\d+\s+','',m['name'])
    d=meta(m['id'],title,'metric',metric_domain(m),m['source'],f"medida {m['table']}[{m['name']}], linha {m['line']}")
    d['kind']=metric_kind(m)
    d['definition']=DEFS.get(m['name']) or m['description'] or ('Medida de composição visual; consultar implementação e inventário de cálculos internos.' if d['kind']=='renderizacao_html' else None)
    d['definition_basis']='leitura_da_implementacao' if m['name'] in DEFS or d['kind']=='renderizacao_html' else 'descricao_do_modelo' if m['description'] else None
    d['source_description']=m['description']
    d['business_questions']=None;d['synonyms']=[m['name']]
    d['unit']=None
    d['grain']={'source':None,'calculation':None}
    d['time']={'event':None,'timezone':None,'calendar':'dTempo; comportamento específico depende do contexto DAX','context_functions':m['context_functions']}
    d['formula']={'conceptual':None,'dependencies':m['measure_dependencies']}
    d['aggregation']={'rule':None,'additivity':None}
    d['dimensions']=None;d['relationships']=None
    d['filters']={'mandatory':None,'optional':None,'exclusions':None,'note':'Extrair os filtros efetivos da expressão e de suas dependências; não interpretar comentários históricos como regra ativa.'}
    deps=closure(m['id']);cols={(c['table'],c['column']) for mid in deps for c in MEASURES[mid]['column_dependencies']}
    tables=sorted({t for t,c in cols if t in TABLES} | {t for mid in deps for t in MEASURES[mid].get('table_dependencies',[]) if t in TABLES})
    d['data_sources']=[{'semantic_table':t,'physical_sources':physical(TABLES[t])} for t in tables]
    d['implementations']={'dax':{'expression':m.get('expression'),'table':m['table'],'properties':m['properties'],'execution_validated':False,'note':'Expressão extraída, preservando comentários. Fonte PBIP é a evidência; este contrato é um rascunho de ingestão.'}}
    d['dependencies']={'columns_direct':m['column_dependencies'],'tables_direct':m.get('table_dependencies',[]),'measures_transitive':sorted(deps-{m['id']}),'unqualified_references':sorted(set(m['unresolved_bracket_references'])),'method':'Extração lexical exclui comentários e literais de texto; referências sem tabela podem ser colunas virtuais, não erros de modelo.'}
    if m.get('expression_properties'):d['source_expression_properties']=m['expression_properties']
    d['edge_cases']=None;d['checks']=None
    d['usage']=[{'page_id':p['id'],'page_title':p['title'],'visual_id':v['id'],'source':v['source'],'locator':r['locator']} for p in DATA['pages'] for v in p['visuals'] for r in v['refs'] if r['kind']=='Measure' and r['property']==m['name']]
    for c in m['column_dependencies']:
        if c['table'] in TABLES and c['column'] not in [x['name'] for x in TABLES[c['table']]['columns']]:
            missing_columns.append({'metric_id':m['id'],**c})
            d['pending'].append(f"Referência ativa a {c['table']}[{c['column']}] não encontrada nas colunas desta exportação.")
    if not d['definition']:d['pending'].append('Descrição de negócio não declarada no modelo; formular com a área responsável.')
    d['pending'].append('Confirmar unidade/moeda, granularidade, aditividade e dimensões permitidas; não inferir a aprovação a partir dos relacionamentos existentes.')
    ydoc(mpath(m),d)

for t in DATA['tables']:
    path=tpath(t);d=meta('tabela_'+slug(t['name']),t['name'],'data_product',domain(t['name']),t['source'])
    rows=['| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |','|---|---|---|---|---|---|---|']
    for c in t['columns']:
        p=c['properties'];rows.append('| '+' | '.join(esc(x) for x in [c['name'],p.get('dataType'),p.get('sourceColumn'),p.get('summarizeBy'),p.get('isHidden','não declarado'),c['description'] or 'Não declarada',c['line']])+' |')
    specs='### Origem e linhagem\n\n```json\n'+json.dumps(physical(t),ensure_ascii=False,indent=2)+'\n```\n\n### Dicionário de colunas\n\n'+'\n'.join(rows)
    specs+='\n\nOs nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.\n'
    for c in t['columns']:
        if c.get('expression'):specs+=f"\n### Coluna calculada: {c['name']}\n\n```dax\n{c['expression']}\n```\n"
    for p in t['partitions']:
        specs+=f"\n### Partição: {p['name']}\n\nTipo: {p['kind']}. Propriedades: `{json.dumps(p['properties'],ensure_ascii=False)}`. Fonte: linha {p['source_line']}.\n\n"
        # Do not duplicate hostnames or full embedded rows; preserve source pointer.
        e=no_comments(p.get('expression') or '')
        if 'Binary.FromText' in e:specs+='Consulta M contém uma tabela embutida comprimida. Ver definição na fonte; não foi materializada como dados no catálogo.\n'
        else:
            e=re.sub(r'AmazonRedshift.Database\("[^"]+"', 'AmazonRedshift.Database("<endpoint na fonte original>"',e)
            specs+='```'+('dax' if p['kind']=='calculated' else 'powerquery')+'\n'+e.strip()+'\n```\n'
    if t['hierarchies']:
        specs+='\n### Hierarquias declaradas\n\n'+'\n'.join('```tmdl\n'+h['definition']+'\n```' for h in t['hierarchies'])
    related=[r for r in DATA['relationships'] if any(v.startswith(t['name']+'.') for k,v in r['properties'].items() if k in ('fromColumn','toColumn'))]
    users=[m for m in DATA['measures'] if any(c['table']==t['name'] for c in m['column_dependencies'])]
    deps='Relacionamentos: '+str(len(related))+f'. Consultar o [inventário técnico](../../{INGESTION}/modelo.md).\n\nMedidas com referência direta:\n\n'+'\n'.join('- '+link(m['name'],mpath(m),path) for m in users)
    mdoc(path,d,[('Objetivo','Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.'),('Definição e escopo','Objeto técnico observado na fonte de descoberta. Significado completo, granularidade e chaves naturais: pendentes de confirmação.'),('Especificação',specs),('Exemplos','Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.'),('Validação',f"Inventariadas {len(t['columns'])} colunas e {len(t['partitions'])} partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo."),('Dependências e impactos',deps),('Pendências','Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.'),('Fontes',link('Definição TMDL',t['source'],path))])

for r in DATA['relationships']:
    p=r['properties'];id='relacionamento_'+slug(r['name']);d=meta(id,p['fromColumn']+' → '+p['toColumn'],'relationship','corporativo',r['source'],f"relationship {r['name']}; linha {r['line']}")
    d.update(relationship_kind='semantic_model_join',from_object=p['fromColumn'],to_object=p['toColumn'],business_verb=None,declared_properties=p,cardinality={'from':p.get('fromCardinality'),'to':p.get('toCardinality'),'note':'null significa propriedade omitida no TMDL; não é cardinalidade medida nos dados.'},active_declared=p.get('isActive'),filter_direction_declared=p.get('crossFilteringBehavior'),join_sql=None,orphan_handling=None,fanout_risk='Revisar muitos-para-muitos e duplicidade das chaves; não traduzir relacionamento automaticamente em JOIN SQL.')
    ydoc(f'ontology/relationships/{id}.yaml',d)

# Preserve all column metadata in a machine-readable inventory as well as readable dictionaries.
write(f'{INGESTION}/colunas.json',json.dumps([{'table':t['name'],'source':t['source'],**c} for t in DATA['tables'] for c in t['columns']],ensure_ascii=False,indent=2))
write(f'{INGESTION}/manifesto_fontes.json',json.dumps(DATA['manifest'],ensure_ascii=False,indent=2))
write(f'{INGESTION}/uso_no_relatorio.json',json.dumps(DATA['pages'],ensure_ascii=False,indent=2))

model=['# Inventário técnico da primeira fonte','', '20 tabelas, 241 colunas, 90 medidas e 28 relacionamentos. Extração estática; estado inicial `draft`.','', '## Tabelas','', '| Tabela | Colunas | Partições |','|---|---:|---:|']
for t in DATA['tables']:model.append(f"| {link(t['name'],tpath(t),INGESTION+'/modelo.md')} | {len(t['columns'])} | {len(t['partitions'])} |")
model+=['','## Relacionamentos','', 'Valores não declarados permanecem pendentes; não são inferidos como resultados de testes de cardinalidade.','', '| Origem | Destino | Ativo declarado | Cardinalidade destino declarada | Contrato |','|---|---|---|---|---|']
for r in DATA['relationships']:
    p=r['properties'];rp=f"ontology/relationships/relacionamento_{slug(r['name'])}.yaml"
    model.append('| '+' | '.join([esc(p['fromColumn']),esc(p['toColumn']),esc(p.get('isActive','omitido')),esc(p.get('toCardinality','omitido')),link('abrir',rp,INGESTION+'/modelo.md')])+' |')
model+=['','## Segurança declarada','', 'As quatro roles abaixo declaram `modelPermission: read`. Os arquivos não contêm `tablePermission` ou filtros RLS. A associação de usuários e as permissões no serviço não estão disponíveis nesta exportação. Nomes como Acesso_Executivo não comprovam isolamento por executivo.','']
model+=['- '+link(r['definition'].splitlines()[0],r['source'],INGESTION+'/modelo.md') for r in DATA['roles']]
model+=['','## Parâmetros e atualização','', 'RangeStart e RangeEnd estão declarados em expressions.tmdl. Sua mera presença não comprova atualização incremental; as partições lidas não referenciam esses parâmetros. A tabela Atualização usa DateTimeZone.LocalNow com deslocamento -3; isso representa a execução da consulta, não comprova a data máxima dos eventos da origem.','', '## Método','', 'Extração lexical específica para este PBIP, guiada pela [sintaxe TMDL da Microsoft](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview). Comentários `///` são descrições; expressões e suas fontes foram preservadas. Não houve execução no Power BI.']
write(f'{INGESTION}/modelo.md','\n'.join(model))

pages=['# Uso observado na primeira fonte','', 'As referências incluem consultas, filtros e formatação. Uma referência em filtro não prova que o indicador é exibido. Elementos homônimos são identificados pelo ID. [Inventário detalhado](uso_no_relatorio.json).']
for p in DATA['pages']:
    pages+=['',f"## {p['title']} — {p['id']}",'',f"{len(p['visuals'])} visuais. Visibilidade declarada: {p['visibility'] or 'não especificada'}. Fonte: "+link('page.json',p['source'],INGESTION+'/paginas.md'),'', '| Visual | Tipo | Medidas referenciadas |','|---|---|---|']
    for v in p['visuals']:
        names=sorted(set(r['property'] for r in v['refs'] if r['kind']=='Measure'))
        links=[link(n,mpath(BYNAME[n]),INGESTION+'/paginas.md') if n in BYNAME else esc(n)+' **não encontrada**' for n in names]
        pages.append('| '+link(v['id'],v['source'],INGESTION+'/paginas.md')+' | '+esc(v['type'])+' | '+', '.join(links)+' |')
    cols=sorted(set(r['table']+'.'+r['property'] for v in p['visuals'] for r in v['refs'] if r['kind']=='Column' and r['table']))
    pages+=['','Campos referenciados: '+', '.join('`'+x+'`' for x in cols)+'.']
write(f'{INGESTION}/paginas.md','\n'.join(pages))

# Index every top-level variable in HTML expressions, including computational
# variables that do not exist as independent model measures. Do not mint fake measures.
var_inventory=[]
for m in DATA['measures']:
    if 'HTML' not in m['name']:continue
    e=m['expression'];masked=no_comments(e,True)
    matches=list(re.finditer(r'(?im)^VAR\s+(\w+)\s*=',masked))
    records=[]
    for i,a in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(e)
        ret=re.search(r'(?im)^RETURN\b',masked[a.end():end])
        if ret:end=a.end()+ret.start()
        expr=e[a.end():end].strip();clean=no_comments(expr,True)
        references=sorted(set(re.findall(r'\[([^\]]+)\]',clean)))
        functions=sorted(set(re.findall(r'\b([A-Z][A-Z0-9_.]*)\s*\(',clean)))
        records.append({'variable':a[1],'expression_line':e[:a.start()].count('\n')+1,'expression':expr,'references':references,'functions':functions,'classification':'calculo_ou_contexto' if references or any(f in functions for f in ['DIVIDE','SUMX','CALCULATE','COUNTROWS','DATESBETWEEN']) else 'apoio_ou_apresentacao'})
    var_inventory.append({'metric_id':m['id'],'variables':[{k:v for k,v in r.items() if k!='expression'} for r in records]})
    path=f"{INGESTION}/calculos_html/{m['id']}.md"
    text=f"# Cálculos internos — {m['name']}\n\nImplementação canônica: {link(m['name'],mpath(m),path)}. As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.\n\n| Variável | Linha DAX | Classificação | Referências |\n|---|---:|---|---|\n"
    for r in records:text+='| '+r['variable']+' | '+str(r['expression_line'])+' | '+r['classification']+' | '+esc(', '.join(r['references']))+' |\n'
    write(path,text)
write(f'{INGESTION}/variaveis_html.json',json.dumps(var_inventory,ensure_ascii=False,indent=2))

write(f'{INGESTION}/pendencias_referencias.json',json.dumps({'missing_qualified_columns':missing_columns,'missing_visual_measures':[{'page_id':p['id'],'visual':v['source'],**r} for p in DATA['pages'] for v in p['visuals'] for r in v['refs'] if r['kind']=='Measure' and r['property'] not in BYNAME]},ensure_ascii=False,indent=2))
write(f'{INGESTION}/indice_objetos.json',json.dumps(CAT,ensure_ascii=False,indent=2))
write('docs/catalogo.md','# Catálogo Atlas\n\nCatálogo canônico do Atlas. A primeira carga foi descoberta em um artefato mantido por uma área de negócio; a ferramenta e o arquivo de origem permanecem apenas na proveniência de cada objeto. Todos os objetos estão em rascunho. Medidas técnicas e de apresentação permanecem identificadas pelo campo `kind` e não equivalem a indicadores de negócio.\n\n| ID | Nome | Tipo | Domínio | Status |\n|---|---|---|---|---|\n'+'\n'.join('| '+link(x['id'],x['path'],'docs/catalogo.md')+' | '+esc(x['title'])+' | '+x['type']+' | '+x['domain']+' | '+x['status']+' |' for x in CAT))
print(json.dumps({'objects':len(CAT),'kinds':dict(Counter(metric_kind(m) for m in DATA['measures'])),'missing_qualified_columns':missing_columns,'html_variables':sum(len(v['variables']) for v in var_inventory)},ensure_ascii=False))
