import pandas as pd


from carregamento.dados_tabulares_principais import CarregadorDadosBrutos

import constantes.pre_processamento_cedc as padroes

from utils.decoradores import marcar_tempo_de_execucao
import utils.pre_processamento as pre_processamento




@marcar_tempo_de_execucao()
def estruturar_arquivo_ips(arquivo_final) -> None:
    df = CarregadorDadosBrutos.ips()

    df = pre_processamento.simplificar_nomes_de_colunas(df, padroes.mapa_traducao)
    df = df.rename(columns=padroes.colunas_renomeadas_ips)

    df = pre_processamento.padronizar_nomes_de_municipios(df, padroes.municipios_para_padronizar)

    df.to_csv(arquivo_final, index=False)