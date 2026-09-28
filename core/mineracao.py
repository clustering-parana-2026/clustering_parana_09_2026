"""Ajuste e seleção de modelos K-Means para diferentes números de clusters."""

from threadpoolctl import threadpool_limits


import numpy as np
import pandas as pd

from sklearn.cluster import KMeans




class Mineracao:
    """Métodos para ajuastar modelos de clusterização."""

    @staticmethod
    def obter_modelos_kmeans(
        X: np.ndarray,
        k: list[int],
    ) -> dict[int, KMeans]:
        """Ajusta e seleciona o modelo K-Means de menor SSE para cada k.

        Parameters
        ----------
        X : numpy.ndarray of shape (n_objetos, n_atributos)
            Matriz de atributos utilizada no ajuste dos modelos.
            Deve estar previamente preparada na escala desejada,
            pois o método não realiza padronização.
        k : list[int]
            Números de clusters a serem avaliados. Cada valor deve
            estar entre 1 e o número de objetos.

        Returns
        -------
        dict[int, sklearn.cluster.KMeans]
            Mapeamento entre cada número de clusters e o modelo
            ajustado de menor SSE entre as dez sementes avaliadas.
            Os rótulos em ``labels_`` seguem a ordem das linhas de ``X``.

        Notes
        -----
        Para cada valor de k, ajusta dez modelos com sementes de 0 a 9.
        Cada ajuste utiliza inicialização ``k-means++`` e 30
        inicializações, totalizando 300 inicializações por valor de k.

        A seleção utiliza ``inertia_``, que representa a soma dos
        quadrados das distâncias dos objetos aos respectivos
        centroides. Em caso de empate, seleciona o primeiro modelo
        encontrado.

        Durante os ajustes, limita a uma thread os pools de threads
        das bibliotecas nativas controladas por ``threadpoolctl``.
        As sementes fixas e a limitação de threads visam reproduzir os
        mesmos resultados em chamadas realizadas em diferentes partes
        da aplicação, para os mesmos dados de entrada.

        Retorna um modelo para cada k, sem escolher o número de
        clusters. A seleção da menor inércia entre os modelos
        avaliados não garante o mínimo global.
        """
        melhores_modelos = {}

        with threadpool_limits(limits=1):
            for valor_de_k in k:
                modelos = [
                    KMeans(
                        n_clusters=valor_de_k,
                        init="k-means++",
                        n_init=30,
                        random_state=semente,
                    ).fit(X)
                    for semente in range(10)
                ]

                melhores_modelos[valor_de_k] = min(
                    modelos,
                    key=lambda m: m.inertia_,
                )

        return melhores_modelos
