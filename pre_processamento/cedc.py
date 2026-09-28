"""Pré-processar dados CEDC.

Implementa a classe interna _PreProcessamento
para gerenciar as operações do processo.

"""

import pandas as pd


from carregamento.dados_tabulares_principais import CarregadorDadosBrutos

import constantes.pre_processamento_cedc as padroes
import constantes.pre_processamento_geral as padroes_gerais
from constantes.microrregioes import mesorregiao_por_microrregioes_por_municipios

from utils.decoradores import marcar_tempo_de_execucao
from utils.pre_processamento import PreProcessamentoGeral





@marcar_tempo_de_execucao()
def executar_pre_processamento_cedc(arquivo_final: str) -> None:
    df = CarregadorDadosBrutos.cedc()

    pp_geral = PreProcessamentoGeral(df)

    # Remover caracteres indesejados dos nomes de coluna.
    pp_geral.simplificar_nomes_de_colunas(
        padroes_gerais.colunas_caractere_antigo_por_caractere_novo
    )

    # Padronizar nomes de municípios.
    pp_geral.padronizar_nomes_de_municipios(
        padroes_gerais.municipios_nome_antigo_por_nome_novo
    )


    pp_local = _PreProcessamento(pp_geral.df)

    # Renomear colunas.
    pp_local.renomear_colunas(padroes.colunas_nome_antigo_por_nome_novo)

    # Modificar estruturas de dados.
    pp_local.modificar_estruturas_de_dados()

    # Combinar dados para incluir informação de interesse.
    pp_local.incluir_novas_colunas(
        microrregioes=mesorregiao_por_microrregioes_por_municipios,
        dict_novas_colunas=padroes.nome_nova_coluna_por_dict_valor_antigo_por_valor_novo
    )

    # Remover colunas indesejadas.
    pp_local.remover_colunas_indesejadas(padroes.colunas_para_remover)

    # Remover linhas indesejadas.
    pp_local.remover_linhas_indesejadas(padroes.linhas_para_remover)

    # Reordenar colunas.
    pp_local.reordenar_colunas(padroes.nova_ordem_das_colunas)

    # Salvar resultados.
    pp_local.df.to_csv(arquivo_final, index=False) 



