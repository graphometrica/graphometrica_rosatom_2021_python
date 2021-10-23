from typing import Tuple
import numpy as np
import network as nx

def lp2qubo(g: nx.Graph) -> Tuple[np.array, float, int]:
    n = g.number_of_nodes()
    size = n + 1
    shape = size * size
    qubo = np.zeros((shape, shape), dtype=np.float64)

    a = 1
    b = shape

    return None
