from typing import Tuple
import numpy as np
import networkx as nx

def lp2qubo(g: nx.Graph) -> Tuple[np.array, float, int]:
    n = g.number_of_nodes()
    size = n + 1
    shape = n * size
    qubo = np.zeros((shape, shape), dtype=np.float64)

    a = 5
    b = -1

    for i in range(n):
        partial = [1,]
        for j in range(n):
            partial.append((i + j * n, -1))

        for k in partial:
            for l in partial:
                if k == 1:
                    if l == 1:
                        continue
                    else:
                        qubo[l[0], l[0]] += a * l[1]
                elif l == 1:
                    qubo[k[0], k[0]] += a * k[1]
                else:
                    qubo[k[0], l[0]] += a * k[1] * l[1]

    for i in range(n):
        qubo[size + i * n - 1, size + i * n - 1] += a

    for i in range(n):
        for j in range(n):
            if g.has_edge(i, j):
                coef = b
            else:
                coef = a

            for k in range(n - 1):
                qubo[i + k * size, j + (k + 1) * size] += coef

    return (qubo, b, n)
