"""Registra a curadoria inicial do snapshot de 2026-09-06; não sobrescreve contratos."""
from ingest_powerbi import *
import os

D=extract(); TS={t['name']:t for t in D['tables']}; MS={m['name']:m for m in D['measures']}
DATE='2026-09-06'; ADDED=[]

def yaml(x,n=0):
    pad='  '*n
    if isinstance(x,dict):
        return '\n'.join(pad+k+':\n'+yaml(v,n+1) if isinstance(v,(dict,list)) and v else pad+k+': '+json.dumps(v,ensure_ascii=False) for k,v in x.items())
    return '\n'.join(pad+'-\n'+yaml(v,n+1) if isinstance(v,dict) else pad+'- '+json.dumps(v,ensure_ascii=False) for v in x)

def write(p,s):
    p=ROOT/p
    if p.exists():raise FileExistsError(p)
    p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s.rstrip()+'\n',encoding='utf-8')

def mdomain(m):
    f=m['properties'].get('displayFolder','')
    return 'financeiro' if f=='03 Financeiro' else 'logistica' if f=='04 Logística' else 'corporativo' if f in ('00 Auxiliares','Bi_novo') else 'comercial'

def metric_path(name):
    m=MS[name];return f"metrics/{mdomain(m)}/{m['id']}.yaml"

def link(label,target,current):
    return f'[{label}](<'+os.path.relpath(ROOT/target,(ROOT/current).parent).replace('\\','/')+'>)'

def meta(id,title,type,domain,sources):
    return dict(schema_version=1,id=id,title=title,type=type,domain=domain,status='draft',version='0.1.0',owners=dict(business=None,technical=None),created_at=DATE,updated_at=DATE,sources=[dict(reference=p,locator=l,accessed_at=DATE) for p,l in sources],validation=dict(reviewed_by=None,reviewed_at=None,evidence=['Leitura estática do snapshot PBIP; sem execução ou certificação de negócio.']),pending=['Confirmar interpretação, responsáveis e comportamento com dados reais.'])

def save(path,d,body=None):
    write(path,yaml(d) if body is None else '---\n'+yaml(d)+'\n---\n\n# '+d['title']+'\n\n'+body)
    ADDED.append(dict(id=d['id'],title=d['title'],type=d['type'],domain=d['domain'],status='draft',path=path))

ENTITIES=[
('cliente','Cliente','dClientes_unificada','chave_cliente','Organização ou pessoa representada pelo cadastro de clientes; a natureza exata deve ser confirmada. Não assumir que cliente, grupo e raiz de documento são a mesma entidade.'),
('produto','Produto / SKU','dMaterial_unificada','codigo_produto','Item de material do cadastro unificado, com marca, segmento, classificação e atributos de produto. EAN e SKU não devem ser tratados como equivalentes sem verificar as chaves.'),
('empresa','Empresa / companhia','dEmpresa','Company','Companhia usada para segmentar os fatos; Empresa e Description são níveis de apresentação observados no relatório.'),
('executivo','Executivo comercial','dExecutivos_unificada','executivo_chave','Responsável comercial cadastrado com coordenador e gerente regional; hierarquia inferida dos atributos, não validação de responsabilidade atual.'),
('regional','Regional comercial','dRegional','order_sale_order_office_code','Agrupamento comercial codificado; sua relação com região geográfica não é identidade.'),
('pedido','Pedido de venda','fVendas_unificada',None,'Objeto comercial com número de pedido, cliente, produto, data e status. A tabela mistura atributos de pedido e faturamento; a chave do item e sua unicidade não estão declaradas.'),
('faturamento','Evento de faturamento','fVendas_unificada',None,'Evento representado por nota fiscal, data de movimento, valores e quantidades faturadas. Não equivale ao momento de criação do pedido.'),
('devolucao','Evento de devolução','fDevolucao_unificada',None,'Evento com data de movimento, cliente, SKU, nota e depósito. Depósito 52 é tratado como refaturamento nas medidas; validar a semântica fiscal.'),
('meta_comercial','Meta comercial','fMeta_unificada',None,'Objetivo por contexto comercial e data-alvo. A medida Meta RSL agrupa empresa, executivo, regional, segmento, marca, receita e data; isso não prova a chave natural da origem.'),
('posicao_estoque','Posição de estoque e planejamento','fPlanProd_unificada',None,'Posição por referência de data, companhia e SKU, inferida dos campos; medidas de estoque exigem confirmar a regra de snapshot e não somar datas indiscriminadamente.'),
('snapshot_carteira','Snapshot de carteira','fCarteira_pedidos_unificada',None,'Registro de carteira associado à data_carteira, com valores e quantidades de pedido e faturamento. Confirmar granularidade item × snapshot.')]
for id,title,table,key,definition in ENTITIES:
    t=TS[table];d=meta(id,title,'entity','operacoes' if id=='posicao_estoque' else 'comercial',[(t['source'],'declaração de tabela e colunas')])
    d.update(definition=definition,evidence_level='interpretacao_proposta_a_partir_do_modelo',identifier=key,identifier_basis='coluna usada pelo modelo; unicidade não testada' if key else None,grain=None,attributes=[c['name'] for c in t['columns']],physical_mappings=[dict(semantic_table=table,source=t['source'])])
    save(f'ontology/entities/{id}.yaml',d)

