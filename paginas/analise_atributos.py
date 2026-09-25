import streamlit as st


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

from core.analise_atributos import AnaliseAtributos

import utils.componentes as comp

import visualizacoes.barras_anl_atributos as barras
import visualizacoes.tabelas as tabelas





def pg_analise_atributos() -> None:
    # Inicialização.
    anl = AnaliseAtributos(
        CarregadorDadosEstruturados.cedc()
    )

    # Visualizar frequência dos subgrupos de desastre.
    frequencia_desastres = anl.calcular_frequencia_desastres()
    grafico_freq_desastres = barras.barras_frequencia_desastres(frequencia_desastres)
    st.markdown(f'## frequencia_desastres')
    comp.grafico(grafico_freq_desastres)

    # Visualizar frequência a frequência com que cada material foi enviado.
    frequencia_materiais = anl.calcular_frequencia_materiais()
    grafico_freq_materiais = barras.barras_frequencia_materiais(frequencia_materiais)
    st.markdown(f'## frequencia_materiais')
    comp.grafico(grafico_freq_materiais)

    # Observar estatíticas relacionadas aos lotes de cada tipo de material.
    sumario_envios_de_material = anl.calcular_sumario_envios_de_material()
    grafico_sumario_envios = (
        tabelas.tabela_sumario_envios_envios_de_material(
            sumario_envios_de_material
        )
    )
    st.markdown(f'## sumario_lotes')
    comp.grafico(grafico_sumario_envios)

    # Observar relacão entre materiais por subgrupo de desastre.
    quantidade_normalizada_de_material_por_desastre = (
        anl.calcular_quantidade_normalizada_de_material_por_agrupamento(
            col='desastre',
        )
    )
    grafico_qtd_material_por_desastre = (
        tabelas.tabela_quantidades_normalizadas_por_desastre(
            quantidade_normalizada_de_material_por_desastre
        )
    )
    st.markdown(f'## relacoes_material_desastre')
    comp.grafico(grafico_qtd_material_por_desastre)

    # Correlação.
    correlacao_desastres_sobre_material = (
        quantidade_normalizada_de_material_por_desastre
        .T
        .corr()
    )
    grafico_correlacao_desastres_sobre_material = (
        tabelas.tabela_correlacao_desastres_sobre_material(
            correlacao_desastres_sobre_material
        )
    )
    st.markdown(f'## correlacao_desastres_sobre_material')
    comp.grafico(grafico_correlacao_desastres_sobre_material)

    # Observar relacão entre materiais por subgrupo de desastre.
    quantidade_normalizada_de_material_por_atributo = (
        anl.calcular_quantidade_normalizada_de_material_por_agrupamento(
            col='agrupamento_desastre',
        )
    )
    grafico_qtd_material_por_atributo = (
        tabelas.tabela_quantidades_normalizadas_por_atributo(
            quantidade_normalizada_de_material_por_atributo
        )
    )
    st.markdown(f'## relacoes_material_atributo')
    comp.grafico(grafico_qtd_material_por_atributo)

