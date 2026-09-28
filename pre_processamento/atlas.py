"""Pré-processar dados ATLAS."""

import pandas as pd


from utils.decoradores import marcar_tempo_de_execucao

from carregamento.dados_tabulares_principais import CarregadorDadosBrutos




# Não atualizada, precisa de manutenção!

@marcar_tempo_de_execucao() 
def estruturar_arquivo_atlas(arquivo_final) -> None:
    df = CarregadorDadosBrutos.atlas()

    apenas_parana = df['Sigla_UF'] == 'PR'
    df_parana = df[apenas_parana].copy()

    df_parana['Data_Registro'] = pd.to_datetime(df_parana['Data_Registro'])
    apenas_2010_em_diante = df_parana['Data_Registro'] > '2010-01-01'
    df_parana_pos_2010 = df_parana[apenas_2010_em_diante].copy()

    df_parana_pos_2010.to_csv(arquivo_final, index=False)


