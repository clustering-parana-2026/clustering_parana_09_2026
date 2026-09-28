"""Transformar dados CEDC.

Implementa a classe interna _Transformacao
para gerenciar as operações do processo.

"""

import pandas as pd 


import constantes.transformacao_cedc as padroes

from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

from utils.decoradores import marcar_tempo_de_execucao




@marcar_tempo_de_execucao()
def executar_transformacao_cedc(arquivo_final: str) -> None:
    df = CarregadorDadosEstruturados.cedc()

    trf = _Transformacao(df)

    trf.substituir_valores(padroes.coluna_por_dict_valores_novos)
    trf.criar_novas_colunas(padroes.coluna_nova_por_dict_valores_novos)
    trf.reordenar_colunas(padroes.nova_ordem_das_colunas)

    trf.df.to_csv(arquivo_final, index=False)



class _Transformacao:
    def __init__(self, df):
        """Aplica transformações aos registros da CEDC.

        Parameters
        ----------
        df : pandas.DataFrame
            Dados a transformar. Para criar as colunas derivadas, deve
            conter ``desastre``, ``material`` e ``quantidade_material``.

        Attributes
        ----------
        df : pandas.DataFrame
            Dados em transformação. Inicialmente, referencia o DataFrame
            recebido, sem criar uma cópia. A seleção de colunas substitui
            essa referência pelo DataFrame resultante.
        """

        self.df = df


    def substituir_valores(
        self,
        dict_valores_novos: dict[str, dict[str, str]],
    ) -> None:
        """Substitui valores nas colunas indicadas.

        Parameters
        ----------
        dict_valores_novos : dict[str, dict[str, str]]
            Mapeamento entre nomes de colunas e seus dicionários de
            substituição. Cada dicionário associa valores encontrados
            aos respectivos valores novos.

        Notes
        -----
        Atualiza as colunas diretamente em ``self.df``.
        Valores não presentes nos mapeamentos são preservados.
        """
        for col, para_substituir in dict_valores_novos.items():
            self.df[col] = self.df[col].replace(para_substituir)


    def criar_novas_colunas(
        self,
        valores_novas_colunas: dict,
    ) -> pd.DataFrame:
        """Cria agrupamentos de desastres e quantidades normalizadas.

        Parameters
        ----------
        valores_novas_colunas : dict
            Dicionário cuja chave ``agrupamento_desastre`` contém o
            mapeamento de tipos de desastre para suas categorias
            de agrupamento.

        Notes
        -----
        Cria ou substitui duas colunas em ``self.df``:

        - ``agrupamento_desastre``: aplica o mapeamento à coluna
          ``desastre``, preservando os valores não mapeados.
        - ``qtd_material_normalizada``: divide a quantidade de cada
          registro pela quantidade média da respectiva categoria
          de material.

        As médias são calculadas apenas sobre registros cuja
        ``quantidade_material`` seja diferente de zero. Para materiais
        ausentes da série de médias, utiliza o divisor 1.
        """
        # Criar coluna de agrupamento desastre por material.
        self.df['agrupamento_desastre'] = (
            self.df
            ['desastre']
            .replace(valores_novas_colunas['agrupamento_desastre'])
        )

        # Criar coluna de quantidade de material normalizada.
        envios_material = (
            self.df
            [self.df['quantidade_material'] != 0]
        )
        media = (
            envios_material
            .groupby('material')
            ['quantidade_material']
            .mean()
        )
        lista: list[int] = []
        for indice, linha in self.df.iterrows():
            if linha['material'] not in media.index:
                lista.append(1)
            else:
                lista.append(
                    media
                    .loc[linha['material']]
                )
        self.df['qtd_material_normalizada'] = (
            self.df['quantidade_material'] 
            / pd.Series(lista)
        )

    def reordenar_colunas(self, nova_ordem_colunas: list) -> None:
        """Seleciona as colunas e define sua ordem.

        Parameters
        ----------
        nova_ordem_colunas : list[str]
            Nomes das colunas que serão mantidas, na ordem desejada.
            Colunas não incluídas na lista são removidas do resultado.

        Notes
        -----
        Substitui ``self.df`` pelo DataFrame com as colunas selecionadas.
        """
        self.df = (
            self.df[nova_ordem_colunas]
        )