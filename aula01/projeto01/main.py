from typing import List, Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path

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
# gt -> deve ser maior que 
#lt deve ser menor que
async def get_curso(curso_id : int = Path(title="ID do curso", description="Deve ser entre 1 e 2",gt=0, lt=3)):
    try:
        curso = cursos[curso_id]
        # coloca uma nova chave chamada id e coloca o id
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe o curso com o id {curso_id}")

@app.delete('/cursos/{curso_id}')
async def curso_delete(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content="Deletado com sucesso")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe o curso com o id {curso_id}")

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso): #Optional[Curso] = None):
    next_id = len(cursos) + 1
    # curso.id = next_id
    cursos[next_id] = curso
    del curso.id
    return curso
        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host='127.0.0.1', port=8000, log_level="info", reload=True) 