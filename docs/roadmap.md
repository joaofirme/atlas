# Construção do Atlas

## Concluído nesta ingestão

- Padrão documental e skill de manutenção.
- Inventário do BI corporativo e rastreabilidade das fontes locais.
- Catálogo de medidas, tabelas/colunas, joins, dimensões, conceitos e regras observadas.
- Índice dos cálculos internos das medidas HTML e mapa de uso nos visuais.

## Próximas etapas

1. **Revisar as pendências prioritárias:** colunas ausentes nas metas, filtro de medida ausente, tabela desconectada de Logística/CS e diferenças entre descrição e DAX. Aceite: decisão registrada para cada divergência.
2. **Confirmar definições de negócio:** RSL, RL, receita bruta, devolução/refaturamento, carteira e snapshot de estoque. Identificar responsáveis, unidade/moeda e granularidade. Aceite: contratos revisados pelos responsáveis, com evidências.
3. **Completar linhagem upstream:** obter definições das views Redshift e dos dataflows. Aceite: chaves, cálculos tributários, deduplicação e atualizações explicados até sua origem.
4. **Reconciliar resultados no Power BI:** quando solicitado, usar o modelo em execução e contextos acordados para comparar medidas e visuais. Aceite: amostras de comparação com período, filtros, resultado e tolerância. A validação automática permanece fora do escopo atual.
5. **Criar a primeira skill analítica do negócio:** escolher perguntas reais atendidas por definições revisadas. Aceite: procedimento reutiliza IDs canônicos e informa limites e evidências.
6. **Evoluir o consumo por agentes:** implementar descoberta e leitura; depois projetar consultas controladas e integração com Fabric. Aceite: APIs, permissões, runtime e paridade definidos. Essas capacidades ainda não estão implementadas.
