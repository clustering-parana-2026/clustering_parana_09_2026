import pandas as pd


from carregamento.dados_tabulares_principais import CarregadorDadosBrutos

import constantes.pre_processamento_cedc as padroes
import constantes.pre_processamento_geral as padroes_gerais
from constantes.microrregioes import mesorregiao_por_microrregioes_por_municipios

from utils.decoradores import marcar_tempo_de_execucao
import utils.pre_processamento as funcoes





@marcar_tempo_de_execucao()
def executar_pre_processamento_cedc(arquivo_final: str) -> None:
    df = CarregadorDadosBrutos.major_daniel()

    # Remover caracteres indesejados dos nomes de coluna.
    df = funcoes.simplificar_nomes_de_colunas(
        df, 
        padroes_gerais.colunas_caractere_antigo_por_caractere_novo
    )

    # Padronizar nomes de municípios.
    df = funcoes.padronizar_nomes_de_municipios(
        df, 
        padroes_gerais.municipios_nome_antigo_por_nome_novo
    )

    pp = _PreProcessamento(df)
    pp.renomear_colunas(padroes.colunas_nome_antigo_por_nome_novo)
    pp.modificar_estruturas_de_dados()
    pp.incluir_novas_colunas(
        microrregioes=mesorregiao_por_microrregioes_por_municipios,
        dict_novas_colunas=padroes.nome_nova_coluna_por_dict_valor_antigo_por_valor_novo
    )
    pp.remover_colunas_indesejadas(padroes.colunas_para_remover)
    pp.remover_linhas_indesejadas(padroes.linhas_para_remover)
    pp.reordenar_colunas(padroes.nova_ordem_das_colunas)

    # Salvar resultados.
    pp.df.to_csv(arquivo_final, index=False) 



class _PreProcessamento:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def renomear_colunas(self, nome_antigo_para_nome_novo: dict) -> None:
        self.df = (
            self.df 
            .rename(columns=nome_antigo_para_nome_novo)
        )

    def modificar_estruturas_de_dados(self) -> None:
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
        dict_novas_colunas: dict,
    ) -> None:
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
        

    def remover_colunas_indesejadas(self, colunas_para_remover: list) -> None:
        self.df = (
            self.df
            .drop(columns=colunas_para_remover)
        )

    def remover_linhas_indesejadas(
        self, 
        linhas_para_remover: dict[str, list[str]]
    ) -> None:
        for col, valores in linhas_para_remover.items():
            self.df = (
                self.df
                [~self.df[col].isin(valores)]
            )

    def reordenar_colunas(self, nova_ordem_colunas: list) -> None:
        self.df = (
            self.df[nova_ordem_colunas]
        )






