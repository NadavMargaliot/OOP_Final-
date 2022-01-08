import time
import pygame
from client import Client
from src.MyNode import MyNode
from src.Pokemons import Pokemons
from src.Agent import Agent
from src.GraphAlgo import *
eps = 0.0000000001
import math
class Game:
    def __init__(self):
        self.pokemons_list = []
        self.agents = {}
        self.graph = DiGraph()
        self.alg = GraphAlgo(self.graph)
        self.client = Client()

    def dist_node_to_node(self, node1: MyNode, node2: MyNode):
        dis = math.sqrt(pow(node1.location[0] - node2.location[0],
                            2) + pow(node1.location[1] - node2.location[1], 2))
        return dis

    def dist_pok_to_node(self, node1: MyNode, pok: Pokemons):
        dis = math.sqrt(
            pow(node1.location[0] - pok.pos[0], 2) + pow(node1.location[1] - pok.pos[1], 2))
        return dis

    def find_src_dest_pok(self, pok: Pokemons) -> None:
        for node1 in self.graph.nodes:
            for node2 in self.graph.nodes:
                dis1 = self.dist_node_to_node(
                    self.graph.nodes[node1], self.graph.nodes[node2])
                dis2 = (self.dist_pok_to_node(
                    self.graph.nodes[node1], pok) + self.dist_pok_to_node(self.graph.nodes[node2], pok))
                if abs(dis1 - dis2) <= eps:
                    if pok.type == -1:
                        pok.src = min(node1, node2)
                        pok.dest = max(node1, node2)
                    else:
                        pok.src = max(node1, node2)
                        pok.dest = min(node1, node2)
                    return

    def update_pokemons_agents(self, pokemons=None, agents=None):
        if agents != None:
            agents_obj = json.loads(agents)
            for a in agents_obj['Agents']:
                id = int(a['Agent']['id'])
                self.agents[id] = Agent(a['Agent'])
        if pokemons != None:
            self.pokemons_list = []
            pokemons_obj = json.loads(pokemons)
            for p in pokemons_obj['Pokemons']:
                pok = Pokemons(p['Pokemon'])
                self.find_src_dest_pok(pok)
                self.pokemons_list.append(pok)

    def update(self, agents=None, pokemons=None, graph=None):
        if agents != None:
            agents_obj = json.loads(agents)
            for a in agents_obj['Agents']:
                id = int(a['Agent']['id'])
                if not id is self.agents:
                    self.agents[id] = Agent(a['Agent'])
                else:
                    self.agents[id].update(a['Agent'])

        if pokemons != None:
            self.pokemons_list = []
            pokemons_obj = json.loads(pokemons)
            for poke in pokemons_obj['Pokemons']:
                p = Pokemons(poke['Pokemon'])
                self.find_src_dest_pok(p)
                self.pokemons_list.append(p)

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
        self.alg.__init__(self.graph)
    # Given a position find the src node
    def find_node(self, pos: tuple = None):
        node_list = self.graph.nodes.values()
        for n in node_list:
            if n.location[0] == pos[0] and n.location[1] == pos[1]:
                return n

    # Given a position on the edge find the src node
    def find_node_by_edge(self, pok: Pokemons):
        self.find_src_dest_pok(pok)
        node_list = self.graph.nodes.values()
        for n in node_list:
            if n.id == pok.src:
                return n


    def allocate_agents(self):
        pok = []
        final_list = []
        for i in self.agents.values():
            temp = []
            for p in self.pokemons_list:
                if p not in pok:
                    distance = self.time_and_shortest(i, p)
                    temp.append((p, distance))
                # (pokemon, (TT, (distance, [path])))
            temp.sort(key=lambda x: x[1][0])
            pok.append(temp)
            final_list.append((i.id, temp[0]))
            # ( agent.id, (pokemon, (TT, (distance, [path]))))     # ( agent.id, (pokemon, (TT, (distance, [path]))))
        final_list.sort(key=lambda x: x[1][1][0])
        final_path = {}
        for i in self.agents.keys():
            for element in final_list:
                if (i == element[0]):
                    final_path[i] = element[1][1][1][1]
        return final_path


    def time_and_shortest(self, agent: Agent, pokemon: Pokemons):
        if agent.src == pokemon.src:
            return 0,(0,[pokemon.dest])
        distance = self.alg.shortest_path(agent.src,pokemon.src)
        travel_time = (distance[0] / agent.speed)
        return travel_time, distance
        # ( TT, (distance, [path]))

    def CMD(self):
        id_path = self.allocate_agents()
        for i in self.agents.keys():
            if self.agents.get(i).dest == -1:
                if len(id_path[i]) > 1:
                    self.client.choose_next_edge(
                        '{"agent_id":%s, "next_node_id":%s}' % (i, id_path[i][1]))
                else:
                    self.client.choose_next_edge(
                        '{"agent_id":%s, "next_node_id":%s}' % (
                            i, id_path[i][0]))


    def addAgents(self):
        size = int(json.loads(self.client.get_info())["GameServer"]["agents"])
        # nodes = []
        # for p in self.pokemons_list:
        #     p_node = self.find_node_by_edge(p)
        #     nodes.append(p_node)
        for i in range(size):
            # i_node = nodes[0]
            # if len(nodes) > 1:
            #     nodes.remove(0)
            self.client.add_agent("{\"id\":" + str(i) + "}")











