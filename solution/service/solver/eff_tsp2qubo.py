from typing import Tuple
import networkx as nx
import numpy as np


def eff_tsp2qubo(g: nx.Graph) -> Tuple[np.array, float, int]:
    n = g.number_of_nodes() - 1
    shape = n * n
    qubo = np.zeros((shape, shape), dtype=np.float64)

    b = 1
    a = 5 * b * max([e[2]["weight"] for e in g.edges(data=True)])

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


    for j in range(n):
        partial = [1,]
        for i in range(n):
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
        for j in range(n):
            if g.has_edge(i + 1, j + 1):
                coef = b * g.get_edge_data(i, j)["weight"]
            else:
                coef = a

            for k in range(n - 1):
                qubo[i + k * n, j + (k + 1) * n] += coef

        if g.has_edge(i + 1, 0):
            coef = b * g.get_edge_data(i + 1, 0)["weight"]
        else:
            coef = a

        qubo[i, i] += coef
        qubo[i + (n - 1) * n, i + (n - 1) * n] += coef

    return (qubo, a, n)
