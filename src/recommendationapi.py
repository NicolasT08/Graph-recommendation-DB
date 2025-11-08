import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from run_recommendation import recomendationGenerate, obtener_contexto, obtener_contexto_completo, Recomendador, URI, AUTH 

app = FastAPI(title="recommendation system")

# Configurar CORS para permitir peticiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:4173", "http://localhost:3000"],  # Puertos comunes de Svelte
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/contexto/{studentId}")
def obtener_contexto_estudiante(studentId: int):
    """
    Obtiene el contexto del estudiante: semestre, cursos cursados y cursos de interés
    Retorna información completa de los cursos (id, nombre, area, nivel, creditos)
    """
    try:
        rec = Recomendador(URI, AUTH)
        contexto = obtener_contexto_completo(rec, studentId)
        rec.cerrar()
        
        return {
            "estudiante_id": studentId,
            "semestre_id": contexto["semestreId"],
            "cursos_cursados": contexto["listaCursosTomados"],
            "cursos_interes": contexto["listaCursosInteres"]
        }
    except Exception as e:
        return {"status": "error", "details": str(e)}

@app.get("/recomendar/{studentId}")
def recomendar(studentId: int):
    recomendationList = recomendationGenerate(studentId)

    if "error" in recomendationList:
        return {"status": "error", "details": recomendationList["error"]}
    
    return {"estudiante_id": studentId, "recomendaciones": recomendationList}
