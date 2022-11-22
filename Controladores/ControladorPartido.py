from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Partido import Partido

class ControladorPartido():
    #Constructor
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
    #Devuelve todos los documentos
    def index(self):
        return self.repositorioPartido.findAll()
    #Crea documentos
    def crearPartido(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.repositorioPartido.save(nuevoPartido)
    #Muestra un documento
    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__
    #Actualiza un documento
    def update(self, id, infoPartido):
        PartidoActual = Partido(self.repositorioPartido.findById(id))
        PartidoActual.nombre = infoPartido["nombre"]
        PartidoActual.lema = infoPartido["lema"]
        return self.repositorioPartido.save(PartidoActual)
    #Borra un documento
    def delete(self, id):
        return self.repositorioPartido.delete(id)