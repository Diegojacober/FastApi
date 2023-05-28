from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: Optional[str]
    descricao: Optional[str]
    url_fonte: Optional[HttpUrl]
    usuario_id: Optional[int]
    
    
    class Config:
        orm_mode = True