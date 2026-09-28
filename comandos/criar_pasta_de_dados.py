"""Criar pasta de dados.

Arquivo executável como módulo:
>>> python3 -m comandos.criar_pasta_de_dados

"""

from pathlib import Path





def main() -> None:
    diretorio_raiz = Path(__file__).parent.parent
        
    caminho_brutos = diretorio_raiz / 'dados' / 'brutos'
    caminho_estruturados = diretorio_raiz / 'dados' / 'estruturados'
    caminho_graficos = diretorio_raiz / 'dados' / 'graficos'
    
    caminho_brutos.mkdir(parents=True, exist_ok=True)
    caminho_estruturados.mkdir(parents=True, exist_ok=True)
    caminho_graficos.mkdir(parents=True, exist_ok=True)
    
    print('Pasta de dados criada!')
    
    print('Adicione os arquivos do drive em dados/brutos/') 



if __name__ == '__main__':
    main()
    
    
    
