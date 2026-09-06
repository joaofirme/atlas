# Cálculos internos — Farmax BI HTML old

Implementação canônica: [Farmax BI HTML old](<../../../../technical/measures/corporativo/metrica_farmax_bi_html_old.yaml>). As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.

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
| fProjecaoFechamento | 198 | calculo_ou_contexto |  |
| fGapProjetado | 199 | calculo_ou_contexto |  |
| fGapProjetadoPerc | 205 | apoio_ou_apresentacao |  |
| tAtingEmpresaBase | 209 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Empresa, Meta RB, Meta RSL |
| tAtingEmpresaFiltrada | 233 | calculo_ou_contexto | __Meta, __Receita |
| tAtingEmpresa | 238 | calculo_ou_contexto | __Empresa |
| vAtingEmpresaQtd | 250 | calculo_ou_contexto |  |
| vAtingNomeX | 252 | apoio_ou_apresentacao |  |
| vAtingTrackX | 253 | apoio_ou_apresentacao |  |
| vAtingTrackW | 254 | apoio_ou_apresentacao |  |
| vAtingValorX | 255 | apoio_ou_apresentacao |  |
| vAtingRowH | 256 | apoio_ou_apresentacao |  |
| vAtingEscalaMaiorMeta | 257 | calculo_ou_contexto | __Meta |
| vAtingEscalaFallback | 262 | calculo_ou_contexto | __Receita |
| vAtingEscalaValorBase | 267 | apoio_ou_apresentacao |  |
| vAtingEscalaValorSeguro | 273 | apoio_ou_apresentacao |  |
| fAtingEscalaMax | 279 | calculo_ou_contexto |  |
| vAtingSVGH | 284 | apoio_ou_apresentacao |  |
| HAtingEmpresaRows | 285 | calculo_ou_contexto | __Empresa, __Meta, __Ordem, __Receita |
| HAtingEmpresaCards | 376 | calculo_ou_contexto | __Empresa, __Meta, __Ordem, __Receita |
| vPMWidth | 430 | calculo_ou_contexto |  |
| vClsDev | 431 | apoio_ou_apresentacao |  |
| vClsPM | 432 | apoio_ou_apresentacao |  |
| vSetaYoY | 433 | apoio_ou_apresentacao |  |
| vSetaMoM | 434 | apoio_ou_apresentacao |  |
| vSetaFatYoY | 435 | apoio_ou_apresentacao |  |
| vSetaFatMoM | 436 | apoio_ou_apresentacao |  |
| fRSL | 437 | calculo_ou_contexto |  |
| fFatNum | 438 | calculo_ou_contexto |  |
| fRSLNum | 439 | calculo_ou_contexto |  |
| fMetaRSL | 440 | calculo_ou_contexto |  |
| fDev | 441 | calculo_ou_contexto |  |
| fRef | 442 | calculo_ou_contexto |  |
| fDevTotNum | 443 | calculo_ou_contexto |  |
| fPercDev | 444 | apoio_ou_apresentacao |  |
| fPercRef | 445 | apoio_ou_apresentacao |  |
| fPercYoY | 446 | apoio_ou_apresentacao |  |
| fPercMoM | 447 | apoio_ou_apresentacao |  |
| fPercFatYoY | 448 | apoio_ou_apresentacao |  |
| fPercFatMoM | 449 | apoio_ou_apresentacao |  |
| fPM | 450 | apoio_ou_apresentacao |  |
| fMetaPM | 451 | apoio_ou_apresentacao |  |
| fAtu | 452 | apoio_ou_apresentacao |  |
| vDiaParcial | 458 | apoio_ou_apresentacao |  |
| fDiaParcial | 463 | apoio_ou_apresentacao |  |
| vTagBase | 466 | apoio_ou_apresentacao |  |
| vEmpresaSelecionada | 476 | calculo_ou_contexto | Empresa |
| vDescricaoEmpresaSelecionada | 481 | calculo_ou_contexto | Description |
| vEmpresaContexto | 486 | calculo_ou_contexto | Description, Empresa |
| vAtualizacaoContexto | 507 | calculo_ou_contexto | 00 Atualização |
| fAtualizacaoContexto | 508 | apoio_ou_apresentacao |  |
| vDataInicialSelecionadaContexto | 518 | calculo_ou_contexto | Data |
| vDataFinalSelecionadaContexto | 519 | calculo_ou_contexto | Data |
| vInicioMesAtualContexto | 520 | apoio_ou_apresentacao |  |
| vFimMesAtualContexto | 521 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesAtualContexto | 522 | apoio_ou_apresentacao |  |
| vParcialBadgeContexto | 527 | apoio_ou_apresentacao |  |
| vDataIniPeriodo | 539 | calculo_ou_contexto | Data |
| vDataFimPeriodo | 540 | calculo_ou_contexto | Data |
| vMesIniPeriodo | 541 | apoio_ou_apresentacao |  |
| vMesFimPeriodo | 548 | apoio_ou_apresentacao |  |
| fPeriodoIniCurto | 555 | apoio_ou_apresentacao |  |
| fPeriodoFimCurto | 556 | apoio_ou_apresentacao |  |
| fPeriodoSelecionado | 557 | apoio_ou_apresentacao |  |
| vPeriodoBadge | 568 | apoio_ou_apresentacao |  |
| vPeriodoIncluiMesCorrente | 569 | apoio_ou_apresentacao |  |
| vParcialBadge | 573 | apoio_ou_apresentacao |  |
| tRegiaoBase | 581 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, Meta RB, Meta RSL, order_sale_order_office |
| tRegiaoFiltrada | 591 | calculo_ou_contexto | __Meta, __Realizado |
| tRegiaoTop | 596 | calculo_ou_contexto | __Nome, __Realizado |
| vRegiaoMaxValor | 603 | calculo_ou_contexto | __Meta, __Realizado |
| vRegiaoMaxSeguro | 608 | apoio_ou_apresentacao |  |
| HRegiaoRows | 610 | calculo_ou_contexto | __Meta, __Nome, __Realizado |
| tMixMarcaBase | 645 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta, novo_segmento |
| tMixMarcaFiltrada | 656 | calculo_ou_contexto | __RSL |
| tMixMarcaTop | 661 | calculo_ou_contexto | __Grupo, __RSL |
| vMixTotal | 669 | calculo_ou_contexto | __RSLTotal |
| vMixTopTotal | 674 | calculo_ou_contexto | __RSL |
| HMixPieSlices | 679 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPieLabels | 729 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPieLegend | 777 | calculo_ou_contexto | __Grupo, __RSL |
| HMixPie | 817 | calculo_ou_contexto |  |
| vCSS01 | 833 | apoio_ou_apresentacao |  |
| vCSS02 | 834 | apoio_ou_apresentacao |  |
| vCSS03 | 835 | apoio_ou_apresentacao |  |
| vCSS04 | 836 | apoio_ou_apresentacao |  |
| vCSS05 | 837 | apoio_ou_apresentacao |  |
| vCSS06 | 838 | apoio_ou_apresentacao |  |
| vCSS07 | 839 | apoio_ou_apresentacao |  |
| vCSS08 | 840 | apoio_ou_apresentacao |  |
| vCSS09 | 841 | apoio_ou_apresentacao |  |
| vCSS10 | 842 | apoio_ou_apresentacao |  |
| vCSS11 | 843 | apoio_ou_apresentacao |  |
| vCSS12 | 844 | apoio_ou_apresentacao |  |
| vCSS13 | 845 | apoio_ou_apresentacao |  |
| vCSS14 | 846 | apoio_ou_apresentacao |  |
| vCSS16 | 848 | apoio_ou_apresentacao |  |
| vCSS17 | 849 | apoio_ou_apresentacao |  |
| vCSS18 | 850 | apoio_ou_apresentacao |  |
| vCSS19 | 851 | apoio_ou_apresentacao |  |
| vCSS20 | 852 | apoio_ou_apresentacao |  |
| vCSS21 | 853 | apoio_ou_apresentacao |  |
| vCSS22 | 854 | apoio_ou_apresentacao |  |
| vCSS24 | 855 | apoio_ou_apresentacao |  |
| vCSS27 | 856 | apoio_ou_apresentacao |  |
| vCSS28 | 857 | apoio_ou_apresentacao |  |
| vCSS29 | 858 | apoio_ou_apresentacao |  |
| vCSS30 | 859 | apoio_ou_apresentacao |  |
| vCSS31 | 861 | apoio_ou_apresentacao |  |
| vCSS32 | 863 | apoio_ou_apresentacao |  |
| vCSS41 | 865 | apoio_ou_apresentacao |  |
| vCSS42 | 867 | apoio_ou_apresentacao |  |
| vCSS43 | 869 | apoio_ou_apresentacao |  |
| vCSS44 | 871 | apoio_ou_apresentacao |  |
| vCSS45 | 873 | apoio_ou_apresentacao |  |
| vCSS46 | 876 | apoio_ou_apresentacao |  |
| vCSS47 | 879 | apoio_ou_apresentacao |  |
| vCSS48 | 880 | apoio_ou_apresentacao |  |
| vCSS49 | 883 | apoio_ou_apresentacao |  |
| vCSS50 | 885 | apoio_ou_apresentacao |  |
| vCSS51 | 888 | apoio_ou_apresentacao |  |
| vCSS52 | 890 | apoio_ou_apresentacao |  |
| vCSS53 | 891 | apoio_ou_apresentacao |  |
| vCSS54 | 893 | apoio_ou_apresentacao |  |
| vCSS55 | 894 | apoio_ou_apresentacao |  |
| vCSS56 | 895 | apoio_ou_apresentacao |  |
| vCSS57 | 896 | apoio_ou_apresentacao |  |
| vCSS58 | 897 | apoio_ou_apresentacao |  |
| vCSS59 | 898 | apoio_ou_apresentacao |  |
| vCSS60 | 899 | apoio_ou_apresentacao |  |
| vCSS61 | 900 | apoio_ou_apresentacao |  |
| vCSS62 | 901 | apoio_ou_apresentacao |  |
| vCSS63 | 902 | apoio_ou_apresentacao |  |
| vCSS64 | 903 | apoio_ou_apresentacao |  |
| vCSS65 | 904 | apoio_ou_apresentacao |  |
| vCSS66 | 905 | apoio_ou_apresentacao |  |
| vCSS67 | 906 | apoio_ou_apresentacao |  |
| vCSS | 908 | apoio_ou_apresentacao |  |
| vSVG2 | 912 | apoio_ou_apresentacao |  |
| HH1 | 916 | apoio_ou_apresentacao |  |
| HH2 | 936 | apoio_ou_apresentacao |  |
| HH3 | 937 | apoio_ou_apresentacao |  |
| HH5 | 938 | apoio_ou_apresentacao |  |
| HH6 | 939 | apoio_ou_apresentacao |  |
| HH8 | 940 | apoio_ou_apresentacao |  |
| HFAT | 943 | apoio_ou_apresentacao |  |
| HRSL | 944 | apoio_ou_apresentacao |  |
| HDEV_TOTAL | 945 | apoio_ou_apresentacao |  |
| HPM_META | 946 | apoio_ou_apresentacao |  |
| vClsPMCard | 952 | apoio_ou_apresentacao |  |
| HPM_TOP | 953 | apoio_ou_apresentacao |  |
| HINDPRINCIPAIS | 959 | apoio_ou_apresentacao |  |
| HG2 | 962 | apoio_ou_apresentacao |  |
| HTOPO | 963 | apoio_ou_apresentacao |  |
| HREGCSS | 964 | apoio_ou_apresentacao |  |
| HG4 | 965 | apoio_ou_apresentacao |  |
| HMIXCSS | 966 | apoio_ou_apresentacao |  |
| HG5 | 967 | apoio_ou_apresentacao |  |
| HCTX | 972 | apoio_ou_apresentacao |  |
| HBASEFLAG | 985 | apoio_ou_apresentacao |  |
| vHTML | 988 | apoio_ou_apresentacao |  |
