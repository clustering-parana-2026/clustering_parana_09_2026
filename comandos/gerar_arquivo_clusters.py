"""Obter arquivo com a relação cluster-microrregião.

Arquivo executável como módulo:
>>> python3 -m comandos.gerar_arquivo_clusters

"""

from pathlib import Path


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados

from core.matrizes import Matrizes
from core.mineracao import Mineracao

from sklearn import preprocessing





def main() -> None:
    # Carregar matriz de atributos.
    D = Matrizes.atributos(
        CarregadorDadosEstruturados.cedc()
    )

    # Aplicar normalização por z-score nos dados.
    X = preprocessing.StandardScaler().fit_transform(D)

    # Executar KMeans.
    k = 7
    modelos = Mineracao.obter_modelos_kmeans(
        X=X,
        k=[k],
    )

    # Obter a matriz com os clusters e as respectivas microrregiões.
    C = Matrizes.clustering(
        D=D,
        rotulos=modelos[k].labels_,
        formato='apenas_microrregioes',
    )

    # Exportar matriz C.
    diretorio_raiz = Path(__file__).parent.parent
    C.to_csv(
        diretorio_raiz / "clusters_microrregioes.csv",
        index=True,
        index_label="microrregiao",
        encoding="utf-8",
    )



if __name__ == '__main__':
    main()