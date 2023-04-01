from typing import Optional

from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1,titulo="Programação com Python",aulas=350,horas=195),
    Curso(id=1,titulo="Programação com PHP",aulas=380,horas=210)
]