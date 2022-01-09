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
# 0 - m138, g79
# 1 - m274, g109
# 2 -m136, g100
# 3 - m273, g104
# 4 - m135, g13
# 5 -m270, g13
# 6 - m137, g40
# 7 - m273, g35
# 8 - m135, g58
# 9 - m266, g201
# 10 - m132, g52
# 11 - m261, g358
# 12 - m133, g26
# 13 - m265 ,g188
# 14 - m131, g94
# 15 - m262, g130