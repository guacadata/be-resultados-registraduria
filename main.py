from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

import pymongo
import certifi

app = Flask(__name__)
cors = CORS(app)
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorResultado = ControladorResultado()


@app.route("/", methods=['GET'])
def test():
    json = {}
    json['mensaje'] = "Servidor ejecutandose"
    return jsonify(json)


# SERVICIOS MESA

@app.route("/mesa", methods=['POST'])
def crearMesa():
    data = request.get_json()
    respuestaCrear = miControladorMesa.crearMesa(data)
    return jsonify(respuestaCrear)

@app.route("/mesa/<string:id>", methods=['GET'])
def mostrarMesa(id):
    respuestaConsultar = miControladorMesa.mostrarMesa(id)
    return jsonify(respuestaConsultar)

@app.route("/mesa", methods=['GET'])
def mostrarMesas():
    respuestaConsultar = miControladorMesa.mostrarMesas()
    return jsonify(respuestaConsultar)

@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    datos = request.get_json()
    respuestaActualizar = miControladorMesa.actualizarMesa(id, datos)
    return jsonify(respuestaActualizar)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    respuestaEliminar = miControladorMesa.eliminarMesa(id)
    return jsonify(respuestaEliminar)

# SERVICIOS CANDIDATO

@app.route("/candidato", methods=['POST'])
def crearMesa():
    data = request.get_json()
    respuestaCrear = miControladorCandidato.crearMesa(data)
    return jsonify(respuestaCrear)

@app.route("/candidato/<string:id>", methods=['GET'])
def mostrarMesa(id):
    respuestaConsultar = miControladorMesa.mostrarMesa(id)
    return jsonify(respuestaConsultar)

@app.route("/mesa", methods=['GET'])
def mostrarMesas():
    respuestaConsultar = miControladorMesa.mostrarMesas()
    return jsonify(respuestaConsultar)

@app.route("/mesa/<string:id>", methods=['PUT'])
def actualizarMesa(id):
    datos = request.get_json()
    respuestaActualizar = miControladorMesa.actualizarMesa(id, datos)
    return jsonify(respuestaActualizar)

@app.route("/mesa/<string:id>", methods=['DELETE'])
def eliminarMesa(id):
    respuestaEliminar = miControladorMesa.eliminarMesa(id)
    return jsonify(respuestaEliminar)

# SERVICIOS PARTIDO

# SERVICIOS RESULTADO


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: " + dataConfig['url-backend'] + " puerto: " + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
