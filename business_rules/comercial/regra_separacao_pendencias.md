---
schema_version: 1
id: "regra_separacao_pendencias"
title: "Distribuição de pendências por área"
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
    locator: "medida 00 Financeiro; linha 5331"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 06 Ret.-Limit.créd.exc.; linha 5308"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 00 Logística; linha 5354"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 00 Customer Service; linha 5901"
    accessed_at: "2026-09-06"
  -
    reference: "powerbi/Farmax v3 (1).SemanticModel/definition/tables/_Medidas.tmdl"
    locator: "medida 06 Aguarda Produção; linha 248"
    accessed_at: "2026-09-06"
validation:
  reviewed_by: null
  reviewed_at: null
  evidence:
    - "Leitura estática do snapshot PBIP; sem execução ou certificação de negócio."
pending:
  - "Confirmar interpretação, responsáveis e comportamento com dados reais."
---

# Distribuição de pendências por área

## Objetivo

Os motivos de pendência derivam de departamentos e bloqueios; financeiro tem regras específicas por empresa. Logística e CS acrescentam uma tabela calculada desconectada.

## Definição e escopo

Interpretação documental da implementação observada na fonte de descoberta. Ainda não é uma definição certificada da empresa.

## Especificação

tLogistica e CS divide valores conforme quantidades de pedido e entrega e agrupa por valores, não por uma chave do pedido. Não há relação declarada dessa tabela com empresa, tempo ou produto. Avaliar perda de contexto e repetição dos valores antes de confiar nas decomposições.

- [00 Financeiro](<../../metrics/financeiro/metrica_financeiro.yaml>)
- [06 Ret.-Limit.créd.exc.](<../../metrics/financeiro/metrica_ret_limit_cred_exc.yaml>)
- [00 Logística](<../../metrics/logistica/metrica_logistica.yaml>)
- [00 Customer Service](<../../metrics/comercial/metrica_customer_service.yaml>)
- [06 Aguarda Produção](<../../metrics/comercial/metrica_aguarda_producao.yaml>)

## Exemplos

Usar a definição em perguntas sobre o indicador, sempre informando base de receita, empresa e período; não há resultados numéricos extraídos.

## Validação

Leitura estática; sem execução DAX, comparação numérica ou revisão de negócio.

## Dependências e impactos

Mudanças nessas definições podem afetar os visuais e cálculos dependentes listados em cada contrato.

## Pendências

Confirmar significado, responsáveis e uso oficial com a área.

## Fontes

- [00 Financeiro](<../../metrics/financeiro/metrica_financeiro.yaml>)
- [06 Ret.-Limit.créd.exc.](<../../metrics/financeiro/metrica_ret_limit_cred_exc.yaml>)
- [00 Logística](<../../metrics/logistica/metrica_logistica.yaml>)
- [00 Customer Service](<../../metrics/comercial/metrica_customer_service.yaml>)
- [06 Aguarda Produção](<../../metrics/comercial/metrica_aguarda_producao.yaml>)
