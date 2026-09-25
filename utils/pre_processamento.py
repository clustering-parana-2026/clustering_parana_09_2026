import pandas as pd





def simplificar_nomes_de_colunas(
    df: pd.DataFrame, 
    caracteres_para_substituir: dict
) -> pd.DataFrame:
    df.columns = (
        df.columns 
        .str.strip()
        .str.lower()
        .str.replace(' ', '_')
        .str.replace('-', '_')
        .str.translate(caracteres_para_substituir)
    )
    
    return df


def padronizar_nomes_de_municipios(
    df: pd.DataFrame, 
    novos_nomes_municipios: dict,
) -> pd.DataFrame:
    df['municipio'] = df['municipio'].astype(str)
    df['municipio'] = df['municipio'].str.strip()

    df['municipio'] = df['municipio'].replace(novos_nomes_municipios)

    return df