DIMS=[
('cliente','Cliente','dClientes_unificada','chave_cliente','cliente',['cliente','cliente_grupo','nome_grupo','cliente_cpf_cnpj_raiz'],'Cliente e agrupamentos usados em análises comerciais. Confirmar quando consolidar por grupo ou documento.'),
('produto','Produto / SKU','dMaterial_unificada','codigo_produto','produto',['codigo_produto','descricao','ean'],'Produto usado nos filtros, pedidos e estoque; confirmar unicidade entre empresas.'),
('marca','Marca','dMaterial_unificada',None,'produto',['marca','brand_novo'],'O modelo contém marca e brand_novo. A matriz e várias análises usam brand_novo; não unificar os campos por semelhança de nome.'),
('segmento','Segmento','dMaterial_unificada',None,'produto',['segmento','novo_segmento'],'Segmentação de produto; segmento e novo_segmento coexistem e exigem tabela de correspondência validada.'),
('classificacao_sku','Classificação SKU','dMaterial_unificada',None,'produto',['level'],'Classificação de produto apresentada como CLASSIFICAÇÃO SKU na matriz dinâmica.'),
('empresa','Empresa / companhia','dEmpresa','Company','empresa',['Company','Description','Empresa','Grupo'],'Eixo organizacional do relatório; inclui apresentação Empresa > Description nos visuais.'),
('executivo','Executivo','dExecutivos_unificada','executivo_chave','executivo',['executivo_cod','executivo_nome','nome_unificado','coordenador_cod','coordenador_nome','gerente_regional_nome'],'Responsável comercial; nome_unificado é usado pela matriz dinâmica.'),
('regional','Regional comercial','dRegional','order_sale_order_office_code','regional',['order_sale_order_office_code','order_sale_order_office'],'Regional de vendas carregada com regras explícitas de seleção e normalização.'),
('tempo','Calendário','dTempo','Data',None,['Data','Ano','MesNum','MesNome','DiaNum','DiaUtil'],'Calendário comum. O evento temporal é escolhido por cada medida, não apenas pelo slicer.'),
('canal','Canal de venda','fVendas_unificada',None,'pedido',['canal_n1'],'Canal usado diretamente no fato de vendas pelo HTML Comercial; compatibilidade com outras tabelas não confirmada.'),
('status_pedido','Status do pedido','fVendas_unificada',None,'pedido',['pedido_status','pedido_tipo','obt_sales_department_status'],'Status comercial, tipo e departamento são campos distintos; regras variam por empresa.'),
('geografia_cliente','Geografia do cliente','dClientes_unificada',None,'cliente',['cidade','estado','pais','regiao'],'Geografia do cadastro. A tabela dUF também contém dados geográficos, mas não tem relacionamento declarado neste modelo.'),
('base_receita','Base de receita','Base Receita',None,None,['Base Receita','Ordem'],'Seletor desconectado com Receita Semi Liquida e Receita Bruta. Altera medidas via SELECTEDVALUE/SWITCH.'),
('matriz_dinamica','Eixo da matriz dinâmica','Parâmetros: Matriz Dinâmica',None,None,['Parâmetro 2','Parâmetro 2 Campos','Parâmetro 2 Pedido'],'Parâmetro de campo que escolhe regional, executivo, cliente, marca, segmento, classificação SKU ou SKU.')]
for id,title,table,key,entity,attrs,definition in DIMS:
    t=TS[table];d=meta('bi_dim_'+id,title,'dimension','comercial',[(t['source'],'colunas e partição')])
    refs=[m['id'] for m in D['measures'] if any(c['table']==table and c['column'] in attrs for c in m['column_dependencies'])]
    d.update(definition=definition,entity=entity,key=key,attributes=attrs,hierarchy=None,physical_mapping=dict(semantic_table=table,columns=attrs),unknown_values=None,historical_behavior=None,compatible_metrics=None,observed_metric_references=refs,compatibility_note='Uso observado não comprova compatibilidade semântica de todos os níveis; revisar granularidade e filtros.')
    save(f'dimensions/comercial/bi_dim_{id}.yaml',d)

