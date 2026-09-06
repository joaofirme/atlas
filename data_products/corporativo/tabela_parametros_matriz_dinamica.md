---
schema_version: 1
id: "tabela_parametros_matriz_dinamica"
title: "Parâmetros: Matriz Dinâmica"
type: "data_product"
domain: "corporativo"
status: "draft"
version: "0.1.0"
owners:
  business: null
  technical: null
created_at: "2026-09-06"
updated_at: "2026-09-06"
sources:
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Parâmetros%3A Matriz Dinâmica.tmdl"
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

# Parâmetros: Matriz Dinâmica

## Objetivo

Mapear a tabela, suas colunas e sua linhagem como evidência para o Atlas.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "DAX calculado",
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Parâmetros%3A Matriz Dinâmica.tmdl:41"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| Parâmetro 2 | Pendente | [Value1] | none | não declarado | Não declarada | 4 |
| Parâmetro 2 Campos | Pendente | [Value2] | none | True | Não declarada | 15 |
| Parâmetro 2 Pedido | Pendente | [Value3] | sum | True | Não declarada | 30 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: Parâmetros: Matriz Dinâmica

Tipo: calculated. Propriedades: `{"mode": "import"}`. Fonte: linha 41.

```dax
{
    ("MARCA", NAMEOF('dMaterial_unificada'[brand_novo]), 3),
    ("SEGMENTO", NAMEOF('dMaterial_unificada'[novo_segmento]), 4),
    ("CLIENTE", NAMEOF('dClientes_unificada'[cliente_grupo]), 2),
    ("REGIONAL", NAMEOF('dRegional'[order_sale_order_office]), 0),
    ("EXECUTIVO", NAMEOF('dExecutivos_unificada'[nome_unificado]), 1),
    ("CLASSIFICAÇÃO SKU", NAMEOF('dMaterial_unificada'[level]), 5),
    ("SKU", NAMEOF('dMaterial_unificada'[descricao]), 6)
}
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 3 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 0. Consultar o [mapa do modelo](../../docs/ingestoes/2026-09-06-modelo-corporativo/modelo.md).

Medidas com referência direta:



## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/Parâmetros%3A Matriz Dinâmica.tmdl>)
