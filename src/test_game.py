import unittest

from typing import Tuple

from src.Game import *
from src.MyNode import MyNode



class MyTestCase(unittest.TestCase):
    def test_dist_node_to_node(self):
        game = Game
        a = MyNode(0, (0,5,0))
        b = MyNode(1, (0,0,0))
        dist = 5
        print(game.dist_node_to_node(a,b))
        self.assertEqual(dist ,game.dist_node_to_node(Game,a,b))
#



if __name__ == '__main__':
    unittest.main()
