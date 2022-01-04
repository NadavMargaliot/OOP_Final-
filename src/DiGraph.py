from src.GraphInterface import GraphInterface
from src.MyNode import MyNode


class DiGraph(GraphInterface):
    def __init__(self):
        self.nodeSize = 0
        self.edgeSize = 0
        self.mc = 0
        self.nodes = {}  # <id , MyNode>

    def get_node(self, node_id):
        """Returns the node of this id if the node is in the graph"""
        if node_id in self.nodes:
            return self.nodes.get(node_id)
        return None

    def v_size(self) -> int:
        """Returns the number of vertices in this graph"""
        return self.nodeSize

    def e_size(self) -> int:
        """Returns the number of edges in this graph"""
        return self.edgeSize

    def get_all_v(self) -> dict:
        """return a dictionary of all the nodes in the Graph, each node is represented using a pair
         (node_id, node_data)"""
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected to (into) node_id ,
        each node is represented using a pair (other_node_id, weight)"""
        return self.nodes.get(id1).neighbors_in

    def all_out_edges_of_node(self, id1: int) -> dict:
        """return a dictionary of all the nodes connected from node_id , each node is represented using a pair
        (other_node_id, weight)
        """
        return self.nodes.get(id1).neighbors_out

    def get_mc(self) -> int:
        """
        Returns the current version of this graph,
        on every change in the graph state - the MC should be increased
        @return: The current version of this graph.
        """
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        Adds an edge to the graph.
        @param id1: The start node of the edge
        @param id2: The end node of the edge
        @param weight: The weight of the edge
        @return: True if the edge was added successfully, False o.w.
        Note: If the edge already exists or one of the nodes dose not exists the functions will do nothing"""
        if id1 == id2:
            return False
        if id1 not in self.nodes or id2 not in self.nodes:
            return False
        if weight < 0:
            raise Exception('Edge must be positive')
        if id2 not in self.nodes.get(id1).neighbors_out.keys():
            self.nodes.get(id1).addNeighborOut(id2, weight)
            self.nodes.get(id2).addNeighborIn(id1, weight)
            self.mc += 1
            self.edgeSize += 1
            return True
        elif id2 in self.nodes.get(id1).neighbors_out.keys():
            self.nodes.get(id1).addNeighborOut(id2, weight)
            self.nodes.get(id2).addNeighborIn(id1, weight)
            self.mc += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        Adds a node to the graph.
        @param node_id: The node ID
        @param pos: The position of the node
        @return: True if the node was added successfully, False o.w.
        Note: if the node id already exists the node will not be added"""
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = MyNode(node_id, pos)
        self.nodeSize += 1
        self.mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        Removes a node from the graph.
        @param node_id: The node ID
        @return: True if the node was removed successfully, False o.w.
        Note: if the node id does not exists the function will do nothing
        """
        if node_id not in self.nodes.keys():
            return False
        nodes_keys = ()
        for node in self.nodes.get(node_id).neighbors_out.keys():
            nodes_keys += (node,)
        [self.remove_edge(node_id , node) for node in nodes_keys]
        for node in self.nodes.get(node_id).neighbors_in.keys():
            nodes_keys += (node,)
        [self.remove_edge(node_id, node) for node in nodes_keys]
        del self.nodes[node_id]
        self.mc += 1
        self.nodeSize -= 1
        return True


    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """remove an edge betwenn two nodes"""
        if node_id2 not in self.nodes.get(node_id1).neighbors_out:
            return False
        if node_id1 not in self.nodes or node_id2 not in self.nodes:
            return False
        if node_id2 not in self.nodes.get(node_id1).neighbors_out:
            return False
        del self.nodes[node_id1].neighbors_out[node_id2]
        del self.nodes[node_id2].neighbors_in[node_id1]
        self.mc += 1
        self.edgeSize -= 1
        return True


    def __str__(self) -> str:
        """@return a string (str) representation of the DiGraph"""
        return f"Graph: |V|={self.nodeSize}, |E|={self.edgeSize}"

    def __repr__(self) -> str:
        """@return a string (repr) representation of the DiGraph"""
        return f"{self.nodes}"
