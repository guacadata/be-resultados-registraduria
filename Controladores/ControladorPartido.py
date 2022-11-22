from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    #Constructor
    def __init__(self):
        print("Creando Controlador Partido")
        self.repositorioPartido = RepositorioPartido()

    #Devuelve todos los documentos
    def mostrarPartidos(self):
        return self.repositorioPartido.findAll()

    #Crea documentos
    def crearPartido(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)

    #Muestra un documento
    def mostrarPartido(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    #Actualiza un documento
    def actualizarPartido(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)

    #Borra un documento
    def eliminarPartido(self, id):
        return self.repositorioPartido.delete(id)