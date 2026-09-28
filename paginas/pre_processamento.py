import streamlit as st


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

import utils.componentes as comp





def pg_pre_processamento() -> None:
    # Carregar dados.
    dfs = [
        CarregadorDadosEstruturados.cedc(),
        # CarregadorDadosEstruturados.atlas(),
        # CarregadorDadosEstruturados.ips(),
    ]


    # Exibir tabela, dimensões e tipos.
    for df in dfs:
        comp.tabela(df)
        st.markdown(f'## Tipos')
        st.write(df.dtypes)