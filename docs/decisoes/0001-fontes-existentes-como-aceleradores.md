# 0001 — Fontes existentes como aceleradores do Atlas

Data: 2026-09-06. Estado: convenção documental inicial, sem certificação dos objetos.

Os artefatos criados e usados pelas áreas de negócio são fontes de descoberta do Atlas. Relatórios, modelos semânticos, consultas, planilhas e documentos permitem identificar métricas, tabelas, colunas, filtros, relacionamentos, conceitos e regras com mais rapidez. Eles registram uma implementação ou uso observado; não se tornam, por isso, a organização central do catálogo nem uma autoridade automática sobre o significado de negócio.

A primeira fonte analisada está preservada em `powerbi/`. Ela antecipou o catálogo comercial, financeiro, logístico e de estoque e produziu um inventário técnico datado em `docs/ingestoes/2026-09-06-modelo-corporativo/`. O nome da tecnologia permanece nesses locais e nos campos de proveniência porque é necessário para reproduzir e avaliar a coleta.

Os objetos canônicos usam IDs e títulos orientados ao negócio, independentes da ferramenta. Medidas usam o prefixo `metrica_`; dimensões, conceitos, regras, tabelas e relacionamentos usam seus próprios tipos como prefixo quando necessário. A ordem visual e o nome do arquivo de origem não fazem parte da identidade canônica.

Uma medida encontrada em uma fonte não é necessariamente um indicador. A primeira coleta também encontrou auxiliares, seletores, cálculos de exibição, renderização e placeholders. O campo `kind` mantém essa distinção, e esses artefatos continuam em rascunho até serem classificados e validados. Variáveis internas de cálculos de apresentação permanecem no inventário técnico, sem gerar métricas artificiais.

Os contratos YAML preservam a expressão observada em `implementations`; `source_description` guarda a descrição original, enquanto `definition` e `definition_basis` registram a interpretação e sua base. Essa separação permite confrontar fontes e corrigir descrições sem perder evidência histórica.

Cada tabela observada é documentada como um produto de dados técnico em `data_products/`, com seu dicionário. O índice de colunas da ingestão é uma visão técnica da mesma coleta, não uma segunda definição de negócio. Dimensões podem reutilizar colunas por nome; entidades continuam sendo interpretações propostas e não equivalem automaticamente às tabelas físicas.

Relacionamentos do modelo e relações conceituais permanecem separados. Propriedades omitidas na fonte ficam explicitamente não declaradas; não inferimos a cardinalidade real dos dados. Um relacionamento em uma ferramenta analítica não autoriza sua tradução direta para um `JOIN` SQL.

## Repetição da coleta

Os scripts em `scripts/` registram como o primeiro lote foi produzido. Eles fazem extração estática específica para essa fonte, recusam sobrescrever contratos existentes e não devem ser usados como sincronização automática sobre conteúdo enriquecido.

Ao incorporar um novo snapshot ou outra fonte: gerar um inventário temporário, comparar nomes, fórmulas, linhagem e hashes, procurar objetos equivalentes no catálogo e aplicar mudanças pontuais. Preservar definições revisadas, registrar divergências e criar um novo objeto somente quando houver significado distinto. O [manifesto da primeira fonte](../ingestoes/2026-09-06-modelo-corporativo/manifesto_fontes.json) registra os arquivos lidos.

Não foi criado ou executado um validador de modelo, conforme preferência do usuário. As conferências realizadas são de cobertura da extração e consistência documental; não se confundem com testes de execução ou certificação.
