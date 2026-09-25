"""
Visualização das análises de dados via Streamlit.

Este módulo provê uma interface para facilitar a visualização 
de operações em DataFrames e gráficos durante o desenvolvimento. 
A utilização do Streamlit permite uma prototipagem mais ágil 
em comparação com ambientes de Notebook tradicionais.
"""


import streamlit as st
st.set_page_config(layout='wide')


from paginas.analise_atributos import pg_analise_atributos
from paginas.pre_processamento import pg_pre_processamento
from paginas.transformacoes import pg_transformacoes
from paginas.analise_silhuetas import pg_analise_silhuetas
from paginas.mineracao import pg_mineracao






paginas = [
    pg_pre_processamento,
    pg_analise_atributos,
    pg_transformacoes,
    pg_analise_silhuetas,
    pg_mineracao,
]

paginas_navegacao = [
    st.Page(pagina)
    for pagina in paginas
]


navegacao = st.navigation(paginas_navegacao)
navegacao.run()


















