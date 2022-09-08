
import osmnx as ox
from AppController import AppController
from utils.SolverUtil import Solver

G = ox.graph_from_xml("map.osm")
PF = Solver(G)
AppController.FindPath(G, 8986661911, 482156286, PF.BFS)
AppController.GenerateTreeFromAlgorithm(G, 8986661911, 482156286, PF.BFS)
