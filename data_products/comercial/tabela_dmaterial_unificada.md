---
schema_version: 1
id: "tabela_dmaterial_unificada"
title: "dMaterial_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dMaterial_unificada.tmdl"
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

# dMaterial_unificada

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
      "comercial.dimensao_ean_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dMaterial_unificada.tmdl:239"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| empresa | string | empresa | none | não declarado | Não declarada | 4 |
| codigo_produto | string | codigo_produto | none | não declarado | Não declarada | 12 |
| descricao | string | descricao | none | não declarado | Não declarada | 20 |
| ean | string | ean | none | não declarado | Não declarada | 28 |
| marca | string | marca | none | não declarado | Não declarada | 36 |
| segmento | string | segmento | none | não declarado | Não declarada | 44 |
| familia | string | familia | none | não declarado | Não declarada | 52 |
| kit_brand | string | kit_brand | none | não declarado | Não declarada | 60 |
| kit_atwrt | string | kit_atwrt | none | não declarado | Não declarada | 68 |
| embalagem_brand | string | embalagem_brand | none | não declarado | Não declarada | 76 |
| embalagem_atwrt | string | embalagem_atwrt | none | não declarado | Não declarada | 84 |
| familia_brand | string | familia_brand | none | não declarado | Não declarada | 92 |
| familia_atwrt | string | familia_atwrt | none | não declarado | Não declarada | 100 |
| subcategoria_brand | string | subcategoria_brand | none | não declarado | Não declarada | 108 |
| subcategoria_atwrt | string | subcategoria_atwrt | none | não declarado | Não declarada | 116 |
| categoria_brand | string | categoria_brand | none | não declarado | Não declarada | 124 |
| categoria_atwrt | string | categoria_atwrt | none | não declarado | Não declarada | 132 |
| publico_brand | string | publico_brand | none | não declarado | Não declarada | 140 |
| publico_atwrt | string | publico_atwrt | none | não declarado | Não declarada | 148 |
| textura_brand | string | textura_brand | none | não declarado | Não declarada | 156 |
| textura_atwrt | string | textura_atwrt | none | não declarado | Não declarada | 164 |
| fragrancia_brand | string | fragrancia_brand | none | não declarado | Não declarada | 172 |
| fragrancia_atwrt | string | fragrancia_atwrt | none | não declarado | Não declarada | 180 |
| principioativo_brand | string | principioativo_brand | none | não declarado | Não declarada | 188 |
| principioativo | string | principioativo | none | não declarado | Não declarada | 196 |
| level | string | level | none | não declarado | Não declarada | 204 |
| gtm_novo | string | gtm_novo | none | não declarado | Não declarada | 212 |
| brand_novo | string | brand_novo | none | não declarado | Não declarada | 220 |
| novo_segmento | string | novo_segmento | none | não declarado | Não declarada | 228 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dMaterial_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 239.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    dimensao_ean_unificada1 = comercial{[Name="dimensao_ean_unificada"]}[Data],
    #"Replaced Value" = Table.ReplaceValue(dimensao_ean_unificada1,"MARCAS PROPRIAS","MARCA PRÓPRIA",Replacer.ReplaceText,{"level"}),
    #"Replaced Value1" = Table.ReplaceValue(#"Replaced Value","MARCAS DO GRUPO","FARMAX",Replacer.ReplaceText,{"level"})
in
    #"Replaced Value1"
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 29 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 5. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Farmax BI HTML old](<../../technical/measures/corporativo/metrica_farmax_bi_html_old.yaml>)
- [% Meta Exibição](<../../technical/measures/comercial/metrica_percentual_meta_exibicao.yaml>)
- [Meta RSL Exibição](<../../technical/measures/comercial/metrica_meta_rsl_exibicao.yaml>)
- [Matriz RSL > Meta](<../../technical/measures/comercial/metrica_matriz_rsl_meta.yaml>)
- [Farmax BI HTML v2](<../../technical/measures/corporativo/metrica_farmax_bi_html_v2.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dMaterial_unificada.tmdl>)
