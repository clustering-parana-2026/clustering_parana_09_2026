"""Padrões para implementar no pré-processamento dos dados gerais"""

colunas_caractere_antigo_por_caractere_novo: dict[str, str] = str.maketrans({
    'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a',
    'é': 'e', 'ê': 'e',
    'í': 'i',
    'ó': 'o', 'õ': 'o', 'ô': 'o',
    'ú': 'u',
    'ç': 'c',
})

municipios_nome_antigo_por_nome_novo: dict[str, str] = {
    "Diamante D'Oeste": "Diamante do Oeste",
    "Itapejara d'Oeste": "Itapejara do Oeste",
    "Pérola d'Oeste": "Pérola do Oeste",
    "São Jorge d'Oeste": "São Jorge do Oeste",
    "Nova Cantu": "Nova Cantú",
    "Rancho Alegre D'Oeste": "Rancho Alegre do Oeste",
}