class PathUtil():
    @staticmethod
    def getPathFromParentList(Graph, goal, ParentList):
        path = []
        path.append(goal)
        nodeList = list(Graph.graph.nodes)
        node = ParentList[nodeList.index(goal)]
        while node != '':
            path.append(node)
            node = ParentList[nodeList.index(node)]
        return path

    @staticmethod
    def getEdgesListFromParentList(Graph, goal, ParentList):
        edgeList = []
        nodeList = list(Graph.nodes)
        edgeList.append((ParentList[nodeList.index(goal)], goal))
        node = ParentList[nodeList.index(goal)]
        while node != '':
            edgeList.append((ParentList[nodeList.index(node)], node))
            node = ParentList[nodeList.index(node)]
        return edgeList
