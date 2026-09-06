---
schema_version: 1
id: "tabela_dregional"
title: "dRegional"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dRegional.tmdl"
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

# dRegional

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
      "cadastro.dim_regional"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dRegional.tmdl:23"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| order_sale_order_office_code | string | order_sale_order_office_code | none | não declarado | Não declarada | 4 |
| order_sale_order_office | string | order_sale_order_office | none | não declarado | Não declarada | 12 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dRegional

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 23.

```powerquery
let
    Fonte = Value.NativeQuery(AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"), "select distinct#(lf)    regional_regional_code as order_sale_order_office_code,#(lf)    regional_regional_name as order_sale_order_office#(lf)from cadastro.dim_regional#(lf)where regional_regional_code ~ '[A-Za-z]'   -- contém pelo menos uma letra#(lf)  and regional_regional_code ~ '[0-9]'      -- contém pelo menos um número#(lf)  and regional_regional_code not in ('R007','R011')#(lf)union all #(lf)#(tab)select 'N/A' as order_sale_order_office_code, 'NÃO INFORMADA' as order_sale_order_office", null, [EnableFolding=true]),
    #"Replaced Value" = Table.ReplaceValue(Fonte,"REG. SETOR COMERCIAL","SETOR COMERCIAL",Replacer.ReplaceText,{"order_sale_order_office"})
in
    #"Replaced Value"
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 2 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 4. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Carteira e Estoque HTML v1](<../../metrics/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Farmax BI HTML old](<../../metrics/corporativo/metrica_farmax_bi_html_old.yaml>)
- [Farmax BI HTML v2](<../../metrics/corporativo/metrica_farmax_bi_html_v2.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dRegional.tmdl>)
