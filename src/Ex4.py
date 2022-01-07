import json


from client import Client
from time import sleep
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
game.addAgents()
game.update(game.client.get_agents(),game.client.get_pokemons(),game.client.get_graph())
game.pokemon_src_dest(game.pokemons_list[0])
x = game.pokemons_list[0].dest
print(x)
y = str(x)
gui = GUI(game,game.client)
game.client.start()


# game.pokemon_src_dest(game.pokemons_list[0])

while game.client.is_running() == 'true':
    game.update(game.client.get_agents(),game.client.get_pokemons())
    time.sleep(0.1)
    game.CMD()
    gui.draw()
    print(game.client.move())
    print(game.client.get_info())



# work - cases
# 0 - work - 79
# 1 -