# main.py
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from database import Base, engine, get_session

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)   # cria as tabelas no Supabase
    yield

app = FastAPI(lifespan=lifespan)
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

@app.get('/')                               # raiz → redireciona para a lista
def home():
    return RedirectResponse(url='/albuns')

# READ — lista todos os álbuns
@app.get('/albuns')
def listar(request: Request, session: Session = Depends(get_session)):
    albuns = session.scalars(select(models.Album)).all()
    return templates.TemplateResponse(request, 'lista.html', {'albuns': albuns})

# CREATE — formulário vazio
@app.get('/albuns/novo')
def form_novo(request: Request):
    return templates.TemplateResponse(request, 'form.html', {'album': None})

# CREATE — grava no banco
@app.post('/albuns')
def criar(
    titulo: str = Form(...), artista_nome: str = Form(...), ano: int = Form(...),
    genero: str = Form(...), nota: float = Form(0), favorito: bool = Form(False),
    session: Session = Depends(get_session),
):
    artista = session.scalars(select(models.Artista).where(models.Artista.nome == artista_nome)).first()
    if not artista:
        artista = models.Artista(nome=artista_nome)
        session.add(artista)
        session.flush()

    album = models.Album(titulo=titulo, ano=ano,
                         genero=genero, nota=nota, favorito=favorito, artista_id=artista.id)
    session.add(album)
    session.commit()
    return RedirectResponse(url='/albuns', status_code=303)

# UPDATE — formulário preenchido
@app.get('/albuns/{album_id}/editar')
def form_editar(album_id: int, request: Request, session: Session = Depends(get_session)):
    album = session.get(models.Album, album_id)
    return templates.TemplateResponse(request, 'form.html', {'album': album})

# UPDATE — salva as alterações
@app.post('/albuns/{album_id}/editar')
def atualizar(
    album_id: int,
    titulo: str = Form(...), artista_nome: str = Form(...), ano: int = Form(...),
    genero: str = Form(...), nota: float = Form(0), favorito: bool = Form(False),
    session: Session = Depends(get_session),
):
    album = session.get(models.Album, album_id)
    
    artista = session.scalars(select(models.Artista).where(models.Artista.nome == artista_nome)).first()
    if not artista:
        artista = models.Artista(nome=artista_nome)
        session.add(artista)
        session.flush()

    album.titulo = titulo
    album.artista_id = artista.id
    album.ano = ano
    album.genero = genero
    album.nota = nota
    album.favorito = favorito
    session.commit()
    return RedirectResponse(url='/albuns', status_code=303)

# DELETE — remove do banco
@app.post('/albuns/{album_id}/excluir')
def excluir(album_id: int, session: Session = Depends(get_session)):
    album = session.get(models.Album, album_id)
    session.delete(album)
    session.commit()
    return RedirectResponse(url='/albuns', status_code=303)