
from cmath import inf
from collections import defaultdict

from numpy import Infinity


class Graph(object):

    def __init__(self, grafo):
        self.graph = grafo

        if grafo.edges != None:
            self.edges = list(grafo.edges.data("length"))

        if grafo.nodes != None:
            self.nodes = list(grafo.nodes)

    def getAttributeFromEdge(self, origin, destiny, att):
        return dict(self.graph.get_edge_data(origin, destiny)).get(0)[att]

    def getAttributeFromNode(self, node, att):
        return dict(self.graph.nodes.data()).get(node)[att]
