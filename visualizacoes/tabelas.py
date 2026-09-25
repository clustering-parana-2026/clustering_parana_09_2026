import plotly.graph_objects as go
import pandas as pd


import constantes.estilos as est

from utils.tipos import Escalar
import utils.plotagem as funcs






def _levar_colunas_do_df_para_plotly(df):
    return list(df.columns)


def _levar_valores_do_df_para_plotly(df):
    return [df[col].to_list() for col in df.columns]


def _template_tabela(
    df: pd.DataFrame,  
    colunas: list[str] | None = None,
    altura: int = est.altura, 
    largura: int = est.largura,
) -> go.Figure:
    """
    Template para as tabelas.
    """
    if colunas is None:
        colunas = list(df.columns)
    df_tabela = df.copy()
    df_tabela.columns = colunas
    df_tabela = df_tabela.round(2)

    fig = go.Figure()
    estilo_tabela = dict(
        font=dict(
            size=11,
            color='black'
        ),
        line=dict(
            color='black'
        ),
        fill_color='rgba(0,0,0,0)',
        align='center',
        height=20,
    )
    fig.add_trace(
        go.Table(
            header=dict(
                values=_levar_colunas_do_df_para_plotly(df_tabela),
                **estilo_tabela,
            ),
            cells=dict(
                values=_levar_valores_do_df_para_plotly(df_tabela),
                **estilo_tabela,
            ),
        )
    )
    fig.update_layout(
        margin=dict(b=10, t=10, l=10, r=10),
        width=largura,
        height=altura,
    )
    return fig


def tabela_sumario_envios_envios_de_material(
    df: pd.DataFrame
) -> go.Figure:
    df_tabela = df.copy()
    df_tabela.insert(0, 'desastre', list(df.index))
     
    fig = _template_tabela(
        df=df_tabela,
        colunas=['Material', 'Média', 'CV', 'Menor Envio', 'Maior Envio'],
        altura=funcs.escalar_altura(0.80),
        largura=funcs.escalar_largura(1.2)
    ) 
    return fig


def tabela_quantidades_normalizadas_por_desastre(
    df: pd.DataFrame
) -> go.Figure:
    df_tabela = df.copy()
    df_tabela.insert(0, '', list(df.index))

    fig = _template_tabela(
        df=df_tabela,
        largura=funcs.escalar_largura(1.4),
    )
    return fig


def tabela_correlacao_desastres_sobre_material(
    df: pd.DataFrame
) -> go.Figure:
    df_tabela = df.copy()
    df_tabela.insert(0, ' ', list(df.columns))
    
    fig = _template_tabela(
        df=df_tabela,
        largura=funcs.escalar_largura(1.6),
    )
    return fig


def tabela_quantidades_normalizadas_por_atributo(
    df: pd.DataFrame
):
    df_tabela = df.copy()
    X_j = [f'X<sub>{i}</sub>' for i in range(1, 3+1)]
    df_tabela.insert(0, '', X_j)       

    fig = _template_tabela(
        df=df_tabela,
        largura=funcs.escalar_largura(1.4),
        altura=funcs.escalar_altura(0.78)   
    )
    return fig        
    