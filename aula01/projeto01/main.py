from typing import List, Optional, Any

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import Depends


from time import sleep

from models import Curso

def fake_db():
    try:
        print('Abindo conexão com o banco de dados')
        sleep(1)
    finally:
        print('Fechando conexão com o banco de dados')
        sleep(1)

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
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

@app.get("/cursos/{curso_id}")
# gt -> deve ser maior que 
#lt deve ser menor que
async def get_curso(curso_id : int = Path(title="ID do curso", description="Deve ser entre 1 e 2",gt=0, lt=3), db: Any = Depends(fake_db)):
    try:
        curso = cursos[curso_id]
        # coloca uma nova chave chamada id e coloca o id
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.get('/calculator/')
async def calcular(a: int = Query(default=None, gt=5, lt=150), b: int = Query(default=None, gt=2), c: Optional[int] = None, x_geek: str = Header(default=None )):
    soma = a + b
    if c:
        soma = a + b +c

    print(f'X_GEEK: {x_geek}')
    return {"resultado": soma}


@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)): #Optional[Curso] = None):
    next_id = len(cursos) + 1
    # curso.id = next_id
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        curso.id = curso_id
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe o curso com o id {curso_id}")

@app.delete('/cursos/{curso_id}')
async def curso_delete(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content="Deletado com sucesso")
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe o curso com o id {curso_id}")


        
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host='192.168.0.89', port=8000, log_level="info", reload=True) 