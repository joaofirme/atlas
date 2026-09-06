# 0001 — Primeira ingestão a partir do Power BI

Data: 2026-09-06. Estado: convenção documental inicial, sem certificação dos objetos.

O usuário escolheu o BI corporativo da pasta `powerbi/` como primeira fonte. Isso antecipa o catálogo comercial, financeiro e de estoque em relação à proposta inicial de um piloto de frete. Não foram inventadas métricas de frete para preencher o roadmap anterior.

Adotamos IDs de medidas com prefixo `bi_`, preservando números e nomes originais normalizados, e `kind` para separar indicadores, auxiliares, seletores, apresentação HTML e placeholders. Uma medida DAX não é necessariamente um KPI: 6 delas renderizam HTML, enquanto 2 retornam apenas um hífen.

Os contratos YAML são o local da expressão extraída; `source_description` preserva a descrição original, enquanto `definition` e `definition_basis` permitem registrar uma interpretação e sua origem. Essa separação evita perpetuar descrições desatualizadas como comportamento comprovado. Fórmulas nas fontes PBIP permanecem evidências históricas deste snapshot; ainda não existe sincronização automática Atlas → Power BI.

Cada tabela semântica é documentada como um produto de dados técnico em `data_products/`, com dicionário completo. `docs/powerbi/colunas.json` é um índice técnico da mesma extração, não uma segunda definição de negócio. Dimensões reutilizam as colunas por nome. Entidades são interpretações propostas e não equivalem automaticamente às tabelas físicas.

Relacionamentos do modelo e relações conceituais são separados. Propriedades omitidas no TMDL permanecem explicitamente não declaradas; não inferimos a cardinalidade real dos dados. Relacionamento tabular não autoriza tradução direta para um JOIN SQL.

As variáveis internas das medidas HTML são indexadas com a medida e a linha relativa na expressão. Não são criadas centenas de métricas artificiais para variáveis de CSS, layout ou tabelas virtuais.

## Repetição da coleta

`scripts/ingest_powerbi.py --output <arquivo-temporario.json>` faz uma extração estática usando apenas Python padrão. Não é um parser TMDL geral nem executa o modelo. Os scripts `document_powerbi.py` e `map_powerbi_semantics.py` registram como o primeiro lote foi produzido e recusam sobrescrever arquivos; não devem ser usados como sincronização automática sobre contratos enriquecidos.

Para um novo snapshot: extrair em arquivo temporário, comparar hashes e nomes, identificar renomeações pelos metadados/linhagem, revisar diferenças e aplicar mudanças pontuais. Preservar definições revisadas e registrar divergências. O [manifesto de fontes](../powerbi/manifesto_fontes.json) registra hashes dos arquivos lidos, excluindo caches e preferências `.pbi`.

Não foi criado ou executado um validador de modelo, conforme preferência do usuário. As conferências realizadas são de cobertura da extração e consistência documental; não se confundem com testes DAX ou certificação.
