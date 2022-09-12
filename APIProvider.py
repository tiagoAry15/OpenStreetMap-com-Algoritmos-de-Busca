from flask import Flask
import osmnx as ox
from AppController import AppController
from utils.SolverUtil import Solver

app = Flask(__name__)


@app.route('/programming_languages', methods=["GET"])
def getPath():
    algoritmo = ''

    AppController
