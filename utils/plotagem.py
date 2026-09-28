"""Funções para ajudar na criação de gráficos.

Implementa funções para ajudar a dimensionar figuras.
"""

from math import ceil


import constantes.estilos as est





def escalar_largura(proporcao, /) -> int:
    """Calcule uma largura proporcional à largura padrão.

    Parameters
    ----------
    proporcao : float
        Fator multiplicativo aplicado a ``constantes.estilos.largura``.
        Deve ser fornecido como argumento posicional.

    Returns
    -------
    int
        Produto de ``constantes.estilos.largura`` por ``proporcao``, 
        arredondado para cima até o inteiro mais próximo.
    """
    return ceil(est.largura * proporcao)



def escalar_altura(proporcao, /) -> dict:
    """Calcule uma altura proporcional à largura padrão.
    
    Parameters
    ----------
    proporcao : float
        Fator multiplicativo aplicado a ``constantes.estilos.largura``.
        Deve ser fornecido como argumento posicional.

    Returns
    -------
    int
        Produto de ``constantes.estilos.largura`` por ``proporcao``, 
        arredondado para cima até o inteiro mais próximo.
    """
    return ceil(est.altura * proporcao)