CONCEPTS=[
('venda','Venda registrada','00 Valor de Vendas','Valor dos pedidos classificados como VENDA, excluindo depósito 52. Não exige status faturado na medida. Não é faturamento.'),
('faturamento','Faturamento','00 Faturamento','Valor de receita de pedidos faturados/parciais por data de movimento. A origem declara desconto de IPI/ST; confirmar a transformação upstream.'),
('receita_semi_liquida','Receita semi líquida (RSL)','03 RSL','Resultado após deduzir devolução total do faturamento. Não confundir com a coluna receita ou com o seletor Faturamento Selecionado.'),
('receita_liquida','Receita líquida (RL)','06 RL','Implementada como agregação dos máximos de ledger_net_subtotal por companhia e Ano0Mes. Requer validação contábil da origem e da repetição do valor nas linhas.'),
('receita_bruta','Receita bruta no dashboard','09 Receita Bruta','No modelo, Receita Bruta já deduz Devolução_Bruta de Faturamento Bruto. O rótulo não significa soma bruta sem deduções.'),
('devolucao_total','Devolução total e refaturamento','02 Devolução Total','Devolução Total inclui as parcelas fora e dentro do depósito 52. Somar Refaturamento novamente duplica essa parcela.'),
('carteira_aberta','Carteira aberta','04 Aberto','A faturar com programação até hoje, independentemente do filtro de calendário removido pela medida base. Não equivale a toda a carteira pendente.'),
('programado','Programado','05 Programado','A faturar com programação posterior a hoje. Programado M+ usa outra regra de mês/ano e não é sinônimo exato.'),
('venda_efetiva','Venda efetiva','00 Venda Efetiva','Venda registrada menos cancelado e programado M+. O resultado depende de datas de eventos que diferem entre as parcelas.'),
('meta','Meta e atingimento','Meta RSL','Meta RSL é deduplicada por um conjunto de campos antes da soma. As metas de RL e unidades usam outra fonte, com referência pendente a uma coluna ausente.'),
('entregue_transito','Entregue e em trânsito','06 Valor Entregue','Entregue usa data de entrega preenchida até hoje sobre faturamento. Em trânsito usa subtotal e janela por data de pedido; não presumir que somam o faturamento sem diferença.'),
('dias_uteis','Dias úteis e projeção','Farmax BI HTML v2','A projeção do HTML usa DiaUtil do calendário (segunda a sexta no M). Meta Diária Atual usa NETWORKDAYS com dFeriado. Os dois calendários úteis precisam ser reconciliados.'),
('estoque_cobertura','Estoque, demanda e cobertura','Carteira e Estoque HTML v1','Estoque, plano médio e cobertura são agregados por SKU dentro do HTML. O alvo visual é 15 dias; a unidade do plano e a validade do alvo exigem confirmação.'),
('pareto_clientes','Pareto de clientes','Comercial HTML v1','Receita por grupo de cliente é ordenada para calcular concentração. A regra observada para classe A conta acumulados até 80% e adiciona 1; confirmar empates e limites.'),
('mes_parcial','Mês parcial e comparabilidade','Farmax BI HTML v2','O HTML aplica corte de data para comparar mês corrente com períodos anteriores. Medidas abertas tradicionais usam maior data de movimento; não presumir resultados idênticos.'),
('margem_proxy','Proxy de margem na apresentação','Pedidos & Faturamentos HTML','vMargemProxy divide receita selecionada por valor vendido; não é margem contábil, pois não usa custo de mercadoria.'),
]

