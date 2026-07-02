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
    return RedirectResponse(url='/filmes')

# READ — lista todos os filmes
@app.get('/filmes')
def listar(request: Request, session: Session = Depends(get_session)):
    filmes = session.scalars(select(models.Filme)).all()
    return templates.TemplateResponse(request, 'lista.html', {'filmes': filmes})

# CREATE — formulário vazio
@app.get('/filmes/novo')
def form_novo(request: Request):
    return templates.TemplateResponse(request, 'form.html', {'filme': None})

# CREATE — grava no banco
@app.post('/filmes')
def criar(
    titulo: str = Form(...), diretor: str = Form(...), ano: int = Form(...),
    genero: str = Form(...), nota: float = Form(0), assistido: bool = Form(False),
    session: Session = Depends(get_session),
):
    filme = models.Filme(titulo=titulo, diretor=diretor, ano=ano,
                         genero=genero, nota=nota, assistido=assistido)
    session.add(filme)
    session.commit()
    return RedirectResponse(url='/filmes', status_code=303)

# main.py (continuação)
# UPDATE — formulário preenchido
@app.get('/filmes/{filme_id}/editar')
def form_editar(filme_id: int, request: Request, session: Session = Depends(get_session)):
    filme = session.get(models.Filme, filme_id)
    return templates.TemplateResponse(request, 'form.html', {'filme': filme})

# UPDATE — salva as alterações
@app.post('/filmes/{filme_id}/editar')
def atualizar(
    filme_id: int,
    titulo: str = Form(...), diretor: str = Form(...), ano: int = Form(...),
    genero: str = Form(...), nota: float = Form(0), assistido: bool = Form(False),
    session: Session = Depends(get_session),
):
    filme = session.get(models.Filme, filme_id)
    filme.titulo, filme.diretor, filme.ano = titulo, diretor, ano
    filme.genero, filme.nota, filme.assistido = genero, nota, assistido
    session.commit()
    return RedirectResponse(url='/filmes', status_code=303)

# DELETE — remove do banco
@app.post('/filmes/{filme_id}/excluir')
def excluir(filme_id: int, session: Session = Depends(get_session)):
    filme = session.get(models.Filme, filme_id)
    session.delete(filme)
    session.commit()
    return RedirectResponse(url='/filmes', status_code=303)