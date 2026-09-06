# Avaliação da primeira ingestão do BI

Fonte: projeto `Farmax v3 (1)` em `powerbi/`. Coleta em 2026-09-06. Uso informado pelo usuário: acompanhamento dos indicadores da empresa pelos times.

O BI concentra vendas, faturamento, receitas, devoluções, carteira, metas, acompanhamento comercial e estoque. Há conhecimento relevante tanto no modelo quanto dentro das expressões que geram páginas HTML. O catálogo representa o que foi encontrado neste snapshot, sem certificar as regras ou alterar o dashboard.

## Cobertura

| Conteúdo | Quantidade | Onde consultar |
|---|---:|---|
| Tabelas semânticas | 20 | [Modelo e dicionários](modelo.md) |
| Colunas | 241 | Dicionários por tabela e [índice técnico](colunas.json) |
| Medidas DAX | 90 | [Catálogo](../catalogo.md) |
| Relacionamentos do modelo | 28 | [Modelo](modelo.md) |
| Páginas / visuais | 6 / 65 | [Páginas](paginas.md) |
| Roles declaradas | 4 | [Segurança declarada](modelo.md#segurança-declarada) |
| Dimensões documentadas | 14 | [Catálogo](../catalogo.md) |
| Entidades propostas | 11 | [Ontologia](ontologia.md) |
| Conceitos / regras | 16 / 10 | [Catálogo](../catalogo.md) |
| Variáveis de nível superior nas 6 medidas HTML | 967 | [Índice de variáveis](variaveis_html.json) |
| Arquivos de origem com hash | 118 | [Manifesto](manifesto_fontes.json) |

Das 90 medidas, a classificação inicial identifica 57 indicadores, 14 auxiliares visuais, 6 renderizadores HTML, 8 medidas de exibição, 3 seletores e 2 placeholders textuais. Essa classificação é documental, não aprovação de negócio. Apenas 37 medidas têm descrição declarada; nenhuma das 241 colunas tem descrição `///` na fonte. As lacunas foram mantidas em vez de preencher definições fictícias.

## Indicadores fundamentais

| Tema | O que está implementado | Contrato |
|---|---|---|
| Venda | Subtotal de pedidos VENDA, excluindo depósito 52. | [Valor de Vendas](../../metrics/comercial/bi_00_valor_de_vendas.yaml) |
| Faturamento | Receita de vendas faturadas/parciais por data de movimento. | [Faturamento](../../metrics/comercial/bi_00_faturamento.yaml) |
| RSL | Faturamento menos devolução total. | [RSL](../../metrics/comercial/bi_03_rsl.yaml) |
| RL | Agregação de máximos de ledger_net_subtotal por companhia e mês. | [RL](../../metrics/comercial/bi_06_rl.yaml) |
| Receita bruta | Faturamento bruto menos Devolução_Bruta. | [Receita Bruta](../../metrics/comercial/bi_09_receita_bruta.yaml) |
| Devolução | Parcelas dentro e fora do depósito 52. | [Devolução Total](../../metrics/comercial/bi_02_devolucao_total.yaml) |
| Carteira | Total a faturar dividido entre programação até hoje e futura. | [Aberto](../../metrics/comercial/bi_04_aberto.yaml), [Programado](../../metrics/comercial/bi_05_programado.yaml) |
| Meta | Meta RSL por contexto comercial e data-alvo. | [Meta RSL](../../metrics/comercial/bi_meta_rsl.yaml) |
| Preço médio | RSL por unidade faturada. | [Preço Médio](../../metrics/comercial/bi_07_preco_medio.yaml) |
| Estoque | Cobertura, plano médio, estoque e carteira por SKU calculados dentro do HTML. | [Carteira e Estoque](../../metrics/corporativo/bi_carteira_e_estoque_html_v1.yaml) |

Não há base para certificar uma métrica de custo de frete/frete por kg neste snapshot: a área chamada Logística trata de pedidos pendentes, entregues e em trânsito.

## Linhagem observada

- **Redshift / comercial:** fatos de vendas/faturamento, devoluções, metas de executivos e carteira; dimensões de clientes, executivos e EAN/produto. Metas gerais são agregadas por SQL a partir de `comercial.obt_sales`.
- **Redshift / cadastro:** regional vem de consulta nativa a `cadastro.dim_regional`.
- **Redshift / operacoes:** planejamento e posição de estoque vêm de `operacoes.fato_plan_prod_unificada`.
- **Dataflows:** empresa, calendário e UF. As transformações anteriores às entidades do dataflow não estão nesta exportação.
- **Definições locais:** feriados embutidos, horário de atualização, seletor de receita, gradiente, parâmetro de matriz e tabela calculada de Logística/CS.

Cada dicionário preserva os nomes físicos confirmados, a transformação M/DAX e a localização da fonte. O nome de uma view não revela seu SQL upstream. A origem de impostos e a granularidade das views continuam pendentes.

## Pendências de maior impacto

### Referências não encontradas

`Meta RL` e `Meta de Unidades Faturadas` usam `fMeta_Geral[company]`. A tabela exportada contém `obt_company`, mas não `company`. Isso merece revisão do modelo/exportação antes de usar essas metas como referência. Não substituí o campo automaticamente. [Detalhes](pendencias_referencias.json).

A matriz na página `e7a7a2fc000d0a5b0c10` tem uma entrada de filtro para `04 Aberto Ajustado`, medida ausente nas 90 definições. A entrada não apresenta condição no trecho inspecionado: pode ser referência residual. Não é evidência, por si só, de que o visual falha ao executar. [Mapa de páginas](paginas.md).

### Descrição e expressão divergem

- **Preço Médio:** a descrição diz faturamento por unidades, mas o numerador ativo é RSL.
- **Programado:** a descrição diz data maior ou igual a hoje; a expressão usa estritamente maior.
- **Devolução/refaturamento:** descrições incluem prefixos de SKU e tipos fiscais que não são filtros ativos dessas medidas. Parte está comentada; confirmar se as restrições ocorrem nas views.

As descrições originais e a leitura da implementação estão separadas nos contratos para permitir revisão sem perda da evidência.

### Receita bruta, devolução e refaturamento

`Devolução_Bruta` referencia `Devolução Total`, embora `fDevolucao_unificada` tenha uma coluna `receita_bruta`. O cálculo não prova uma devolução efetivamente bruta. No HTML de Pedidos & Faturamentos, `vDevRefTotal` soma devolução total com refaturamento, que já integra o total. Isso sugere duplicação dessa parcela de apresentação e precisa de reconciliação. [Regra documentada](../../business_rules/comercial/bi_anatomia_nota.md).

### Logística e CS usam uma tabela desconectada

`tLogistica e CS` é calculada agrupando valores e quantidades, sem chave de pedido/empresa/data. Não há relacionamento declarado para essa tabela. Somá-la às medidas de Logística/CS pode adicionar valores fora do contexto dos filtros, além de agrupar itens distintos com os mesmos valores. Não foi calculado o impacto numérico. [Dicionário](../../data_products/logistica/bi_tabela_tlogistica_e_cs.md).

### Metas e granularidade

Há um relacionamento com destino `many` entre marca das metas e `brand_novo` de material. `fMeta_Geral` tem relação apenas com empresa, sem relação de data declarada. Avaliar filtros temporais e por produto antes de reutilizar metas em novos níveis de análise. `Meta RSL` e `Meta Média` deduplicam conjuntos diferentes de campos. [Modelo](modelo.md).

`Meta RB` e `% Meta RB` retornam `"-"`. As medidas de exibição da matriz têm formato dinâmico que mostra `N/A` em determinados contextos. Ausência de meta, zero e texto de apresentação devem permanecer distintos.

### Calendários e janelas temporais

`fVendas_unificada` filtra `data_pedido > 2024-01-01`; `dTempo` filtra `Ano > 2024`, começando em 2025. Comparações com 2024 e eventos sem correspondência no calendário exigem revisão. A presença de RangeStart/RangeEnd não prova atualização incremental.

O HTML executivo conta dias úteis por `dTempo.DiaUtil`, cuja consulta marca apenas fins de semana. `Meta Diária Atual` usa NETWORKDAYS com feriados; outra medida usa dias planejados de metas gerais. Os denominadores diferem. [Regra de dias úteis](../../business_rules/comercial/bi_dias_uteis_calendarios.md).

### Cálculos embutidos não são necessariamente indicadores oficiais

- Projeção de fechamento: extrapolação do ritmo por dia útil; `vGapProjetado` é realizado menos meta, apesar do nome.
- Estoque: valores usam ticket calculado em janela de 90 dias; subtotais são do Top 20 por demanda valorizada. Não equivalem automaticamente ao estoque contábil ou total da empresa.
- Pareto: implementação de classe A usa acumulado até 80% mais 1; requer revisão de casos de borda.
- Anatomia da nota: o piso visual de 18% para a largura dos impostos não é uma alíquota. A proxy chamada margem não usa custo de mercadoria.

Os índices de variáveis preservam o vínculo com a expressão completa sem promover componentes visuais a métricas certificadas.

### Acesso e atualização

As quatro roles contêm permissão de leitura, sem filtros RLS declarados. Não foram coletadas associações de usuários no serviço. O timestamp de atualização vem da consulta local; não comprova a atualidade dos dados upstream.

## Limites desta entrega

Foi realizada leitura estática dos arquivos PBIP, TMDL e JSON. As expressões e seus vínculos foram extraídos por um parser específico para esta estrutura. Não houve abertura visual/execução do dashboard, consulta ao Redshift/Fabric, extração de registros do cache, validador automático ou alteração das fontes. Por isso, erros de referência e riscos descritos aqui são achados do snapshot, não resultados de testes em produção.

O próximo passo útil é revisar primeiro receitas/devoluções, datas, metas e granularidade com os responsáveis, usando o [catálogo](../catalogo.md) como pauta de trabalho.
