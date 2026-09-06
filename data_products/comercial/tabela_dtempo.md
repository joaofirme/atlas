---
schema_version: 1
id: "tabela_dtempo"
title: "dTempo"
type: "data_product"
domain: "comercial"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dTempo.tmdl"
    locator: "arquivo completo"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Extração estática dos arquivos PBIP/TMDL; nenhuma execução de DAX/M ou consulta aos dados."
pending:
  - "Confirmar responsável de negócio e responsável técnico."
  - "Revisar semântica com a área e validar resultados no modelo em execução."
---

# dTempo

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "Power Platform Dataflow",
    "entities": [
      "dTempo"
    ],
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dTempo.tmdl:145"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| DiaNum | int64 | DiaNum | none | não declarado | Não declarada | 5 |
| DiaComZero | string | DiaComZero | none | não declarado | Não declarada | 16 |
| MesNum | int64 | MesNum | none | não declarado | Não declarada | 24 |
| MesComZero | string | MesComZero | none | não declarado | Não declarada | 33 |
| MesNome | string | MesNome | none | não declarado | Não declarada | 41 |
| MesNomeAbrev | string | MesNomeAbrev | none | não declarado | Não declarada | 50 |
| Ano | int64 | Ano | none | não declarado | Não declarada | 61 |
| Data | dateTime | Data | none | não declarado | Não declarada | 72 |
| Mes/Ano | string | Mes/Ano | none | não declarado | Não declarada | 82 |
| Ano0Mes | string | Ano0Mes | none | não declarado | Não declarada | 93 |
| Ano/MesNum | string | Ano/MesNum | none | não declarado | Não declarada | 101 |
| Estação | string | Estação | none | não declarado | Não declarada | 109 |
| DiaCorrente | string | DiaCorrente | none | não declarado | Não declarada | 117 |
| DiaSemanaAbrev | string | DiaSemanaAbrev | none | não declarado | Não declarada | 125 |
| DiaUtil | int64 | DiaUtil | sum | não declarado | Não declarada | 133 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dTempo-b074aa8d-3514-4068-bd7d-574f5a1e77ca

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 145.

```powerquery
let
    Source = PowerPlatform.Dataflows(null),
    Workspaces = Source{[Id="Workspaces"]}[Data],
    #"4c88a2b6-9309-4368-9a28-168154f1d083" = Workspaces{[workspaceId="4c88a2b6-9309-4368-9a28-168154f1d083"]}[Data],
    #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e" = #"4c88a2b6-9309-4368-9a28-168154f1d083"{[dataflowId="e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"]}[Data],
    dTempo_ = #"e935f8e3-404f-4bbd-8fbb-8942c0e6f04e"{[entity="dTempo",version=""]}[Data],
    #"Removed Other Columns" = Table.SelectColumns(dTempo_,{"Data", "DiaNum", "DiaComZero", "MesNum", "MesComZero", "MesNome", "MesNomeAbrev", "Ano", "Mes/Ano", "Ano0Mes", "Ano/MesNum", "DiaSemanaAbrev", "Estação"}),
    AdicionarDia = Table.AddColumn(#"Removed Other Columns", "DiaCorrente", each DateTime.ToText(DateTime.LocalNow(), "dd")),
    #"Ano > 2024" = Table.SelectRows(AdicionarDia, each [Ano] > 2024),
    #"Added Conditional Column" = Table.AddColumn(#"Ano > 2024", "DiaUtil", each if [DiaSemanaAbrev] = "sáb" then 0 else if [DiaSemanaAbrev] = "dom" then 0 else 1, type any),
    #"Changed Type" = Table.TransformColumnTypes(#"Added Conditional Column",{{"Data", type datetime}, {"DiaUtil", Int64.Type}})
in
    #"Changed Type"
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 15 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 7. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [04 RSL YoY](<../../metrics/comercial/metrica_rsl_yoy.yaml>)
- [01 Unidades Faturadas](<../../metrics/comercial/metrica_unidades_faturadas.yaml>)
- [Meta Diária Atual](<../../metrics/comercial/metrica_meta_diaria_atual.yaml>)
- [Meta Média](<../../metrics/comercial/metrica_meta_media.yaml>)
- [00 Faturamento](<../../metrics/comercial/metrica_faturamento.yaml>)
- [06 RL](<../../metrics/comercial/metrica_rl.yaml>)
- [03 Texto Dias Úteis](<../../technical/measures/corporativo/metrica_texto_dias_uteis.yaml>)
- [04 RSL YoY Fechado %](<../../metrics/comercial/metrica_rsl_yoy_fechado_percentual.yaml>)
- [04 RSL MoM Fechado%](<../../metrics/comercial/metrica_rsl_mom_fechado_percentual.yaml>)
- [04 RSL YoY Aberto %](<../../metrics/comercial/metrica_rsl_yoy_aberto_percentual.yaml>)
- [04 RSL MoM Aberto %](<../../metrics/comercial/metrica_rsl_mom_aberto_percentual.yaml>)
- [04 % Vendas MoM](<../../metrics/comercial/metrica_percentual_vendas_mom.yaml>)
- [04 % Vendas YoY](<../../metrics/comercial/metrica_percentual_vendas_yoy.yaml>)
- [04 Meta RSL MoM %](<../../metrics/comercial/metrica_meta_rsl_mom_percentual.yaml>)
- [04 Meta RSL YoY %](<../../metrics/comercial/metrica_meta_rsl_yoy_percentual.yaml>)
- [04 % Unidades MoM](<../../metrics/comercial/metrica_percentual_unidades_mom.yaml>)
- [04 % Unidades YoY](<../../metrics/comercial/metrica_percentual_unidades_yoy.yaml>)
- [Aux Max Mês](<../../technical/measures/comercial/metrica_aux_max_mes.yaml>)
- [08 Faturamento Bruto](<../../metrics/comercial/metrica_faturamento_bruto.yaml>)
- [Pedidos & Faturamentos HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_html.yaml>)
- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Comercial HTML v1](<../../technical/measures/corporativo/metrica_comercial_html_v1.yaml>)
- [Farmax BI HTML old](<../../technical/measures/corporativo/metrica_farmax_bi_html_old.yaml>)
- [02 Cancelado](<../../metrics/comercial/metrica_cancelado.yaml>)
- [10 Carteira Inicial](<../../metrics/comercial/metrica_carteira_inicial.yaml>)
- [Label Mês Parcial](<../../technical/measures/comercial/metrica_label_mes_parcial.yaml>)
- [Farmax BI HTML v2](<../../technical/measures/corporativo/metrica_farmax_bi_html_v2.yaml>)
- [Pedidos & Faturamentos Menu HTML](<../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_menu_html.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dTempo.tmdl>)
