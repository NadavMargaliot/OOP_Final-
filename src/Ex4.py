import json

from client_python.client import Client
from src.GUI import GUI
from src.Game import Game


# default port

PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
client = Client()
client.start_connection(HOST,PORT)

game = Game()

client.add_agent("{\"id\":0}")

game.update(client.get_pokemons(),client.get_agents(),client.get_graph())
gui = GUI(game,client)
client.start()
while client.is_running() == 'true':
    game.update(client.get_pokemons(), client.get_agents())
    game.CMD()
    gui.draw()


