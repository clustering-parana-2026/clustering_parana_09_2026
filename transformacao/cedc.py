import pandas as pd 


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

import constantes.transformacao_cedc as padroes





def executar_transformacao_cedc(arquivo_final: str) -> None:
    df = CarregadorDadosEstruturados.major_daniel()

    trf = _Transformacao(df)

    trf.substituir_valores(padroes.coluna_por_dict_valores_novos)
    trf.criar_novas_colunas(padroes.coluna_nova_por_dict_valores_novos)
    trf.reordenar_colunas(padroes.nova_ordem_das_colunas)

    trf.df.to_csv(arquivo_final, index=False)



class _Transformacao:
    def __init__(self, df):
        self.df = df


    def substituir_valores(
        self,
        dict_valores_novos: dict[str, dict[str, str]],
    ) -> None:
        for col, para_substituir in dict_valores_novos.items():
            self.df[col] = self.df[col].replace(para_substituir)


    def criar_novas_colunas(
        self,
        valores_novas_colunas: dict,
    ) -> pd.DataFrame:
        # Criar coluna de agrupamento desastre por material.
        self.df['agrupamento_desastre'] = (
            self.df
            ['desastre']
            .replace(valores_novas_colunas['agrupamento_desastre'])
        )

        # --- otimizar!! --- #
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
        self.df = (
            self.df[nova_ordem_colunas]
        )