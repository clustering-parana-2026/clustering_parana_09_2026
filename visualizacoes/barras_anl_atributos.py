from math import ceil


import pandas as pd
import plotly.graph_objects as go


import constantes.estilos as est

from utils.template_plotly import template_plotly
import utils.plotagem as funcs






def _template_barras_horizontais(sr: pd.Series) -> go.Figure:
    """
    Template para os gráficos de barra.
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