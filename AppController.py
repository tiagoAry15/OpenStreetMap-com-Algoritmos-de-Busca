from utils.PathUtil import PathUtil
from utils.PlotUtil import PlotUtil
from utils.SolverUtil import Solver


class AppController():

    def FindPath(Graph, origin, goal, algorithm):

        PF = Solver(Graph)
        parent = algorithm(origin, goal, False)
        path = PathUtil.getPathFromParentList(Graph, 482156286, parent)
        PlotUtil.PlotPathOSM(Graph, origin, goal, path)

    def GenerateTreeFromAlgorithm(Graph, origin, goal, algorithm):
        PF = Solver(Graph)
        parent = algorithm(origin, goal, False)
        grafo_resposta = PF.BFS(origin, goal)
        edgesList = PathUtil.getEdgesListFromParentList(
            Graph, 482156286, parent)
        PlotUtil.drawGraph(grafo_resposta, 8986661911, 482156286, edgesList)
