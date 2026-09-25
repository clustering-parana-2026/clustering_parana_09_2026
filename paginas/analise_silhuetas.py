import streamlit as st

from sklearn import preprocessing


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

from core.matrizes import Matrizes
from core.analise_silhuetas import AnaliseSilhuetas
from core.mineracao import Mineracao

import utils.componentes as comp

from visualizacoes.larguras_medias_silhuetas import larguras_medias_silhuetas
from visualizacoes.silhuetas_clusters import silhuetas_clusters





def pg_analise_silhuetas() -> None:
    # Carregar matriz de atributos.
    D = Matrizes.atributos(
        CarregadorDadosEstruturados.cedc()
    )

    # Aplicar normalização por z-score nos dados.
    X = preprocessing.StandardScaler().fit_transform(D)

    
    # Ajustar os modelos uma vez para cada k.
    modelos = Mineracao.obter_modelos_kmeans(
        X=X,
        k=list(range(2,15)),
    )

    # Instanciar analisados de silhuetas.
    anl_sil = AnaliseSilhuetas(
        modelos=modelos,
    ) 

    # Escolher candidatos para k a partir da silhueta média.
    larguras_medias_globais_das_silhuetas = anl_sil.calcular_largura_media_global_da_silhueta(
        X=X,
        k_de_interesse=list(range(2,15)),
    )
    grafico_silhuetas_medias = larguras_medias_silhuetas(
        larguras_medias_globais_das_silhuetas
    )
    comp.grafico(grafico_silhuetas_medias)

    # Silhuetas por objeto usando os mesmos modelos.
    silhuetas_dos_clusters = (
        anl_sil.calcular_silhuetas_dos_clusters(
            D=D,
            X=X,
            k_de_interesse=[2, 3, 7],
        )
    )
    grafico_silhuetas_clusters = silhuetas_clusters(
        silhuetas_dos_clusters
    )
    comp.grafico(grafico_silhuetas_clusters)

     