"""Funções auxiliares gerais para o pré-processamento dos dados.

Implementa a simplificação dos nomes das colunas (substituição
de caracteres) e padronização dos nomes de município para as 
diferentes fontes.
"""

import pandas as pd




class PreProcessamentoGeral:
    def __init__(self, df: pd.DataFrame):
        """Implementa métodos para o pré-processamento da base de dados.
        
        Parameters
        ----------
        df : pd.DataFrame
            DataFrame bruto com nomes de coluna e de municípios
            originais.

        Attributes
        ----------
        df : pd.DataFrame
            Referência ao DataFrame fornecido, sem a criação de uma
            cópia. Pode ser modificado pelos métodos da classe.

        Notes 
        -----
        Os métodos modificam o DataFrame.
        """

        self.df = df


    def simplificar_nomes_de_colunas(
        self,
        caractere_antigo_por_caractere_novo: dict[str, str],
    ) -> pd.DataFrame:
        """Padroniza os nomes das colunas de um DataFrame.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame com as colunas com os nomes originais.
        caracteres_para_substituir : dict[str, str]
            Tabela de tradução utilizada por ``str.translate``.

        Returns
        -------
        pandas.DataFrame
            O mesmo DataFrame recebido, com os nomes das colunas padronizados.

        Notes
        -----
        Remove espaços em branco nas extremidades, converte os nomes para
        letras minúsculas, substitui espaços e hífens por sublinhados e aplica 
        a tabela de tradução, nessa ordem.
        """
        self.df.columns = (
            self.df.columns 
            .str.strip()
            .str.lower()
            .str.replace(' ', '_')
            .str.replace('-', '_')
            .str.translate(caractere_antigo_por_caractere_novo)
        )


    def padronizar_nomes_de_municipios(
        self,
        municipios_nome_antigo_por_nome_novo: dict,
    ) -> pd.DataFrame:
        """Padroniza os nomes dos municípios na coluna ``municipio``.

        Parameters
        ----------
        df : pandas.DataFrame
            DataFrame que contém a coluna ``municipio``.
            É modificado diretamente.
        novos_nomes_municipios : dict
            Mapeamento entre os nomes encontrados e seus substitutos.
            As chaves devem corresponder aos valores após a conversão
            para strings e a remoção dos espaços nas extremidades.

        Returns
        -------
        pandas.DataFrame
            O mesmo DataFrame recebido, com a coluna ``municipio`` atualizada.
        """
        self.df['municipio'] = (
            self.df['municipio']
            .astype(str)
            .str.strip()
            .replace(municipios_nome_antigo_por_nome_novo)
        )