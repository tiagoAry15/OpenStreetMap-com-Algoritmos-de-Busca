import json


class JsonUtil:
    @staticmethod
    def buildJSONPath(Graph, path):
        if path != []:
            response = []
            for node in path:
                nodeObject = dict()
                nodeCoords = Graph.nodes.get(node)
                nodeObject.update({"id": node})
                nodeObject.update({"x": nodeCoords['x']})
                nodeObject.update({"y": nodeCoords['y']})
                response.append(nodeObject)
            return response
