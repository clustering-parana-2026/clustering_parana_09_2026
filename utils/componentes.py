"""Funções auxiliares para exibir tabelas e gráficos no Streamlit."""

import itertools
from numpy.typing import ArrayLike


import streamlit as st
import plotly.graph_objects as go


import constantes.estilos as est




def tabela(arr: ArrayLike) -> None:
    """Exiba os dados e suas dimensões no Streamlit.

    Parameters
    ----------
    arr : ArrayLike
        Dados exibidos como tabela, com suas dimensões acima.
        Deve possuir o atributo 'shape'.
    """
    st.markdown(f'## {arr.shape}')
    st.dataframe(arr)


_contador_de_chaves_streamlit = itertools.count()

def grafico(plot: go.Figure) -> None:
    """Exiba uma figura Plotly no Streamlit.

    Parameters
    ----------
    plot : plotly.graph_objects.Figure
        Figura a ser exibida.

    Notes
    -----
    Utiliza a largura e a altura definidas no layout da figura.
    Quando ausentes ou iguais a zero, utiliza 'constantes.estilos.largura'
    e 'constantes.estilos.altura', respectivamente.

    Cada chamada recebe uma chave gerada pelo contador global 
    '_contador_de_chaves_streamlit'.
    """
    st.plotly_chart(
        plot,
        width=int(plot.layout.width or est.largura),
        height=int(plot.layout.height or est.altura),
        theme=None,
        key=f"plotly-{next(_contador_de_chaves_streamlit)}",
    )