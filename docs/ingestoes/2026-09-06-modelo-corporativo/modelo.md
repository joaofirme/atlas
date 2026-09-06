# Inventário técnico da primeira fonte

20 tabelas, 241 colunas, 90 medidas e 28 relacionamentos. Extração estática; estado inicial `draft`.

## Tabelas

| Tabela | Colunas | Partições |
|---|---:|---:|
| [_Medidas](<../../../data_products/corporativo/tabela_medidas.md>) | 0 | 1 |
| [Atualização](<../../../data_products/corporativo/tabela_atualizacao.md>) | 1 | 1 |
| [Base Receita](<../../../data_products/corporativo/tabela_base_receita.md>) | 2 | 1 |
| [dClientes_unificada](<../../../data_products/comercial/tabela_dclientes_unificada.md>) | 13 | 1 |
| [dEmpresa](<../../../data_products/comercial/tabela_dempresa.md>) | 5 | 1 |
| [dExecutivos_unificada](<../../../data_products/comercial/tabela_dexecutivos_unificada.md>) | 12 | 1 |
| [dFeriado](<../../../data_products/comercial/tabela_dferiado.md>) | 1 | 1 |
| [dMaterial_unificada](<../../../data_products/comercial/tabela_dmaterial_unificada.md>) | 29 | 1 |
| [dRegional](<../../../data_products/comercial/tabela_dregional.md>) | 2 | 1 |
| [dTempo](<../../../data_products/comercial/tabela_dtempo.md>) | 15 | 1 |
| [dUF](<../../../data_products/comercial/tabela_duf.md>) | 22 | 1 |
| [fCarteira_pedidos_unificada](<../../../data_products/comercial/tabela_fcarteira_pedidos_unificada.md>) | 21 | 1 |
| [fDevolucao_unificada](<../../../data_products/comercial/tabela_fdevolucao_unificada.md>) | 21 | 1 |
| [fMeta_Geral](<../../../data_products/comercial/tabela_fmeta_geral.md>) | 9 | 1 |
| [fMeta_unificada](<../../../data_products/comercial/tabela_fmeta_unificada.md>) | 14 | 1 |
| [fPlanProd_unificada](<../../../data_products/operacoes/tabela_fplanprod_unificada.md>) | 12 | 1 |
| [fVendas_unificada](<../../../data_products/comercial/tabela_fvendas_unificada.md>) | 53 | 1 |
| [Legenda Gradiente](<../../../data_products/corporativo/tabela_legenda_gradiente.md>) | 1 | 1 |
| [Parâmetros: Matriz Dinâmica](<../../../data_products/corporativo/tabela_parametros_matriz_dinamica.md>) | 3 | 1 |
| [tLogistica e CS](<../../../data_products/logistica/tabela_tlogistica_e_cs.md>) | 5 | 1 |

## Relacionamentos

Valores não declarados permanecem pendentes; não são inferidos como resultados de testes de cardinalidade.

