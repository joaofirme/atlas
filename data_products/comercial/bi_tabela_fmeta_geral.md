---
schema_version: 1
id: "bi_tabela_fmeta_geral"
title: "fMeta_Geral"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_Geral.tmdl"
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

# fMeta_Geral

## Objetivo

Mapear a tabela semântica e sua linhagem no BI corporativo.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "Amazon Redshift",
    "database": "farmax_prod",
    "objects": [
      ""
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_Geral.tmdl:95"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| general_target_subtotal_billing | double | general_target_subtotal_billing | sum | não declarado | Não declarada | 4 |
| general_target_subtotal_average_billing | double | general_target_subtotal_average_billing | sum | não declarado | Não declarada | 14 |
| general_target_average_ticket | double | general_target_average_ticket | sum | não declarado | Não declarada | 24 |
| general_target_quantity_billing | double | general_target_quantity_billing | sum | não declarado | Não declarada | 34 |
| general_target_subtotal_return_percent | double | general_target_subtotal_return_percent | sum | não declarado | Não declarada | 44 |
| general_target_inovation_percent | int64 | general_target_inovation_percent | sum | não declarado | Não declarada | 54 |
| general_target_days | int64 | general_target_days | sum | não declarado | Não declarada | 64 |
| general_target_date | dateTime | general_target_date | none | não declarado | Não declarada | 73 |
| obt_company | string | obt_company | none | não declarado | Não declarada | 84 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fMeta_Geral

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 95.

```powerquery
let
    Fonte = Value.NativeQuery(AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"), "with fMetas_Geral as (#(lf)SELECT#(lf)#(tab)obt_company,#(lf)#(tab)max(general_target_subtotal_billing) as general_target_subtotal_billing,#(lf)#(tab)max(general_target_subtotal_average_billing) as general_target_subtotal_average_billing,#(lf)#(tab)max(general_target_average_ticket)as general_target_average_ticket,#(lf)#(tab)max(general_target_quantity_billing)as general_target_quantity_billing,#(lf)#(tab)max(general_target_subtotal_return_percent) as general_target_subtotal_return_percent,#(lf)#(tab)max(general_target_inovation_percent) as general_target_inovation_percent,#(lf)#(tab)max(general_target_days)::int as general_target_days,#(lf)#(tab)(general_target_year||'-'||lpad(general_target_month,2,0)||'-'||'01')::date as general_target_date#(lf)FROM#(lf)#(tab)comercial.obt_sales#(lf)where general_target_year >= 2021#(lf)group by obt_company, general_target_date#(lf))#(lf)select * from fMetas_Geral", null, [EnableFolding=true])
in
    Fonte
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 9 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 1. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:

- [Meta Diária Atual](<../../metrics/comercial/bi_meta_diaria_atual.yaml>)
- [Meta Média](<../../metrics/comercial/bi_meta_media.yaml>)
- [Meta de Unidades Faturadas](<../../metrics/comercial/bi_meta_de_unidades_faturadas.yaml>)
- [Meta RL](<../../metrics/comercial/bi_meta_rl.yaml>)
- [04 % Meta Devolução](<../../metrics/comercial/bi_04_percentual_meta_devolucao.yaml>)
- [Meta Preço Médio](<../../metrics/comercial/bi_meta_preco_medio.yaml>)
- [03 Texto Dias Úteis](<../../metrics/corporativo/bi_03_texto_dias_uteis.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fMeta_Geral.tmdl>)
