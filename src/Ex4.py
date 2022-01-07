import json
import time

import pygame


from client import Client
from GUI import *
from Game import *
# default port

PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
clock = pygame.time.Clock()
# client = Client()
game = Game()
game.client.start_connection(HOST,PORT)
game.client.add_agent("{\"id\":0}")
game.update(game.client.get_agents(),game.client.get_pokemons(),game.client.get_graph())
gui = GUI(game,game.client)
game.client.start()


game.pokemon_src_dest(game.pokemons_list[0])

while game.client.is_running() == 'true':
    game.update(game.client.get_agents(),game.client.get_pokemons())
    time.sleep(0.2)
    game.CMD()
    gui.draw()
    print(game.client.move())
print(game.client.get_info())

