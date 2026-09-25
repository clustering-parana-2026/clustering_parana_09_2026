from sklearn import preprocessing


from core.matrizes import Matrizes
from core.mineracao import Mineracao

from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados
from carregamento.coordenadas_mapa import coletar_coordenadas_parana

import utils.componentes as comp

from visualizacoes.mapa_microrregioes import mapa_microrregioes
from visualizacoes.centroides import centroides





def pg_mineracao() -> None:
    # Carregar matriz de atributos.
    D = Matrizes.atributos(
        CarregadorDadosEstruturados.cedc()
    )

    # Aplicar normalização por z-score nos dados.
    X = preprocessing.StandardScaler().fit_transform(D)

    # Executar KMeans.
    k = 7
    modelos = Mineracao.obter_modelos_kmeans(
        X=X,
        k=[k],
    )

    C = Matrizes.clustering(
        D=D,
        rotulos=modelos[k].labels_,
        formato='dados_originais'
    )

    geo_json = coletar_coordenadas_parana()
    mapa = mapa_microrregioes(
        C=C,
        geo_json=geo_json,
    )
    comp.grafico(mapa)

    fig_medias = centroides(C)
    comp.grafico(fig_medias)
    