import constantes.caminhos as caminhos

from pre_processamento.atlas import estruturar_arquivo_atlas
from pre_processamento.ips import estruturar_arquivo_ips
from pre_processamento.cedc import executar_pre_processamento_cedc

from transformacao.cedc import executar_transformacao_cedc





def pipeline() -> None:
    executar_pre_processamento_cedc(caminhos.arquivo_estruturado_major_daniel,)
    executar_transformacao_cedc(caminhos.arquivo_estruturado_major_daniel,)
    # estruturar_arquivo_atlas(caminhos.arquivo_estruturado_atlas)
    # estruturar_arquivo_ips(caminhos.arquivo_estruturado_ips)



if __name__ == '__main__':
    pipeline()