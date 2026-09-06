---
schema_version: 1
id: "bi_bases_receita"
title: "Bases de receita e apresentação"
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
    locator: "medida Faturamento Selecionado; linha 5415"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Receita Selecionada; linha 5673"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Devolução Selecionada; linha 5533"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida Meta RB; linha 5944"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida % Meta RB; linha 5411"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Bases de receita e apresentação

## Objetivo

A seleção Receita Bruta escolhe as medidas brutas; o restante usa a base semi líquida. Devolução é a mesma nos dois ramos. Meta RB e % Meta RB são placeholders de texto, não valores zero.

## Definição e escopo

Interpretação documental da implementação observada no BI. Ainda não é uma definição certificada da empresa.

## Especificação

Condição: Base Receita via SELECTEDVALUE. Ação: selecionar medidas canônicas. Escopo: matriz e HTML. Autoridade e vigência: pendentes; evidência é o snapshot do modelo.

- [Faturamento Selecionado](<../../metrics/comercial/bi_faturamento_selecionado.yaml>)
- [Receita Selecionada](<../../metrics/comercial/bi_receita_selecionada.yaml>)
- [Devolução Selecionada](<../../metrics/comercial/bi_devolucao_selecionada.yaml>)
- [Meta RB](<../../metrics/comercial/bi_meta_rb.yaml>)
- [% Meta RB](<../../metrics/comercial/bi_percentual_meta_rb.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Faturamento Selecionado](<../../metrics/comercial/bi_faturamento_selecionado.yaml>)
- [Receita Selecionada](<../../metrics/comercial/bi_receita_selecionada.yaml>)
- [Devolução Selecionada](<../../metrics/comercial/bi_devolucao_selecionada.yaml>)
- [Meta RB](<../../metrics/comercial/bi_meta_rb.yaml>)
- [% Meta RB](<../../metrics/comercial/bi_percentual_meta_rb.yaml>)
