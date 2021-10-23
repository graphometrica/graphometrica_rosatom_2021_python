from typing import List

from pydantic import BaseModel


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

    solver_type: str
    solution_type: str
    adj: List[List[float]]
    quba: List[List[float]]
