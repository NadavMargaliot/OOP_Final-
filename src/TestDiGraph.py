import unittest
from MyNode import MyNode
from DiGraph import DiGraph


class MyTestCase(unittest.TestCase):
    # v1 = MyNode
    # v2 = MyNode
    # v3 = MyNode
    # graph = DiGraph
    # graph.add_edge(v1.id, v2.id, 3)
    # graph.add_edge(v2.id,v3.id,4)

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_v_size(self):
        v1 = MyNode(1,None)
        v2 = MyNode(2,None)
        v3 = MyNode(3,None)
        graph = DiGraph()
        self.assertEqual(0 , graph.v_size())
        graph.add_node(v1.id , v1.location)
        self.assertEqual(1, graph.v_size())
        graph.add_node(v2.id, v2.location)
        graph.add_node(v3.id, v3.location)
        self.assertEqual(3 , graph.v_size())
        self.assertEqual(graph.nodeSize , graph.v_size())

    def test_e_size(self):
        """This test includes:
        e_size
        v_size
        add_edge
        remove_edge"""
        v1 = MyNode(1, None)
        v2 = MyNode(2, None)
        v3 = MyNode(3, None)
        graph = DiGraph()
        self.assertEqual(0 , graph.e_size())
        graph.add_node(v1.id, v1.location)
        graph.add_node(v2.id, v2.location)
        graph.add_node(v3.id, v3.location)
        graph.add_edge(1 , 2 , 4)
        self.assertEqual(1, graph.e_size())
        graph.add_edge(1, 3, 5)
        self.assertEqual(2, graph.e_size())
        graph.add_edge(1, 3, 3)
        self.assertEqual(2, graph.e_size())
        graph.add_edge(1, 3, 2)
        self.assertEqual(2, graph.e_size())
        graph.remove_edge(1,3)
        self.assertEqual(1, graph.e_size())
        graph.remove_edge(1, 3)
        self.assertEqual(1, graph.e_size())
        graph.remove_edge(2,1)
        self.assertEqual(1, graph.e_size())
        graph.remove_edge(1,2)
        self.assertEqual(0, graph.e_size())

    def test_remove_node(self):
        v1 = MyNode(1, None)
        v2 = MyNode(2, None)
        v3 = MyNode(3, None)
        graph = DiGraph()
        graph.add_node(v1.id, v1.location)
        graph.add_node(v2.id, v2.location)
        graph.add_node(v3.id, v3.location)
        graph.add_edge(1, 2, 4)
        graph.add_edge(1, 3, 5)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(2, graph.e_size())
        graph.remove_node(1)
        self.assertEqual(2, graph.v_size())
        self.assertEqual(0, graph.e_size())












if __name__ == '__main__':
    v1 = MyNode
    v2 = MyNode
    v3 = MyNode
    graph = DiGraph
    print(graph)


    unittest.main()
