# Atlas

Fonte semântica governada da Farmax: significado dos indicadores, cálculo, datasets, dimensões, relações, regras e procedimentos de análise, versionados em Git.

Comece pelo [guia de consulta](docs/consulta.md). Para navegar manualmente, use o [catálogo de negócio](docs/catalogo.md). Para integração com agentes, use o [MCP Alexandria](mcp/README.md).

O Atlas separa evidência `observed` de conteúdo `certified`. O acervo inicial continua como rascunho observado até revisão humana; somente contratos certificados são verdade oficial. O MCP é somente leitura e não consulta valores atuais.

## Arquitetura

```text
Fontes e implementações (Spark, Redshift, Fabric/Power BI)
                       │ evidência, sem sincronização automática
                       ▼
 Git → métricas ↔ dimensões ↔ datasets ↔ regras/conceitos/skills
                       │
                  catálogos JSON
                       │
                MCP Alexandria (read-only)
                       │
          Agente Alexandria no Copilot Studio
```

Fabric e Power BI permanecem referências de implementação. Spark e a arquitetura atual são preservados; o Atlas não introduz dbt nem transforma SQL em foco.

Para manter o conteúdo: [instruções](.agents/skills/atlas-documentation/SKILL.md), [plano e avaliação](docs/decisoes/0002-consulta-progressiva.md) e [próximas etapas](docs/roadmap.md). Evidências e detalhes de apresentação ficam no [inventário técnico](docs/catalogo-tecnico.md).
