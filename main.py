
import osmnx as ox
from Solver import Solver
from grafo import Graph
from utils.PathUtil import PathUtil
from utils.PlotUtil import PlotUtil


G = ox.graph_from_xml("map.osm")
PF = Solver(G)

grafo_resposta = PF.BFS(8986661911, 482156286)
parent = PF.BFS(8986661911, 482156286, False)

edgesList = PathUtil.getEdgesListFromParentList(
    G, 482156286, parent)

path = PathUtil.getPathFromParentList(G, 482156286, parent)

PlotUtil.drawGraph(grafo_resposta, 8986661911, 482156286, edgesList)

PlotUtil.PlotPathOSM(G, 8986661911, 482156286,
                     path)


# print(grafo_resposta['crs'])
# gdf_nodes, gdf_edges = ox.graph_to_gdfs(grafo_resposta)
# G = ox.graph_from_gdfs(grafo_resposta.nodes, grafo_resposta.edges)
# G.clear()
# G.clear_edges()
# G.add_nodes_from(grafo_resposta.nodes)
# G.add_edges_from(grafo_resposta.edges)
#G.graph['crs'] = 'epsg:4326'
#route = nx.shortest_path(G, 8986661911, 482156286)

# fig, ax = ox.plot_graph_route(
#   G, route, route_linewidth=6, node_size=0, bgcolor='k')

# ox.plot_graph(G)
# PF.BFS(8986661911, 482156286)

# print(G.nodes.data().)
# print(G.out_edges(4751114256))
# print(G.edges(0))
# print(G.graph.keys)
