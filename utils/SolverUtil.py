import networkx as nx
from grafo import Graph

from utils.PathUtil import PathUtil


class Solver():

    def __init__(self, grafo):
        self.graph = Graph(grafo)

    def BFS(self, origin, goal, returnTreeInsteadPath=True):
        stack = []
        noAtual = origin
        distance = 0
        parent = [""]*(len(self.graph.nodes))
        G = nx.MultiDiGraph()
        G.add_node(origin)
        G.add_node(goal)
        while(noAtual != goal):
            adjacent = self.graph.graph.out_edges(noAtual)
            if adjacent != None:
                for o, d, in adjacent:
                    stack.append(d)
                    G.add_node(d)
                    G.add_edge(o, d)
                    parent[self.graph.nodes.index(d)] = o
                    distance += self.graph.getAttributeFromEdge(o, d, 'length')
            noAtual = stack[0]
            stack.remove(stack[0])
        print("from node: ", origin, " to node: ",
              goal, " the distance is: ", distance)

        if returnTreeInsteadPath == True:
            return G
        else:
            return parent
