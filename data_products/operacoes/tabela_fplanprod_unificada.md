---
schema_version: 1
id: "tabela_fplanprod_unificada"
title: "fPlanProd_unificada"
type: "data_product"
domain: "operacoes"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fPlanProd_unificada.tmdl"
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

# fPlanProd_unificada

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

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
      "operacoes.fato_plan_prod_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/fPlanProd_unificada.tmdl:120"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| cobertura_estoque_empresa | string | cobertura_estoque_empresa | none | não declarado | Não declarada | 4 |
| cobertura_estoque_company | string | cobertura_estoque_company | none | não declarado | Não declarada | 12 |
| cobertura_estoque_data_referencia | dateTime | cobertura_estoque_data_referencia | none | não declarado | Não declarada | 20 |
| cobertura_estoque_sku | string | cobertura_estoque_sku | none | não declarado | Não declarada | 31 |
| cobertura_estoque_quantidade | double | cobertura_estoque_quantidade | sum | não declarado | Não declarada | 39 |
| cobertura_estoque_plano_medio | double | cobertura_estoque_plano_medio | sum | não declarado | Não declarada | 49 |
| cobertura_estoque_cobertura | double | cobertura_estoque_cobertura | sum | não declarado | Não declarada | 59 |
| status_sku | string | status_sku | none | não declarado | Não declarada | 69 |
| estq_transito | double | estq_transito | sum | não declarado | Não declarada | 77 |
| estq_qual | double | estq_qual | sum | não declarado | Não declarada | 87 |
| quant_falta | double | quant_falta | sum | não declarado | Não declarada | 97 |
| vr_medio_faltas | double | vr_medio_faltas | sum | não declarado | Não declarada | 107 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: fPlanProd_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Fato"}`. Fonte: linha 120.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    operacoes = Source{[Name="operacoes"]}[Data],
    fato_plan_prod_unificada = operacoes{[Name="fato_plan_prod_unificada"]}[Data]
in
    fato_plan_prod_unificada
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 12 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 3. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/fPlanProd_unificada.tmdl>)
