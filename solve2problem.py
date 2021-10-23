import sys
from pathlib import Path

import networkx as nx
import numpy as np
from qboard import Solver

from solution.converters import lp2qubo
from solution.graph_utils import csv2graph

if __name__ == "__main__":
    passwd = sys.argv[1]
    params = {"remote_addr": "https://remote.qboard.tech", "access_key": passwd}

    problem = csv2graph(
        Path(__file__).parent.joinpath("data").joinpath("problem2_graph.csv"),
        directed=True
    )
    g = problem[0]
    qubo, a, n = lp2qubo(g)
    s = Solver(mode="remote:simcim", params=params)

    spins, energy = s.solve_qubo(qubo, timeout=30)

    qboard_sol = []
    for i in range(n):
        print(spins[i * (n + 1) : (i + 1) * (n + 1)])
        k = -1
        is_used = int(not spins[n + i * (n + 1)])
        for i, spin in enumerate(
            spins[i * (n + 1) : (i + 1) * n - 1]
        ):
            if spin == 1:
                k = i
        qboard_sol.append((k, is_used))


    print("Solution from the QBOARD:")
    print(qboard_sol)

    is_correct = True

    for i in range(len(qboard_sol) - 1):
        src = qboard_sol[i]
        dst = qboard_sol[i + 1]

        if (src[0] == -1) and src[1]:
            is_correct = False
            continue

        if (dst[0] == -1) and dst[1]:
            is_correct = False
            continue

        if src[1] and dst[1]:
            if not g.has_edge(src[0], dst[0]):
                is_correct = False

    print(f"Is solution correct? {is_correct}")
