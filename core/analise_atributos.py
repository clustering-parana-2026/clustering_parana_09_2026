import numpy as np
import pandas as pd





class AnaliseAtributos:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def calcular_frequencia_desastres(self) -> pd.Series:
        eventos_unicos = (
            self.df
            .groupby('numero_da_ocorrencia')
            .first()
        )
        frequencia_desastres = (
            eventos_unicos
            .groupby('desastre')
            .size()
            .sort_values(ascending=True)
        )
        return frequencia_desastres


    def calcular_frequencia_materiais(self) -> pd.Series:
        envios_material = (
            self.df
            [self.df['quantidade_material'] != 0]
        )
        frequencia_envios = (
            envios_material
            .groupby('material')
            .size()
            .sort_values(ascending=True)
        )
        return frequencia_envios


    def calcular_sumario_envios_de_material(self) -> pd.DataFrame:
        envios_material = (
            self.df
            [self.df['quantidade_material'] != 0]
        )
        sumario = (
            envios_material
            .groupby('material')
            ['quantidade_material']
            .agg(['mean', 'std', 'min', 'max'])
        )
        sumario = sumario.drop(index=['outro'])
        cv = sumario['std'] / sumario['mean']
        sumario = sumario.drop(columns=['std'])
        sumario.insert(1, 'cv', cv)
        return sumario.sort_values(by='mean', ascending=True)


    def calcular_quantidade_normalizada_de_material_por_agrupamento(
        self,
        col: str, 
    ) -> pd.DataFrame:
        envios_material = (
            self.df
            [self.df['qtd_material_normalizada'] != 0]
            [self.df[col] != 'outro']
        )
        relacao = (
            envios_material
            .groupby(['material', col])
            ['qtd_material_normalizada']
            .sum()
            .unstack(level=col, fill_value=0)
            .drop(index=['outro'])
            .T
        )
        return relacao





