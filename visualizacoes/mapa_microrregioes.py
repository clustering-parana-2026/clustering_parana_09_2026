"""Visualização dos clusters das microrregiões do Paraná em mapa."""

import plotly.graph_objects as go
import pandas as pd


import constantes.estilos as est

from utils.template_plotly import template_plotly
import utils.plotagem as funcs





def mapa_microrregioes(
    C: pd.DataFrame,
    geo_json,
) -> go.Figure:
    """Constrói um mapa das microrregiões coloridas por cluster.

    Parameters
    ----------
    C : pandas.DataFrame
        Tabela com os nomes das microrregiões no índice e seus rótulos
        de agrupamento na coluna ``cluster``. Os rótulos devem ser
        inteiros não negativos que indexem a paleta de cores do projeto.
    geo_json : dict
        Dados geográficos das microrregiões no formato GeoJSON.
        Cada feição deve conter o nome da microrregião em
        ``properties.nome``, correspondente ao nome utilizado no
        índice de ``C``.

    Returns
    -------
    plotly.graph_objects.Figure
        Mapa com uma cor por cluster, limites das microrregiões em
        branco e legenda com os rótulos dos agrupamentos. Apresenta
        fundo branco e moldura preta.

    Notes
    -----
    A correspondência entre as observações de ``C`` e as feições
    geográficas é estabelecida pelos nomes das microrregiões.

    Cada cluster recebe a cor da paleta do projeto na posição
    indicada por seu rótulo. O mapa é centralizado no Paraná,
    nas coordenadas de latitude -24,5 e longitude -51,5.
    """
    fig = go.Figure()

    for cluster, grupo in C.groupby("cluster", sort=True):
        cor = est.cores_padrao[int(cluster)]

        fig.add_trace(
            go.Choroplethmapbox(
                geojson=geo_json,
                locations=grupo.index,
                featureidkey="properties.nome",
                z=[0] * len(grupo),
                zmin=0,
                zmax=1,
                colorscale=[[0, cor], [1, cor]],
                showscale=False,
                showlegend=True,
                name=f"C<sub>{cluster}</sub>",
                marker=dict(
                    line=dict(
                        width=0.5, 
                        color="white"
                    ),
                ),
            )
        )

    escala = 1.6
    fig.update_layout(
        template=template_plotly,
        paper_bgcolor="white",
        mapbox=dict(
            style="white-bg",
            center=dict(
                lat=-24.5, 
                lon=-51.50
            ),
            zoom=5.0,
            domain=dict(
                x=[0, 0.80], 
                y=[0, 1]
            ),
        ),
        width=funcs.escalar_largura(escala),
        height=funcs.escalar_altura(escala),
        margin=dict(l=10, r=10, t=10, b=10),
        showlegend=True,
        legend=dict(
            orientation="v",
            x=0.85,
            xanchor="right",
            y=0.5,
            yanchor="middle",
            bgcolor="white",        
            font=dict(
                size=25     
            ),
        ),
    )

    fig.add_shape(
        type="rect",
        xref="paper",
        yref="paper",
        x0=0,
        y0=0,
        x1=1,
        y1=1,
        line=dict(color="black", width=1),
        fillcolor="rgba(0,0,0,0)",
        layer="above",
    )

    return fig


