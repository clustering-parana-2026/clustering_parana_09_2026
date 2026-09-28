"""Visualização das silhuetas das observações por cluster e valor de k."""

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


import constantes.estilos as est


from utils.template_plotly import template_plotly
import utils.plotagem as funcs





def silhuetas_clusters(
    s_por_objeto_por_agrupamento: dict[int, pd.DataFrame],
) -> go.Figure:
    """Constrói gráficos de silhueta para diferentes valores de k.

    Parameters
    ----------
    s_por_objeto_por_agrupamento : dict[int, pandas.DataFrame]
        Dicionário que associa cada número de clusters ``k`` a uma
        tabela com uma linha por observação. Cada tabela deve conter
        as colunas ``cluster``, com os rótulos dos clusters, e ``s``,
        com as larguras de silhueta previamente calculadas.
        Deve conter pelo menos um agrupamento.

    Returns
    -------
    plotly.graph_objects.Figure
        Figura com um painel por agrupamento, disposto na ordem
        de inserção das chaves do dicionário. Cada barra horizontal
        representa a largura de silhueta de uma observação, com
        cores e espaçamento que distinguem os clusters.

    Notes
    -----
    Os clusters são apresentados em ordem crescente de seus rótulos.
    Dentro de cada cluster, as observações são ordenadas por largura
    de silhueta decrescente, de cima para baixo.

    Em cada painel, a linha vertical cinza indica o valor zero,
    enquanto a linha preta tracejada indica a largura média global
    da silhueta, calculada sobre as observações da tabela.

    O eixo horizontal é limitado ao intervalo [-0,2, 1], já que
    não se observou valores inferiores a -0,2.
    """
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

