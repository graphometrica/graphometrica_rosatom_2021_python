from typing import Tuple
import networkx as nx
import numpy as np


def tsp2qubo(g: nx.Graph) -> Tuple[np.array, float, int]:
    """
    H = \\
        A * \sum_i (1 - \sum_j x_{i,j})^2 + \\
        A * \sum_j (1 - \sum_i x_{i,j})^2 + \\
        A * \sum_{u,v \notin E} \sum_j x_{u,j} x_{v, j+1} + \\
        B * \sum_{u,v \in E} w_{u,v} \sum_j x_{u,j} x_{v, j+1}

    input: networkx.Graph
    output: QUBO, A-contrain, Problem size
    """
    n = g.number_of_nodes()
    shape = n * n
    qubo = np.zeros((shape, shape), dtype=np.float64)

    b = 1
    a = 5 * b * max([e[2]["weight"] for e in g.edges(data=True)])

    # A * \sum_i (1 - \sum_j x_{i,j})^2
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


    # A * \sum_j (1 - \sum_i x_{i,j})^2
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

    # A * \sum_{u,v \notin E} \sum_j x_{u,j} x_{v, j+1}
    # B * \sum_{u,v \in E} w_{u,v} \sum_j x_{u,j} x_{v, j+1}
    # We could see that the 3d and 4th parts of \hat{H} have the difference in coefficeint only.
    # That is why they were combined into one loop.
    for i in range(n):
        for j in range(n):
            if g.has_edge(i, j):
                coef = b * g.get_edge_data(i, j)["weight"]
            else:
                coef = a

            for k in range(n - 1):
                qubo[i + k * n, j + (k + 1) * n] += coef

            qubo[i + (n - 1) * n, j] += coef

    return (qubo, a, n)
