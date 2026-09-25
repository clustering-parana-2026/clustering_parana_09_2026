import itertools


import streamlit as st
import pandas as pd
import plotly.graph_objects as go


import constantes.estilos as est




def tabela(df: pd.DataFrame) -> None:
    st.markdown(f'## {df.shape}')
    st.dataframe(df)


_key_counter = itertools.count()

def grafico(plot: go.Figure) -> None:
    st.plotly_chart(
        plot,
        width=int(plot.layout.width or est.largura),
        height=int(plot.layout.height or est.altura),
        theme=None,
        key=f"plotly-{next(_key_counter)}",
    )