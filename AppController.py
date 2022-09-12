from utils.PathUtil import PathUtil
from utils.PlotUtil import PlotUtil
from utils.SolverUtil import Solver


class AppController():

    def plotMap(Graph):
        PlotUtil.plotOSM(Graph)

    def FindPath(Graph, origin, goal, algorithm):
        path = algorithm(origin, goal)
        print(path)
        PlotUtil.PlotPathOSM(Graph, origin, goal, path)

    def GenerateTreeFromAlgorithm(Graph, origin, goal, algorithm):
        parent = algorithm(origin, goal, False)
        grafo_resposta = algorithm(origin, goal)
        edgesList = PathUtil.getEdgesListFromParentList(
            Graph, goal, parent)
        PlotUtil.plotMapWithPath(
            grafo_resposta, origin, goal, edgesList)
