from Repositorios.Interfaces import Interfaces
from Modelos.Resultado import Resultado
from bson import ObjectId

class RepositorioResultado(Interfaces[Resultado]):
    #Da las votaciones por mesa
    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    #Da las votaciones por candidato
    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    # Numero mayor de una cédula
    def getNumeroCedulaMayorCandidato(self):
        query = {
            "$group":{
                "_id": "$candidato",
                "Total_votaciones_por_id": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }
        pipeline = [query]
        return self.queryAggregation(pipeline)
