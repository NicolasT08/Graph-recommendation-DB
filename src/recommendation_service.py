from connection import connection

class Recomendador:
    def __init__(self, uri, auth):
        self.conn = connection(uri, auth=auth)

    def cerrar(self):
        self.conn.close()

    def prerequisito(self, cursosTomadosIDs):
        query = """
        MATCH (c_tomado:Curso)-[:ES_REQUISITO_DE]->(reco:Curso)
        WHERE c_tomado.id IN $cursosTomadosIDs AND NOT reco.id IN $cursosTomadosIDs
        RETURN reco.id AS id, reco.nombre AS nombre
        """
        return self.conn.query(query, {"cursosTomadosIDs": cursosTomadosIDs})

    def complementario(self, cursosBaseIDs):
        query = """
        MATCH (c_base:Curso)-[:COMPLEMENTA]-(reco:Curso)
        WHERE c_base.id IN $cursosBaseIDs AND NOT reco.id IN $cursosBaseIDs
        RETURN reco.id AS id, reco.nombre AS nombre
        """
        return self.conn.query(query, {"cursosBaseIDs": cursosBaseIDs})

    def area_interes(self, listaCursosInteres, listaCursosTomados):
        query = """
        MATCH (c_interes:Curso)-[:PERTENECE_A]->(area:AreaTematica)
        WHERE c_interes.id IN $listaCursosInteres
        MATCH (reco:Curso)-[:PERTENECE_A]->(area)
        WHERE NOT reco.id IN $listaCursosInteres AND NOT reco.id IN $listaCursosTomados
        RETURN reco.id AS id, reco.nombre AS nombre
        """
        return self.conn.query(query, {"listaCursosInteres": listaCursosInteres, "listaCursosTomados": listaCursosTomados})

    def por_semestre(self, semestreDelEstudiante, listaCursosTomados):
        query = """
        MATCH (reco:Curso)-[:ES_PARTE_DE]->(s:Semestre {id: $semestreDelEstudiante})
        WHERE NOT reco.id IN $listaCursosTomados
        RETURN reco.id AS id, reco.nombre AS nombre
        """
        return self.conn.query(query, {"semestreDelEstudiante": semestreDelEstudiante, "listaCursosTomados": listaCursosTomados})

    def colaborativo(self, cursosTomadosIDs):
        query = """
        MATCH (e_similar:Estudiante)-[:HA_TOMADO]->(c_comun:Curso)
        WHERE c_comun.id IN $cursosTomadosIDs
        MATCH (e_similar)-[:HA_TOMADO]->(reco:Curso)
        WHERE NOT reco.id IN $cursosTomadosIDs
        RETURN reco.id AS id, reco.nombre AS nombre, COUNT(e_similar) AS ranking
        ORDER BY ranking DESC
        """
        return self.conn.query(query, {"cursosTomadosIDs": cursosTomadosIDs})
