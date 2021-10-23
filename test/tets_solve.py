import json
import os
import sys
from pathlib import Path

from solution.graph_utils import csv2graph
from solution.service.serialization import EdgeList, Result
from solution.service.solver import solve

if __name__ == "__main__":
    g, _ = csv2graph(Path(".").joinpath("data").joinpath("paths.csv"))
    edges = EdgeList.parse_raw(
        json.dumps(
            [
                {"src": e[0], "dst": e[1], "weight": e[2]["weight"]}
                for e in g.edges(data=True)
            ]
        )
    )

    os.environ["QBOARD_TOKEN"] = sys.argv[1]
    os.environ["QBOARD_SOLVER"] = "remote:simcim"
    os.environ["QBOARD_SERVER"] = "https://remote.qboard.tech"

    result = solve(edges)

    print(result.json())
