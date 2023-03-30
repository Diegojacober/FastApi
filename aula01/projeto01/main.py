from typing import List, Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models import Curso
app = FastAPI()

cursos = {
    1: {
        "titulo" : "Programação com Python",
        "aulas" : 350,
        "horas": 195
    },
    2:{
        "titulo" : "Programação com PHP",
        "aulas" : 380,
        "horas": 210
    }
}

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id : int):
    try:
        curso = cursos[curso_id]
        # coloca uma nova chave chamada id e coloca o id
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso): #Optional[Curso] = None):
    next_id = len(cursos) + 1
    # curso.id = next_id
    cursos[next_id] = curso
    del curso.id
    return curso
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)