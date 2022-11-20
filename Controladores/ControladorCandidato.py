from Modelos.Candidato import Candidato
from Repositorios.RepositorioCandidato import RepositorioCandidato

class ControladorCandidato():
    def __init__(self):
        print("Creando Controlador Candidato")
        self.repositorioCandidato = RepositorioCandidato()

    def crearCandidato(self, infoCandidato):
        print("Crear un Candidato")
        candidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(candidato)

    def mostrarCandidato(self, id):
        print("Mostrando el Candidato con id: "+id)
        candidato = Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__

    def mostrarcandidatos(self):
        print("Mostrando todos los Candidatos")
        return self.repositorioCandidato.findAll()

    def actualizar(self,id,infoCandidato):
        print("Actualizando el Candidato con id: "+id)
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numeroresolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)

    def eliminar(self,id):
        print("eliminando el candidato con id: "+id)
        return self.repositorioCandidato.delete(id)
