# Cálculos internos — Comercial HTML v1

Implementação canônica: [Comercial HTML v1](<../../../metrics/corporativo/bi_comercial_html_v1.yaml>). As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.

| Variável | Linha DAX | Classificação | Referências |
|---|---:|---|---|
| vBaseReceitaSelecionada | 2 | calculo_ou_contexto | Base Receita |
| vUsarReceitaBruta | 3 | apoio_ou_apresentacao |  |
| vRSLBase | 4 | calculo_ou_contexto | 03 RSL |
| vReceitaBruta | 5 | calculo_ou_contexto | 09 Receita Bruta |
| vRSL | 6 | apoio_ou_apresentacao |  |
| vBaseTagReceita | 7 | apoio_ou_apresentacao |  |
| vTagBase | 8 | apoio_ou_apresentacao |  |
| vFonteBaseReceita | 9 | apoio_ou_apresentacao |  |
| vDataIni | 10 | calculo_ou_contexto | Data |
| vDataFim | 11 | calculo_ou_contexto | Data |
| vMesIni | 12 | apoio_ou_apresentacao |  |
| vMesFim | 13 | apoio_ou_apresentacao |  |
| fPeriodo | 14 | apoio_ou_apresentacao |  |
| vPeriodoBadge | 15 | apoio_ou_apresentacao |  |
| vEmpresaSelecionada | 20 | calculo_ou_contexto | Empresa |
| vDescricaoEmpresaSelecionada | 25 | calculo_ou_contexto | Description |
| vEmpresaContexto | 30 | calculo_ou_contexto | Description, Empresa |
| vAtualizacaoContexto | 51 | calculo_ou_contexto | 00 Atualização |
| fAtualizacaoContexto | 52 | apoio_ou_apresentacao |  |
| vDataInicialSelecionada | 68 | calculo_ou_contexto | Data |
| vDataFinalSelecionada | 69 | calculo_ou_contexto | Data |
| vInicioMesAtual | 70 | apoio_ou_apresentacao |  |
| vFimMesAtual | 71 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesAtual | 72 | apoio_ou_apresentacao |  |
| vParcialBadge | 77 | apoio_ou_apresentacao |  |
| tCanalBase | 86 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, canal_n1 |
| tCanalFiltrada | 87 | calculo_ou_contexto | __Fat |
| tCanalTop | 88 | calculo_ou_contexto | __Fat, __Nome |
| vCanalTotal | 89 | calculo_ou_contexto | __Fat |
| vCanalTopSoma | 90 | calculo_ou_contexto | __Fat |
| vCanalOutros | 91 | apoio_ou_apresentacao |  |
| vCanalOutrosQtd | 92 | calculo_ou_contexto |  |
| HCanalOutros | 93 | calculo_ou_contexto |  |
| HCanalTotal | 94 | calculo_ou_contexto |  |
| HCanalTabela | 95 | calculo_ou_contexto | __Fat, __Nome |
| tCliBase | 97 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, cliente, estado |
| tCliFiltrada | 98 | calculo_ou_contexto | __Fat |
| tCliTop15 | 99 | calculo_ou_contexto | __Fat, __Nome |
| vCliMaxSeg | 100 | calculo_ou_contexto | __Fat |
| HCliRows | 101 | calculo_ou_contexto | __Fat, __Nome |
| tCliPareto | 103 | calculo_ou_contexto | __Fat, __Nome |
| vTotalCli | 104 | calculo_ou_contexto | __Fat |
| vTotalCliSeg | 105 | apoio_ou_apresentacao |  |
| tCliRanked | 106 | calculo_ou_contexto | __Fat |
| vClasseACount | 107 | calculo_ou_contexto | __Acum, __Fat, __Rank |
| tParetoRnk | 108 | calculo_ou_contexto | __Fat |
| tParetoFull | 109 | calculo_ou_contexto | __Fat, __R2, __Rnk |
| vPMaxFat | 110 | calculo_ou_contexto | __Fat |
| vPMaxSeg | 111 | apoio_ou_apresentacao |  |
| vCL | 112 | apoio_ou_apresentacao |  |
| vCR | 113 | apoio_ou_apresentacao |  |
| vCT | 114 | apoio_ou_apresentacao |  |
| vCB | 115 | apoio_ou_apresentacao |  |
| vCH | 116 | apoio_ou_apresentacao |  |
| vParetoQtd | 117 | apoio_ou_apresentacao |  |
| vBW | 118 | apoio_ou_apresentacao |  |
| vBG | 119 | calculo_ou_contexto |  |
| HPBars | 120 | calculo_ou_contexto | __Fat, __Nome, __Rnk |
| HPLine | 139 | calculo_ou_contexto | __CumPct, __Rnk |
| HPDots | 140 | calculo_ou_contexto | __CumPct, __Rnk |
| HPHitTips | 141 | calculo_ou_contexto | __CumPct, __Fat, __Nome, __Rnk, __UF |
| vCutY | 174 | apoio_ou_apresentacao |  |
| HParetoSVG | 175 | calculo_ou_contexto |  |
| vCSS01 | 193 | apoio_ou_apresentacao |  |
| vCSS02 | 194 | apoio_ou_apresentacao |  |
| vCSS03 | 195 | apoio_ou_apresentacao |  |
| vCSS05 | 196 | apoio_ou_apresentacao |  |
| vCSS06 | 197 | apoio_ou_apresentacao |  |
| vCSS07 | 198 | apoio_ou_apresentacao |  |
| vCSS08 | 199 | apoio_ou_apresentacao |  |
| vCSS09 | 200 | apoio_ou_apresentacao |  |
| vCSS10 | 201 | apoio_ou_apresentacao |  |
| vCSS11 | 202 | apoio_ou_apresentacao |  |
| vCSS12 | 203 | apoio_ou_apresentacao |  |
| vCSS13 | 205 | apoio_ou_apresentacao |  |
| vCSS | 207 | apoio_ou_apresentacao |  |
| HCTX | 209 | apoio_ou_apresentacao |  |
| HCANAL_TAB | 222 | apoio_ou_apresentacao |  |
| HCLI_RANK | 223 | apoio_ou_apresentacao |  |
| HPARETO | 224 | apoio_ou_apresentacao |  |
| vHTML | 225 | apoio_ou_apresentacao |  |
