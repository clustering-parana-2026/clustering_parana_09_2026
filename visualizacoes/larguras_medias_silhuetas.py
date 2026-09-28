"""Visualização da largura média da silhueta para cada k.

Marca cada k de interesse invidualmente.

Utiliza os coeficientes de silhueta como uma medida de 
validação relativa.
"""

from numpy.typing import ArrayLike


import pandas as pd
import plotly.graph_objects as go


import constantes.estilos as est

from utils.template_plotly import template_plotly





def larguras_medias_silhuetas(sr: pd.Series) -> go.Figure:
    """Simples gráfico bivariado para as larguras médias globais de silhueta.

    Parameters
    ----------
    sr : pd.Series
        Série com o eixo x no index e com o 
        eicxo y no nos valores.

    Returns
    -------
    plotly.graph_objects.Figure
        Gráfico de linhas e pontos atribuindo uma largura média 
        global de silhueta para cada número de clusters.
    """
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=sr.index,
            y=sr.values,
            mode='lines+markers',
            line=dict(
                width=2,
                color=est.cores_padrao[0],
            ),
            marker=dict(
                size=5,
                color=est.cores_padrao[0],
            ),
        )
    )
    k_candidatos = sr.nlargest(n=3)
    for k, s in k_candidatos.items():
        fig.add_shape(
            type='line',
            x0=k,
            x1=k,
            y0=0.25,
            y1=s,
            line=dict(
                color='black', 
                width=0.5, 
                dash='dash'
            ),
            layer='below',
        )
    fig.update_layout(
        template=template_plotly,
        xaxis=dict(
            title=dict(
                text='k'
            ),
            tickmode='linear',
            tick0=2,
            dtick=1,
        ),
        yaxis=dict(
            title=dict(
                text='s&#773;(k)'
            ),
            range=[0.25, 0.55]
        ),
    )

    return fig