import streamlit as st


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

import utils.componentes as comp

from visualizacoes.fluxogramas import fluxograma_metodo





def pg_pre_processamento() -> None:
    dfs = [
        CarregadorDadosEstruturados.cedc(),
        # CarregadorDadosEstruturados.atlas(),
        # CarregadorDadosEstruturados.ips(),
    ]

    for df in dfs:
        comp.tabela(df)
        st.markdown(f'## Tipos')
        st.write(df.dtypes)