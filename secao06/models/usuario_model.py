from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UserModel(settings.DB_BASEMODEL):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    is_admin = Column(Boolean, default=False)
    artigos = relationship(
        "ArtigoModel",
        cascade='all, delete-orphan',
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    