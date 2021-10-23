from pathlib import Path

import matplotlib.pyplot as plt
import networkx as nx


def plot_graph(g: nx.Graph, prefix: Path) -> None:
    pos = nx.drawing.layout.circular_layout(g)
    nx.draw(g, pos=pos)
    edge_weights = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos=pos, edge_labels=edge_weights)
    labels = nx.get_node_attributes(g, "name")
    nx.draw_networkx_labels(g, pos=pos, labels=labels)

    plt.margins(0.1)
    plt.savefig(
        str(prefix.joinpath("problem_graph.png").absolute()),
        dpi=150,
    )
