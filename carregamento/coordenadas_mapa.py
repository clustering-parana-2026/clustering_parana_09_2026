import requests

import constantes.urls as urls






def coletar_coordenadas_parana():
    try:
        # Geometrias das 39 microrregiões do PR.
        pr_geo_json = requests.get(urls.url_malha).json()

        # Nomes das microrregiões (a malha só traz o código 'codarea').
        microrregioes = requests.get(urls.url_nomes).json()
        codigo_para_nome = {str(m['id']): m['nome'] for m in microrregioes}

        # Injeta o nome em cada feature pra poder casar com o df depois.
        for feature in pr_geo_json['features']:
            codigo = feature['properties']['codarea']
            feature['properties']['nome'] = codigo_para_nome.get(codigo, codigo)
            feature['id'] = feature['properties']['nome']

    except Exception as e:
        print('Erro na coleta de dados para a mapa:', e)
    else:
        return pr_geo_json