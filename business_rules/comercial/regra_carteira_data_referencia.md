---
schema_version: 1
id: "regra_carteira_data_referencia"
title: "Período do painel Carteira & Estoque"
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
    locator: "medida Carteira e Estoque HTML v1; linha 2872"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 00 Atualização; linha 661"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Período do painel Carteira & Estoque

## Objetivo

A página define snapshot até a data de atualização e fluxo no mês dessa referência, construindo filtros que removem dTempo.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

O código tenta converter o texto de atualização em data e usa TODAY() em caso de erro. Confirmar o parse e a interação efetiva entre filtros do HTML e REMOVEFILTERS das medidas base. O comentário sobre ignorar slicers não substitui um teste de contexto.

- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [00 Atualização](<../../technical/measures/corporativo/metrica_atualizacao.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [Carteira e Estoque HTML v1](<../../technical/measures/corporativo/metrica_carteira_e_estoque_html_v1.yaml>)
- [00 Atualização](<../../technical/measures/corporativo/metrica_atualizacao.yaml>)
