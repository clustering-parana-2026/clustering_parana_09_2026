from pathlib import Path

from math import ceil


import plotly.graph_objects as go
import graphviz


from .tipos import Escalar

import constantes.estilos as est





def escalar_largura(proporcao, /) -> dict:
    return ceil(est.largura * proporcao)


def escalar_altura(proporcao, /) -> dict:
    return ceil(est.altura * proporcao)
