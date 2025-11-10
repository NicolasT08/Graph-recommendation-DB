import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from run_recommendation import recomendationGenerate, obtener_contexto, obtener_contexto_completo, Recomendador, URI, AUTH 
from student_service import StudentService

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

@app.get("/cursos")
def obtener_cursos():
    """
    Obtiene la lista de todos los cursos disponibles en el sistema
    Retorna: Lista de cursos con id, nombre, area, nivel, creditos
    """
    try:
        service = StudentService()
        cursos = service.obtener_cursos_disponibles()
        service.cerrar()
        return {
            "success": True,
            "cursos": cursos
        }
    except Exception as e:
        return {"success": False, "status": "error", "details": str(e)}

@app.get("/semestres")
def obtener_semestres():
    """
    Obtiene la lista de todos los semestres disponibles en el sistema
    Retorna: Lista de semestres con id y numero
    """
    try:
        service = StudentService()
        semestres = service.obtener_semestres_disponibles()
        service.cerrar()
        return {
            "success": True,
            "semestres": semestres
        }
    except Exception as e:
        return {"success": False, "status": "error", "details": str(e)}

@app.post("/estudiante/{studentId}/curso/{cursoId}")
def agregar_curso_estudiante(studentId: int, cursoId: int):
    """
    Agrega una materia cursada a un estudiante
    Crea la relación HA_TOMADO entre el estudiante y el curso
    Args:
        studentId: ID del estudiante
        cursoId: ID del curso a agregar
    """
    try:
        service = StudentService()
        resultado = service.agregar_curso_estudiante(studentId, cursoId)
        service.cerrar()
        return resultado
    except Exception as e:
        return {"success": False, "status": "error", "details": str(e)}

@app.post("/estudiante/{studentId}/interes/{cursoId}")
def agregar_curso_interes(studentId: int, cursoId: int):
    """
    Agrega una materia a los intereses de un estudiante
    Crea la relación LE_INTERESA entre el estudiante y el curso
    Args:
        studentId: ID del estudiante
        cursoId: ID del curso a agregar a intereses
    """
    try:
        service = StudentService()
        resultado = service.agregar_curso_interes(studentId, cursoId)
        service.cerrar()
        return resultado
    except Exception as e:
        return {"success": False, "status": "error", "details": str(e)}

@app.put("/estudiante/{studentId}/semestre/{semestreId}")
def cambiar_semestre_estudiante(studentId: int, semestreId: int):
    """
    Cambia el semestre de un estudiante
    Actualiza la relación PERTENECE_A entre el estudiante y el semestre
    Args:
        studentId: ID del estudiante
        semestreId: ID del nuevo semestre
    """
    try:
        service = StudentService()
        resultado = service.cambiar_semestre_estudiante(studentId, semestreId)
        service.cerrar()
        return resultado
    except Exception as e:
        return {"success": False, "status": "error", "details": str(e)}
