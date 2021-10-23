from typing import List, Optional

from pydantic import BaseModel, validator


class Edge(BaseModel):
    src: int
    dst: int
    weight: float


class EdgeList(BaseModel):
    __root__: List[Edge]


class Result(BaseModel):
    path: List[int]
    ham_energy: float
    energy: float

    router_id: str
    solver_type: str
    solution_type: str
    adj: List[List[float]]
    qubo: List[List[float]]


class Input(BaseModel):
    edge_list: EdgeList
    solver_type: str
    router_id: str
