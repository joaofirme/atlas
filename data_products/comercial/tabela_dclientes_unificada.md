---
schema_version: 1
id: "tabela_dclientes_unificada"
title: "dClientes_unificada"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dClientes_unificada.tmdl"
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

# dClientes_unificada

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
      "comercial.dimensao_clientes_unificada"
    ],
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/dClientes_unificada.tmdl:112"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| empresa | string | empresa | none | não declarado | Não declarada | 4 |
| companhia | string | companhia | none | não declarado | Não declarada | 12 |
| cliente_codigo | int64 | cliente_codigo | sum | não declarado | Não declarada | 20 |
| cliente | string | cliente | none | não declarado | Não declarada | 29 |
| cliente_cpf_cnpj_completo | string | cliente_cpf_cnpj_completo | none | não declarado | Não declarada | 37 |
| cliente_cpf_cnpj_raiz | string | cliente_cpf_cnpj_raiz | none | não declarado | Não declarada | 45 |
| cidade | string | cidade | none | não declarado | Não declarada | 53 |
| estado | string | estado | none | não declarado | Não declarada | 61 |
| pais | string | pais | none | não declarado | Não declarada | 69 |
| regiao | string | regiao | none | não declarado | Não declarada | 77 |
| chave_cliente | string | chave_cliente | none | não declarado | Não declarada | 85 |
| nome_grupo | string | nome_grupo | none | não declarado | Não declarada | 93 |
| cliente_grupo | string | cliente_grupo | none | não declarado | Não declarada | 101 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: dClientes_unificada

Tipo: m. Propriedades: `{"mode": "import", "queryGroup": "Dimensão"}`. Fonte: linha 112.

```powerquery
let
    Source = AmazonRedshift.Database("<endpoint na fonte original>","farmax_prod"),
    comercial = Source{[Name="comercial"]}[Data],
    dimensao_clientes_unificada1 = comercial{[Name="dimensao_clientes_unificada"]}[Data]
in
    dimensao_clientes_unificada1
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 13 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 2. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:

- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [Comercial HTML v1](<../../technical/measures/corporativo/metrica_comercial_html_v1.yaml>)
- [% Meta Exibição](<../../technical/measures/comercial/metrica_percentual_meta_exibicao.yaml>)
- [Meta RSL Exibição](<../../technical/measures/comercial/metrica_meta_rsl_exibicao.yaml>)
- [Matriz RSL > Meta](<../../technical/measures/comercial/metrica_matriz_rsl_meta.yaml>)

## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/dClientes_unificada.tmdl>)
