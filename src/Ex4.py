from GUI import *
from Game import *
# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
clock = pygame.time.Clock()
game = Game()
game.client.start_connection(HOST,PORT)
game.addAgents()
game.update(game.client.get_agents(),game.client.get_pokemons(),game.client.get_graph())
gui = GUI(game,game.client)
game.client.start()
while game.client.is_running() == 'true':
    game.update(game.client.get_agents(),game.client.get_pokemons())
    time.sleep(0.2)
    game.CMD()
    gui.draw()
    print(game.client.move())
    print(game.client.get_info())



# work - cases
# 0 - work - 79
# 8 - m133, g52
# 9 - m266, g201
# 10 - m132, g52
# 11 - m261, g358
# 12 - m133, g26
# 13 - m265 ,g188
# 14 - m131, g94
# 15 - m262, g130