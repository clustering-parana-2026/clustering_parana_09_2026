import numpy as np 
import pandas as pd






class Interpretacao:
    def __init__(self, df: pd.DataFrame):
        self._df = df


    def calcular_lead_time_medio(self) -> pd.Series:
        df_nat = (
            self._df 
            [self._df['data_envio'].notna()]
        )
        lead_time_medio = (
            df_nat
            .groupby('microrregiao')
            ['tempo_para_envio']
            .mean()
            / pd.Timedelta(days=1)
        ).sort_values(ascending=False)

        return lead_time_medio