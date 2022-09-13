
from flask import Flask, jsonify, request
import osmnx as ox
from AppController import AppController
from utils.JsonUtil import JsonUtil
from utils.SolverUtil import Solver
app = Flask(__name__)

G = ox.graph_from_xml("map.osm")
PF = Solver(G)
algorithms = [PF.BFS, PF.DFS, PF.buscaCustoUniforme,
              PF.BestFirst, PF.HillClimbing, PF.Aestrela]


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/rota/<num>', methods=['GET', 'POST'])
def getPath(num):
    req = request.get_json()
    origem = (req['origem']['x'], req['origem']['y'])
    destino = (req['destino']['x'], req['destino']['y'])
    for node in G.nodes:
        id = node
        no = G.nodes.get(node)
        no = (no['x'], no['y'])
        if origem == no:
            origem = id
        if destino == no:
            destino = id
    num = int(num)
    algorithms[num]
    path = AppController.FindPath(G, origem, destino, algorithms[num])
    return jsonify(JsonUtil.buildJSONPath(G, path))
