from pathlib import Path




if __name__ == '__main__':
    diretorio_raiz = Path(__file__).parent.parent
    
    caminho_brutos = diretorio_raiz / 'dados' / 'brutos'
    caminho_estruturados = diretorio_raiz / 'dados' / 'estruturados'
    
    caminho_brutos.mkdir(parents=True, exist_ok=True)
    caminho_estruturados.mkdir(parents=True, exist_ok=True)
    
    print('Pasta "dados/brutos" criada.')
    print('Pasta "dados/estruturados" criada.')
    
    print('Adicione os arquivos do drive') 
    
    
