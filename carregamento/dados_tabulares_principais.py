import pandas as pd


import constantes.caminhos as caminhos





class CarregadorDadosBrutos:
    def cedc() -> pd.DataFrame:
        return pd.read_csv(
            caminhos.arquivo_bruto_cedc,
            sep=';', 
            thousands='.', 
            decimal=','
        )

    
    def atlas() -> pd.DataFrame:
        return pd.read_excel(
            caminhos.arquivo_bruto_atlas,
        )

    
    def ips() -> pd.DataFrame:
        return pd.read_csv(
            caminhos.arquivo_bruto_ips
        )



class CarregadorDadosEstruturados:
    def cedc() -> pd.DataFrame:
        return pd.read_csv(
            caminhos.arquivo_estruturado_cedc, 
            parse_dates=['data_ocorrencia', 'data_envio', 'data_solicitacao'],
            converters={"tempo_para_envio": pd.to_timedelta},
        )

    
    def atlas() -> pd.DataFrame:
        return pd.read_csv(
            caminhos.arquivo_estruturado_atlas,
            parse_dates=['Data_Registro'],
        )

    
    def ips() -> pd.DataFrame:
        return pd.read_csv(
            caminhos.arquivo_estruturado_ips
        )
    
    



    

    