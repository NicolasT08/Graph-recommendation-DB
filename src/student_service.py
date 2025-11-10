from connection import connection
from connection import URI, AUTH

class StudentService:
    """Servicio para gestionar estudiantes, cursos e intereses"""
    
    def __init__(self, uri=URI, auth=AUTH):
        self.conn = connection(uri, auth=auth)
    
    def cerrar(self):
        """Cierra la conexión a la base de datos"""
        self.conn.close()
    
    def obtener_cursos_disponibles(self):
        """
        Obtiene la lista de todos los cursos disponibles en el sistema
        Returns: Lista de cursos con id, nombre, area, nivel, creditos
        """
        query = """
        MATCH (c:Curso)
        RETURN c.id AS id, c.nombre AS nombre, c.area AS area, 
               c.nivel AS nivel, c.creditos AS creditos
        ORDER BY c.id
        """
        return self.conn.query(query)
    
    def obtener_semestres_disponibles(self):
        """
        Obtiene la lista de todos los semestres disponibles en el sistema
        Returns: Lista de semestres con id y numero
        """
        query = """
        MATCH (s:Semestre)
        RETURN s.id AS id, s.numero AS numero
        ORDER BY s.numero
        """
        return self.conn.query(query)
    
    def agregar_curso_estudiante(self, estudiante_id, curso_id):
        """
        Agrega una relación HA_TOMADO entre un estudiante y un curso
        Args:
            estudiante_id: ID del estudiante
            curso_id: ID del curso
        Returns: Resultado de la operación con success, message y datos
        """
        # Verificar que el estudiante y el curso existan y si la relación ya existe
        query = """
        MATCH (e:Estudiante {id: $estudiante_id})
        MATCH (c:Curso {id: $curso_id})
        OPTIONAL MATCH (e)-[r:HA_TOMADO]->(c)
        WITH e, c, r
        WHERE r IS NULL
        CREATE (e)-[:HA_TOMADO]->(c)
        RETURN e.id AS estudiante_id, c.id AS curso_id, c.nombre AS curso_nombre, 'created' AS accion
        """
        resultado = self.conn.query(query, {
            "estudiante_id": estudiante_id,
            "curso_id": curso_id
        })
        
        if resultado:
            return {
                "success": True,
                "message": "Curso agregado exitosamente",
                "estudiante_id": estudiante_id,
                "curso_id": curso_id,
                "curso_nombre": resultado[0].get("curso_nombre")
            }
        else:
            # Verificar si existe el estudiante y curso, o si la relación ya existe
            verificar_query = """
            MATCH (e:Estudiante {id: $estudiante_id})
            MATCH (c:Curso {id: $curso_id})
            OPTIONAL MATCH (e)-[r:HA_TOMADO]->(c)
            RETURN e, c, r
            """
            verificacion = self.conn.query(verificar_query, {
                "estudiante_id": estudiante_id,
                "curso_id": curso_id
            })
            
            if not verificacion:
                return {"success": False, "message": "Estudiante o curso no encontrado"}
            elif verificacion[0].get("r") is not None:
                return {"success": False, "message": "El estudiante ya tiene este curso registrado"}
            else:
                return {"success": False, "message": "Error al agregar el curso"}
    
    def agregar_curso_interes(self, estudiante_id, curso_id):
        """
        Agrega una relación LE_INTERESA entre un estudiante y un curso
        Args:
            estudiante_id: ID del estudiante
            curso_id: ID del curso
        Returns: Resultado de la operación con success, message y datos
        """
        # Verificar que el estudiante y el curso existan y si la relación ya existe
        query = """
        MATCH (e:Estudiante {id: $estudiante_id})
        MATCH (c:Curso {id: $curso_id})
        OPTIONAL MATCH (e)-[r:LE_INTERESA]->(c)
        WITH e, c, r
        WHERE r IS NULL
        CREATE (e)-[:LE_INTERESA]->(c)
        RETURN e.id AS estudiante_id, c.id AS curso_id, c.nombre AS curso_nombre, 'created' AS accion
        """
        resultado = self.conn.query(query, {
            "estudiante_id": estudiante_id,
            "curso_id": curso_id
        })
        
        if resultado:
            return {
                "success": True,
                "message": "Curso agregado a intereses exitosamente",
                "estudiante_id": estudiante_id,
                "curso_id": curso_id,
                "curso_nombre": resultado[0].get("curso_nombre")
            }
        else:
            # Verificar si existe el estudiante y curso, o si la relación ya existe
            verificar_query = """
            MATCH (e:Estudiante {id: $estudiante_id})
            MATCH (c:Curso {id: $curso_id})
            OPTIONAL MATCH (e)-[r:LE_INTERESA]->(c)
            RETURN e, c, r
            """
            verificacion = self.conn.query(verificar_query, {
                "estudiante_id": estudiante_id,
                "curso_id": curso_id
            })
            
            if not verificacion:
                return {"success": False, "message": "Estudiante o curso no encontrado"}
            elif verificacion[0].get("r") is not None:
                return {"success": False, "message": "El estudiante ya tiene este curso en sus intereses"}
            else:
                return {"success": False, "message": "Error al agregar el curso a intereses"}
    
    def cambiar_semestre_estudiante(self, estudiante_id, semestre_id):
        """
        Cambia el semestre de un estudiante (actualiza la relación PERTENECE_A)
        Args:
            estudiante_id: ID del estudiante
            semestre_id: ID del nuevo semestre
        Returns: Resultado de la operación
        """
        # Verificar que el estudiante y el semestre existan
        verificar_query = """
        MATCH (e:Estudiante {id: $estudiante_id})
        MATCH (s:Semestre {id: $semestre_id})
        RETURN e, s
        """
        resultado = self.conn.query(verificar_query, {
            "estudiante_id": estudiante_id,
            "semestre_id": semestre_id
        })
        
        if not resultado:
            return {"success": False, "message": "Estudiante o semestre no encontrado"}
        
        # Eliminar la relación antigua si existe
        eliminar_query = """
        MATCH (e:Estudiante {id: $estudiante_id})-[r:PERTENECE_A]->(s:Semestre)
        DELETE r
        """
        self.conn.query(eliminar_query, {"estudiante_id": estudiante_id})
        
        # Crear la nueva relación
        crear_query = """
        MATCH (e:Estudiante {id: $estudiante_id})
        MATCH (s:Semestre {id: $semestre_id})
        CREATE (e)-[:PERTENECE_A]->(s)
        RETURN e.id AS estudiante_id, s.id AS semestre_id, s.numero AS semestre_numero
        """
        resultado = self.conn.query(crear_query, {
            "estudiante_id": estudiante_id,
            "semestre_id": semestre_id
        })
        
        if resultado:
            return {
                "success": True,
                "message": "Semestre actualizado exitosamente",
                "estudiante_id": estudiante_id,
                "semestre_id": semestre_id,
                "semestre_numero": resultado[0].get("semestre_numero")
            }
        else:
            return {"success": False, "message": "Error al actualizar el semestre"}

