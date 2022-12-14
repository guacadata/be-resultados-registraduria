from Modelos.Mesa import Mesa
from Repositorios.RepositorioMesa import RepositorioMesa


class ControladorMesa():
    def __init__(self):
        print("Creando Controlador Mesa")
        self.repositorioMesa = RepositorioMesa()

    def crearMesa(self, infoMesa):
        print("Crear una mesa")
        mesa = Mesa(infoMesa)
        return self.repositorioMesa.save(mesa)

    def mostrarMesa(self, _id):
        print("Mostrando mesa con id: " + _id)
        mesa = Mesa(self.repositorioMesa.findById(_id))
        return mesa.__dict__

    def mostrarMesas(self):
        print("Mostrando todas las mesas")
        return self.repositorioMesa.findAll()

    def actualizarMesa(self, _id, infoMesa):
        print("Actualizando la mesa con id: " + _id)
        mesaActual = Mesa(self.repositorioMesa.findById(_id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)

    def eliminarMesa(self, _id):
        print("Eliminando la mesa con id: " + _id)
        return self.repositorioMesa.delete(_id)