def narrative(id,title,type,domain,definition,names,extra='',pending='Confirmar significado, responsáveis e uso oficial com a área.'):
    sources=[(MS[n]['source'],f"medida {n}; linha {MS[n]['line']}") for n in names]
    d=meta(id,title,type,domain,sources);path=f"ontology/concepts/{id}.md" if type=='concept' else f"business_rules/{domain}/{id}.md"
    refs='\n'.join('- '+link(n,metric_path(n),path) for n in names)
    body='## Objetivo\n\n'+definition+'\n\n## Definição e escopo\n\nInterpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.\n\n## Especificação\n\n'+(extra or 'As expressões são mantidas nos contratos canônicos abaixo. Consultar também os filtros das páginas e as dependências transitivas.')+'\n\n'+refs+'\n\n## Exemplos\n\nUsar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.\n\n## Validação\n\nLeitura estática; sem execução DAX, comparação numérica ou revisão de negócio.\n\n## Dependências e impactos\n\nMudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.\n\n## Pendências\n\n'+pending+'\n\n## Fontes\n\n'+refs
    save(path,d,body)

for id,title,name,definition in CONCEPTS:narrative('bi_'+id,title,'concept','operacoes' if id=='estoque_cobertura' else 'comercial',definition,[name])

RULES=[
('bases_receita','Bases de receita e apresentação',['Faturamento Selecionado','Receita Selecionada','Devolução Selecionada','Meta RB','% Meta RB'],'A seleção Receita Bruta escolhe as medidas brutas; o restante usa a base semi líquida. Devolução é a mesma nos dois ramos. Meta RB e % Meta RB são placeholders de texto, não valores zero.','Condição: Base Receita via SELECTEDVALUE. Ação: selecionar medidas canônicas. Escopo: matriz e HTML. Autoridade e vigência: pendentes; evidência é o snapshot do modelo.'),
('datas_eventos','Datas dos eventos',['00 Valor de Vendas','00 Faturamento','02 Cancelado','04 Aberto'],'Pedido usa a relação padrão com data_pedido; faturamento ativa data_movimento. Cancelamento FARMAX usa sale_cancellation_date, SANAVITA usa data_pedido. A carteira pendente remove filtros de dTempo.','Não comparar indicadores como se todos representassem eventos ocorridos no mesmo período. Registrar o evento de cada parcela e os filtros adicionais do visual.'),
('separacao_pendencias','Distribuição de pendências por área',['00 Financeiro','06 Ret.-Limit.créd.exc.','00 Logística','00 Customer Service','06 Aguarda Produção'],'Os motivos de pendência derivam de departamentos e bloqueios; financeiro tem regras específicas por empresa. Logística e CS acrescentam uma tabela calculada desconectada.','tLogistica e CS divide valores conforme quantidades de pedido e entrega e agrupa por valores, não por uma chave do pedido. Não há relação declarada dessa tabela com empresa, tempo ou produto. Avaliar perda de contexto e repetição dos valores antes de confiar nas decomposições.'),
('matriz_exibicao','Unidade e ausência de meta na matriz',['Meta RSL Exibição','% Meta Exibição','Vendido Matriz','Linha Matriz Possui Movimento'],'Medidas da matriz dividem valores por 1000. Algumas retornam zero quando não há meta compatível e branco quando não há movimento.','A indisponibilidade depende de base bruta e níveis cliente_grupo, descricao, level e novo_segmento. Esse zero é uma convenção visual, não aprovação de meta zero.'),
('projecao_fechamento','Projeção, ritmo e gap',['Farmax BI HTML v2'],'O painel executivo projeta fechamento a partir do ritmo por dia útil; o campo vGapProjetado, apesar do nome, calcula realizado menos meta.','Variáveis: vRitmoAtualDU = receita / dias úteis realizados; vProjecaoFechamento = ritmo × dias úteis totais; vRitmoNecessarioDU = receita faltante / dias restantes. A projeção é extrapolação, não previsão estatística. Gap não usa a projeção nessa implementação. Sem meta, status SEM META.'),
('estoque_valorizacao','Estoque e carteira por SKU',['Carteira e Estoque HTML v1'],'O HTML filtra demanda positiva e status diferente de INATIVO/DESCONTINUADO. Mostra os 20 SKUs por DemandaValor e seus subtotais.','TicketMedio usa receita/quantidade de FATURADO na janela de 90 dias da maior data de pedido global, removendo filtros. EstoqueCalculadoValor = estoque × ticket; DemandaValor = demanda × ticket; EstoqueTotalValor acrescenta A Faturar. Não equivale automaticamente a estoque físico ou valorização contábil. O subtotal se refere ao Top 20, não a todos os SKUs.'),
('carteira_data_referencia','Período do painel Carteira & Estoque',['Carteira e Estoque HTML v1','00 Atualização'],'A página define snapshot até a data de atualização e fluxo no mês dessa referência, construindo filtros que removem dTempo.','O código tenta converter o texto de atualização em data e usa TODAY() em caso de erro. Confirmar o parse e a interação efetiva entre filtros do HTML e REMOVEFILTERS das medidas base. O comentário sobre ignorar slicers não substitui um teste de contexto.'),
('dias_uteis_calendarios','Calendários úteis distintos',['Meta Diária Atual','Farmax BI HTML v2','Meta Média'],'Há pelo menos três origens para dias úteis: dTempo.DiaUtil, NETWORKDAYS com dFeriado e general_target_days.','dTempo exclui sábado e domingo no M, sem consultar dFeriado. Não usar intercambiavelmente esses denominadores até revisar feriados, mês corrente, corte de atualização e contexto da meta.'),
('anatomia_nota','Anatomia da nota e proxies',['Pedidos & Faturamentos HTML'],'O HTML chama de impostos a diferença positiva entre Receita Bruta e RSL. A largura visual dessa parcela tem piso de 18%.','O piso é de apresentação, não alíquota. A diferença entre receitas não comprova a decomposição tributária. A variável vDevRefTotal soma devolução total e refaturamento; como devolução total já o inclui, há risco de duplicação dessa parcela na apresentação.'),
('pareto_classificacao','Classificação Pareto',['Comercial HTML v1'],'O HTML calcula receita por cliente/grupo, ranking denso e participação acumulada; usa 80% para delimitar classe A.','A implementação adiciona 1 ao número de clientes com participação acumulada até 80%. Rever empates, conjunto vazio, único cliente e a delimitação do cliente que cruza o limiar. O Top 15 exibido não corresponde necessariamente ao universo inteiro do Pareto.'),
]
for id,title,names,definition,extra in RULES:narrative('bi_'+id,title,'business_rule','operacoes' if 'estoque' in id else 'comercial',definition,names,extra)

cat=ROOT/'docs/catalogo.md'
with cat.open('a',encoding='utf-8') as f:
    for x in ADDED:f.write('| '+link(x['id'],x['path'],'docs/catalogo.md')+' | '+x['title']+' | '+x['type']+' | '+x['domain']+' | draft |\n')
index=ROOT/'docs/powerbi/indice_objetos.json';all_objects=json.loads(read(index))+ADDED;index.write_text(json.dumps(all_objects,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'added_semantic_objects':len(ADDED),'total_objects':len(all_objects)},ensure_ascii=False))
