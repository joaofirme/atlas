---
schema_version: 1
id: "bi_tabela_legenda_gradiente"
title: "Legenda Gradiente"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Legenda Gradiente.tmdl"
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

# Legenda Gradiente

## Objetivo

Mapear a tabela semântica e sua linhagem no BI corporativo.

## Definição e escopo

Objeto técnico observado na exportação PBIP. Consumidores: modelo semântico e relatório Farmax v3 (1). Significado completo, granularidade e chaves naturais: pendentes de confirmação.

## Especificação

### Origem e linhagem

```json
[
  {
    "engine": "DAX calculado",
    "upstream": null,
    "source_locator": "powerbi/Farmax v3 (1).SemanticModel/definition/tables/Legenda Gradiente.tmdl:15"
  }
]
```

### Dicionário de colunas

| Coluna | Tipo | Coluna de origem | Resumo padrão | Oculta (declarado) | Descrição original | Linha |
|---|---|---|---|---|---|---|
| Value | Pendente | [Value] | sum | não declarado | Não declarada | 4 |

Os nomes e tipos são observados; uma tradução do nome não equivale a uma definição de negócio. Unicidade e granularidade física não foram verificadas. Campos de CPF/CNPJ e e-mail são apenas nomes de colunas; nenhum registro foi extraído.

### Partição: Legenda Gradiente

Tipo: calculated. Propriedades: `{"mode": "import"}`. Fonte: linha 15.

```dax
GENERATESERIES(1, 100, 1)
```


## Exemplos

Consultar os nomes de colunas e as medidas dependentes. Não foram coletadas amostras de linhas.

## Validação

Inventariadas 1 colunas e 1 partições. Sem consulta à origem, teste de cardinalidade ou execução do modelo.

## Dependências e impactos

Relacionamentos: 0. Consultar o [mapa do modelo](../../docs/powerbi/modelo.md).

Medidas com referência direta:



## Pendências

Responsáveis, política de atualização/SLA, qualidade, acesso, chaves e granularidade. A consulta de uma view não revela sua transformação upstream.

## Fontes

[Definição TMDL](<../../powerbi/Farmax v3 (1).SemanticModel/definition/tables/Legenda Gradiente.tmdl>)
