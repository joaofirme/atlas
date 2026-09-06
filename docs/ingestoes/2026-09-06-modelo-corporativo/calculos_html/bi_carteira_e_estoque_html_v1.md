# Cálculos internos — Carteira e Estoque HTML v1

Implementação canônica: [Carteira e Estoque HTML v1](<../../../../metrics/corporativo/metrica_carteira_e_estoque_html_v1.yaml>). As variáveis abaixo pertencem ao escopo dessa expressão e não são medidas independentes. Números de linha são relativos à expressão DAX extraída. Índice lexical de variáveis de nível superior; variáveis aninhadas continuam preservadas na expressão completa.

| Variável | Linha DAX | Classificação | Referências |
|---|---:|---|---|
| vDataRefAtual | 13 | calculo_ou_contexto | 00 Atualização |
| vPrimeiroDiaMesAtual | 25 | apoio_ou_apresentacao |  |
| fltCarteiraData | 28 | calculo_ou_contexto | Data |
| fltCarteiraDataMes | 37 | calculo_ou_contexto | Data |
| vPrimeiroDiaMesAnterior | 47 | apoio_ou_apresentacao |  |
| vUltimoDiaMesAnterior | 48 | apoio_ou_apresentacao |  |
| vPrimeiroDiaMesAnteriorMoM | 50 | apoio_ou_apresentacao |  |
| vDataRefAnteriorMoM | 51 | apoio_ou_apresentacao |  |
| fltCarteiraDataMesAnteriorMoM | 52 | calculo_ou_contexto | Data |
| fltCarteiraDataMesAnterior | 61 | calculo_ou_contexto | Data |
| vEmpresaTxt | 71 | calculo_ou_contexto | Company |
| vEscopoTxt | 76 | apoio_ou_apresentacao |  |
| vIsSanavitaOnly | 83 | calculo_ou_contexto | Empresa |
| vBaseReceitaTxt | 93 | calculo_ou_contexto | Base Receita |
| vUsarReceitaBruta | 95 | apoio_ou_apresentacao |  |
| vBaseTag | 96 | apoio_ou_apresentacao |  |
| vTagBase | 97 | apoio_ou_apresentacao |  |
| vDataIniPeriodo | 101 | apoio_ou_apresentacao |  |
| vDataFimPeriodo | 102 | apoio_ou_apresentacao |  |
| vMesIniPeriodo | 104 | apoio_ou_apresentacao |  |
| vMesFimPeriodo | 111 | apoio_ou_apresentacao |  |
| fPeriodoIniCurto | 118 | apoio_ou_apresentacao |  |
| fPeriodoFimCurto | 119 | apoio_ou_apresentacao |  |
| fPeriodoSelecionado | 120 | apoio_ou_apresentacao |  |
| vAberto | 133 | calculo_ou_contexto | 04 Aberto |
| vProg | 134 | calculo_ou_contexto | 05 Programado |
| vTAF | 135 | calculo_ou_contexto | 03 Total a Faturar |
| vProgM | 137 | calculo_ou_contexto | 05 Programado M+ |
| vVendas | 138 | calculo_ou_contexto | 00 Valor de Vendas |
| vCancelado | 139 | calculo_ou_contexto | 02 Cancelado |
| vDevolucao | 140 | calculo_ou_contexto | 02 Devolução Total |
| vCanceladoMesAnterior | 143 | calculo_ou_contexto | 02 Cancelado |
| vCanceladoDeltaPerc | 148 | calculo_ou_contexto |  |
| vCanceladoDeltaCls | 149 | apoio_ou_apresentacao |  |
| vCanceladoDeltaSeta | 150 | apoio_ou_apresentacao |  |
| fCanceladoDelta | 151 | apoio_ou_apresentacao |  |
| vDevolucaoMesAnterior | 153 | calculo_ou_contexto | 02 Devolução Total |
| vDevolucaoDeltaPerc | 158 | calculo_ou_contexto |  |
| vDevolucaoDeltaCls | 159 | apoio_ou_apresentacao |  |
| vRefaturamento | 161 | calculo_ou_contexto | 01 Refaturamento |
| fRefaturamento | 162 | calculo_ou_contexto |  |
| vDevolucaoDeltaSeta | 163 | apoio_ou_apresentacao |  |
| fDevolucaoDelta | 164 | apoio_ou_apresentacao |  |
| vMesAnteriorNum | 165 | apoio_ou_apresentacao |  |
| fMesAnteriorNome | 166 | apoio_ou_apresentacao |  |
| vEmpresaSelecionada | 178 | calculo_ou_contexto | Empresa |
| vDescricaoEmpresaSelecionada | 183 | calculo_ou_contexto | Description |
| vEmpresaContexto | 188 | calculo_ou_contexto | Description, Empresa |
| vAtualizacao | 209 | calculo_ou_contexto | 00 Atualização |
| vProd | 210 | calculo_ou_contexto | 06 Aguarda Produção |
| vMotSemEstoque | 215 | calculo_ou_contexto | 06 Aguarda Produção |
| vMotAguardProg | 216 | calculo_ou_contexto | 00 Customer Service |
| vMotCredito | 217 | calculo_ou_contexto | 06 Ret.-Limit.créd.exc. |
| vMotBloqFin | 218 | calculo_ou_contexto | 00 Financeiro, 06 Ret.-Limit.créd.exc. |
| vMotLogistica | 223 | calculo_ou_contexto | 00 Logística |
| vMotNaoClassificado | 224 | apoio_ou_apresentacao |  |
| vMotTotalPrev | 227 | apoio_ou_apresentacao |  |
| tMotivos | 228 | apoio_ou_apresentacao |  |
| tMotivoTop | 237 | calculo_ou_contexto | Nome, Valor |
| vMotivoPrincipalNome | 238 | calculo_ou_contexto | Nome |
| vMotivoPrincipalCor | 239 | calculo_ou_contexto | Cor |
| vMotivoPrincipalValor | 240 | calculo_ou_contexto | Valor |
| fMotivoPrincipalPerc | 241 | calculo_ou_contexto |  |
| fMotivoPrincipalValorFmt | 242 | calculo_ou_contexto |  |
| vPercAberto | 245 | calculo_ou_contexto |  |
| vPercProg | 246 | calculo_ou_contexto |  |
| vPercCancel | 247 | calculo_ou_contexto |  |
| vClsCanc | 248 | apoio_ou_apresentacao |  |
| vPercDevolucao | 249 | calculo_ou_contexto |  |
| vClsDevol | 250 | apoio_ou_apresentacao |  |
| fTAFNum | 253 | calculo_ou_contexto |  |
| fAbertoNum | 254 | calculo_ou_contexto |  |
| fProgNum | 255 | calculo_ou_contexto |  |
| fProgM | 256 | calculo_ou_contexto |  |
| vProgMesAtual | 257 | apoio_ou_apresentacao |  |
| fProgMesAtual | 258 | calculo_ou_contexto |  |
| fCancelNum | 259 | calculo_ou_contexto |  |
| fDevolucaoNum | 260 | calculo_ou_contexto |  |
| fProdNum | 261 | calculo_ou_contexto |  |
| fPercAberto | 263 | apoio_ou_apresentacao |  |
| fPercProg | 264 | apoio_ou_apresentacao |  |
| fPercCancel | 265 | apoio_ou_apresentacao |  |
| fAtu | 266 | apoio_ou_apresentacao |  |
| vDiaParcial | 272 | apoio_ou_apresentacao |  |
| fDiaParcial | 273 | apoio_ou_apresentacao |  |
| vParcialBadge | 275 | apoio_ou_apresentacao |  |
| vRSLCarteira | 285 | calculo_ou_contexto | 03 RSL |
| vReceitaBrutaCarteira | 287 | calculo_ou_contexto | 09 Receita Bruta |
| vReceita | 289 | apoio_ou_apresentacao |  |
| vReceitaMesAnterior | 290 | calculo_ou_contexto | 03 RSL, 09 Receita Bruta |
| vReceitaDeltaPerc | 296 | calculo_ou_contexto |  |
| vReceitaDeltaCls | 298 | apoio_ou_apresentacao |  |
| vReceitaDeltaSeta | 299 | apoio_ou_apresentacao |  |
| fReceitaDelta | 300 | apoio_ou_apresentacao |  |
| fReceitaNum | 301 | calculo_ou_contexto |  |
| vMetaRBTextoCarteira | 303 | calculo_ou_contexto | Meta RB |
| vMetaReceita | 304 | calculo_ou_contexto | Meta RSL |
| vTemMetaReceita | 314 | apoio_ou_apresentacao |  |
| fMetaReceita | 315 | calculo_ou_contexto |  |
| HK0 | 318 | apoio_ou_apresentacao |  |
| HK1 | 319 | apoio_ou_apresentacao |  |
| HK2 | 320 | apoio_ou_apresentacao |  |
| HK3 | 321 | apoio_ou_apresentacao |  |
| HK5 | 322 | apoio_ou_apresentacao |  |
| HK6 | 323 | apoio_ou_apresentacao |  |
| HKF | 324 | apoio_ou_apresentacao |  |
| vFunilCarteiraInicial | 331 | calculo_ou_contexto | 10 Carteira Inicial |
| vFunilVenda | 334 | apoio_ou_apresentacao |  |
| vFunilProgramadoMFuturo | 337 | calculo_ou_contexto | 05 Programado M+ |
| vFunilCancelado | 340 | calculo_ou_contexto | 02 Cancelado |
| vFunilProgramadoAtual | 343 | calculo_ou_contexto | 05 Programado, 05 Programado M+ |
| vFunilFaturado | 346 | calculo_ou_contexto | 00 Faturamento |
| vF_CarteiraInicial | 348 | apoio_ou_apresentacao |  |
| vF_Venda | 349 | apoio_ou_apresentacao |  |
| vF_Massa | 350 | apoio_ou_apresentacao |  |
| vF_Faturavel | 351 | apoio_ou_apresentacao |  |
| vMotFinanceiroFunil | 354 | calculo_ou_contexto | 00 Financeiro |
| vF_AposSemEstoque | 357 | apoio_ou_apresentacao |  |
| vF_AposAguardProg | 358 | apoio_ou_apresentacao |  |
| vF_AposFinanceiro | 359 | apoio_ou_apresentacao |  |
| vF_AposLogistica | 360 | apoio_ou_apresentacao |  |
| vF_AposNaoClassif | 361 | apoio_ou_apresentacao |  |
| vF_FaturadoCalc | 364 | apoio_ou_apresentacao |  |
| vF_DiferencaTeste | 366 | apoio_ou_apresentacao |  |
| fDebugTeste | 367 | calculo_ou_contexto |  |
| vF_Faturado | 372 | apoio_ou_apresentacao |  |
| mCarteiraInicial | 374 | calculo_ou_contexto |  |
| mVenda | 375 | calculo_ou_contexto |  |
| mProgramadoMFuturo | 376 | calculo_ou_contexto |  |
| mCancelado | 377 | calculo_ou_contexto |  |
| mFaturavel | 378 | calculo_ou_contexto |  |
| mMotSemEstoque | 379 | calculo_ou_contexto |  |
| mMotAguardProg | 380 | calculo_ou_contexto |  |
| mMotFinanceiro | 381 | calculo_ou_contexto |  |
| mMotLogistica | 382 | calculo_ou_contexto |  |
| mMotNaoClassificado | 383 | calculo_ou_contexto |  |
| mProgramadoAtual | 384 | calculo_ou_contexto |  |
| mFaturado | 385 | calculo_ou_contexto |  |
| vMaxAbsRaw | 387 | calculo_ou_contexto | Value |
| vArred | 396 | apoio_ou_apresentacao |  |
| vMaxMi | 406 | apoio_ou_apresentacao |  |
| vBaseY | 407 | apoio_ou_apresentacao |  |
| vTopY | 408 | apoio_ou_apresentacao |  |
| vPlotH | 409 | apoio_ou_apresentacao |  |
| vScale | 410 | calculo_ou_contexto |  |
| hCI | 412 | apoio_ou_apresentacao |  |
| yCI | 413 | apoio_ou_apresentacao |  |
| clsCI | 414 | apoio_ou_apresentacao |  |
| yAfterVenda | 416 | apoio_ou_apresentacao |  |
| hVenda | 417 | apoio_ou_apresentacao |  |
| yVendaTop | 418 | apoio_ou_apresentacao |  |
| yAfterProgramadoMFuturo | 420 | apoio_ou_apresentacao |  |
| hProgramadoMFuturo | 421 | apoio_ou_apresentacao |  |
| yProgramadoMFuturoTop | 422 | apoio_ou_apresentacao |  |
| yFaturavel | 424 | apoio_ou_apresentacao |  |
| hCancelado | 425 | apoio_ou_apresentacao |  |
| yCanceladoTop | 426 | apoio_ou_apresentacao |  |
| hFaturavel | 428 | apoio_ou_apresentacao |  |
| clsFaturavel | 429 | apoio_ou_apresentacao |  |
| yAposSemEstoque | 432 | apoio_ou_apresentacao |  |
| hMotSemEstoque | 433 | apoio_ou_apresentacao |  |
| yMotSemEstoqueTop | 434 | apoio_ou_apresentacao |  |
| yAposAguardProg | 436 | apoio_ou_apresentacao |  |
| hMotAguardProg | 437 | apoio_ou_apresentacao |  |
| yMotAguardProgTop | 438 | apoio_ou_apresentacao |  |
| yAposFinanceiro | 440 | apoio_ou_apresentacao |  |
| hMotFinanceiro | 441 | apoio_ou_apresentacao |  |
| yMotFinanceiroTop | 442 | apoio_ou_apresentacao |  |
| yAposLogistica | 444 | apoio_ou_apresentacao |  |
| hMotLogistica | 445 | apoio_ou_apresentacao |  |
| yMotLogisticaTop | 446 | apoio_ou_apresentacao |  |
| yAposNaoClassificado | 448 | apoio_ou_apresentacao |  |
| hMotNaoClassificado | 449 | apoio_ou_apresentacao |  |
| yMotNaoClassificadoTop | 450 | apoio_ou_apresentacao |  |
| yAposProgramadoAtual | 453 | apoio_ou_apresentacao |  |
| hProgramadoAtual | 454 | apoio_ou_apresentacao |  |
| yProgramadoAtualTop | 455 | apoio_ou_apresentacao |  |
| yFaturado | 457 | apoio_ou_apresentacao |  |
| hFaturado | 458 | apoio_ou_apresentacao |  |
| clsFaturado | 459 | apoio_ou_apresentacao |  |
| bw | 461 | apoio_ou_apresentacao |  |
| x1 | 462 | apoio_ou_apresentacao |  |
| x2 | 463 | apoio_ou_apresentacao |  |
| x3 | 464 | apoio_ou_apresentacao |  |
| x4 | 465 | apoio_ou_apresentacao |  |
| x5 | 466 | apoio_ou_apresentacao |  |
| x6 | 467 | apoio_ou_apresentacao |  |
| x7 | 468 | apoio_ou_apresentacao |  |
| x8 | 469 | apoio_ou_apresentacao |  |
| x9 | 470 | apoio_ou_apresentacao |  |
| x10 | 471 | apoio_ou_apresentacao |  |
| x11 | 472 | apoio_ou_apresentacao |  |
| x12 | 473 | apoio_ou_apresentacao |  |
| vBandTop | 475 | apoio_ou_apresentacao |  |
| vBandBottom | 476 | apoio_ou_apresentacao |  |
| vBandH | 477 | apoio_ou_apresentacao |  |
| vBandPad | 478 | apoio_ou_apresentacao |  |
| vYelX | 480 | apoio_ou_apresentacao |  |
| vYelW | 481 | apoio_ou_apresentacao |  |
| HBandMotivos | 482 | apoio_ou_apresentacao |  |
| vLarW | 485 | apoio_ou_apresentacao |  |
| HBandProgMFuturo | 486 | apoio_ou_apresentacao |  |
| HBandProgAtual | 488 | apoio_ou_apresentacao |  |
| HBandCancelados | 490 | apoio_ou_apresentacao |  |
| gStep | 493 | calculo_ou_contexto |  |
| g1v | 494 | apoio_ou_apresentacao |  |
| g2v | 495 | apoio_ou_apresentacao |  |
| g3v | 496 | apoio_ou_apresentacao |  |
| g4v | 497 | apoio_ou_apresentacao |  |
| g5v | 498 | apoio_ou_apresentacao |  |
| g1y | 499 | apoio_ou_apresentacao |  |
| g2y | 500 | apoio_ou_apresentacao |  |
| g3y | 501 | apoio_ou_apresentacao |  |
| g4y | 502 | apoio_ou_apresentacao |  |
| g5y | 503 | apoio_ou_apresentacao |  |
| HGrid | 505 | apoio_ou_apresentacao |  |
| HBarCarteiraInicial | 519 | apoio_ou_apresentacao |  |
| HBarVenda | 531 | apoio_ou_apresentacao |  |
| HBarProgramadoMFuturo | 539 | apoio_ou_apresentacao |  |
| HBarCancelado | 547 | apoio_ou_apresentacao |  |
| HBarFaturavel | 552 | apoio_ou_apresentacao |  |
| HBarMotSemEstoque | 560 | apoio_ou_apresentacao |  |
| HBarMotAguardProg | 568 | apoio_ou_apresentacao |  |
| HBarMotFinanceiro | 576 | apoio_ou_apresentacao |  |
| HBarMotLogistica | 581 | apoio_ou_apresentacao |  |
| HBarMotNaoClassificado | 586 | apoio_ou_apresentacao |  |
| HBarProgramadoAtual | 594 | apoio_ou_apresentacao |  |
| HBarFaturado | 602 | apoio_ou_apresentacao |  |
| HHoverZones | 607 | calculo_ou_contexto | Value |
| vSVGFunil | 614 | apoio_ou_apresentacao |  |
| HFUNIL | 624 | apoio_ou_apresentacao |  |
| fSitEntregue | 705 | calculo_ou_contexto |  |
| fSitTransito | 706 | calculo_ou_contexto |  |
| fSitProgramado | 707 | calculo_ou_contexto |  |
| fSitAberto | 708 | calculo_ou_contexto |  |
| fSitBloqueio | 709 | calculo_ou_contexto |  |
| fSitCancelado | 710 | calculo_ou_contexto |  |
| HSitLegend | 712 | apoio_ou_apresentacao |  |
| HSITUACAO | 722 | apoio_ou_apresentacao |  |
| tPedidosFarmax | 730 | calculo_ou_contexto | canal_n1, chave_cliente, data_pedido, empresa, obt_sales_department_status, order_sale_subtotal, pedido, pedido_status, pedido_tipo, regional_cod, sale_program_date, sku |
| tPedidosSanavita | 748 | calculo_ou_contexto | canal_n1, chave_cliente, data_pedido, empresa, obt_sales_department_status, order_sale_subtotal, pedido, pedido_status, pedido_tipo, regional_cod, sale_program_date, sku |
| tPedidosBase | 766 | apoio_ou_apresentacao |  |
| tPedidosComNomeCliente | 768 | calculo_ou_contexto | chave_cliente, cliente, codigo_produto, descricao, order_sale_order_office, order_sale_order_office_code, regional_cod, sku |
| tPedidosComTrim | 785 | calculo_ou_contexto | obt_sales_department_status |
| tPedidosComNome | 792 | calculo_ou_contexto | __StatusDeptTrim, sale_program_date |
| tPedidosSoAberto | 824 | calculo_ou_contexto | __StatusCls |
| tPedidosTop | 826 | calculo_ou_contexto | Pendente |
| vPedSubtotal | 828 | calculo_ou_contexto | Pendente |
| fPedSubtotal | 829 | calculo_ou_contexto |  |
| HPedTotal | 833 | apoio_ou_apresentacao |  |
| HPedHead | 839 | apoio_ou_apresentacao |  |
| HPedRows | 842 | calculo_ou_contexto | Pendente, __MotivoCls, __MotivoTxt, __NomeCliente, __NomeRegional, __NomeSKU, __StatusCls, __StatusTxt, canal_n1, data_pedido, pedido |
| HPEDIDOS | 873 | apoio_ou_apresentacao |  |
| vAlvoDias | 883 | apoio_ou_apresentacao |  |
| tSKUBase | 885 | calculo_ou_contexto | cobertura_estoque_cobertura, cobertura_estoque_plano_medio, cobertura_estoque_quantidade, cobertura_estoque_sku, status_sku |
| tSKUComDemandaPositiva | 894 | calculo_ou_contexto | Demanda |
| tSKUAtivos | 896 | calculo_ou_contexto | StatusSKU |
| tSKUComNome | 902 | calculo_ou_contexto | cobertura_estoque_sku, codigo_produto, descricao |
| tSKUComCarteira | 911 | calculo_ou_contexto | 03 Total a Faturar, cobertura_estoque_sku, sku |
| tSKUComTicket | 924 | calculo_ou_contexto | cobertura_estoque_sku, data_pedido, pedido_status, pedido_tipo, quantidade, receita, sku |
| tSKUComValores | 946 | calculo_ou_contexto | Demanda, EstoqueCalculado, TicketMedio |
| tSKUComEstoqueTotal | 953 | calculo_ou_contexto | A Faturar, EstoqueCalculadoValor |
| tSKUComDiasTratados | 959 | calculo_ou_contexto | Dias |
| tSKUOrd | 964 | calculo_ou_contexto | DiasTratado |
| tSKUTop | 965 | calculo_ou_contexto | DemandaValor, cobertura_estoque_sku |
| vSkuMaxDias | 967 | calculo_ou_contexto | DiasTratado |
| vSkuScaleMax | 968 | apoio_ou_apresentacao |  |
| vSkuTargetPct | 969 | calculo_ou_contexto |  |
| vSkuTotDemanda | 971 | calculo_ou_contexto | DemandaValor |
| vSkuTotEstqTot | 972 | calculo_ou_contexto | EstoqueTotalValor |
| vSkuTotCart | 973 | calculo_ou_contexto | A Faturar |
| vSkuTotEstqCal | 974 | calculo_ou_contexto | EstoqueCalculadoValor |
| fSkuTotDemanda | 976 | calculo_ou_contexto |  |
| fSkuTotEstqTot | 980 | calculo_ou_contexto |  |
| fSkuTotCart | 984 | calculo_ou_contexto |  |
| fSkuTotEstqCal | 988 | calculo_ou_contexto |  |
| HSkuTotal | 992 | apoio_ou_apresentacao |  |
| HSkuHead | 1002 | apoio_ou_apresentacao |  |
| HSkuRows | 1005 | calculo_ou_contexto | A Faturar, DemandaValor, DiasTratado, EstoqueCalculadoValor, EstoqueTotalValor, __NomeSKU |
| HSKU | 1054 | apoio_ou_apresentacao |  |
| vCSSBase | 1064 | apoio_ou_apresentacao |  |
| vCSSBadges | 1068 | apoio_ou_apresentacao |  |
| vCSSContext | 1071 | apoio_ou_apresentacao |  |
| vCSSKpi | 1074 | apoio_ou_apresentacao |  |
| vCSSChart | 1080 | apoio_ou_apresentacao |  |
| vCSSSku | 1083 | apoio_ou_apresentacao |  |
| vCSSPedidos | 1086 | apoio_ou_apresentacao |  |
| vCSSTotais | 1089 | apoio_ou_apresentacao |  |
| vCSSKpiSec | 1091 | apoio_ou_apresentacao |  |
| vCSSInfo | 1093 | apoio_ou_apresentacao |  |
| vCSS | 1095 | apoio_ou_apresentacao |  |
| HCTX | 1098 | apoio_ou_apresentacao |  |
| vHTML | 1113 | apoio_ou_apresentacao |  |
