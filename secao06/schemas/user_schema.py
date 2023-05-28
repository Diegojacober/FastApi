from typing import Optional, List

from schemas.artigo_schema import ArtigoSchema

from pydantic import BaseModel, EmailError, EmailStr

class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    is_admin: bool = False
    
    
    class Config:
        orm_mode = True
        

class UserSchemaCreate(UserSchemaBase):
    senha: str
    
    
class UserSchemaArtigos(UserSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    

class UserSchemaUp(UserSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    is_admin: Optional[bool]
    senha: Optional[str]
