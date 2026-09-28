"""Extrair dados do IBGE para construir mapa do Paraná."""

import requests

import constantes.urls as urls





def coletar_coordenadas_parana():
    """Obtém a malha do Paraná e associa nomes às microrregiões.

    Returns
    -------
    dict or None
        GeoJSON obtido da URL configurada, com o nome de cada
        microrregião em ``properties['nome']`` e em ``id``.
        Retorna None se ocorrer uma exceção durante a coleta
        ou o processamento.

    Notes
    -----
    Consulta as URLs ``constantes.urls.url_malha`` e 
    ``constantes.urls.url_nomes`` para obter as geometrias e 
    a relação entre códigos e nomes.

    Associa cada código ``codarea`` ao nome correspondente. Quando
    não encontra correspondência, utiliza o próprio código como nome
    e identificador da feição.

    Realiza novas requisições a cada chamada, sem armazenamento local.
    Em caso de exceção, imprime uma mensagem de erro.
    """
    try:
        # Geometrias das 39 microrregiões do PR.
        pr_geo_json = requests.get(urls.url_malha).json()

        # Nomes das microrregiões (a malha só traz o código 'codarea').
        microrregioes = requests.get(urls.url_nomes).json()
        codigo_para_nome = {str(m['id']): m['nome'] for m in microrregioes}

        # Insere o nome em cada feature pra poder casar com o DataFrame depois.
        for feature in pr_geo_json['features']:
            codigo = feature['properties']['codarea']
            feature['properties']['nome'] = codigo_para_nome.get(codigo, codigo)
            feature['id'] = feature['properties']['nome']

    except Exception as e:
        print('Erro na coleta de dados para a mapa:', e)
    else:
        return pr_geo_json