import os

import networkx as nx
from qboard import Solver

from ..serialization import EdgeList, Result
from .as_graph import as_graph
from .eff_tsp2qubo import eff_tsp2qubo


def solve(
        edges: EdgeList,
        solver_type: str = "remote:simcim",
        router_id: str = "12345"
) -> Result:
    g, mapping = as_graph(edges)
    token = os.environ["QBOARD_TOKEN"]
    server = os.environ["QBOARD_SERVER"]
    params = {
        "remote_addr": server,
        "access_key": token,
    }

    s = Solver(mode=solver_type, params=params)
    qubo, penalty, n = eff_tsp2qubo(g)
    spins, energy = s.solve_qubo(qubo, timeout=30)

    q_path = [0,]
    for i in range(n):
        k = 0
        for i, spin in enumerate(spins[i * n:(i+1) * n]):
            if spin == 1:
                k = i + 1
        q_path.append(k)
    q_path.append(0)

    time = 0
    for i in range(len(q_path) - 1):
        time += g.get_edge_data(q_path[i], q_path[i + 1])["weight"]

    res = Result(
        path = [mapping[idx] for idx in q_path],
        ham_energy = energy,
        energy = time,
        router_id = router_id,
        solver_type = solver_type,
        solution_type = "feasible",
        adj = nx.adjacency_matrix(g).todense().tolist(),
        qubo = qubo.tolist(),
    )

    return res