class _PreProcessamento:
    def __init__(self, df: pd.DataFrame):
        """Prepara os registros para a etapa de transformação.

        Parameters
        ----------
        df : pandas.DataFrame
            Dados a serem pré-processados. As colunas necessárias dependem
            dos métodos chamados.

        Attributes
        ----------
        df : pandas.DataFrame
            Dados no estado atual do pré-processamento. Inicialmente,
            referencia o DataFrame recebido, sem criar uma cópia.

        Notes
        -----
        Os métodos alteram ``self.df`` ou substituem sua referência pelo
        resultado de uma operação. Não retornam os dados processados.

        A conversão das colunas de data deve ocorrer antes do cálculo
        de ``tempo_para_envio``.
        """

        self.df = df


    def renomear_colunas(self, nome_antigo_para_nome_novo: dict[str, str]) -> None:
        """Renomeia as colunas indicadas no mapeamento.

        Parameters
        ----------
        nome_antigo_para_nome_novo : dict[str, str]
            Mapeamento entre os nomes atuais das colunas e os novos
            nomes desejados.

        Notes
        -----
        Colunas não mencionadas são preservadas. Chaves que não
        correspondem a colunas existentes são ignoradas.
        """
        self.df = (
            self.df 
            .rename(columns=nome_antigo_para_nome_novo)
        )


    def modificar_estruturas_de_dados(self) -> None:
        """Converte quantidades, valores monetários e datas.

        Notes
        -----
        Na coluna ``quantidade_material``, substitui o marcador ``'-'``
        por zero e converte os valores para o tipo numérico 
        ``Float64``.

        Nas colunas ``pib``, ``receita_corrente_liquida``,
        ``prejuizo_publico`` e ``prejuizo_privado``, remove ``R$`` e
        pontos, substitui vírgulas por pontos e hífens por zeros.
        Em seguida, converte os valores para ``Float64``. 

        Converte ``data_ocorrencia``, ``data_envio`` e
        ``data_solicitacao`` para valores temporais, utilizando o
        formato ``'%d/%m/%Y %H:%M'``. Datas inválidas ou incompatíveis
        com esse formato são convertidas para ``NaT``.
        """
        # Converter quantidades de material para tipo numérico.
        self.df['quantidade_material'] = (
            self.df['quantidade_material']
            .replace('-', 0)
            .astype('Float64')
        )

        # Converter colunas de valor monetário para tipo numérico.
        cols_dinheiro = [
            'pib', 'receita_corrente_liquida', 
            'prejuizo_publico', 'prejuizo_privado'
        ]
        self.df[cols_dinheiro] = (
            self.df[cols_dinheiro]
            .apply(
                lambda col: col
                .str.replace('R$', '', regex=False)
                .str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
                .str.replace('-', '0', regex=False)
            )
            .astype('Float64')
        )

        # Alterações em colunas de data.
        cols_data = [
            'data_ocorrencia', 'data_envio',
            'data_solicitacao',
        ]
        for col in cols_data:
            self.df[col] = pd.to_datetime(
                arg=self.df[col],    
                format='%d/%m/%Y %H:%M',
                errors='coerce',
            )


    def incluir_novas_colunas(
        self,
        microrregioes: dict[str, dict[str, list]],
        dict_novas_colunas: dict[str, dict[str, str]],
    ) -> None:
        """Acrescenta regiões, tempo para envio e grupos de desastres.

        Parameters
        ----------
        microrregioes : dict[str, dict[str, list]]
            Estrutura que associa cada mesorregião a um dicionário
            de microrregiões e suas listas de municípios:
            ``{mesorregiao: {microrregiao: [municipios]}}``.
        dict_novas_colunas : dict[str, dict[str, str]]
            Dicionário cuja chave ``grupo_desastre`` contém o
            mapeamento entre tipos de desastre e seus grupos.

        Notes
        -----
        Cria as seguintes colunas:

        - ``mesorregiao``: mesorregião associada ao município.
        - ``microrregiao``: microrregião associada ao município.
        - ``tempo_para_envio``: diferença entre ``data_envio`` e
          ``data_solicitacao``.
        - ``grupo_desastre``: grupo associado ao tipo de desastre.

        As colunas de data devem estar previamente convertidas para
        tipos temporais. O intervalo calculado representa o tempo
        entre solicitação e envio, não o tempo até a entrega.

        Municípios e desastres ausentes dos respectivos mapeamentos
        mantêm seus valores originais nas colunas criadas.
        """
        # Adicionar coluna mesorregiões
        mesorregioes: dict[str, list[str]] = {
            meso: [
                municipio 
                for municipios in v.values() 
                for municipio in municipios
            ]
            for meso, v in microrregioes.items()
        }
        municipio_para_meso = {
            municipio: meso
            for meso, municipios in mesorregioes.items()
            for municipio in municipios
        }
        self.df['mesorregiao'] = (
            self.df['municipio']
            .replace(municipio_para_meso)
        )
    
        # Criar coluna microrregiões
        municipio_para_micro = {
            municipio: micro 
            for meso, micros in microrregioes.items()
            for micro, municipios in micros.items()
            for municipio in municipios
        }
        self.df['microrregiao'] = (
            self.df['municipio']
            .replace(municipio_para_micro)
        )

        # Adicionar coluna de tempo para entrega.
        self.df['tempo_para_envio'] = (
            self.df['data_envio']
            - self.df['data_solicitacao']
        )

        # Criar coluna de grupo do desastre.
        self.df['grupo_desastre'] = (
            self.df['desastre']
            .replace(dict_novas_colunas['grupo_desastre'])
        )
        

    def remover_colunas_indesejadas(self, colunas_para_remover: list[str]) -> None:
        """Remove as colunas especificadas.

        Parameters
        ----------
        colunas_para_remover : list[str]
            Nomes das colunas que serão removidas de ``self.df``.
            Todas devem existir no DataFrame.
        """
        self.df = (
            self.df
            .drop(columns=colunas_para_remover)
        )


    def remover_linhas_indesejadas(
        self, 
        linhas_para_remover: dict[str, list[str]]
    ) -> None:
        """Remove registros que contenham os valores indicados.

        Parameters
        ----------
        linhas_para_remover : dict[str, list[str]]
            Mapeamento entre nomes de colunas e listas de valores
            que motivam a remoção de um registro.

        Notes
        -----
        Aplica os filtros sequencialmente. Um registro é removido
        se corresponder a qualquer uma das condições informadas.

        Preserva os índices e a ordem relativa dos registros restantes,
        sem redefinir o índice.
        """
        for col, valores in linhas_para_remover.items():
            self.df = (
                self.df
                [~self.df[col].isin(valores)]
            )


    def reordenar_colunas(self, nova_ordem_colunas: list[str]) -> None:
        """Seleciona as colunas e define sua ordem.

        Parameters
        ----------
        nova_ordem_colunas : list[str]
            Nomes das colunas que serão mantidas, na ordem desejada.
            Todas devem existir no DataFrame.

        Notes
        -----
        Colunas não incluídas na lista são excluídas do resultado.
        """
        self.df = (
            self.df[nova_ordem_colunas]
        )






