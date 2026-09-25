from typing import Literal
from numpy.typing import ArrayLike


import numpy as np
import pandas as pd






class Matrizes:
    def atributos(df: pd.DataFrame) -> pd.DataFrame:
        D = (
            df
            [~df['agrupamento_desastre'].isin(['outro'])]
            .groupby('numero_da_ocorrencia').first()
            .reset_index(drop=True)
            .groupby(['microrregiao', 'agrupamento_desastre'])
            ['quantidade_material']
            .count()
            .unstack(level='agrupamento_desastre', fill_value=0)
        )
        return D


    def clustering(
        D: pd.DataFrame, 
        rotulos: ArrayLike,
        formato: Literal['apenas_microrregioes', 'dados_originais', 'dados_normalizados'] = 'apenas_microrregioes'
    ) -> pd.DataFrame:
        C = D.copy()
        C.insert(0, 'cluster', rotulos)
        if formato == 'apenas_microrregioes':
            C = C[['cluster']]
            return C
        elif formato == 'dados_originais':
            return C
        

    def silhuetas(
        C: pd.DataFrame,
        s: ArrayLike,
    ) -> pd.DataFrame:
        S = C.copy()
        S['s'] = s
        return S
        










    





        

        
    




    







        

