# Construção do Atlas

## Concluído nesta ingestão

- Padrão documental e skill de manutenção.
- Inventário da primeira fonte de descoberta e rastreabilidade dos arquivos observados.
- Catálogo de métricas, dimensões, datasets, conceitos, regras e skills, além do inventário técnico preservado.
- Índice dos cálculos internos e do uso observado, sem promovê-los automaticamente a indicadores.
- Consulta progressiva, separação de negócio/apresentação, busca local e expansão de dependências, impactos e páginas.
- Primeira skill analítica de carteira em rascunho e testes semânticos de governança e referências.
- Contratos iniciais de datasets orientados ao negócio com rastreabilidade para tabelas e Fabric/Power BI.
- MCP Alexandria read-only com sete tools para agentes, incluindo o futuro Agente Alexandria no Copilot Studio.

## Próximas etapas

1. **Revisar as pendências prioritárias:** colunas ausentes nas metas, filtro de medida ausente, tabela desconectada de Logística/CS e diferenças entre descrição e DAX. Aceite: decisão registrada para cada divergência.
2. **Confirmar definições de negócio:** RSL, RL, receita bruta, devolução/refaturamento, carteira e snapshot de estoque. Identificar responsáveis, unidade/moeda e granularidade. Aceite: contratos revisados pelos responsáveis, com evidências.
3. **Completar linhagem upstream:** obter definições das views Redshift e dos dataflows. Aceite: chaves, cálculos tributários, deduplicação e atualizações explicados até sua origem.
4. **Reconciliar resultados nas fontes:** usar cada artefato em seu contexto de execução para comparar definições e resultados. Aceite: amostras com período, filtros, resultado, tolerância e origem registradas. A validação automática permanece fora do escopo atual.
5. **Validar a skill de carteira:** executar com snapshots e eventos reais, revisar critérios de decomposição e obter aprovação da área. O procedimento documental já existe; causas ainda não foram verificadas.
6. **Publicar o MCP para o Agente Alexandria:** escolher transporte, identidade, rede, observabilidade e política de acesso no ambiente Farmax; configurar o Copilot Studio. O servidor local read-only existe, mas não foi implantado.
7. **Implantar aprovação por domínio:** criar times GitHub de Comercial, Logística, Financeiro e Data & AI e substituir os responsáveis provisórios no CODEOWNERS. Exigir aprovação dos times nas regras de proteção da master.
8. **Certificar por ondas:** preencher owners, definição, unidade, granularidade, dimensões, dataset, regras, fontes e evidências; reconciliar resultados antes de mudar `status` e `evidence_status` para `certified`.

Fora de escopo: sincronização automática com Fabric/Power BI, execução de DAX/SQL pelo MCP, introdução de dbt e substituição do processamento Spark atual.
