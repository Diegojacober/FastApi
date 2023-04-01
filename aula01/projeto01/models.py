from typing import Optional

from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int
    
    @validator('titulo')
    def valid_title(cls, value: str):
        palavras = value.split(' ')
        if len(palavras) < 3:
            raise ValueError('O titulo de ter pelo menos 3 palavras.')
        
        if len(palavras) > 10:
            raise ValueError('O titulo deve ser menor que 10 palavras.')
        return value

cursos = [
    Curso(id=1,titulo="Programação com Python",aulas=350,horas=195),
    Curso(id=1,titulo="Programação com PHP",aulas=380,horas=210)
]