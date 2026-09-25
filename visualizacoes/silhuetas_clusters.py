from numpy.typing import ArrayLike


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


import constantes.estilos as est


from utils.template_plotly import template_plotly
import utils.plotagem as funcs






def silhuetas_clusters(
    s_por_objeto_por_agrupamento: dict[int, pd.DataFrame],
) -> go.Figure:
    fig = make_subplots(
        rows=1,
        cols=len(s_por_objeto_por_agrupamento),
        subplot_titles=[
            f"k={k}" for k in s_por_objeto_por_agrupamento
        ],
        x_title="s(x<sub>i</sub>)",
    )

    for coluna, (k, df) in enumerate(
        s_por_objeto_por_agrupamento.items(),
        start=1,
    ):
        inicio = 1
        posicoes, nomes = [], []

        for i, (cluster, grupo) in enumerate(df.groupby("cluster")):
            valores = grupo["s"].sort_values(ascending=False)
            fim = inicio + len(valores)
            cor = est.cores_padrao[i % len(est.cores_padrao)]

            fig.add_trace(
                go.Bar(
                    x=valores,
                    y=list(range(inicio, fim)),
                    orientation="h",
                    width=1,
                    marker=dict(
                        color=cor,
                        line=dict(
                            width=0,
                        ),
                    ),
                    name=f"k={k}, C={cluster}",
                ),
                row=1,
                col=coluna,
            )

            posicoes.append((inicio + fim - 1) / 2)
            nomes.append(f"C{cluster}")
            inicio = fim + 2

        fig.add_vline(
            x=0,
            line=dict(
                color="gray",
                width=1,
            ),
            row=1,
            col=coluna,
        )
        fig.add_vline(
            x=df["s"].mean(),
            line=dict(
                color="black",
                dash="dash",
            ),
            row=1,
            col=coluna,
        )
        fig.update_yaxes(
            tickmode="array",
            tickvals=posicoes,
            ticktext=nomes,
            autorange="reversed",
            row=1,
            col=coluna,
        )

    fig.update_xaxes(
        range=[-0.2, 1],
        dtick=0.25,
    )
    fig.update_yaxes(
        title=dict(
            text="Cluster",
        ),
        row=1,
        col=1,
    )

    fig.update_layout(
        template=template_plotly,
        barmode="overlay",
        bargap=0,

        width=funcs.escalar_largura(1.6),
        height=funcs.escalar_altura(1.4),
        margin=dict(t=30, b=65)
    )

    return fig

