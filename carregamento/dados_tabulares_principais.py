"""Carregamento dos dados principais da aplicação.

Implementa a classe ``CarregadorDadosBrutos`` para 
carregar os dados brutos da aplicação e a classe 
``CarregadorDadosEstruturados`` para carregar os 
dados apóes o pré-processamento e/ou após a
transformação.
"""

import pandas as pd


import constantes.caminhos as caminhos





class CarregadorDadosBrutos:
    @staticmethod
    def cedc() -> pd.DataFrame:
        """Carrega os registros brutos da CEDC a partir de um CSV.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de ``caminhos.arquivo_bruto_cedc``.

        Notes
        -----
        Utiliza ponto e vírgula como separador de campos, ponto
        como separador de milhares e vírgula como separador decimal.
        """
        return pd.read_csv(
            caminhos.arquivo_bruto_cedc,
            sep=';', 
            thousands='.',  
            decimal=','
        )

    
    @staticmethod
    def atlas() -> pd.DataFrame:
        """Carrega os dados brutos do Atlas a partir de um arquivo Excel.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de``caminhos.arquivo_bruto_atlas``.
        """
        return pd.read_excel(
            caminhos.arquivo_bruto_atlas,
        )


    @staticmethod
    def ips() -> pd.DataFrame:
        """Carrega os dados brutos do IPS a partir de um CSV.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de ``caminhos.arquivo_bruto_ips``,
            utilizando as opções padrão de ``pandas.read_csv``.
        """
        return pd.read_csv(
            caminhos.arquivo_bruto_ips
        )



class CarregadorDadosEstruturados:
    """Carregamento dos arquivos estruturados e leitura de campos temporais."""

    @staticmethod
    def cedc() -> pd.DataFrame:
        """Carrega os dados estruturados da CEDC e seus campos temporais.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de ``caminhos.arquivo_estruturado_cedc``.

        Notes
        -----
        Solicita a interpretação de ``data_ocorrencia``, ``data_envio``
        e ``data_solicitacao`` como datas durante a leitura.

        Converte ``tempo_para_envio`` para intervalos de tempo
        utilizando ``pandas.to_timedelta``.
        """
        return pd.read_csv(
            caminhos.arquivo_estruturado_cedc, 
            parse_dates=['data_ocorrencia', 'data_envio', 'data_solicitacao'],
            converters={"tempo_para_envio": pd.to_timedelta},
        )


    @staticmethod
    def atlas() -> pd.DataFrame:
        """Carrega os dados estruturados do Atlas e suas datas de registro.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de ``caminhos.arquivo_estruturado_atlas``.

        Notes
        -----
        Solicita a interpretação de ``Data_Registro`` como data
        durante a leitura.
        """
        return pd.read_csv(
            caminhos.arquivo_estruturado_atlas,
            parse_dates=['Data_Registro'],
        )


    @staticmethod
    def ips() -> pd.DataFrame:
        """Carrega os dados estruturados do IPS a partir de um CSV.

        Returns
        -------
        pandas.DataFrame
            Dados lidos de ``caminhos.arquivo_estruturado_ips``,
            utilizando as opções padrão de ``pandas.read_csv``.
        """
        return pd.read_csv(
            caminhos.arquivo_estruturado_ips
        )
    
    



    

    