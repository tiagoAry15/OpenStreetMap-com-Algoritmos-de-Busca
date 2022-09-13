
import osmnx as ox
from AppController import AppController
from utils.JsonUtil import JsonUtil
from utils.SolverUtil import Solver

G = ox.graph_from_xml("map.osm")
PF = Solver(G)
print(G.nodes.get(253406715))
# AppController.plotMap(G)
#path = AppController.FindPath(G, 8986661911, 253406715, PF.Aestrela)
#JsonUtil.buildJSONPath(G, path)
#AppController.GenerateTreeFromAlgorithm(G, 8986661911, 265021150, PF.BFS)
