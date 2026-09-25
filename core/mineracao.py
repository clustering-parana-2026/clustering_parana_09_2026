from threadpoolctl import threadpool_limits


import numpy as np
import pandas as pd

from sklearn.cluster import KMeans




class Mineracao:
    @staticmethod
    def obter_modelos_kmeans(
        X: np.ndarray,
        k: list[int],
    ) -> dict[int, KMeans]:
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
