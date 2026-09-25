from numpy.typing import ArrayLike


import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.cluster import KMeans

from .mineracao import Mineracao
from .matrizes import Matrizes





class AnaliseSilhuetas:
    def __init__(
        self,
        modelos: dict[int, KMeans],
    ):
        self.modelos = modelos

    def calcular_largura_media_global_da_silhueta(
        self,
        X: np.ndarray,
        k_de_interesse: list[int],
    ) -> pd.Series:
        s_por_agrupamento: dict[int, float] = {}

        for k in k_de_interesse:
            rotulos = self.modelos[k].labels_
            s_por_agrupamento[k] = metrics.silhouette_score(
                X,
                rotulos,
            )

        resultado = pd.Series(
            s_por_agrupamento,
            name="s_bar(k)",
        )
        resultado.index.name = "k"

        return resultado

    def calcular_silhuetas_dos_clusters(
        self,
        D: pd.DataFrame,
        X: np.ndarray,
        k_de_interesse: list[int],
    ) -> dict[int, pd.DataFrame]:
        s_por_objeto_por_agrupamento: dict[int, pd.DataFrame] = {}

        for k in k_de_interesse:
            rotulos = self.modelos[k].labels_
            s = metrics.silhouette_samples(
                X,
                rotulos,
            )
            C = Matrizes.clustering(
                D=D,
                rotulos=rotulos,
            )
            S = Matrizes.silhuetas(
                C=C,
                s=s,
            )

            s_por_objeto_por_agrupamento[k] = S

        return s_por_objeto_por_agrupamento


        
        





    


    

    