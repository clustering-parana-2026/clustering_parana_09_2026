import pandas as pd
import plotly.graph_objects as go


import constantes.estilos as est

from utils.template_plotly import template_plotly
import utils.plotagem as funcs





def centroides(C) -> go.Figure:
    df_desastre_por_cluster = C.groupby('cluster').mean()
    media_geral = C.drop(columns='cluster').mean()

    fig = go.Figure()
    for cluster in df_desastre_por_cluster.index:
        fig.add_trace(
            go.Scatter(
                x=df_desastre_por_cluster.columns,
                y=df_desastre_por_cluster.iloc[cluster, :],
                name=f"\u03BC<sub>{cluster}</sub>",
                mode='lines+markers',
                line=dict(
                    width=2,
                    color=est.cores_padrao[cluster],
                ),
                marker=dict(
                    size=6.5,
                    color=est.cores_padrao[cluster],
                ),
            )
        )
    fig.add_trace(
        go.Scatter(
            x=media_geral.index,
            y=media_geral,
            mode='lines+markers',
            name="D\u0305",
            line=dict(
                dash='dash', 
                color='gray',
                width=2
            ),
            marker=dict(
                size=6.5,
            ),
        )
    )
    escala=1.4
    fig.update_layout(
        showlegend=True,
        template=template_plotly,
        xaxis=dict(
            title=dict(
                text='X<sub>j</sub>'
            ),
            tickmode="array",
            tickvals=[
                "alagamento_chuva_enxurrada_inundacao",
                "estiagem",
                "granizo_vendaval",
            ],
            ticktext=[
                f'X<sub>{i}</sub>' 
                for i in range(1, 3+1)
            ]
        ),
        yaxis=dict(
            title=dict(
                text='Média de Ocorrências'
            )
        ),
        width=funcs.escalar_largura(escala),
        height=funcs.escalar_altura(escala),
    )
    return fig