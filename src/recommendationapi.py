import sys
import os
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from run_recommendation import recomendationGenerate 

app = FastAPI(title="recommendation system")

@app.get("/recomendar/{studentId}")
def recomendar(studentId: int):
    recomendationList = recomendationGenerate(studentId)

    if "error" in recomendationList:
        return {"status": "error", "details": recomendationList["error"]}
    
    return {"estudiante_id": studentId, "recomendaciones": recomendationList}
