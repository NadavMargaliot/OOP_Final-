import pygame
from pygame import *
from pygame import gfxdraw

from client_python.client import Client
from src.Game import Game
WIDTH, HEIGHT = 1080, 720
radius = 15
background = "/Users/adielbenmeir/Desktop/pics_Ex4/battle_field.jpeg"
pokeball = "/Users/adielbenmeir/Desktop/pics_Ex4/pokeball2.png"
bulbasaur = "/Users/adielbenmeir/Desktop/pics_Ex4/bulbasaur.png"
pygame.init()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
pokeball_image = image.load(pokeball)
pokeball_image = pygame.transform.scale(pokeball_image, (50, 50))
bulbasaur_image = image.load(bulbasaur)
bulbasaur_image = pygame.transform.scale(bulbasaur_image, (50, 50))
background_img = image.load(background)

class GUI():
    def __init__(self, game:Game , client:Client):
        self.client = Client
        self.game = game
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
        self.min_x = float('inf')
        self.max_x = float('inf')
        self.min_y = float('inf')
        self.max_y = float('inf')
        for node in self.game.graph.nodes.values():
            x = node.location[0]
            y = node.location[1]
            self.min_x = min(self.min_x,x)
            self.min_y = min(self.min_y,y)
            self.max_x = max(self.max_x,x)
            self.max_y = max(self.max_y,y)

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height()-50, self.min_y, self.max_y)

    def drawNode(self):
        graph = self.game.graph
        for n in graph.nodes.values():
            x = self.my_scale(n.location[0], x=True)
            y = self.my_scale(n.location[1], y=True)
            gfxdraw.filled_circle(self.screen, int(x), int(y),
                                  radius, Color(64, 80, 174))
            gfxdraw.aacircle(self.screen, int(x), int(y),
                             radius, Color(255, 255, 255))

            # draw the node id
            id_srf = FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            self.screen.blit(id_srf, rect)

    def drawEdges(self):
        graph = self.game.graph
        for node in graph.get_all_v().values():
            for e in graph.get_node(graph.all_out_edges_of_node(node.id)):
                src = graph.nodes[e[0]]
                dest = graph.nodes[e[1]]
                src_x = self.my_scale(src.location[0], x=True) + radius / 2
                src_y = self.my_scale(src.location[1], y=True) + radius / 2
                dest_x = self.my_scale(dest.location[0], x=True) + radius / 2
                dest_y = self.my_scale(dest.location[1], y=True) + radius / 2
                pygame.draw.line(self.screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y), 5)

    def drawPokemons(self):
        pokemons = self.game.pokemons_list
        for pok in pokemons:
            x = self.my_scale(pok.pos[0], x=True)
            y = self.my_scale(pok.pos[1], y=True)
            self.screen.blit(bulbasaur_image, (x,y))

    def drawAgents(self):
        agents = self.game.agents.values()
        for agent in agents:
            x = self.my_scale(agent.pos[0], x=True) - radius / 2
            y = self.my_scale(agent.pos[1], y=True) - radius / 2

            self.screen.blit(pokeball_image, (x, y))

    def draw(self) -> bool:
        background_image = transform.scale(background_img, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background_image, [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
                return False
        self.drawEdges()
        self.drawNode()
        self.drawPokemons()
        self.drawAgents()
        display.update()
        return True
