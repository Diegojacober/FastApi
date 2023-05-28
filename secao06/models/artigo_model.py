from sqlalchemy import Column, Integer, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from core.configs import settings

class ArtigoModel(settings.DB_BASEMODEL):
    __tablename__ = 'artigos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(256))
    descricao = Column(Text)
    url_font: str = Column(String(String(256)))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    criador = relationship("UserModel",
                           back_populates='artigos',
                           lazy='joined')