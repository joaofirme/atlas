---
name: analisar-carteira
description: Localizar a receita a faturar e investigar variações da carteira aberta ou programada.
metadata:
  schema_version: 1
  id: analisar_carteira
  title: Analisar carteira a faturar
  type: analysis_skill
  domain: comercial
  status: draft
  version: 0.1.0
  owners: {business: null, technical: null}
  created_at: '2026-09-06'
  updated_at: '2026-09-06'
  sources:
    - reference: metrics/comercial/metrica_aberto.yaml
      locator: implementations.dax e formula.dependencies
      accessed_at: '2026-09-06'
    - reference: business_rules/comercial/regra_datas_eventos.md
      locator: Especificação
      accessed_at: '2026-09-06'
  validation:
    reviewed_by: null
    reviewed_at: null
    evidence: ['Procedimento documental; sem execução nos dados ou aprovação de negócio.']
  pending:
    - Confirmar acesso a snapshots comparáveis, unidade, chaves, granularidade e dimensões aprovadas.
    - Validar o procedimento e o fechamento de variações com a área comercial.
---

# Analisar carteira a faturar

## Quando usar

Perguntas sobre quanto há a faturar, carteira aberta ou programada, onde o indicador aparece e por que seu valor mudou.

## Entradas e pré-condições

Definir se o usuário quer aberto até hoje ou toda a carteira; empresa, unidade/moeda, data de referência, comparação e filtros. Para números, exigir conexão autorizada aos dados/modelo. Para variação histórica, exigir snapshots ou histórico de eventos comparáveis: a posição atual não reconstrói automaticamente a carteira passada.

## Referências canônicas

- [metrica_aberto](../../../metrics/comercial/metrica_aberto.yaml)
- [metrica_total_a_faturar](../../../metrics/comercial/metrica_total_a_faturar.yaml)
- [metrica_programado](../../../metrics/comercial/metrica_programado.yaml)
- [regra_datas_eventos](../../../business_rules/comercial/regra_datas_eventos.md)
- [regra_carteira_data_referencia](../../../business_rules/comercial/regra_carteira_data_referencia.md)
- [regra_separacao_pendencias](../../../business_rules/comercial/regra_separacao_pendencias.md)
- [dimensao_cliente](../../../dimensions/comercial/dimensao_cliente.yaml), [dimensao_produto](../../../dimensions/comercial/dimensao_produto.yaml), [dimensao_empresa](../../../dimensions/comercial/dimensao_empresa.yaml)

## Procedimento

1. Buscar a pergunta, resolver a ambiguidade entre os três contratos e ler a implementação escolhida e suas dependências. Não usar medidas de matriz escaladas como valor bruto.
2. Consultar `show` para localizar tabelas físicas, dependências, impactos, dimensões candidatas e páginas. Para reproduzir um dashboard, conferir filtros da página, do visual, seletores, medidas HTML intermediárias e data de atualização no snapshot. Informar o nome da página e a evidência local; URL publicada permanece desconhecida.
3. Verificar os filtros efetivos e a remoção do calendário nos contratos. Um filtro de mês não transforma automaticamente posição de carteira em movimento mensal. Considerar que a passagem do dia pode mudar a classificação entre aberto e programado.
4. Consultar o valor com o mesmo contexto do modelo. Validar moeda, granularidade e cardinalidade antes de traduzir DAX para SQL; não somar registros presumindo uma linha por pedido. Não tratar joins observados como aprovados.
5. Para duas posições comparáveis, calcular diferença absoluta e percentual; quando a base anterior for zero, apresentar a diferença absoluta e a variação percentual como indefinida.
6. Abrir a diferença por empresa e, após validar compatibilidade, cliente/grupo, produto, marca, regional e executivo. Reconciliar contribuições ao total, incluindo desconhecidos e restante fora do Top N. Separar contribuição por segmento de explicação causal.
7. Se houver histórico por chave validada, investigar entradas de pedidos, faturamentos, cancelamentos, reprogramações e alterações de quantidade/preço. Evitar contar o mesmo evento duas vezes. Só atribuir valores a cada motivo quando a trilha de eventos permitir reconciliação; reportar resíduo não explicado.
8. Usar bloqueios financeiros, produção e logística como hipóteses a testar com eventos/evidências. A regra de pendências alerta para tabela desconectada e perda de contexto: não supor que as parcelas somam a carteira.

## Validação

Comparar resultado com o modelo para contexto idêntico, conferir atualização, nulos de programação, chaves duplicadas e fechamento das contribuições. Não presumir que aberto e programado reconciliam com o total antes de testar datas em branco e coerções do modelo. Registrar consulta, horário, filtros e resultados das verificações. Esta skill ainda não foi executada sobre dados.

## Formato de saída

Informar indicador e status, valor/unidade, data de referência, filtros, comparação, maiores contribuições, causas comprovadas, hipóteses e resíduo. Citar contratos, consulta e página quando aplicável. Sem acesso aos dados, entregar definição e caminho de consulta, explicitando a impossibilidade de informar valor atual ou causa.

## Limites e pendências

Contratos não certificados; unidade, granularidade, acesso e joins exigem confirmação. Uma correlação, impacto em fórmula ou nome de departamento não prova causa. Posição atual isolada não explica a mudança histórica.

## Fontes

Os contratos e regras acima apontam para o snapshot TMDL e as evidências de origem. As etapas de investigação são uma proposta documental, sujeita a validação pela área.
