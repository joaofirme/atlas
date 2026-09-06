# Cálculos internos — Farmax BI HTML v2

Implementação canônica: [Farmax BI HTML v2](<../../../metrics/corporativo/bi_farmax_bi_html_v2.yaml>). As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.

| Variável | Linha DAX | Classificação | Referências |
|---|---:|---|---|
| vBaseReceitaSelecionada | 5 | calculo_ou_contexto | Base Receita |
| vUsarReceitaBruta | 6 | apoio_ou_apresentacao |  |
| vFaturamentoLiquido | 7 | calculo_ou_contexto | 00 Faturamento |
| vFaturamentoBruto | 8 | calculo_ou_contexto | 08 Faturamento Bruto |
| vFaturamento | 9 | apoio_ou_apresentacao |  |
| vRSLBase | 10 | calculo_ou_contexto | 03 RSL |
| vReceitaBruta | 11 | calculo_ou_contexto | 09 Receita Bruta |
| vRSL | 12 | apoio_ou_apresentacao |  |
| vDataInicioSelecionada | 16 | calculo_ou_contexto | Data |
| vDataFimSelecionada | 17 | calculo_ou_contexto | Data |
| vMesSelecionadoAtual | 18 | apoio_ou_apresentacao |  |
| vDataFimComparavel | 21 | apoio_ou_apresentacao |  |
| vDataInicioComparavel | 27 | apoio_ou_apresentacao |  |
| vDiaCorteComparavel | 33 | apoio_ou_apresentacao |  |
| vDataInicioLY | 34 | apoio_ou_apresentacao |  |
| vDataFimLY | 35 | apoio_ou_apresentacao |  |
| vSelecaoDentroDeUmMes | 45 | apoio_ou_apresentacao |  |
| vSelecaoMesCompleto | 48 | apoio_ou_apresentacao |  |
| vDataInicioPM | 52 | apoio_ou_apresentacao |  |
| vDataFimPM | 58 | apoio_ou_apresentacao |  |
| vBaseTagReceita | 64 | apoio_ou_apresentacao |  |
| vMetaRBTexto | 67 | calculo_ou_contexto | Meta RB |
| vMetaRSL | 68 | calculo_ou_contexto | Meta RSL |
| vTemMeta | 74 | apoio_ou_apresentacao |  |
| vDevolucao | 75 | calculo_ou_contexto | 00 Devolução |
| vRefaturamento | 76 | calculo_ou_contexto | 01 Refaturamento |
| vDevolucaoTotal | 77 | apoio_ou_apresentacao |  |
| vPercDevolucao | 81 | calculo_ou_contexto |  |
| vPercRefaturamento | 82 | calculo_ou_contexto |  |
| vPercDevolucaoTotalFat | 85 | calculo_ou_contexto |  |
| vFatLY | 86 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, Data |
| vFaturamentoYoY | 95 | calculo_ou_contexto |  |
| vFatPM | 96 | calculo_ou_contexto | 00 Faturamento, 08 Faturamento Bruto, Data |
| vFaturamentoMoM | 105 | calculo_ou_contexto |  |
| vReceitaLY | 106 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Data |
| vPercYoY | 115 | calculo_ou_contexto |  |
| vReceitaPM | 116 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Data |
| vReceitaMoM | 125 | calculo_ou_contexto |  |
| vMetaPrecoMedio | 126 | calculo_ou_contexto | Meta Preço Médio |
| vPrecoMedio | 127 | calculo_ou_contexto | 07 Preço Médio, 07 Preço Médio Bruto |
| vAtualizacao | 136 | calculo_ou_contexto | 00 Atualização |
| vDataAtualizacao | 137 | apoio_ou_apresentacao |  |
| vDataCorteDecisao | 150 | apoio_ou_apresentacao |  |
| vInicioMesDecisao | 151 | apoio_ou_apresentacao |  |
| vFimMesDecisao | 152 | apoio_ou_apresentacao |  |
| vDiasUteisTotal | 153 | calculo_ou_contexto | Data, DiaUtil |
| vDiasUteisRealizados | 160 | calculo_ou_contexto | Data, DiaUtil |
| vDiasUteisRestantes | 167 | apoio_ou_apresentacao |  |
| vPercDiasUteis | 168 | calculo_ou_contexto |  |
| vAtingimentoDecisao | 169 | calculo_ou_contexto |  |
| vRitmoAtualDU | 170 | calculo_ou_contexto |  |
| vReceitaFaltante | 171 | apoio_ou_apresentacao |  |
| vRitmoNecessarioDU | 172 | calculo_ou_contexto |  |
| vMultiplicadorRitmo | 173 | calculo_ou_contexto |  |
| vProjecaoFechamento | 176 | apoio_ou_apresentacao |  |
| vGapProjetado | 180 | apoio_ou_apresentacao |  |
| vGapProjetadoPerc | 181 | calculo_ou_contexto |  |
| vStatusDecisao | 182 | apoio_ou_apresentacao |  |
| vStatusDecisaoCls | 183 | apoio_ou_apresentacao |  |
| vMesDecisao | 184 | apoio_ou_apresentacao |  |
| fAtingimentoDecisao | 193 | apoio_ou_apresentacao |  |
| fPercDiasUteis | 194 | apoio_ou_apresentacao |  |
| fRitmoAtualDU | 195 | calculo_ou_contexto |  |
| fRitmoNecessarioDU | 196 | calculo_ou_contexto |  |
| fMultiplicadorRitmo | 197 | apoio_ou_apresentacao |  |
| fGapProjetado | 198 | calculo_ou_contexto |  |
| fGapProjetadoPerc | 204 | apoio_ou_apresentacao |  |
| tAtingEmpresaBase | 208 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Empresa, Meta RB, Meta RSL |
| tAtingEmpresaFiltrada | 232 | calculo_ou_contexto | __Meta, __Receita |
| tAtingEmpresa | 237 | calculo_ou_contexto | __Empresa |
| vAtingEmpresaQtd | 249 | calculo_ou_contexto |  |
| vAtingNomeX | 251 | apoio_ou_apresentacao |  |
| vAtingTrackX | 252 | apoio_ou_apresentacao |  |
| vAtingTrackW | 253 | apoio_ou_apresentacao |  |
| vAtingValorX | 254 | apoio_ou_apresentacao |  |
| vAtingRowH | 255 | apoio_ou_apresentacao |  |
| vAtingEscalaMaiorMeta | 256 | calculo_ou_contexto | __Meta |
| vAtingEscalaFallback | 261 | calculo_ou_contexto | __Receita |
| vAtingEscalaValorBase | 266 | apoio_ou_apresentacao |  |
| vAtingEscalaValorSeguro | 272 | apoio_ou_apresentacao |  |
| HAtingEmpresaCards | 279 | calculo_ou_contexto | __Empresa, __Meta, __Ordem, __Receita |
| vClsDev | 333 | apoio_ou_apresentacao |  |
| vClsPM | 334 | apoio_ou_apresentacao |  |
| vSetaYoY | 335 | apoio_ou_apresentacao |  |
| vSetaMoM | 336 | apoio_ou_apresentacao |  |
| vSetaFatYoY | 337 | apoio_ou_apresentacao |  |
| vSetaFatMoM | 338 | apoio_ou_apresentacao |  |
| fRSL | 339 | calculo_ou_contexto |  |
| fFatNum | 340 | calculo_ou_contexto |  |
| fRSLNum | 341 | calculo_ou_contexto |  |
| fMetaRSL | 342 | calculo_ou_contexto |  |
| fDev | 343 | calculo_ou_contexto |  |
| fRef | 344 | calculo_ou_contexto |  |
| fDevTotNum | 345 | calculo_ou_contexto |  |
| fPercDev | 346 | apoio_ou_apresentacao |  |
| fPercRef | 347 | apoio_ou_apresentacao |  |
| fPercYoY | 348 | apoio_ou_apresentacao |  |
| fPercMoM | 349 | apoio_ou_apresentacao |  |
| fPercFatYoY | 350 | apoio_ou_apresentacao |  |
| fPercFatMoM | 351 | apoio_ou_apresentacao |  |
| fPM | 352 | apoio_ou_apresentacao |  |
| fMetaPM | 353 | apoio_ou_apresentacao |  |
| fAtu | 354 | apoio_ou_apresentacao |  |
| vDiaParcial | 360 | apoio_ou_apresentacao |  |
| fDiaParcial | 365 | apoio_ou_apresentacao |  |
| vTagBase | 368 | apoio_ou_apresentacao |  |
| vEmpresaSelecionada | 378 | calculo_ou_contexto | Empresa |
| vDescricaoEmpresaSelecionada | 383 | calculo_ou_contexto | Description |
| vEmpresaContexto | 388 | calculo_ou_contexto | Description, Empresa |
| vAtualizacaoContexto | 409 | calculo_ou_contexto | 00 Atualização |
| fAtualizacaoContexto | 410 | apoio_ou_apresentacao |  |
| vDataInicialSelecionadaContexto | 420 | calculo_ou_contexto | Data |
| vDataFinalSelecionadaContexto | 421 | calculo_ou_contexto | Data |
| vInicioMesAtualContexto | 422 | apoio_ou_apresentacao |  |
| vFimMesAtualContexto | 423 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesAtualContexto | 424 | apoio_ou_apresentacao |  |
| vParcialBadgeContexto | 429 | apoio_ou_apresentacao |  |
| vDataIniPeriodo | 441 | calculo_ou_contexto | Data |
| vDataFimPeriodo | 442 | calculo_ou_contexto | Data |
| vMesIniPeriodo | 443 | apoio_ou_apresentacao |  |
| vMesFimPeriodo | 450 | apoio_ou_apresentacao |  |
| fPeriodoIniCurto | 457 | apoio_ou_apresentacao |  |
| fPeriodoFimCurto | 458 | apoio_ou_apresentacao |  |
| fPeriodoSelecionado | 459 | apoio_ou_apresentacao |  |
| vPeriodoBadge | 470 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesCorrente | 471 | apoio_ou_apresentacao |  |
| vParcialBadge | 475 | apoio_ou_apresentacao |  |
| tRegiaoBase | 483 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Meta RB, Meta RSL, order_sale_order_office |
| tRegiaoFiltrada | 493 | calculo_ou_contexto | __Meta |
| tRegiaoTop | 498 | calculo_ou_contexto | __Nome, __Realizado |
| vRegiaoMaxValor | 505 | calculo_ou_contexto | __Meta, __Realizado |
| vRegiaoMaxSeguro | 510 | apoio_ou_apresentacao |  |
| HRegiaoRows | 512 | calculo_ou_contexto | __Meta, __Nome, __Realizado |
| tMixMarcaBase | 547 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, novo_segmento |
| tMixMarcaFiltrada | 558 | calculo_ou_contexto | __RSL |
| tMixMarcaTop | 563 | calculo_ou_contexto | __Grupo, __RSL |
| vMixTotal | 571 | calculo_ou_contexto | __RSLTotal |
| HMixPieSlices | 576 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPieLabels | 626 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPieLegend | 674 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPie | 714 | calculo_ou_contexto |  |
| vCSS01 | 730 | apoio_ou_apresentacao |  |
| vCSS02 | 731 | apoio_ou_apresentacao |  |
| vCSS03 | 732 | apoio_ou_apresentacao |  |
| vCSS04 | 733 | apoio_ou_apresentacao |  |
| vCSS05 | 734 | apoio_ou_apresentacao |  |
| vCSS06 | 735 | apoio_ou_apresentacao |  |
| vCSS07 | 736 | apoio_ou_apresentacao |  |
| vCSS08 | 737 | apoio_ou_apresentacao |  |
| vCSS09 | 738 | apoio_ou_apresentacao |  |
| vCSS10 | 739 | apoio_ou_apresentacao |  |
| vCSS11 | 740 | apoio_ou_apresentacao |  |
| vCSS12 | 741 | apoio_ou_apresentacao |  |
| vCSS13 | 742 | apoio_ou_apresentacao |  |
| vCSS14 | 743 | apoio_ou_apresentacao |  |
| vCSS16 | 745 | apoio_ou_apresentacao |  |
| vCSS17 | 746 | apoio_ou_apresentacao |  |
| vCSS18 | 747 | apoio_ou_apresentacao |  |
| vCSS19 | 748 | apoio_ou_apresentacao |  |
| vCSS20 | 749 | apoio_ou_apresentacao |  |
| vCSS21 | 750 | apoio_ou_apresentacao |  |
| vCSS22 | 751 | apoio_ou_apresentacao |  |
| vCSS24 | 752 | apoio_ou_apresentacao |  |
| vCSS27 | 753 | apoio_ou_apresentacao |  |
| vCSS28 | 754 | apoio_ou_apresentacao |  |
| vCSS29 | 755 | apoio_ou_apresentacao |  |
| vCSS30 | 756 | apoio_ou_apresentacao |  |
| vCSS31 | 758 | apoio_ou_apresentacao |  |
| vCSS32 | 760 | apoio_ou_apresentacao |  |
| vCSS41 | 762 | apoio_ou_apresentacao |  |
| vCSS42 | 764 | apoio_ou_apresentacao |  |
| vCSS43 | 766 | apoio_ou_apresentacao |  |
| vCSS44 | 768 | apoio_ou_apresentacao |  |
| vCSS45 | 770 | apoio_ou_apresentacao |  |
| vCSS46 | 773 | apoio_ou_apresentacao |  |
| vCSS47 | 776 | apoio_ou_apresentacao |  |
| vCSS48 | 777 | apoio_ou_apresentacao |  |
| vCSS49 | 780 | apoio_ou_apresentacao |  |
| vCSS50 | 782 | apoio_ou_apresentacao |  |
| vCSS51 | 785 | apoio_ou_apresentacao |  |
| vCSS52 | 787 | apoio_ou_apresentacao |  |
| vCSS53 | 788 | apoio_ou_apresentacao |  |
| vCSS54 | 790 | apoio_ou_apresentacao |  |
| vCSS55 | 791 | apoio_ou_apresentacao |  |
| vCSS56 | 792 | apoio_ou_apresentacao |  |
| vCSS57 | 793 | apoio_ou_apresentacao |  |
| vCSS58 | 794 | apoio_ou_apresentacao |  |
| vCSS59 | 795 | apoio_ou_apresentacao |  |
| vCSS60 | 796 | apoio_ou_apresentacao |  |
| vCSS61 | 797 | apoio_ou_apresentacao |  |
| vCSS62 | 798 | apoio_ou_apresentacao |  |
| vCSS63 | 799 | apoio_ou_apresentacao |  |
| vCSS64 | 800 | apoio_ou_apresentacao |  |
| vCSS65 | 801 | apoio_ou_apresentacao |  |
| vCSS66 | 802 | apoio_ou_apresentacao |  |
| vCSS67 | 803 | apoio_ou_apresentacao |  |
| vCSS68 | 805 | apoio_ou_apresentacao |  |
| vCSS69 | 806 | apoio_ou_apresentacao |  |
| vCSS70 | 808 | apoio_ou_apresentacao |  |
| vCSS | 810 | apoio_ou_apresentacao |  |
| vSVG2 | 814 | apoio_ou_apresentacao |  |
| HH1 | 818 | apoio_ou_apresentacao |  |
| HFAT | 840 | apoio_ou_apresentacao |  |
| HRSL | 841 | apoio_ou_apresentacao |  |
| HDEV_TOTAL | 842 | apoio_ou_apresentacao |  |
| HPM_META | 843 | apoio_ou_apresentacao |  |
| vClsPMCard | 849 | apoio_ou_apresentacao |  |
| HPM_TOP | 850 | apoio_ou_apresentacao |  |
| HINDPRINCIPAIS | 856 | apoio_ou_apresentacao |  |
| HG2 | 859 | apoio_ou_apresentacao |  |
| HTOPO | 860 | apoio_ou_apresentacao |  |
| HREGCSS | 861 | apoio_ou_apresentacao |  |
| HG4 | 862 | apoio_ou_apresentacao |  |
| HMIXCSS | 863 | apoio_ou_apresentacao |  |
| HG5 | 864 | apoio_ou_apresentacao |  |
| HCTX | 869 | apoio_ou_apresentacao |  |
| vHTML | 884 | apoio_ou_apresentacao |  |
