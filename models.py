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
    artista_id: Mapped[int] = mapped_column(ForeignKey('artistas.id'))
    artista: Mapped['Artista'] = relationship(back_populates='albuns')
    musicas: Mapped[list['Musica']] = relationship(back_populates='album', cascade='all, delete-orphan')

class Musica(Base):
    __tablename__ = 'musicas'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    duracao: Mapped[str] = mapped_column(default='0:00')   # ex: "3:45"
    numero_faixa: Mapped[int] = mapped_column(default=1)
    album_id: Mapped[int] = mapped_column(ForeignKey('albuns.id'))
    album: Mapped['Album'] = relationship(back_populates='musicas')