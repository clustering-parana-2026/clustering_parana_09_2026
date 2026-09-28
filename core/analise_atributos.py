"""Análise descritiva de ocorrências de desastres e envios de materiais.

Disponibiliza a classe ``AnaliseAtributos`` para calcular frequências
de desastres, contagens de registros de envio, estatísticas das
quantidades enviadas e totais normalizados por agrupamento.

"""

import numpy as np
import pandas as pd





class AnaliseAtributos:
    def __init__(self, df: pd.DataFrame):
        """Calcula frequências e estatísticas de desastres e materiais enviados.

        Parameters
        ----------
        df : pandas.DataFrame
            Deve conter as colunas ``numero_da_ocorrencia``, ``desastre``,
            ``material``, ``quantidade_material`` e
            ``qtd_material_normalizada``.

        Attributes
        ----------
        df : pandas.DataFrame
            Referência ao DataFrame fornecido, sem criação de uma cópia.

        Notes
        -----
        Os métodos retornam os resultados sem modificar o DataFrame original.
        As quantidades normalizadas devem estar previamente calculadas.
        """

        self.df = df


    def calcular_frequencia_desastres(self) -> pd.Series:
        """Conta as ocorrências por tipo desastre.

        Returns
        -------
        pandas.Series
            Número de ocorrências por desastre, com as categorias no
            índice e os valores ordenados de forma crescente.

        Notes
        -----
        Agrupa os registros por ``numero_da_ocorrencia`` antes da
        contagem, utilizando o primeiro valor não nulo de ``desastre``
        de cada ocorrência. Pressupõe que cada ocorrência esteja
        associada a uma única categoria de desastre.
        """
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
        """Conta os registros de envio por categoria de material.

        Returns
        -------
        pandas.Series
            Número de registros por material, com as categorias no
            índice e as contagens ordenadas de forma crescente.

        Notes
        -----
        Considera apenas os registros cuja ``quantidade_material``
        seja diferente de zero. Cada linha selecionada é contada
        como um registro de envio.

        A contagem representa registros, não unidades de material.
        """
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
        """Resume as quantidades enviadas por categoria de material.

        Returns
        -------
        pandas.DataFrame
            Estatísticas por material, ordenadas pela média crescente.
            O índice contém as categorias de material e as colunas são:

            - ``mean``: média das quantidades enviadas.
            - ``cv``: desvio-padrão amostral dividido pela média.
            - ``min``: menor quantidade enviada.
            - ``max``: maior quantidade enviada.

        Notes
        -----
        Exclui os registros com ``quantidade_material`` igual a zero
        antes de calcular as estatísticas. Remove a categoria ``outro``
        do resultado.

        Para categorias com apenas uma quantidade válida, o desvio-padrão 
        amostral e o coeficiente de variação são NaN.
        """
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
    ) -> pd.DataFrame:
        """Soma as quantidades normalizadas por agrupamento de desastre e material.

        Returns
        -------
        pandas.DataFrame
            Totais de ``qtd_material_normalizada``, com os valores de
            ``desastre`` no índice e as categorias de ``material`` nas
            colunas. Combinações ausentes recebem zero.

        Notes
        -----
        Exclui os registros com quantidade normalizada igual a zero
        e aqueles cujo valor em ``desastre`` seja ``outro``. Após a
        agregação, remove também a categoria de material ``outro``.
        """
        envios_material = (
            self.df
            [self.df['qtd_material_normalizada'] != 0]
            [self.df['desastre'] != 'outro']
        )
        relacao = (
            envios_material
            .groupby(['material', 'desastre'])
            ['qtd_material_normalizada']
            .sum()
            .unstack(level='desastre', fill_value=0)
            .drop(index=['outro'])
            .T
        )
        return relacao





