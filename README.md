# Projeto Discografia CRUD

Este é um projeto de um CRUD de discografia utilizando FastAPI, SQLAlchemy e banco de dados Supabase. O projeto permite criar, listar, editar e excluir álbuns, além de relacionar cada álbum a um Artista.

## Tema Escolhido
**Catálogo de Discografia (Álbuns Musicais)**
As entidades principais do sistema são:
- **Album**: A entidade principal do CRUD.
- **Artista**: Entidade relacionada através de uma Foreign Key (1 para N).

## Integrantes do Grupo
* Matheus Fernandes de Meneses
* Guilherme Marques Carneiro
* Francisco das Chagas dos Santos

## Funcionalidades
- [x] CRUD completo (criar, listar, editar, excluir)
- [x] Conexão e persistência no Supabase
- [x] Páginas HTML estilizadas (CSS próprio)
- [x] Relacionamento entre 2 entidades (FK)
- [x] .env no .gitignore

## Prints / Apresentação
*()*

## Como rodar localmente
1. Instale as dependências.
2. Crie um arquivo `.env` com a URL do Supabase:
```env
DATABASE_URL=postgresql://postgres:[SENHA]@db.[PROJECT_REF].supabase.co:5432/postgres
```
3. Execute o servidor:
```bash
uvicorn main:app --reload
```
