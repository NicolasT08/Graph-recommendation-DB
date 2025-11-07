# src/run_recommendation.py
# Script listo para ejecutar que usa tu RecommendationService / recommendation_service
# Muestra las 5 listas y calcula el ranking final.

import sys

# Intentamos importar la clase Recomendador del nombre de módulo que tengas (case-insensitive attempt)
Recomendador = None
possible_modules = ["recommendation_service", "RecommendationService", "recommendationservice"]
for m in possible_modules:
    try:
        mod = __import__(f"src.{m}", fromlist=["Recomendador"])
        Recomendador = getattr(mod, "Recomendador")
        break
    except Exception:
        try:
            mod = __import__(m, fromlist=["Recomendador"])
            Recomendador = getattr(mod, "Recomendador")
            break
        except Exception:
            pass

if Recomendador is None:
    # Try importing as a sibling module (if you run from project root)
    try:
        mod = __import__("recommendation_service", fromlist=["Recomendador"])
        Recomendador = getattr(mod, "Recomendador")
    except Exception as e:
        print("ERROR: No se pudo importar la clase Recomendador.\nAsegúrate de que el archivo esté en src/ y se llame recommendation_service.py o RecommendationService.py")
        print("Excepción:", e)
        sys.exit(1)

# Configuración de conexión (usa los valores que ya tienes)
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

def imprimir_lista(nombre, lista):
    print(f"\n--- {nombre} ({len(lista)} resultados) ---")
    if not lista:
        print("  (vacía)")
        return
    for item in lista:
        # item puede venir con 'id' y 'nombre' y en colaborativo 'ranking'
        if "ranking" in item:
            print(f"  id: {item.get('id')} | nombre: {item.get('nombre')} | ranking: {item.get('ranking')}")
        else:
            print(f"  id: {item.get('id')} | nombre: {item.get('nombre')}")

def main():
    rec = Recomendador(URI, AUTH)
    try:
        # Cambia el estudianteId si quieres (por defecto 1 = Carlos Pérez en tu init.cypher)
        estudianteId = 1

        #obtener contexto del estudiante desde la BD
        ctx = obtener_contexto(rec, estudianteId)
        cursosTomadosIDs = ctx["listaCursosTomados"]
        listaCursosInteres = ctx["listaCursosInteres"]
        semestreId = ctx["semestreId"]

        print("Contexto del estudiante (extraído desde Neo4j):")
        print("  estudianteId:", estudianteId)
        print("  semestreId:", semestreId)
        print("  cursosTomadosIDs:", cursosTomadosIDs)
        print("  listaCursosInteres:", listaCursosInteres)

        # 1) Ejecutar las 5 funciones (listas)
        lista_prerequisitos = rec.prerequisito(cursosTomadosIDs)
        lista_complementarios = rec.complementario(cursosTomadosIDs + listaCursosInteres)
        lista_area = rec.area_interes(listaCursosInteres, cursosTomadosIDs)
        lista_semestre = rec.por_semestre(semestreId, cursosTomadosIDs)
        lista_colab = rec.colaborativo(cursosTomadosIDs)

        # 2) Mostrar las 5 listas claramente
        imprimir_lista("Lista por prerrequisito", lista_prerequisitos)
        imprimir_lista("Lista complementaria", lista_complementarios)
        imprimir_lista("Lista por área de interés", lista_area)
        imprimir_lista("Lista por semestre", lista_semestre)
        imprimir_lista("Lista colaborativa", lista_colab)

        # 3) Especifiacadion de los pesos
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

        # Agrego listyas
        add_items(lista_prerequisitos, PESOS["PESO_PREREQUISITO"], "prerrequisito")
        add_items(lista_complementarios, PESOS["PESO_COMPLEMENTARIO"], "complementario")
        add_items(lista_area, PESOS["PESO_AREA_INTERES"], "area_interes")
        add_items(lista_semestre, PESOS["PESO_SEMESTRE"], "semestre")

        # Para la lista colaborativa, multiplicamos por ranking si existe
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

        # 4) Ordeno por su puntaje y muestro el Top-N
        ranked = sorted(puntajes.values(), key=lambda x: x["score"], reverse=True)
        top_n = 10
        print(f"\n\n=== TOP {top_n} RECOMENDACIONES (con puntajes) ===")
        if not ranked:
            print("No hay recomendaciones (lista vacía).")
        else:
            for i, item in enumerate(ranked[:top_n], start=1):
                origenes = ", ".join(sorted(item["origenes"]))
                print(f"{i}. id:{item['id']} | nombre:{item['nombre']} | puntaje:{item['score']} | origenes:[{origenes}]")

    finally:
        try:
            rec.cerrar()
        except Exception:
            pass

if __name__ == "__main__":
    main()