| Origem | Destino | Ativo declarado | Cardinalidade destino declarada | Contrato |
|---|---|---|---|---|
| fDevolucao_unificada.chave_cliente | dClientes_unificada.chave_cliente | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_autodetected_3a7ec5fb_e044_4d8e_bb91_64b680a0678c.yaml>) |
| fVendas_unificada.chave_cliente | dClientes_unificada.chave_cliente | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_autodetected_dce192c7_5eac_41c2_9f47_8e110cb40084.yaml>) |
| fVendas_unificada.companhia | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_572c3062_14e1_a275_25a7_19f0278a9b03.yaml>) |
| fVendas_unificada.data_pedido | dTempo.Data | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_e9e81fbe_ef49_0ef5_e02a_9db5336157a2.yaml>) |
| fVendas_unificada.regional_cod | dRegional.order_sale_order_office_code | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_bc2323fc_68b3_6afa_f392_e7b6ff622dfe.yaml>) |
| fVendas_unificada.sale_cancellation_date | dTempo.Data | false | omitido | [abrir](<../../../ontology/relationships/relacionamento_b2283a9e_b095_76c3_b789_78e205056c3f.yaml>) |
| fVendas_unificada.data_movimento | dTempo.Data | false | omitido | [abrir](<../../../ontology/relationships/relacionamento_2dd7faaf_5dc2_863e_2cfe_ea85d901ab43.yaml>) |
| fDevolucao_unificada.data_movimento | dTempo.Data | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_e2a996b8_b1f2_5ccb_31e2_781e618d5da9.yaml>) |
| fDevolucao_unificada.regional_codigo | dRegional.order_sale_order_office_code | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_f4eedbc4_ea27_34bd_8aa5_d01a57f6ab93.yaml>) |
| fDevolucao_unificada.companhia | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_e03fc402_c1d4_be6e_bf2e_c296a9afc19e.yaml>) |
| fDevolucao_unificada.chave_executivo | dExecutivos_unificada.executivo_chave | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_161570b7_b26e_3199_c561_a7dc1a96bc9a.yaml>) |
| fDevolucao_unificada.sku | dMaterial_unificada.codigo_produto | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_dc76daf3_fd84_0178_4fdf_6a5a48125462.yaml>) |
| fVendas_unificada.sku | dMaterial_unificada.codigo_produto | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_674b67a1_daba_f6f8_f065_acfb362ed046.yaml>) |
| fMeta_unificada.meta_data_alvo | dTempo.Data | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_dd11cd0b_c3a6_7323_3051_65b6486f480e.yaml>) |
| fMeta_unificada.companhia | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_2ec3f4a3_a809_1d18_fdee_30075a931950.yaml>) |
| fMeta_unificada.chave_executivo | dExecutivos_unificada.executivo_chave | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_aa41f29b_e09e_855b_507d_cc07db2208eb.yaml>) |
| fVendas_unificada.chave_executivo | dExecutivos_unificada.executivo_chave | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_db327af3_92e6_8445_b77e_ff98d2e263c4.yaml>) |
| fMeta_unificada.chave_regional | dRegional.order_sale_order_office_code | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_a22dd875_10a7_c4b2_067b_67da443a6c7d.yaml>) |
| fCarteira_pedidos_unificada.data_carteira | dTempo.Data | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_ab55d04b_2753_63db_2450_20f80863e1f8.yaml>) |
| fMeta_unificada.chave_marca | dMaterial_unificada.brand_novo | omitido | many | [abrir](<../../../ontology/relationships/relacionamento_964182c1_8e30_6d21_fa74_e19b722a13a0.yaml>) |
| dExecutivos_unificada.empresa | dEmpresa.Empresa | false | many | [abrir](<../../../ontology/relationships/relacionamento_7eae087a_220d_86ff_9076_bc68cdf46e41.yaml>) |
| fPlanProd_unificada.cobertura_estoque_sku | dMaterial_unificada.codigo_produto | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_ff396aa3_4800_911b_45e1_5af2ad74ff9a.yaml>) |
| fPlanProd_unificada.cobertura_estoque_company | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_30bf1785_b290_6345_d8cc_c2a7023759b4.yaml>) |
| fPlanProd_unificada.cobertura_estoque_data_referencia | dTempo.Data | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_576e8b79_7e81_5ac5_2b3e_0a6a755ba7cd.yaml>) |
| fCarteira_pedidos_unificada.company | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_autodetected_a3c943a9_e146_4ffd_8b12_28019512d403.yaml>) |
| fCarteira_pedidos_unificada.order_sale_order_office_code | dRegional.order_sale_order_office_code | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_autodetected_5a6f9eb5_31ba_4e18_9194_10d04b1f1b35.yaml>) |
| fCarteira_pedidos_unificada.order_sale_material_code | dMaterial_unificada.codigo_produto | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_a04926d7_79bd_54e5_051a_393022f4a582.yaml>) |
| fMeta_Geral.obt_company | dEmpresa.Company | omitido | omitido | [abrir](<../../../ontology/relationships/relacionamento_f35e2acf_6f9c_39ee_899b_4d2415430cdb.yaml>) |

## Segurança declarada

As quatro roles abaixo declaram `modelPermission: read`. Os arquivos não contêm `tablePermission` ou filtros RLS. A associação de usuários e as permissões no serviço não estão disponíveis nesta exportação. Nomes como Acesso_Executivo não comprovam isolamento por executivo.

- [role Acesso_Coordenador](<../../../powerbi/Farmax v3 (1).SemanticModel/definition/roles/Acesso_Coordenador.tmdl>)
- [role Acesso_Executivo](<../../../powerbi/Farmax v3 (1).SemanticModel/definition/roles/Acesso_Executivo.tmdl>)
- [role Acesso_Gerente](<../../../powerbi/Farmax v3 (1).SemanticModel/definition/roles/Acesso_Gerente.tmdl>)
- [role Geral](<../../../powerbi/Farmax v3 (1).SemanticModel/definition/roles/Geral.tmdl>)

## Parâmetros e atualização

RangeStart e RangeEnd estão declarados em expressions.tmdl. Sua mera presença não comprova atualização incremental; as partições lidas não referenciam esses parâmetros. A tabela Atualização usa DateTimeZone.LocalNow com deslocamento -3; isso representa a execução da consulta, não comprova a data máxima dos eventos da origem.

## Método

Extração lexical específica para este PBIP, guiada pela [sintaxe TMDL da Microsoft](https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview). Comentários `///` são descrições; expressões e suas fontes foram preservadas. Não houve execução no Power BI.
