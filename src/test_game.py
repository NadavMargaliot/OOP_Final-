import unittest

from typing import Tuple

from src.Game import *
from src.MyNode import MyNode


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'
# initializing the Client
client = Client()
client.start_connection(HOST, PORT)
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")
client.start()
# initializing the game
game = Game()



class MyTestCase(unittest.TestCase):
    def test_update(self):
        # for case 1
        game.update( client.get_agents(), client.get_pokemons(), client.get_graph())
        self.assertEqual(1, len(game.agents))
        self.assertEqual(2, len(game.pokemons_list))
        self.assertIsNotNone(game.alg.get_graph())

    def test_find_src_dest_pok(self):
        game.update( client.get_agents(), client.get_pokemons(), client.get_graph())
        self.assertEqual(game.pokemons_list[0].src, None)
        self.assertEqual(game.pokemons_list[0].dest, None)
        game.update(client.get_pokemons(), client.get_agents())
        self.assertEqual(game.pokemons_list[0].src, 9)
        self.assertEqual(game.pokemons_list[0].dest, 8)



#



if __name__ == '__main__':
    unittest.main()
