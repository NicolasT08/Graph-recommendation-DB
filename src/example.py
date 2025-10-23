from connection import connection

URI = "bolt://localhost:7687" 
AUTH = ("neo4j", "neo4j1234")

if __name__ == "__main__":
    conn = connection(URI, auth=AUTH)

    query = """
    MATCH (e:Estudiante {nombre: "Carlos Pérez"})-[:LE_INTERESA]->(c:Curso)
    RETURN e.nombre AS estudiante, c.nombre AS curso_interes
    """
    
    result = conn.query(query)

    print("Resultados:")
    for r in result:
        print(r)

    conn.close()
