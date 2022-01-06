
import json

import pygame

from src.DiGraph import DiGraph
from src.MyNode import MyNode
from src.Pokemons import Pokemons
from src.Agent import Agent
from src.GraphAlgo import GraphAlgo
from client_python.client import Client
eps = 0.0000000001
import math

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

clock = pygame.time.Clock()
client = Client()
client.start_connection(HOST,PORT)

class Game:
    def __init__(self):
        self.pokemons_list = []
        self.agents = {}
        self.graph = DiGraph()
        self.alg = GraphAlgo(self.graph)
        self.client = Client()
        self.shortest = []

    def dist_node_to_node(self, node1: MyNode, node2: MyNode):
        dis = math.sqrt(pow(node1.location[0] - node2.location[0],
                            2) + pow(node1.location[1] - node2.location[1], 2))
        return dis

    def dist_pok_to_node(self, node1: MyNode, pok: Pokemons):
        dis = math.sqrt(
            pow(node1.location[0] - pok.pos[0], 2) + pow(node1.location[1] - pok.pos[1], 2))
        return dis

    def pokemon_src_dest(self, pok: Pokemons) -> None:
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
                self.pokemon_src_dest(pok)
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
                self.pokemon_src_dest(p)
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

    def find_node(self, pos: tuple = None):
        node_list = self.graph.nodes.values()
        for n in node_list:
            if n.location[0] == pos[0] and n.location[1] == pos[1]:
                return n

    def find_node_by_edge(self, pok: Pokemons):
        self.pokemon_src_dest(pok)
        node_list = self.graph.nodes.values()
        for n in node_list:
            if n.id == pok.src:
                return n

    # def shortest_path(self, id1: int, id2: int) -> (float, list):
    #     """
    #     Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
    #     @param id1: The start node id
    #     @param id2: The end node id
    #     @return: The distance of the path, a list of the nodes ids that the path goes through"""
    #     """initialize all weights of nodes to infinity"""
    #     dist_weight = {node: math.inf for node in self.graph.nodes.keys()}
    #     """keeping track on the shortest path to the nodes"""
    #     previous_nodes = {id1: -1}
    #     dist_weight[id1] = 0
    #     queue = []
    #     heapq.heappush(queue, (0, id1))
    #     while queue:
    #         current_node = heapq.heappop(queue)[1]
    #         if dist_weight[current_node] == math.inf:
    #             break
    #         """iterating on the neighbors of the current node as pairs (neighbor = id , weight = weight)"""
    #         for neighbour, weight in self.graph.nodes.get(current_node).neighbors_out.items():
    #             alternative_route = dist_weight[current_node] + weight
    #             if alternative_route < dist_weight[neighbour]:
    #                 dist_weight[neighbour] = alternative_route
    #                 previous_nodes[neighbour] = current_node
    #                 """adding to the queue the distance to the neighbor and the neighbor as a pair
    #                 the queue is a priority queue so when it will pop an node, it will pop the node
    #                  with the smallest dist_weight"""
    #                 heapq.heappush(queue, (dist_weight[neighbour], neighbour))
    #             if current_node == id2:
    #                 break
    #     path = []
    #     current_node = id2
    #     if dist_weight[id2] == math.inf:
    #         """there isn't a path from id1 to id2"""
    #         return math.inf, []
    #     while current_node != -1:
    #         path.insert(0, current_node)
    #         """shortest path"""
    #         current_node = previous_nodes[current_node]
    #
    #     return dist_weight[id2], path

    def list_to_go(self):
        dis = math.inf
        res = []
        for age in self.agents.values():
            a_node = self.find_node(age.pos)
            for pok in self.pokemons_list:
                self.pokemon_src_dest(pok)
                p_node = self.find_node_by_edge(pok)
                if self.alg.shortest_path(a_node.id, p_node.id)[0] < dis:
                    dis = self.alg.shortest_path(a_node.id, p_node.id)[0]
                    res = self.alg.shortest_path(a_node.id, p_node.id)[1]

        self.shortest = res

    def next_edge(self, client: Client):
        for agent in self.agents.values():
            if agent.dest == -1:
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.id) + ', "next_node_id":' + str(self.pokemons_list[0]) + '}')


    def dist_time_pok_agent(self, a: Agent, p: Pokemons):
        if a.src == p.src:
            return (0,(0,[]))
        sp = self.alg.shortest_path(a.src, p.src)
        time = (sp[0] / a.speed)
        return (time, sp)

    def allocate_agents(self):
        final_list = []
        for i in self.agents.values():
            temp = []
            for p in self.pokemons_list:
                distance = self.calculate_dist(i, p)
                temp.append((p, distance))
                # (pokemon, (TT, (distance, [path])))
            temp.sort(key=lambda x: x[1][0])
            final_list.append((i.id, temp[0]))
            # ( agent.id, (pokemon, (TT, (distance, [path]))))
        final_list.sort(key=lambda x: x[1][1][0])
        agent_to_pokemon = final_list[0]
        # ( agent.id, (pokemon, (TT, (distance, [path]))))
        agent_path = []
        agent_path.append(final_list[0][1][1][1][1])
        return agent_to_pokemon

    def calculate_dist(self, agent: Agent, pokemon: Pokemons):
        if agent.src == pokemon.src:
            return (0,(0,[]))
        distance = self.alg.shortest_path(agent.src,pokemon.src)
        # distance = self.shortest_path(agent.src, pokemon.src)
        travel_time = (distance[0] / agent.speed)
        return travel_time, distance
        # ( TT, (distance, [path]))



if __name__ == '__main__':
    client.add_agent("{\"id\":0}")
    client.start()
    game = Game()
    game.update(client.get_agents(),client.get_pokemons(),client.get_graph())
    print(game.agents)
    print(game.pokemons_list)
    print(game.graph)
    print(client.get_info())
    print(game.alg.shortest_path(2,5))

    while client.is_running() == 'true':
        for i in game.agents.values():
            game.pokemon_src_dest(game.pokemons_list[0])
            curr_list = game.allocate_agents()[1][1][1][1]
            print(game.allocate_agents())
            curr_list.remove(0)
            clock.tick(60)

            for x in curr_list:
                if i.dest == -1:
                    next_node = x
                    client.choose_next_edge(
                        '{"agent_id":' + str(i.id) + ', "next_node_id":' + str(next_node) + '}')
                print(client.move())
            print(client.get_info())



        # if i.dest == -1:
        #     client.choose_next_edge(
        #         '{"agent_id":' + str(i.id) + ', "next_node_id":' + str(0) + '}')
        # client.move()
        # print(i.src)
        # print(client.get_info())
        # if i.dest == -1:
        #     client.choose_next_edge(
        #         '{"agent_id":' + str(i.id) + ', "next_node_id":' + str(10) + '}')
        # client.move()
        # print(i.src)
        # print(client.get_info())








