from flask import Flask, jsonify
import osmnx as ox
from AppController import AppController
from utils.JsonUtil import JsonUtil
from utils.SolverUtil import Solver

app = Flask(__name__)

G = ox.graph_from_xml("map.osm")
PF = Solver(G)


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/rota')
def getPath():
    path = AppController.FindPath(G, 8986661911, 253406715, PF.Aestrela)
    return jsonify(JsonUtil.buildJSONPath(G, path))
