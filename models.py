# models.py
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

class Artista(Base):
    __tablename__ = 'artistas'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    albuns: Mapped[list['Album']] = relationship(back_populates='artista')

class Album(Base):
    __tablename__ = 'albuns'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    ano: Mapped[int]
    genero: Mapped[str]
    nota: Mapped[float] = mapped_column(default=0)
    favorito: Mapped[bool] = mapped_column(default=False)
    artista_id: Mapped[int] = mapped_column(ForeignKey('artistas.id'))   # FK
    artista: Mapped['Artista'] = relationship(back_populates='albuns')