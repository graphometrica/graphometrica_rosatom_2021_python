from typing import Dict, Union

import networkx as nx

from ..serialization import EdgeList


def as_graph(edges: EdgeList) -> Union[nx.Graph, Dict[int, int]]:
    g = nx.Graph()
    nodes = {}

    k = 0
    for e in edges.__root__:
        if e.src not in nodes.keys():
            nodes[e.src] = k
            k += 1
        if e.dst not in nodes.keys():
            nodes[e.dst] = k
            k += 1

        g.add_edge(nodes[e.src], nodes[e.dst], weight=e.weight)

    nodes_reverse = {v: k for k, v in nodes.items()}

    return (g, nodes_reverse)
