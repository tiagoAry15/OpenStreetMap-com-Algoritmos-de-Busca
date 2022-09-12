from dis import dis
from queue import PriorityQueue
from turtle import st
import networkx as nx
from grafo import Graph

from utils.PathUtil import PathUtil


class Solver():

    def __init__(self, grafo):
        self.graph = Graph(grafo)

    def BFS(self, origin, goal):
        stack = []
        noAtual = origin
        distance = 0
        totalNodes = len(self.graph.nodes)
        parent = [""]*(totalNodes)
        visited = [False]*(totalNodes)
        stack.append(noAtual)
        while noAtual != goal and stack:
            noAtual = stack.pop(0)
            adjacent = self.graph.graph.out_edges(noAtual)
            if len(list(adjacent)) != 0:
                for o, d, in adjacent:
                    if visited[self.graph.nodes.index(d)] == False:
                        visited[self.graph.nodes.index(noAtual)] = True
                        stack.append(d)
                        parent[self.graph.nodes.index(d)] = o

        print("from node: ", origin, " to node: ",
              goal, " the distance is: ", distance)

        return PathUtil.getPathFromParentList(self.graph, d, parent)

    def DFS(self, origin, goal):
        stack = []
        noAtual = origin
        totalNodes = len(self.graph.nodes)
        distance = 0
        visited = [False]*(totalNodes)
        parent = [""]*(totalNodes)
        stack.append(noAtual)
        while noAtual != goal and stack:
            noAtual = stack.pop()
            if visited[self.graph.nodes.index(noAtual)] == False:
                visited[self.graph.nodes.index(noAtual)] = True
                adjacent = list(self.graph.graph.out_edges(noAtual))
                if adjacent != []:
                    for o, d, in adjacent:
                        if visited[self.graph.nodes.index(d)] == False:
                            stack.append(d)
                            parent[self.graph.nodes.index(d)] = o
                            distance += self.graph.getAttributeFromEdge(
                                o, d, 'length')

        print("from node: ", origin, " to node: ",
              goal, " the distance is: ", distance)

        return PathUtil.getPathFromParentList(self.graph, d, parent)

    def buscaCustoUniforme(self, origin, goal):
        totalNodes = len(self.graph.nodes)
        distance = 0
        visited = [False]*(totalNodes)
        D = {v: float('inf') for v in range(totalNodes)}
        D[self.graph.nodes.index(origin)] = 0
        paths = [[origin]] * totalNodes
        listaP = PriorityQueue()
        listaP.put((0, origin))
        while not listaP.empty():
            (dist, noAtual) = listaP.get()
            visited[self.graph.nodes.index(noAtual)] = True
            adjacent = self.graph.graph.out_edges(noAtual)
            for o, d, in adjacent:
                caminho = []
                caminho.append(d)
                distance = self.graph.getAttributeFromEdge(
                    o, d, 'length')
                if visited[self.graph.nodes.index(d)] == False:

                    custo_anterior = D[self.graph.nodes.index(d)]
                    novo_custo = D[self.graph.nodes.index(noAtual)] + distance
                    novo_caminho = paths[self.graph.nodes.index(
                        noAtual)] + caminho
                    if novo_custo < custo_anterior and novo_custo < D[self.graph.nodes.index(d)]:
                        paths[self.graph.nodes.index(d)] = novo_caminho
                        listaP.put((novo_custo, d))
                        D[self.graph.nodes.index(d)] = novo_custo

        path = ''
        if D[self.graph.nodes.index(goal)] != path:
            path = paths[self.graph.nodes.index(goal)]
            print(path)
        return path

    def BestFirst(self, origin, goal):
        noAtual = ''
        totalNodes = len(self.graph.nodes)
        parent = [""]*(totalNodes)
        visited = [False]*(totalNodes)
        listaP = PriorityQueue()
        listaP.put((0, origin))
        while listaP.empty() == False:
            (dist, noAtual) = listaP.get()
            if noAtual == goal:
                break
            adjacent = self.graph.graph.out_edges(noAtual)
            if len(list(adjacent)) != 0:
                for o, d, in adjacent:
                    if visited[self.graph.nodes.index(d)] == False:
                        visited[self.graph.nodes.index(noAtual)] = True
                        cost = self.graph.getAttributeFromEdge(
                            o, d, 'length')
                        listaP.put(cost, d)
                        parent[self.graph.nodes.index(d)] = o
        return PathUtil.getPathFromParentList(self.graph, d, parent)

    def HillClimbing(self, origin, goal):
        totalNodes = len(self.graph.nodes)
        parent = [""]*(totalNodes)
        listaP = PriorityQueue()
        listaP.put((0, origin))
        while listaP.empty() == False:
            (dist, noAtual) = listaP.get()
            if noAtual == goal:
                break
            adjacent = list(self.graph.graph.out_edges(noAtual))
            if list != []:
                bestChoice = (10**8, noAtual)
                for o, d, in adjacent:
                    distance = self.graph.getAttributeFromEdge(
                        o, d, 'length')
                    if distance < bestChoice[0]:
                        bestChoice = (distance, d)
                        parent[self.graph.nodes.index(d)] = o
                listaP.put(bestChoice)
        return PathUtil.getPathFromParentList(self.graph, d, parent)
