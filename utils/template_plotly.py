"""Template geral para os gráficos Plotly."""

import plotly.graph_objects as go


import constantes.estilos as est




 
template_plotly = go.layout.Template()
template_plotly.layout = dict(
    autosize=False,
    showlegend=False,

    xaxis=dict( 
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
                color='black'
            ),
            standoff=15,
        ),
        tickfont=dict(
            size=10,
            color='black'
        ),

        gridcolor='black',
        linecolor='black',
    ),
    yaxis=dict( 
        showgrid=False,
        zeroline=False,
        showline=True,
        mirror=True,

        title=dict(
            font=dict(
                size=14,
            ),
            standoff=10,
        ),
        tickfont=dict(
            size=10,
            color='black'
        ),

        gridcolor='black',
        linecolor='black', 
    ),
    margin=dict(t=10,b=45,r=50,l=50),
    paper_bgcolor='white',
    plot_bgcolor='white',
    width=est.largura,
    height=est.altura,
)