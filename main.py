
import osmnx as ox
from AppController import AppController
from utils.SolverUtil import Solver

G = ox.graph_from_xml("map.osm")
PF = Solver(G)

# AppController.plotMap(G)
AppController.FindPath(G, 8986661911, 253406715, PF.Aestrela)
#AppController.GenerateTreeFromAlgorithm(G, 8986661911, 265021150, PF.BFS)
