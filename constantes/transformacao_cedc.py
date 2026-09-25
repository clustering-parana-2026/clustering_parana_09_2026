coluna_por_dict_valores_novos: dict[str, dict[str, str]] = {
    'desastre': {
        'Tempestade Local/Convectiva - Chuvas Intensas': 'chuva_intensa',
        'Tempestade Local/Convectiva - Granizo': 'granizo',
        'Tempestade Local/Convectiva - Vendaval': 'vendaval',
        'Onda de Frio - Geadas': 'outro',
        'Onda de Frio - Friagem': 'outro',
        'Tempestade Local/Convectiva - Tornados': 'outro',
        'Ciclones - Marés de Tempestade (Ressacas)': 'outro',
        'Enxurradas': 'enxurrada',
        'Alagamentos': 'alagamento',
        'Inundações': 'inundacao',
        'Estiagem': 'estiagem',
        'Incêndio Florestal - Incêndios em Parques, Áreas de Proteção Ambiental e Áreas de Preservação Permanente Nacionais, Estaduais ou Municipais': 'outro',
        'Erosão Continental - Boçorocas': 'outro',
        'Erosão Continental - Ravinas': 'outro',
        'Deslizamentos': 'outro',
    },
    'material': {
        'Colchonete': 'kit_dormitorio',
        'Cobertor': 'kit_dormitorio',
        'Colchão Solteiro': 'kit_dormitorio',
        'Colchão': 'kit_dormitorio',
        'Kit Dormitório - SEDEC (1 Colchão de solteiro, 1 cobertor de solteiro, 1 lençol de solteiro, 1 fronha, 1 travesseiro)': 'kit_dormitorio',
        'Kit Dormitório-(1 cobertor solteiro, 1 lençol solteiro, 1 fronha e 1 travesseiro)': 'kit_dormitorio',

        'Cesta Básicas, via Coordenação Estadual da Defesa Civil': 'cesta_basica',
        'Cesta Básica': 'cesta_basica',

        'Kit Higiene - SEDEC': 'kit_higiene',
        'Kit Higiene': 'kit_higiene',

        'Kit Limpeza - SEDEC': 'kit_limpeza',
        'Kit Limpeza': 'kit_limpeza',

        'Telhas Ficbrocimento (2,44X0,50X0,004) - SEDEC': 'telhas',
        'Telha Fibrocimento 2.44x500x4mm': 'telhas',

        'Máscara N95': 'outro',
        'Máscara de proteção facial': 'outro',
        'Máscara facial FP2': 'outro',
        'MASCARA PROTEÇÃO (EPI)': 'outro',
        'Alcool gel 70% (unidade)': 'outro',
        'Alcool líquido 70% (litro)': 'outro',
        'Lona Plástica Preta - Rolo com 4x100 metros': 'outro',
    }
}

coluna_nova_por_dict_valores_novos = {
    'agrupamento_desastre': {
        'alagamento': 'alagamento_chuva_enxurrada_inundacao',
        'inundacao': 'alagamento_chuva_enxurrada_inundacao',
        'chuva_intensa': 'alagamento_chuva_enxurrada_inundacao',
        'enxurrada': 'alagamento_chuva_enxurrada_inundacao',
        'vendaval': 'granizo_vendaval',
        'granizo': 'granizo_vendaval',
    }
}

nova_ordem_das_colunas: list[str] = [
    'mesorregiao',
    'microrregiao',
    'municipio', 
    'numero_da_ocorrencia',
    'desastre', 
    'grupo_desastre',
    'agrupamento_desastre',
    'data_ocorrencia', 
    'material',
    'quantidade_material', 
    'qtd_material_normalizada',
    'data_envio',
    'data_solicitacao', 
    'tempo_para_envio',
    'populacao', 
    'pib', 
    'receita_corrente_liquida',
    'prejuizo_publico', 
    'prejuizo_privado',
]