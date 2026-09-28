from sklearn import preprocessing


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

from core.matrizes import Matrizes

import utils.componentes as comp





def pg_transformacoes() -> None:
    # Carregar matriz de atributos.
    D = Matrizes.atributos(
        CarregadorDadosEstruturados.cedc()
    )
    comp.tabela(D)
    

    # Aplicar normalização por z-score nos dados.
    X = preprocessing.StandardScaler().fit_transform(D)
    comp.tabela(X)

    