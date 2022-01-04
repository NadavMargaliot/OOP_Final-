import heapq
import json
import random
import sys
from itertools import permutations
from typing import List
from numpy import inf
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
        :return the directed graph on which the algorithm works on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
        """
        try:
            self.graph = DiGraph()
            f = open(file_name, 'r')
            curr_graph = json.load(f)
            edges_dict = curr_graph.get('Edges')
            nodes_dict = curr_graph.get('Nodes')

            for node in nodes_dict:
                if node.get('pos') is not None:
                    pos_node = node['pos']
                    pos_list = pos_node.split(',')
                    id_node = node.get('id')
                    self.graph.add_node(node_id=id_node, pos=(float(pos_list[0]), float(pos_list[1]),
                                                              float(pos_list[2])))
                else:
                    x = random.uniform(0, 100)
                    y = random.uniform(0, 100)
                    id_node = int(node.get('id'))
                    self.graph.add_node(id_node, (x, y, 0))

            for edge in edges_dict:
                weight = edge.get('w')
                src = edge.get('src')
                dest = edge.get('dest')
                self.graph.add_edge(src, dest, weight)
            f.close()
        except FileExistsError:
            return False
        return True

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        if self.graph is None:
            return False
        nodes = []
        edges = []
        """saving the nodes to nodes[]"""
        for node in self.graph.nodes:
            id = node
            pos_node = self.graph.nodes.get(node).location
            pos_node_string = "{},{},{}"
            pos_node_string = pos_node_string.format(pos_node[0], pos_node[1], pos_node[2])
            nodes.append({"id": id, "pos": pos_node_string})
        """saving the edges to edges[]"""
        for src in self.graph.nodes:
            for dest in self.graph.get_node(src).neighbors_out:
                weight = self.graph.get_node(src).neighbors_out[dest]
                edges.append({"src": src, "dest": dest, "w": weight})

        curr_graph = {"Nodes": nodes, "Edges": edges}
        with open(file_name, 'w') as json_file:
            json.dump(curr_graph, json_file)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through"""
        """initialize all weights of nodes to infinity"""
        dist_weight = {node: inf for node in self.graph.nodes.keys()}
        """keeping track on the shortest path to the nodes"""
        previous_nodes = {id1: -1}
        dist_weight[id1] = 0
        queue = []
        heapq.heappush(queue, (0, id1))
        while queue:
            current_node = heapq.heappop(queue)[1]
            if dist_weight[current_node] == inf:
                break
            """iterating on the neighbors of the current node as pairs (neighbor = id , weight = weight)"""
            for neighbour, weight in self.graph.nodes.get(current_node).neighbors_out.items():
                alternative_route = dist_weight[current_node] + weight
                if alternative_route < dist_weight[neighbour]:
                    dist_weight[neighbour] = alternative_route
                    previous_nodes[neighbour] = current_node
                    """adding to the queue the distance to the neighbor and the neighbor as a pair
                    the queue is a priority queue so when it will pop an node, it will pop the node
                     with the smallest dist_weight"""
                    heapq.heappush(queue, (dist_weight[neighbour], neighbour))
                if current_node == id2:
                    break
        path = []
        current_node = id2
        if dist_weight[id2] == inf:
            """there isn't a path from id1 to id2"""
            return inf, []
        while current_node != -1:
            path.insert(0, current_node)
            """shortest path"""
            current_node = previous_nodes[current_node]

        return dist_weight[id2], path

    def tsp_helper(self, start_node, node_list):
        best_path = []
        path = []
        temp_list = []
        for node_i in node_list:
            if node_i != start_node:
                temp_list.append(node_i)
        min_weight = sys.maxsize
        permu = permutations(temp_list)

        for curr_permutation in permu:
            path.clear()
            relevant = True
            curr_weight = 0
            k = start_node
            path.append(k)
            for node_j in curr_permutation:
                weight = self.shortest_path(k, node_j)[0]
                for n in range(len(self.shortest_path(k, node_j)[1])):
                    if n != 0:
                        path.append(self.shortest_path(k, node_j)[1][n])
                if weight == float('inf'):
                    relevant = False
                    break
                curr_weight += weight
                k = node_j
            if relevant:
                if min_weight > curr_weight:
                    min_weight = curr_weight
                    best_path = path
        return best_path, min_weight

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """
        best_weight = sys.maxsize
        for starting_n in node_lst:
            if self.tsp_helper(starting_n, node_lst)[1] < best_weight:
                best_weight = self.tsp_helper(starting_n, node_lst)[1]
                best_path, weight = self.tsp_helper(starting_n, node_lst)
        if best_weight == sys.maxsize:
            return [], float('inf')
        return best_path, weight

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """
        if self.graph.nodeSize == 0:
            return None, None
        result_min_distance = inf
        result_id = 0
        curr_max = 0
        for node1 in self.graph.nodes.values():
            for node2 in self.graph.nodes.values():
                distance = self.shortest_path(node1.id, node2.id)[0]
                if distance > curr_max:
                    curr_max = distance
            if curr_max < result_min_distance:
                result_min_distance = curr_max
                result_id = node1.id
            curr_max = 0
        result = (result_id, result_min_distance)
        return result

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """
        for node in self.graph.nodes.values():
            if node.location is None:
                location1 = (random.uniform(0, 100), random.uniform(0, 100), 0.0)
                node.setLocation(location1)
            x1, y1, z1 = node.location
            plt.plot(x1, y1, markersize=15, marker='.', color='orange')
            plt.text(x1, y1, str(node.id), color='blue', fontsize=10)
            for dest_id, w in self.graph.all_out_edges_of_node(node.id).items():
                dest = self.graph.get_node(dest_id)
                if dest.location is None:
                    location2 = (random.uniform(0, 100), random.uniform(0, 100), 0.0)
                    dest.setLocation(location2)
                x2, y2, z2 = dest.location
                plt.annotate("", xy=(x1, y1), xytext=(x2, y2), arrowprops=dict(arrowstyle="<|-"))
        plt.show()
