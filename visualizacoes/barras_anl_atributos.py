"""Construção de gráficos de barras para a análise descritiva dos atributos."""

import pandas as pd
import plotly.graph_objects as go


import constantes.estilos as est

from utils.template_plotly import template_plotly
import utils.plotagem as funcs





def _template_barras_horizontais(sr: pd.Series) -> go.Figure:
    """Constrói um gráfico de barras horizontais a partir de uma série.

    Parameters
    ----------
    sr : pandas.Series
        Série com as categorias no índice e os valores numéricos
        representados pelo comprimento das barras.

    Returns
    -------
    plotly.graph_objects.Figure
        Figura com as categorias no eixo vertical e os valores no
        eixo horizontal, formatada segundo os estilos do projeto.

    Notes
    -----
    A espessura das barras é definida como ``0.075 * sr.size``,
    para padronizar a espessura mesmo para diferentes números de 
    barras.
    """
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=sr.values,
            y=sr.index,
            orientation='h',
            width=sr.size * 0.075,
            marker=dict(
                color=est.cores_padrao[0]
            ),
        )
    )
    fig.update_layout(
        template=template_plotly,
        barcornerradius=8,
        width=funcs.escalar_largura(1.3),  
        margin=dict(l=70, r=70)
    )
    return fig


def barras_frequencia_materiais(sr: pd.Series) -> go.Figure:
    fig = _template_barras_horizontais(sr)
    fig.update_layout(
        xaxis=dict(
            title=dict(
                text='Total de Envios'
            )
        ),
    )
    return fig


def barras_frequencia_desastres(sr: pd.Series) -> go.Figure:
    fig = _template_barras_horizontais(sr)
    fig.update_layout(
        xaxis=dict(
            title=dict(
                text='Total de Ocorrências'
            )
        ),
    )
    return fig