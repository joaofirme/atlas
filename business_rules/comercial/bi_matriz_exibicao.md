---
schema_version: 1
id: "bi_matriz_exibicao"
title: "Unidade e ausência de meta na matriz"
type: "business_rule"
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
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Meta RSL Exibição; linha 5603"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida % Meta Exibição; linha 5433"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Vendido Matriz; linha 5752"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Linha Matriz Possui Movimento; linha 5864"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Unidade e ausência de meta na matriz

## Objetivo

Medidas da matriz dividem valores por 1000. Algumas retornam zero quando não há meta compatível e branco quando não há movimento.

## Definição e escopo

Interpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.

## Especificação

A indisponibilidade depende de base bruta e níveis cliente_grupo, descricao, level e novo_segmento. Esse zero é uma convenção visual, não aprovação de meta zero.

- [Meta RSL Exibição](<../../metrics/comercial/bi_meta_rsl_exibicao.yaml>)
- [% Meta Exibição](<../../metrics/comercial/bi_percentual_meta_exibicao.yaml>)
- [Vendido Matriz](<../../metrics/comercial/bi_vendido_matriz.yaml>)
- [Linha Matriz Possui Movimento](<../../metrics/comercial/bi_linha_matriz_possui_movimento.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Meta RSL Exibição](<../../metrics/comercial/bi_meta_rsl_exibicao.yaml>)
- [% Meta Exibição](<../../metrics/comercial/bi_percentual_meta_exibicao.yaml>)
- [Vendido Matriz](<../../metrics/comercial/bi_vendido_matriz.yaml>)
- [Linha Matriz Possui Movimento](<../../metrics/comercial/bi_linha_matriz_possui_movimento.yaml>)
