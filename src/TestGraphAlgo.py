import unittest

from src.DiGraph import DiGraph
from src.MyNode import MyNode
from GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
    A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
    A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
    A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
    A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
    A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
    T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"


    def test_save_to_json(self):
        A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
        A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"
        alg1 = GraphAlgo()
        alg1.load_from_json(A1)
        alg1.save_to_json("cheking")


    def test_load_from_json(self):
        A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
        A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"
        alg1 = GraphAlgo()
        alg1.load_from_json(A0)
        self.assertEqual(11 , alg1.graph.nodeSize)
        alg1.load_from_json(A1)
        self.assertEqual(17, alg1.graph.nodeSize)




    def test_shortest_path(self):
        alg1 = GraphAlgo()
        A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
        A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"
        alg1.load_from_json(A1)
        alg1.shortest_path(1, 9)
        graph = DiGraph()
        a = MyNode(1, None)
        b = MyNode(2, None)
        c = MyNode(3, None)
        d = MyNode(4, None)
        e = MyNode(5, None)
        f = MyNode(6, None)
        g = MyNode(7, None)
        graph.add_node(a.id, a.location)
        graph.add_node(b.id, b.location)
        graph.add_node(c.id, c.location)
        graph.add_node(d.id, d.location)
        graph.add_node(e.id, e.location)
        graph.add_node(f.id, f.location)
        graph.add_node(g.id, g.location)
        graph.add_edge(a.id, c.id, 3)
        graph.add_edge(a.id, f.id, 2)
        graph.add_edge(f.id, c.id, 2)
        graph.add_edge(c.id, d.id, 4)
        graph.add_edge(c.id, e.id, 1)
        graph.add_edge(f.id, e.id, 3)
        graph.add_edge(e.id, b.id, 2)
        graph.add_edge(f.id, b.id, 6)
        graph.add_edge(f.id, g.id, 5)
        graph.add_edge(g.id, b.id, 2)
        graph.add_edge(d.id, b.id, 1)
        alg = GraphAlgo(graph)
        self.assertEqual((6, [1, 3, 5, 2]), alg.shortest_path(a.id, b.id))
        # print(alg.shortest_path(a.id,b.id))

    def test_TSP(self):
        alg1 = GraphAlgo()
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        A7 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A7_1000.json"
        A8 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A8_10000.json"
        alg1.load_from_json(A5)
        alg1.TSP([1,4,6,8,16])


    def test_centerPoint(self):
        alg1 = GraphAlgo()
        A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
        A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"
        alg1.load_from_json(A0)
        self.assertEqual(7 , alg1.centerPoint()[0])
        alg1.load_from_json(A1)
        self.assertEqual(8, alg1.centerPoint()[0])
        alg1.load_from_json(A2)
        self.assertEqual(0, alg1.centerPoint()[0])
        alg1.load_from_json(A3)
        self.assertEqual(2, alg1.centerPoint()[0])
        alg1.load_from_json(A4)
        self.assertEqual(6, alg1.centerPoint()[0])
        alg1.load_from_json(A5)
        self.assertEqual(40, alg1.centerPoint()[0])
        alg1.centerPoint()

    def test_plot_graph(self):
        g = DiGraph()
        alg1 = GraphAlgo(g)
        A0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A0.json"
        A1 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A1.json"
        A2 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A2.json"
        A3 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A3.json"
        A4 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A4.json"
        A5 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/A5.json"
        T0 = "/Users/adielbenmeir/PycharmProjects/Ex3_Directed_Graph_Algo/data/T0.json"
        alg1.load_from_json(T0)
        alg1.plot_graph()

        graph = DiGraph()
        a = MyNode(1, None)
        b = MyNode(2, None)
        c = MyNode(3, None)
        d = MyNode(4, None)
        e = MyNode(5, None)
        f = MyNode(6, None)
        g = MyNode(7, None)
        graph.add_node(a.id, a.location)
        graph.add_node(b.id, b.location)
        graph.add_node(c.id, c.location)
        graph.add_node(d.id, d.location)
        graph.add_node(e.id, e.location)
        graph.add_node(f.id, f.location)
        graph.add_node(g.id, g.location)
        graph.add_edge(a.id, c.id, 3)
        graph.add_edge(a.id, f.id, 2)
        graph.add_edge(f.id, c.id, 2)
        graph.add_edge(c.id, d.id, 4)
        graph.add_edge(c.id, e.id, 1)
        graph.add_edge(f.id, e.id, 3)
        graph.add_edge(e.id, b.id, 2)
        graph.add_edge(f.id, b.id, 6)
        graph.add_edge(f.id, g.id, 5)
        graph.add_edge(g.id, b.id, 2)
        graph.add_edge(d.id, b.id, 1)
        alg = GraphAlgo(graph)
    #    alg.plot_graph()


if __name__ == '__main__':
    unittest.main()
