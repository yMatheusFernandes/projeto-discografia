# 🎵 Discografia CRUD

> Catálogo de álbuns musicais com interface inspirada no Spotify, construído com FastAPI, SQLAlchemy e Supabase (PostgreSQL).

---

## Integrantes

| Nome | Papel |
|------|-------|
| Matheus Fernandes de Meneses | Desenvolvimento full-stack |
| Guilherme Marques Carneiro | Desenvolvimento full-stack |
| Francisco das Chagas dos Santos | Desenvolvimento full-stack |

---

## 📋 Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Modelo de Dados](#modelo-de-dados)
- [Funcionalidades](#funcionalidades)
- [Screenshots](#screenshots)
- [Como Rodar Localmente](#como-rodar-localmente)
- [Banco de Dados (Seed)](#banco-de-dados-seed)
- [Integrantes](#integrantes)
- [Conclusão](#conclusão)

---

## Sobre o Projeto

O **Discografia CRUD** é uma aplicação web completa desenvolvida como trabalho acadêmico da disciplina de Banco de Dados. O sistema permite gerenciar uma coleção de álbuns musicais e suas respectivas músicas, demonstrando na prática os conceitos de CRUD (Create, Read, Update, Delete) com persistência em banco de dados relacional.

A interface foi projetada com tema escuro inspirado no Spotify, priorizando uma experiência visual moderna e totalmente responsiva — adaptando-se tanto a desktops quanto a dispositivos móveis.

---

## Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Backend | [FastAPI](https://fastapi.tiangolo.com/) (Python) |
| ORM | [SQLAlchemy 2.0](https://www.sqlalchemy.org/) com mapeamento tipado |
| Banco de Dados | [Supabase](https://supabase.com/) (PostgreSQL gerenciado na nuvem) |
| Driver PostgreSQL | [psycopg 3](https://www.psycopg.org/) |
| Templates | [Jinja2](https://jinja.palletsprojects.com/) |
| Frontend | HTML5 + CSS3 puro (sem frameworks) |
| Gerenciador de Pacotes | [uv](https://github.com/astral-sh/uv) |
| Task Runner | [Taskipy](https://github.com/taskipy/taskipy) |
| Configuração | [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) + `.env` |

---

## Modelo de Dados

O sistema possui **3 entidades** com relacionamentos entre si:

```
Artista (1) ──────< Album (N) ──────< Musica (N)
```

### Entidade `Artista`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer (PK) | Identificador único |
| `nome` | String | Nome do artista ou banda |

### Entidade `Album`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer (PK) | Identificador único |
| `titulo` | String | Título do álbum |
| `ano` | Integer | Ano de lançamento |
| `genero` | String | Gênero musical |
| `nota` | Float | Avaliação de 0 a 10 |
| `favorito` | Boolean | Marcado como favorito |
| `artista_id` | Integer (FK) | Referência ao Artista |

### Entidade `Musica`
| Campo | Tipo | Descrição |
|-------|------|-----------|
| `id` | Integer (PK) | Identificador único |
| `titulo` | String | Nome da faixa |
| `duracao` | String | Duração no formato `mm:ss` |
| `numero_faixa` | Integer | Posição na tracklist |
| `album_id` | Integer (FK) | Referência ao Álbum |

---

## Funcionalidades

- [x] **CREATE** — Cadastro de álbuns com artista, ano, gênero, nota e favorito
- [x] **READ** — Listagem de todos os álbuns e visualização detalhada com tracklist
- [x] **UPDATE** — Edição completa dos dados de um álbum
- [x] **DELETE** — Exclusão de álbuns (com cascade para músicas) e remoção de faixas individuais
- [x] **Músicas** — Adição e remoção de faixas em cada álbum
- [x] **Relacionamento FK** — Artista ↔ Album ↔ Musica (dois níveis de FK)
- [x] **Conexão Supabase** — Persistência em PostgreSQL na nuvem
- [x] **Interface responsiva** — Layout adaptado para mobile e desktop
- [x] **Seed de dados** — Script para popular o banco com álbuns lendários do rock
- [x] **Variáveis de ambiente** — Configuração via `.env` (protegido pelo `.gitignore`)

---

## Screenshots

| Desktop | Desktop |
|---------|---------|
| <img src="static/screenshots/Captura%20de%20tela%20de%202026-07-05%2016-14-05.png" width="420"> | <img src="static/screenshots/Captura%20de%20tela%20de%202026-07-05%2016-13-58.png" width="420"> |

| Mobile | Mobile | Mobile |
|--------|--------|--------|
| <img src="static/screenshots/413281c1-f10f-4d54-9643-e405eda6e158.jpeg" width="220"> | <img src="static/screenshots/067323d3-fb0a-458d-875d-aa4de7f138b0.jpeg" width="220"> | <img src="static/screenshots/c4d87641-b154-4df4-8024-efc995881321.jpeg" width="220"> |

---

## Como Rodar Localmente

### Pré-requisitos
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) instalado

### Passo a passo

**1. Clone o repositório e entre na pasta:**
```bash
git clone <url-do-repositorio>
cd projeto-discografia
```

**2. Crie e ative o ambiente virtual:**
```bash
uv sync
source .venv/bin/activate
```

**3. Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto com a URL do seu banco Supabase:
```env
DATABASE_URL=postgresql+psycopg://postgres.[PROJECT_REF]:[SENHA]@aws-0-sa-east-1.pooler.supabase.com:5432/postgres?sslmode=require
```

**4. Suba o servidor de desenvolvimento:**
```bash
task run
```

A aplicação estará disponível em: `http://localhost:8000`

---

## Banco de Dados (Seed)

Para popular o banco com álbuns lendários do rock, execute:

```bash
task seed
```

O script insere os seguintes artistas e álbuns (idempotente — pode ser executado múltiplas vezes sem duplicar dados):

| Artista | Álbum | Ano |
|---------|-------|-----|
| Pink Floyd | The Dark Side of the Moon | 1973 |
| Pink Floyd | The Wall | 1979 |
| Nirvana | MTV Unplugged in New York | 1994 |
| Titãs | Acústico MTV | 1997 |
| Bob Dylan | Highway 61 Revisited | 1965 |
| Led Zeppelin | Led Zeppelin IV | 1971 |
| Led Zeppelin | Led Zeppelin II | 1969 |
| Capital Inicial | Acústico MTV | 2000 |
| The Rolling Stones | Sticky Fingers | 1971 |
| The Beatles | Abbey Road | 1969 |

---

## Comandos Disponíveis

```bash
task run     # Inicia o servidor FastAPI em modo de desenvolvimento
task seed    # Popula o banco com dados iniciais
task lint    # Verifica problemas de formatação com Ruff
task format  # Formata o código automaticamente com Ruff
```


## Conclusão

O **Projeto Discografia CRUD** atingiu com sucesso todos os requisitos estabelecidos para o trabalho acadêmico. Ao longo do desenvolvimento, foram aplicados na prática conceitos fundamentais de banco de dados e desenvolvimento web:

### O que foi implementado

**Banco de Dados Relacional:**
- Modelagem de 3 tabelas (`artistas`, `albuns`, `musicas`) com relacionamentos via Foreign Key
- Integridade referencial com `cascade delete` (ao excluir um álbum, suas músicas são removidas automaticamente)
- Uso do ORM SQLAlchemy com tipagem moderna (`Mapped`, `mapped_column`) para mapeamento objeto-relacional

**Backend com FastAPI:**
- Arquitetura RESTful com rotas separadas por recurso
- Injeção de dependência para gerenciamento de sessão com o banco de dados
- Redirecionamentos pós-formulário (padrão PRG — Post/Redirect/Get) para evitar resubmissão

**Frontend Responsivo:**
- Interface 100% construída com HTML5 semântico e CSS3 puro (sem frameworks)
- Layout adaptativo para desktop (sidebar + grid) e mobile (bottom navigation + layout em coluna)
- Tema dark inspirado no Spotify com gradientes dinâmicos por álbum

**Nuvem e DevOps:**
- Banco de dados PostgreSQL hospedado no Supabase (cloud)
- Credenciais protegidas com `.env` e `.gitignore`
- Script de seed idempotente para facilitar a configuração do ambiente

### Aprendizados

Este projeto demonstrou como uma aplicação web moderna integra diversas camadas tecnológicas de forma coesa: desde o design da interface até a persistência dos dados na nuvem, passando pela lógica de negócio no backend. A experiência com FastAPI, SQLAlchemy e Supabase proporcionou uma visão prática e completa do ciclo de vida de uma aplicação web com banco de dados relacional.
