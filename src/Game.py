import json

from src.DiGraph import DiGraph
from src.MyNode import MyNode
from src.Pokemons import Pokemons
from src.Agent import Agent
from src.GraphAlgo import GraphAlgo
from client_python.client import Client

eps = 0.0000000001
import math


class Game:
    def __init__(self):
        self.pokemons = []
        self.agents = {}
        self.graph = DiGraph()
        self.alg = GraphAlgo(self.graph)
        self.client = Client()

    def distance_two_nodes(self, pos1: tuple = None, pos2: tuple = None):
        return math.sqrt(pow(pos1[0] - pos2[0], 2) +
                         pow(pos1[1] - pos2[1], 2))

    def pok_to_edge(self, p: Pokemons):
        node_list = self.graph.get_all_v()
        for n in node_list:
            edge_list = self.graph.all_out_edges_of_node(n.id)
            for e in edge_list:
                d1 = self.distance_two_nodes(n.pos, self.graph.get_node(e[0]).pos)
                d2 = self.distance_two_nodes(n.pos, p.pos) + self.distance_two_nodes(self.graph.get_node(e[0]).pos,
                                                                                     p.pos)
                if d1 > d2 - eps:
                    return e

    def pokemon_src_dest(self, p: Pokemons) -> None:
        for node1 in self.graph.nodes:
            for node2 in self.graph.nodes:
                d1 = self.distance_two_nodes(self.graph.nodes[node1].pos, self.graph.nodes[node2].pos)
                d2 = (self.distance_two_nodes(self.graph.nodes[node1].pos, p.pos)
                      + self.distance_two_nodes(self.graph.nodes[node2].pos, p.pos))
                if abs(d1 - d2) <= eps:
                    if p.type == -1:
                        p.src = min(node1, node2)
                        p.dest = max(node1, node2)
                    else:
                        p.src = max(node1, node2)
                        p.dest = min(node1, node2)
                    return

    def update(self, agents=None, pokemons=None, graph=None):
        if pokemons != None:
            self.pokemons = []
            pokemons_obj = json.loads(pokemons)
            for poke in pokemons_obj['Pokemons']:
                p = Pokemons(poke['Pokemon'])
                self.pokemon_src_dest(p)
                self.pokemons.append(p)
        if agents != None:
            agents_obj = json.loads(agents)
            for a in agents_obj['Agents']:
                id = int(a['Agent']['id'])
                if not id is self.agents:
                    self.agents[id] = Agent(a['Agent'])
                else:
                    self.agents[id].update(a['Agent'])

        if graph != None:
            self.graph = DiGraph()
            graph_obj = json.loads(graph)
            for node in graph_obj["Nodes"]:
                id = int(node["id"])
                if "pos" in node:
                    posData = node["pos"].split(',')
                    self.graph.add_node(
                        id, (float(posData[0]), float(posData[1]), float(posData[2])))
                else:
                    self.graph.add_node(id)
            for edge in graph_obj["Edges"]:
                self.graph.add_edge(int(edge["src"]), int(
                    edge["dest"]), float(edge["w"]))

        # if pokemons != None:
        #     self.pokemons = []
        #     pokemons_obj = json.loads(pokemons)
        #     for poke in pokemons_obj['Pokemons']:
        #         p = Pokemons(poke['Pokemon'])
        #         self.pokemon_src_dest(p)
        #         self.pokemons.append(p)

    def list_to_go(self):
        dis = math.inf
        res = []
        for age in self.agents:

            for pok in self.pokemons:
                if self.alg.shortest_path(age.src , self.pok_to_edge(pok).src)[0] < dis:
                    dis = self.alg.shortest_path(age.src , self.pok_to_edge(pok).src)[0]
                    res = self.alg.shortest_path(age.src , self.pok_to_edge(pok).src)[1]

        return res






