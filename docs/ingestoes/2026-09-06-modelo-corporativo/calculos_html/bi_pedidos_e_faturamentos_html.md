# Cálculos internos — Pedidos & Faturamentos HTML

Implementação canônica: [Pedidos & Faturamentos HTML](<../../../../technical/measures/corporativo/metrica_pedidos_e_faturamentos_html.yaml>). As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.

| Variável | Linha DAX | Classificação | Referências |
|---|---:|---|---|
| vBaseReceitaSelecionada | 9 | calculo_ou_contexto | Base Receita |
| vUsarReceitaBruta | 15 | apoio_ou_apresentacao |  |
| vNomeFaturamento | 18 | apoio_ou_apresentacao |  |
| vNomeReceita | 21 | apoio_ou_apresentacao |  |
| vSiglaReceita | 24 | apoio_ou_apresentacao |  |
| vTagBase | 31 | apoio_ou_apresentacao |  |
| vFonteBase | 38 | apoio_ou_apresentacao |  |
| vVendido | 44 | calculo_ou_contexto | 00 Valor de Vendas |
| vFaturado | 49 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto |
| vRSLBase | 58 | calculo_ou_contexto | 03 RSL |
| vMetaRSL | 63 | calculo_ou_contexto | Meta RSL |
| vAberto | 68 | calculo_ou_contexto | 04 Aberto |
| vProgramado | 76 | calculo_ou_contexto | 05 Programado |
| vProgramadoM | 84 | calculo_ou_contexto | 05 Programado M+ |
| vCarteiraAtual | 92 | apoio_ou_apresentacao |  |
| vPercAbertoCarteira | 95 | calculo_ou_contexto |  |
| fPercAbertoCarteira | 102 | apoio_ou_apresentacao |  |
| fProgramadoM | 108 | calculo_ou_contexto |  |
| vEntregue | 114 | calculo_ou_contexto | 06 Valor Entregue |
| vReceitaBruta | 119 | calculo_ou_contexto | 09 Receita Bruta |
| vReceitaSelecionada | 124 | apoio_ou_apresentacao |  |
| vDevolucao | 130 | calculo_ou_contexto | 00 Devolução |
| vRefaturamento | 135 | calculo_ou_contexto | 01 Refaturamento |
| vCancelados | 140 | calculo_ou_contexto | 02 Cancelado |
| vAtingMeta | 142 | calculo_ou_contexto |  |
| vMargemProxy | 149 | calculo_ou_contexto |  |
| vImpostos | 157 | apoio_ou_apresentacao |  |
| vDevRefTotal | 162 | apoio_ou_apresentacao |  |
| vPercImpostosReal | 168 | calculo_ou_contexto |  |
| vPercRSLReal | 178 | calculo_ou_contexto |  |
| vMinImpostosVisual | 193 | apoio_ou_apresentacao |  |
| vPercImpostosVisual | 196 | apoio_ou_apresentacao |  |
| vPercRSLVisual | 207 | apoio_ou_apresentacao |  |
| wAnatomiaRSL | 216 | apoio_ou_apresentacao |  |
| wAnatomiaImpostos | 226 | apoio_ou_apresentacao |  |
| fPercRSLAnatomia | 238 | apoio_ou_apresentacao |  |
| fPercImpostosAnatomia | 244 | apoio_ou_apresentacao |  |
| vDataInicialSelecionada | 255 | calculo_ou_contexto | Data |
| vDataFinalSelecionada | 258 | calculo_ou_contexto | Data |
| vMesSelecionadoAtual | 261 | apoio_ou_apresentacao |  |
| vDataFinalComparavel | 266 | apoio_ou_apresentacao |  |
| vDataInicialComparavel | 276 | apoio_ou_apresentacao |  |
| vDiaCorteComparavel | 287 | apoio_ou_apresentacao |  |
| vDataInicialLY | 291 | apoio_ou_apresentacao |  |
| vDataFinalLY | 294 | apoio_ou_apresentacao |  |
| vSelecaoDentroDeUmMes | 310 | apoio_ou_apresentacao |  |
| vSelecaoMesCompleto | 314 | apoio_ou_apresentacao |  |
| vDataInicialLM | 324 | apoio_ou_apresentacao |  |
| vDataFinalLM | 331 | apoio_ou_apresentacao |  |
| vVendidoLY | 341 | calculo_ou_contexto | 00 Valor de Vendas, Data |
| vFaturadoLY | 355 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, Data |
| vReceitaSelecionadaLY | 373 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Data |
| vAbertoLY | 391 | calculo_ou_contexto | 03 Total a Faturar, Data |
| vProgramadoLY | 405 | calculo_ou_contexto | 05 Programado, Data |
| vEntregueLY | 419 | calculo_ou_contexto | 06 Valor Entregue, Data |
| vYoYVendido | 433 | calculo_ou_contexto |  |
| vYoYFaturado | 436 | calculo_ou_contexto |  |
| vYoYReceita | 439 | calculo_ou_contexto |  |
| vYoYAberto | 446 | calculo_ou_contexto |  |
| vYoYProgramado | 449 | calculo_ou_contexto |  |
| vYoYEntregue | 452 | calculo_ou_contexto |  |
| vPercEntregueReceita | 455 | calculo_ou_contexto |  |
| fPercEntregueReceita | 462 | apoio_ou_apresentacao |  |
| fVendido | 468 | calculo_ou_contexto |  |
| fFaturado | 469 | calculo_ou_contexto |  |
| fReceitaSelecionada | 470 | calculo_ou_contexto |  |
| fRSLBase | 476 | calculo_ou_contexto |  |
| fMetaRSL | 481 | calculo_ou_contexto |  |
| fAberto | 482 | calculo_ou_contexto |  |
| fProgramado | 483 | calculo_ou_contexto |  |
| fAbertoNum | 484 | calculo_ou_contexto |  |
| fProgramadoNum | 485 | calculo_ou_contexto |  |
| fEntregue | 486 | calculo_ou_contexto |  |
| fReceitaBruta | 487 | calculo_ou_contexto |  |
| fImpostos | 488 | calculo_ou_contexto |  |
| fDevolucao | 489 | calculo_ou_contexto |  |
| fRefaturamento | 490 | calculo_ou_contexto |  |
| fAtingMeta | 491 | apoio_ou_apresentacao |  |
| fMargem | 492 | apoio_ou_apresentacao |  |
| fYoYVendido | 494 | apoio_ou_apresentacao |  |
| fYoYFaturado | 495 | apoio_ou_apresentacao |  |
| fYoYReceita | 496 | apoio_ou_apresentacao |  |
| fYoYAberto | 497 | apoio_ou_apresentacao |  |
| fYoYProgramado | 498 | apoio_ou_apresentacao |  |
| fYoYEntregue | 499 | apoio_ou_apresentacao |  |
| sUp | 501 | apoio_ou_apresentacao |  |
| sDn | 502 | apoio_ou_apresentacao |  |
| vMesFiltrado | 505 | apoio_ou_apresentacao |  |
| vInicioMesAtual | 516 | apoio_ou_apresentacao |  |
| vFimMesAtual | 519 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesAtual | 522 | apoio_ou_apresentacao |  |
| vParcialBadge | 528 | apoio_ou_apresentacao |  |
| vVendidoLM | 540 | calculo_ou_contexto | 00 Valor de Vendas, Data |
| vFaturadoLM | 554 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, Data |
| vMoMVendido | 572 | calculo_ou_contexto |  |
| vMoMFaturado | 575 | calculo_ou_contexto |  |
| fMoMVendido | 578 | apoio_ou_apresentacao |  |
| fMoMFaturado | 581 | apoio_ou_apresentacao |  |
| vSparkUltimaDataSelecionada | 590 | calculo_ou_contexto | Data |
| vSparkUltimoMesCompleto | 596 | apoio_ou_apresentacao |  |
| vSparkDataFinal | 605 | apoio_ou_apresentacao |  |
| tSparkMeses | 608 | calculo_ou_contexto | Value |
| tSparkVendido | 624 | calculo_ou_contexto | 00 Valor de Vendas, Data, __DataFim, __DataInicio |
| vSparkVendidoMin | 645 | calculo_ou_contexto | __Valor |
| vSparkVendidoMax | 651 | calculo_ou_contexto | __Valor |
| vSparkVendidoAmplitude | 657 | apoio_ou_apresentacao |  |
| vSparkVendidoPontos | 660 | calculo_ou_contexto | __Ordem, __Valor |
| vSparkVendidoAreaPontos | 696 | apoio_ou_apresentacao |  |
| HSparkVendido | 700 | apoio_ou_apresentacao |  |
| tSparkFaturado | 726 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, Data, __DataFim, __DataInicio |
| vSparkFaturadoMin | 751 | calculo_ou_contexto | __ValorFaturado |
| vSparkFaturadoMax | 754 | calculo_ou_contexto | __ValorFaturado |
| vSparkFaturadoAmplitude | 757 | apoio_ou_apresentacao |  |
| vSparkFaturadoPontos | 760 | calculo_ou_contexto | __Ordem, __ValorFaturado |
| vSparkFaturadoAreaPontos | 785 | apoio_ou_apresentacao |  |
| HSparkFaturado | 790 | apoio_ou_apresentacao |  |
| tSparkEntregue | 816 | calculo_ou_contexto | 06 Valor Entregue, Data, __DataFim, __DataInicio |
| vSparkEntregueMin | 837 | calculo_ou_contexto | __ValorEntregue |
| vSparkEntregueMax | 840 | calculo_ou_contexto | __ValorEntregue |
| vSparkEntregueAmplitude | 843 | apoio_ou_apresentacao |  |
| vSparkEntreguePontos | 846 | calculo_ou_contexto | __Ordem, __ValorEntregue |
| vSparkEntregueAreaPontos | 871 | apoio_ou_apresentacao |  |
| HSparkEntregue | 876 | apoio_ou_apresentacao |  |
| vEmpresaSelecionada | 903 | calculo_ou_contexto | Empresa |
| vDescricaoEmpresaSelecionada | 908 | calculo_ou_contexto | Description |
| vEmpresaContexto | 913 | calculo_ou_contexto | Description, Empresa |
| vAtualizacaoContexto | 934 | calculo_ou_contexto | 00 Atualização |
| fAtualizacaoContexto | 935 | apoio_ou_apresentacao |  |
| CSS | 946 | apoio_ou_apresentacao |  |
| HCTX | 1523 | apoio_ou_apresentacao |  |
| HTop | 1537 | apoio_ou_apresentacao |  |
| HAnatomia | 1616 | apoio_ou_apresentacao |  |
