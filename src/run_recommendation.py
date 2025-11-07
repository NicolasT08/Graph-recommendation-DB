from recommendation_service import Recomendador

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "neo4j1234")

def obtener_contexto(rec, estudianteId):
    # Consulta para obtener semestre, cursos tomados e intereses
    q = """
    MATCH (e:Estudiante {id: $estudianteId})
    OPTIONAL MATCH (e)-[:HA_TOMADO]->(c_t:Curso)
    OPTIONAL MATCH (e)-[:LE_INTERESA]->(c_i:Curso)
    OPTIONAL MATCH (e)-[:PERTENECE_A]->(s:Semestre)
    RETURN s.id AS semestreId,
           COLLECT(DISTINCT c_t.id) AS listaCursosTomados,
           COLLECT(DISTINCT c_i.id) AS listaCursosInteres
    """
    res = rec.conn.query(q, {"estudianteId": estudianteId})
    if not res:
        return {"semestreId": None, "listaCursosTomados": [], "listaCursosInteres": []}
    r = res[0]
    # Asegurar tipos
    return {
        "semestreId": r.get("semestreId"),
        "listaCursosTomados": r.get("listaCursosTomados") or [],
        "listaCursosInteres": r.get("listaCursosInteres") or []
    }

def recomendationGenerate(studentId):
    rec = Recomendador(URI,AUTH)

    ctx = obtener_contexto(rec, studentId)
    cursosTomadosIDs = ctx["listaCursosTomados"]
    listaCursosInteres = ctx["listaCursosInteres"]
    semestreId = ctx["semestreId"]

    lista_prerequisitos = rec.prerequisito(cursosTomadosIDs)
    lista_complementarios = rec.complementario(cursosTomadosIDs + listaCursosInteres)
    lista_area = rec.area_interes(listaCursosInteres, cursosTomadosIDs)
    lista_semestre = rec.por_semestre(semestreId, cursosTomadosIDs)
    lista_colab = rec.colaborativo(cursosTomadosIDs)

    PESOS = {
            "PESO_PREREQUISITO": 10,
            "PESO_SEMESTRE": 8,
            "PESO_COMPLEMENTARIO": 7,
            "PESO_AREA_INTERES": 5,
            "PESO_COLABORATIVO": 3,
        }

    puntajes = {}  

    def add_items(items, peso, origen):
        for it in items:
            cid = it.get("id")
            nombre = it.get("nombre")
            if cid is None:
                continue
            if cid not in puntajes:
                puntajes[cid] = {"id": cid, "nombre": nombre, "score": 0, "origenes": set()}
            puntajes[cid]["score"] += peso
            puntajes[cid]["origenes"].add(origen)

    add_items(lista_prerequisitos, PESOS["PESO_PREREQUISITO"], "prerrequisito")
    add_items(lista_complementarios, PESOS["PESO_COMPLEMENTARIO"], "complementario")
    add_items(lista_area, PESOS["PESO_AREA_INTERES"], "area_interes")
    add_items(lista_semestre, PESOS["PESO_SEMESTRE"], "semestre")

    for it in lista_colab:
                cid = it.get("id")
                nombre = it.get("nombre")
                ranking = it.get("ranking", 1)
                if cid is None:
                    continue
                if cid not in puntajes:
                    puntajes[cid] = {"id": cid, "nombre": nombre, "score": 0, "origenes": set()}
                puntajes[cid]["score"] += PESOS["PESO_COLABORATIVO"] * ranking
                puntajes[cid]["origenes"].add("colaborativo")
    
    ranked = sorted(puntajes.values(), key=lambda x: x["score"], reverse=True)
    for r in ranked:
            r["origenes"] = list(r["origenes"])

    rec.cerrar()
    return ranked
