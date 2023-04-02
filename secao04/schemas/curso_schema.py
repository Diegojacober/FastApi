from typing import Optional

from pydantic import BaseModel as SCBaseModel

#para cada model um schema

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True
