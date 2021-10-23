from pathlib import Path
from typing import Dict, Tuple

import networkx as nx


def csv2graph(csv_file: Path) -> Tuple[nx.Graph, Dict[str, int]]:
    g = nx.Graph()
    lines = csv_file.read_text().split("\n")
    lines.pop(0)

    nodes = {}

    k = 0
    for l in lines:
        if len(l) > 0:
            src, dst, weight = l.split(",")
            if src not in nodes.keys():
                nodes[src] = k
                k += 1
            if dst not in nodes.keys():
                nodes[dst] = k
                k += 1

            g.add_edge(nodes[src], nodes[dst], weight=float(weight))

    nodes_reverse = {v: k for k, v in nodes.items()}
    nx.set_node_attributes(g, name="name", values=nodes_reverse)

    return (g, nodes_reverse)
