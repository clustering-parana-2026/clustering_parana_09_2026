from pathlib import Path


from sklearn import preprocessing

import plotly.graph_objects as go
import graphviz


from carregamento.dados_tabulares_principais import CarregadorDadosEstruturados
from carregamento.coordenadas_mapa import coletar_coordenadas_parana

import constantes.estilos as est

from utils.decoradores import marcar_tempo_de_execucao

from visualizacoes.fluxogramas import fluxograma_metodo
from visualizacoes.larguras_medias_silhuetas import larguras_medias_silhuetas
import visualizacoes.barras_anl_atributos as barras
import visualizacoes.tabelas as tabelas
from visualizacoes.silhuetas_clusters import silhuetas_clusters
from visualizacoes.centroides import centroides
from visualizacoes.mapa_microrregioes import mapa_microrregioes

from core.analise_atributos import AnaliseAtributos
from core.matrizes import Matrizes
from core.analise_silhuetas import AnaliseSilhuetas
from core.mineracao import Mineracao







class _Downloader:
    def __init__(self, path: Path) -> None:
        self.path = path


    def download_plotly(
        self,
        plot: go.Figure, 
        filename: str, 
    ) -> None:
        output_file = self.path / filename
        plot.write_image(
            output_file, 
            width=int(plot.layout.width or est.largura),
            height=int(plot.layout.height or est.altura),
        )
        

    def download_graphviz(self, plot: graphviz.Digraph, filename: str) -> None:
        plot.render(
            filename=filename, 
            directory=self.path,
            view=False,
            cleanup=True,
            format='pdf'
        )




@marcar_tempo_de_execucao()
def main() -> None:
    # --- Setup --- #

    # Criar pasta para armazenar os gráficos.
    output_dir = Path('visualizacoes_exportadas')
    output_dir.mkdir(exist_ok=True)

    # Instanciar gerenciador de downloads de gráficos.
    DWLD = _Downloader(output_dir)

    # --- Fluxogramas --- #

    fluxograma_kdd = fluxograma_metodo()
    DWLD.download_graphviz(fluxograma_kdd, 'metodo_kdd')

    # --- Análise Atributos --- #

    # Inicialização.
    anl_atr = AnaliseAtributos(
        CarregadorDadosEstruturados.cedc()
    )

    # Visualizar frequência dos subgrupos de desastre.
    frequencia_desastres = anl_atr.calcular_frequencia_desastres()
    grafico_freq_desastres = barras.barras_frequencia_desastres(frequencia_desastres)
    DWLD.download_plotly(grafico_freq_desastres, 'freq_desastres.pdf')

    # Visualizar frequência a frequência com que cada material foi enviado.
    frequencia_materiais = anl_atr.calcular_frequencia_materiais()
    grafico_freq_materiais = barras.barras_frequencia_materiais(frequencia_materiais)
    DWLD.download_plotly(grafico_freq_materiais, 'freq_materiais.pdf')

    # Observar estatíticas relacionadas aos lotes de cada tipo de material.
    sumario_envios_de_material = anl_atr.calcular_sumario_envios_de_material()
    grafico_sumario_envios = (
        tabelas.tabela_sumario_envios_envios_de_material(
            sumario_envios_de_material
        )
    )
    DWLD.download_plotly(grafico_sumario_envios, 'sumario_envios.pdf')

    # Observar relacão entre materiais por subgrupo de desastre.
    quantidade_normalizada_de_material_por_desastre = (
        anl_atr.calcular_quantidade_normalizada_de_material_por_agrupamento(
            col='desastre'
        )
    )
    grafico_qtd_material_por_desastre = (
        tabelas.tabela_quantidades_normalizadas_por_desastre(
            quantidade_normalizada_de_material_por_desastre
        )
    )
    DWLD.download_plotly(grafico_qtd_material_por_desastre, 'material_por_desastre.pdf')

    # Correlação.
    correlacao_desastres_sobre_material = (
        quantidade_normalizada_de_material_por_desastre
        .T
        .corr()
    )
    grafico_correlacao_desastres_sobre_material = (
        tabelas.tabela_correlacao_desastres_sobre_material(
            correlacao_desastres_sobre_material
        )
    )
    DWLD.download_plotly(grafico_correlacao_desastres_sobre_material, 'correlacao_desastres.pdf')

    # Observar relacão entre materiais por subgrupo de desastre.
    quantidade_normalizada_de_material_por_atributo = (
        anl_atr.calcular_quantidade_normalizada_de_material_por_agrupamento(
            col='agrupamento_desastre',
        )
    )
    grafico_qtd_material_por_atributo = (
        tabelas.tabela_quantidades_normalizadas_por_atributo(
            quantidade_normalizada_de_material_por_atributo
        )
    )
    DWLD.download_plotly(grafico_qtd_material_por_atributo, 'material_por_atributo.pdf')

    
    # --- Análise silhuetas e mineração --- #

    # Carregar matriz de atributos.
    D = Matrizes.atributos(
        CarregadorDadosEstruturados.major_daniel()
    )

    # Aplicar normalização por z-score nos dados.
    X = preprocessing.StandardScaler().fit_transform(D)

    # Ajustar os modelos uma vez para cada k.
    modelos = Mineracao.obter_modelos_kmeans(
        X=X,
        k=list(range(2,15)),
    )

    # Instanciar analisados de silhuetas.
    anl_sil = AnaliseSilhuetas(
        modelos=modelos,
    ) 

    # Escolher candidatos para k, a partir do score do clustering.
    larguras_medias_globais_das_silhuetas = anl_sil.calcular_largura_media_global_da_silhueta(
        X=X,
        k_de_interesse=list(range(2,15)),
    )
    grafico_silhuetas_medias = larguras_medias_silhuetas(
        larguras_medias_globais_das_silhuetas
    )   
    DWLD.download_plotly(grafico_silhuetas_medias, 'silhuetas_medias.pdf')

    # Por cluster.
    silhuetas_dos_clusters = (
        anl_sil.calcular_silhuetas_dos_clusters(
            D=D,
            X=X,
            k_de_interesse=[2, 3, 7],
        )
    )
    grafico_silhuetas_clusters = silhuetas_clusters(
        silhuetas_dos_clusters
    )
    DWLD.download_plotly(grafico_silhuetas_clusters, 'silhuetas_clusters.pdf')

    # Executar KMeans.
    rotulos = modelos[7].labels_
    C = Matrizes.clustering(
        D=D,
        rotulos=rotulos,
        formato='dados_originais'
    )

    geo_json = coletar_coordenadas_parana()
    grafico_mapa = mapa_microrregioes(
        C=C,
        geo_json=geo_json,
    )
    DWLD.download_plotly(grafico_mapa, 'mapa_microrregioes.pdf')

    grafico_medias = centroides(C)
    DWLD.download_plotly(grafico_medias, 'medias_por_cluster.pdf')




if __name__ == '__main__':
    main()

