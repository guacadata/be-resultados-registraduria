from crypt import methods
from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS
from waitress import serve

from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

import json
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

@app.route("/candidatos", methods =["POST"])
def crearCandidato():
    data = request.get_json()
    respuestaCrear = miControladorCandidato.crearCandidato(data)
    return jsonify(respuestaCrear)

@app.route("/candidatos", methods = ["GET"])
def mostrarCandidatos():
    respuestaMostrar = miControladorCandidato.mostrarCandidatos()
    return jsonify(respuestaMostrar)

@app.route("/candidatos/<string:id_candidato>", methods = ["GET"])
def mostrarCandidato(id_candidato):
    respuestaMostrar = miControladorCandidato.mostrarCandidato(id_candidato)
    return jsonify(respuestaMostrar)

@app.route("/candidatos/<string:id_candidato>", methods = ["PUT"])
def actualizarCandidato(id_candidato):
    data = request.get_json()
    respuestaActualizar = miControladorCandidato.actualizarCandidato(id_candidato, data)
    return jsonify(respuestaActualizar)

@app.route("/candidatos/<string:id_candidato>", methods = ["DELETE"])
def eliminarCandidato(id_candidato):
    json = miControladorCandidato.delete(id_candidato)
    return jsonify(json)

@app.route("/candidatos/<string:id_candidato>/partido/<string:id_partido>", methods=["PUT"])
def asignarPartidoCandidato(id_candidato, id_partido):
    json = miControladorCandidato.asignarCandidato(id_candidato, id_partido)
    return jsonify(json)

# SERVICIOS PARTIDO

@app.route("/partidos", methods=["POST"])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.crearPartido(data)
    return jsonify(json)

@app.route("/partidos", methods=["GET"])
def mostrarPartidos():
    json = miControladorPartido.mostrarPartidos()
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["GET"])
def mostrarPartido(id):
    json = miControladorPartido.mostrarPartido(id)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["PUT"])
def actualizarPartido(id):
    data = request.get_json()
    json = miControladorPartido.actualizarPartido(id, data)
    return jsonify(json)

@app.route("/partidos/<string:id>", methods=["DELETE"])
def eliminarPartido(id):
    json = miControladorPartido.eliminarPartido(id)
    return jsonify(json)


# SERVICIOS RESULTADO

#Obtener todos los resultados
@app.route("/resultados", methods = ["GET"])
def mostrarResultados():
    json = miControladorResultado.mostrarResultados()
    return jsonify(json)


#Añadir un resultado a una mesa
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods =["POST"])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.crearResultado(data, id_mesa, id_candidato)
    return jsonify(json)


#Obtener resultado especifico
@app.route("/resultados/<string:id>", methods=["GET"])
def mostrarResultado(id):
    json = miControladorResultado.mostrarResultado(id)
    return jsonify(json)

#Modificar un resultado
@app.route("/resultados/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def actualizarResultado(id_resultado, id_mesa, id_candidato):
    data={}
    json = miControladorResultado.actualizarResultado(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)

#Eliminar Resultado
@app.route("/resultados/<string:id>", methods=["DELETE"])
def eliminarResultado(id):
    json = miControladorResultado.eliminarResultado(id)
    return jsonify(json)

#Buscar los candidatos votados en una mesa
@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def inscritosMesa(id_mesa):
    json = miControladorResultado.getListarCandidatosMesa(id_mesa)
    return jsonify(json)

#Buscar el candidato en las mesas
@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def inscritoEnMesas(id_candidato):
    json = miControladorResultado.getListarMesasDeInscritoCandidato(id_candidato)
    return jsonify(json)

#Buscar total de votos 
@app.route("/resultados/maxdocument", methods=["GET"])
def getMaxDocument():
    json = miControladorResultado.getMayorCedula()
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Servidor corriendo en: " + dataConfig['url-backend'] + " puerto: " + str(dataConfig['port']))
    serve(app, host=dataConfig['url-backend'], port=dataConfig['port'])
