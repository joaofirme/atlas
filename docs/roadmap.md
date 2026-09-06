# Construção do Atlas

## Concluído nesta ingestão

- Padrão documental e skill de manutenção.
- Inventário da primeira fonte de descoberta e rastreabilidade dos arquivos observados.
- Catálogo de medidas, tabelas/colunas, joins, dimensões, conceitos e regras observadas.
- Índice dos cálculos internos e do uso observado, sem promovê-los automaticamente a indicadores.
- Consulta progressiva, separação de negócio/apresentação, busca local e expansão de dependências, impactos e páginas.
- Primeira skill analítica de carteira em rascunho e testes estruturais de descoberta e referências.

## Próximas etapas

1. **Revisar as pendências prioritárias:** colunas ausentes nas metas, filtro de medida ausente, tabela desconectada de Logística/CS e diferenças entre descrição e DAX. Aceite: decisão registrada para cada divergência.
2. **Confirmar definições de negócio:** RSL, RL, receita bruta, devolução/refaturamento, carteira e snapshot de estoque. Identificar responsáveis, unidade/moeda e granularidade. Aceite: contratos revisados pelos responsáveis, com evidências.
3. **Completar linhagem upstream:** obter definições das views Redshift e dos dataflows. Aceite: chaves, cálculos tributários, deduplicação e atualizações explicados até sua origem.
4. **Reconciliar resultados nas fontes:** usar cada artefato em seu contexto de execução para comparar definições e resultados. Aceite: amostras com período, filtros, resultado, tolerância e origem registradas. A validação automática permanece fora do escopo atual.
5. **Validar a skill de carteira:** executar com snapshots e eventos reais, revisar critérios de decomposição e obter aprovação da área. O procedimento documental já existe; causas ainda não foram verificadas.
6. **Conectar o agente aos dados:** usar a busca e expansão locais já disponíveis como descoberta, definir APIs, permissões e consultas controladas. Nenhum servidor/API ou acesso a valores atuais está implementado.
