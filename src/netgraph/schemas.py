from typing import List
from pydantic import BaseModel

class BaseNode(BaseModel):
    ip: str
    name: str
    hostname: str
    model: str
    mac: str
    uplink: int

class Node(BaseNode):
    id: int
    ro_community: str
    level: int

class NodeCreate(BaseNode):
    pass

class BaseEdge(BaseModel):
    source_id: int
    source_port: int
    target_id: int
    target_port: int
    netmap_id: int

class Edge(BaseEdge):
    id: int

class EdgeCreate(BaseEdge):
    pass

class BaseNetmap(BaseModel):
    name: str

class Netmap(BaseNetmap):
    nodes: List[Node]
    edges: List[Edge]

class NetmapCreate(BaseNetmap):
    pass