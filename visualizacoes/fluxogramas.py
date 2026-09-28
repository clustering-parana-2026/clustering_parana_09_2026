"""Construção do fluxograma das etapas do processo de KDD."""

import graphviz


import utils.plotagem as funcs





def fluxograma_metodo() -> graphviz.Digraph:
    """Constrói um fluxograma com as cinco etapas do processo de KDD.

    Returns
    -------
    graphviz.Digraph
        Grafo direcionado denominado ``fluxograma_metodo``, configurado
        para renderização em PDF. Contém as etapas Seleção,
        Pré-processamento, Transformação, Mineração e Interpretação,
        conectadas sequencialmente da esquerda para a direita.

    Notes
    -----
    Representa as etapas por caixas preenchidas com cantos arredondados,
    conectadas por setas, sobre fundo transparente.

    As dimensões utilizadas no atributo ``size`` são calculadas a
    partir de 1,7 vezes a largura padrão e 1,6 vezes a altura padrão
    do projeto, convertidas para polegadas considerando 96 pixels
    por polegada.
    """
    grafo_direcionado = graphviz.Digraph("fluxograma_metodo", format="pdf")

    pixels_por_polegada = 96
    largura = funcs.escalar_largura(1.7) / pixels_por_polegada
    altura = funcs.escalar_altura(1.6) / pixels_por_polegada

    grafo_direcionado.attr(
        rankdir="LR",
        size=f"{largura},{altura}",
        margin="0",
        pad="0.10",
        ranksep="0.18",
        bgcolor="transparent",
    )

    grafo_direcionado.attr(
        "node",
        shape="box",
        style="rounded,filled",
        fillcolor="#EFF6FF",
        color="#64748B",
        fontcolor="#1E293B",
        fontname="Arial",
        fontsize="10",
        fixedsize="false",
        margin="0.10,0.08",
        height="0.50",
        penwidth="1.0",
    )

    grafo_direcionado.attr(
        "edge",
        color="#64748B",
        penwidth="1.0",
        arrowsize="0.60",
    )

    passos = [
        ("sel", "Seleção"),
        ("pre", "Pré-\nprocessamento"),
        ("trans", "Transformação"),
        ("min", "Mineração"),
        ("interp", "Interpretação"),
    ]

    for id_nodo, titulo in passos:
        grafo_direcionado.node(id_nodo, titulo)

    for (cauda, _), (cabeca, _) in zip(passos, passos[1:]):
        grafo_direcionado.edge(cauda, cabeca)

    return grafo_direcionado
