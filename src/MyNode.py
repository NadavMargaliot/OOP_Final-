import random


class MyNode:
    def __init__(self, id: int, location: tuple = None):
        self.id = id
        self.tag = 0;
        self.info = ""
        if location is not None:
            self.location = location
        else:
            self.location = (random.uniform(0, 100), random.uniform(0, 100), 0)
        self.neighbors_out = {}  # <dest_id , weight>
        self.neighbors_in = {}  # <src_id , weight>

    def __str__(self) -> str:
        """@return a string (str) representation of the NodeData"""
        return f"{self.id}"

    def __repr__(self) -> str:
        """@return a string (repr) representation of the NodeData"""
        return f"{self.id}: |edges out| {len(self.neighbors_out)} |edges in| {len(self.neighbors_in)}"



    def setLocation(self, location: tuple):
        self.location = location

    def addNeighborIn(self, neighbor_id, weight: float) -> None:
        """Adding an edge to the node from a neighbor"""
        self.neighbors_in[neighbor_id] = weight

    def addNeighborOut(self, neighbor_id, weight: float) -> None:
        """Adding an edge to the neighbor from the node"""
        self.neighbors_out[neighbor_id] = weight
