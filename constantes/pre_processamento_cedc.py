colunas_nome_antigo_por_nome_novo: dict[str, str] = {
    'quantidade': 'quantidade_material',
    'data_da_solicitacao': 'data_solicitacao',
    'data_do_envio': 'data_envio',
    'data_da_ocorrencia': 'data_ocorrencia',
}

nome_nova_coluna_por_dict_valor_antigo_por_valor_novo = {
    'grupo_desastre': {
        'Tempestade Local/Convectiva - Chuvas Intensas': 'metereologico', 
        'Tempestade Local/Convectiva - Granizo': 'metereologico',
        'Tempestade Local/Convectiva - Vendaval': 'metereologico',
        'Onda de Frio - Geadas': 'metereologico',
        'Onda de Frio - Friagem': 'metereologico',
        'Tempestade Local/Convectiva - Tornados': 'metereologico',
        'Ciclones - Marés de Tempestade (Ressacas)': 'metereologico',
        'Enxurradas': 'hidrologico',
        'Alagamentos': 'hidrologico',
        'Inundações': 'hidrologico',
        'Estiagem': 'climatologico',
        'Incêndio Florestal - Incêndios em Parques, Áreas de Proteção Ambiental e Áreas de Preservação Permanente Nacionais, Estaduais ou Municipais': 'climatologico',
        'Erosão Continental - Boçorocas': 'geologico',
        'Erosão Continental - Ravinas': 'geologico',
        'Deslizamentos': 'geologico',
        'Doenças infecciosas virais': 'biologico',
    },
}

colunas_para_remover: list[str] = [
    'idhm', 
    'prefeito'
]

linhas_para_remover: dict[str, list[str]] = {
    'grupo_desastre': [
        'biologico',
    ],
}

nova_ordem_das_colunas: list[str] = [
    'mesorregiao',
    'microrregiao',
    'municipio', 
    'numero_da_ocorrencia',
    'desastre', 
    'grupo_desastre',
    # 'agrupamento_desastre',
    'data_ocorrencia', 
    'material',
    'quantidade_material', 
    # 'qtd_material_normalizada',
    'data_envio',
    'data_solicitacao', 
    'tempo_para_envio',
    'populacao', 
    'pib', 
    'receita_corrente_liquida',
    'prejuizo_publico', 
    'prejuizo_privado',
]
