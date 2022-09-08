import networkx as nx
import osmnx as ox
import matplotlib.pyplot as plt

import random


class PlotUtil():
    @staticmethod
    def drawGraph(Graph, origin, goal, path):

        color_map = ['red' if (node ==
                     origin or node ==
                     goal) else 'green' for node in Graph.nodes]

        edge_map = ['red' if ((origin, destiny) in
                              path) else 'green' for origin, destiny, weight in Graph.edges]

        nx.draw_networkx(Graph, hierarchy_pos(Graph, origin),
                         node_color=color_map, edge_color=edge_map)  # node lable
        plt.show()

    @staticmethod
    # mudar caminho para path quando for colocar o grafo para aparecer
    def PlotPathOSM(Graph, origin, goal, path):
        caminho = nx.shortest_path(Graph, origin, goal)
        ox.plot_graph_route(
            Graph, caminho, route_linewidth=6, node_size=0, bgcolor='k')


def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):

    if not nx.is_tree(G):
        raise TypeError(
            'cannot use hierarchy_pos on a graph that is not a tree')

    if root is None:
        if isinstance(G, nx.DiGraph):
            # allows back compatibility with nx version 1.11
            root = next(iter(nx.topological_sort(G)))
        else:
            root = random.choice(list(G.nodes))

    def _hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5, pos=None, parent=None):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if not isinstance(G, nx.DiGraph) and parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width/len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, width=dx, vert_gap=vert_gap,
                                     vert_loc=vert_loc-vert_gap, xcenter=nextx,
                                     pos=pos, parent=root)
        return pos

    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)
