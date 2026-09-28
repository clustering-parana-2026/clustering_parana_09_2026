"""Construção de matrizes de atributos, clusters e silhuetas."""

from typing import Literal
from numpy.typing import ArrayLike


import pandas as pd




class Matrizes:
    """Funções auxiliares para construir as matrizes utilizadas nas análises."""

    @staticmethod
    def atributos(df: pd.DataFrame) -> pd.DataFrame:
        """Constrói a matriz de atributos por microrregião.

        Parameters
        ----------
        df : pandas.DataFrame
            Registros contendo as colunas ``agrupamento_desastre``,
            ``numero_da_ocorrencia``, ``microrregiao`` e
            ``quantidade_material``.

        Returns
        -------
        pandas.DataFrame
            Matriz com microrregiões no índice e agrupamentos de
            desastres nas colunas. Cada entrada contém a contagem
            de ocorrências com quantidade de material não nula.
            Combinações ausentes recebem zero.

        Notes
        -----
        Exclui os registros classificados como ``outro`` antes de
        agrupar por número da ocorrência. Para cada ocorrência,
        seleciona o primeiro valor não nulo de cada coluna.

        Pressupõe que os registros de uma mesma ocorrência sejam
        consistentes quanto à microrregião e ao agrupamento de desastre.

        Valores de quantidade iguais a zero são contados; valores
        ausentes não são. O DataFrame recebido não é modificado.
        """
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
    

    @staticmethod
    def clustering(
        D: pd.DataFrame, 
        rotulos: ArrayLike,
        formato: Literal['apenas_microrregioes', 'dados_originais'] = 'apenas_microrregioes'
    ) -> pd.DataFrame:
        """Associa os objetos da matriz de atributos aos seus clusters.

        Parameters
        ----------
        D : pandas.DataFrame
            Matriz de atributos com os objetos no índice.
        rotulos : array_like of shape (n_objetos,)
            Rótulo do cluster de cada objeto, na ordem das linhas de
            ``D``. Se fornecidos como uma Series, o pandas realiza
            o alinhamento pelo índice.
        formato : str, optional
            Define as colunas incluídas no resultado:

            - ``'apenas_microrregioes'``: retorna apenas ``cluster``,
              preservando o índice de ``D``.
            - ``'dados_originais'``: retorna ``cluster`` seguido das
              colunas de ``D``, sem alterar seus valores.

            O padrão é ``'apenas_microrregioes'``.

        Returns
        -------
        pandas.DataFrame
            Cópia dos dados selecionados, com os rótulos na coluna
            ``cluster`` e o índice original preservado. 

        Notes
        -----
        Não ajusta modelos nem normaliza os atributos. O DataFrame
        recebido não é modificado.
        """
        C = D.copy()
        C.insert(0, 'cluster', rotulos)
        if formato == 'apenas_microrregioes':
            C = C[['cluster']]
            return C
        elif formato == 'dados_originais':
            return C
        
        
    @staticmethod
    def silhuetas(
        C: pd.DataFrame,
        s: ArrayLike,
    ) -> pd.DataFrame:
        """Acrescenta os coeficientes de silhueta à matriz de clusters.

        Parameters
        ----------
        C : pandas.DataFrame
            Dados dos objetos e de sua associação aos clusters.
        s : array_like of shape (n_objetos,)
            Coeficiente de silhueta de cada objeto, na ordem das
            linhas de ``C``. Se fornecidos como uma Series, o pandas
            realiza o alinhamento pelo índice.

        Returns
        -------
        pandas.DataFrame
            Cópia de ``C`` com os coeficientes na coluna ``s``.
            Preserva o índice, a ordem das linhas e as demais colunas.
            Se a coluna ``s`` já existir, seus valores são substituídos.

        Notes
        -----
        Apenas organiza os coeficientes fornecidos; não calcula
        silhuetas. O DataFrame recebido não é modificado.
        """
        S = C.copy()
        S['s'] = s
        return S
        










    





        

        
    




    







        

