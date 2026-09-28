"""Análise das silhuetas das clusterizações.

Disponibiliza a classe ``AnaliseSilhuetas`` para calcular a largura
média global da silhueta e os coeficientes individuais dos objetos
para diferentes números de clusters.
"""

import numpy as np
import pandas as pd

from sklearn import metrics
from sklearn.cluster import KMeans

from .matrizes import Matrizes





class AnaliseSilhuetas:
    def __init__(
        self,
        modelos: dict[int, KMeans],
    ):
        """Avalia modelos K-Means previamente ajustados por meio de silhuetas.

        Parameters
        ----------
        modelos : dict[int, sklearn.cluster.KMeans]
            Mapeamento entre o número de clusters e o modelo ajustado
            correspondente. Cada modelo deve possuir o atributo ``labels_``.

        Attributes
        ----------
        modelos : dict[int, sklearn.cluster.KMeans]
            Referência ao dicionário de modelos fornecido, sem criação
            de uma cópia.

        Notes
        -----
        Os métodos utilizam os rótulos existentes nos modelos, sem realizar
        novos ajustes ou predições. As distâncias são calculadas com a
        métrica euclidiana sobre os dados fornecidos em ``X``.
        """
        
        self.modelos = modelos
        

    def calcular_largura_media_global_da_silhueta(
        self,
        X: np.ndarray,
        k_de_interesse: list[int],
    ) -> pd.Series:
        """Calcula a largura média global da silhueta para cada modelo.

        Parameters
        ----------
        X : numpy.ndarray of shape (n_objetos, n_atributos)
            Matriz de atributos utilizada no cálculo das distâncias.
            As linhas devem corresponder aos objetos de ``labels_``,
            na mesma ordem. Deve conter os dados na escala em que
            se deseja avaliar a clusterização.
        k_de_interesse : list[int]
            Números de clusters cujos modelos serão avaliados.
            Cada valor deve existir como chave em ``modelos``.

        Returns
        -------
        pandas.Series
            Média dos coeficientes de silhueta dos objetos para cada
            valor de k. A série tem nome ``s_bar(k)`` e índice
            denominado ``k``, seguindo a ordem da primeira ocorrência
            de cada valor em ``k_de_interesse``.

        Notes
        -----
        A média considera todos os objetos, sem amostragem.
        Valores repetidos de k são recalculados, mas aparecem apenas
        uma vez no resultado.
        """
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
        """Calcula e organiza os coeficientes de silhueta dos objetos.

        Parameters
        ----------
        D : pandas.DataFrame
            Dados dos objetos utilizados na construção da representação
            dos clusters por ``Matrizes.clustering``. As linhas devem
            corresponder às de ``X`` e aos rótulos dos modelos,
            na mesma ordem.
        X : numpy.ndarray of shape (n_objetos, n_atributos)
            Matriz de atributos utilizada no cálculo das distâncias
            euclidianas. Deve conter os dados na escala em que se
            deseja avaliar a clusterização.
        k_de_interesse : list[int]
            Números de clusters cujos modelos serão avaliados.
            Cada valor deve existir como chave em ``modelos``.

        Returns
        -------
        dict[int, pandas.DataFrame]
            Mapeamento entre cada valor de k e o DataFrame produzido
            por ``Matrizes.silhuetas``, a partir da representação dos
            clusters e dos coeficientes individuais de silhueta.

        Notes
        -----
        Os coeficientes são calculados a partir de ``X``.
        O DataFrame ``D`` é utilizado na organização dos resultados,
        não no cálculo das distâncias.
        """
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


        
        





    


    

    