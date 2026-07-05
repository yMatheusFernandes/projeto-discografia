# seed.py
import sys
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import engine, Base
import models

# Dados dos artistas, seus álbuns e músicas
DADOS_SEED = [
    {
        "artista": "Pink Floyd",
        "albuns": [
            {
                "titulo": "The Dark Side of the Moon",
                "ano": 1973,
                "genero": "Progressive Rock",
                "nota": 10.0,
                "favorito": True,
                "musicas": [
                    {"titulo": "Speak to Me", "duracao": "1:05", "numero_faixa": 1},
                    {"titulo": "Breathe (In the Air)", "duracao": "2:49", "numero_faixa": 2},
                    {"titulo": "On the Run", "duracao": "3:45", "numero_faixa": 3},
                    {"titulo": "Time", "duracao": "6:53", "numero_faixa": 4},
                    {"titulo": "The Great Gig in the Sky", "duracao": "4:44", "numero_faixa": 5},
                    {"titulo": "Money", "duracao": "6:23", "numero_faixa": 6},
                    {"titulo": "Us and Them", "duracao": "7:49", "numero_faixa": 7},
                    {"titulo": "Any Colour You Like", "duracao": "3:26", "numero_faixa": 8},
                    {"titulo": "Brain Damage", "duracao": "3:46", "numero_faixa": 9},
                    {"titulo": "Eclipse", "duracao": "2:10", "numero_faixa": 10},
                ]
            },
            {
                "titulo": "The Wall",
                "ano": 1979,
                "genero": "Progressive Rock / Rock Opera",
                "nota": 9.8,
                "favorito": True,
                "musicas": [
                    {"titulo": "In the Flesh?", "duracao": "3:16", "numero_faixa": 1},
                    {"titulo": "The Thin Ice", "duracao": "2:27", "numero_faixa": 2},
                    {"titulo": "Another Brick in the Wall, Pt. 1", "duracao": "3:11", "numero_faixa": 3},
                    {"titulo": "The Happiest Days of Our Lives", "duracao": "1:46", "numero_faixa": 4},
                    {"titulo": "Another Brick in the Wall, Pt. 2", "duracao": "3:59", "numero_faixa": 5},
                    {"titulo": "Mother", "duracao": "5:32", "numero_faixa": 6},
                    {"titulo": "Hey You", "duracao": "4:40", "numero_faixa": 7},
                    {"titulo": "Comfortably Numb", "duracao": "6:22", "numero_faixa": 8},
                    {"titulo": "Run Like Hell", "duracao": "4:20", "numero_faixa": 9},
                ]
            }
        ]
    },
    {
        "artista": "Nirvana",
        "albuns": [
            {
                "titulo": "MTV Unplugged in New York",
                "ano": 1994,
                "genero": "Grunge / Acoustic",
                "nota": 9.7,
                "favorito": True,
                "musicas": [
                    {"titulo": "About a Girl", "duracao": "3:37", "numero_faixa": 1},
                    {"titulo": "Come as You Are", "duracao": "4:13", "numero_faixa": 2},
                    {"titulo": "Jesus Doesn't Want Me for a Sunbeam", "duracao": "4:37", "numero_faixa": 3},
                    {"titulo": "The Man Who Sold the World", "duracao": "4:20", "numero_faixa": 4},
                    {"titulo": "Pennyroyal Tea", "duracao": "3:40", "numero_faixa": 5},
                    {"titulo": "Dumb", "duracao": "2:52", "numero_faixa": 6},
                    {"titulo": "Polly", "duracao": "3:16", "numero_faixa": 7},
                    {"titulo": "On a Plain", "duracao": "3:44", "numero_faixa": 8},
                    {"titulo": "Something in the Way", "duracao": "4:01", "numero_faixa": 9},
                    {"titulo": "All Apologies", "duracao": "3:51", "numero_faixa": 10},
                    {"titulo": "Where Did You Sleep Like Night", "duracao": "5:08", "numero_faixa": 11},
                ]
            }
        ]
    },
    {
        "artista": "Titãs",
        "albuns": [
            {
                "titulo": "Acústico MTV",
                "ano": 1997,
                "genero": "Brazilian Rock / Acoustic",
                "nota": 9.5,
                "favorito": True,
                "musicas": [
                    {"titulo": "Comida", "duracao": "4:59", "numero_faixa": 1},
                    {"titulo": "Go Back", "duracao": "3:44", "numero_faixa": 2},
                    {"titulo": "Família", "duracao": "3:37", "numero_faixa": 3},
                    {"titulo": "Pra Dizer Adeus", "duracao": "3:42", "numero_faixa": 4},
                    {"titulo": "Marvin", "duracao": "4:24", "numero_faixa": 5},
                    {"titulo": "O Pulso", "duracao": "3:15", "numero_faixa": 6},
                    {"titulo": "Flores", "duracao": "3:35", "numero_faixa": 7},
                    {"titulo": "Homem Primata", "duracao": "3:27", "numero_faixa": 8},
                    {"titulo": "Os Cegos do Castelo", "duracao": "4:50", "numero_faixa": 9},
                    {"titulo": "Sonífera Ilha", "duracao": "2:50", "numero_faixa": 10},
                ]
            }
        ]
    },
    {
        "artista": "Bob Dylan",
        "albuns": [
            {
                "titulo": "Highway 61 Revisited",
                "ano": 1965,
                "genero": "Folk Rock",
                "nota": 9.6,
                "favorito": False,
                "musicas": [
                    {"titulo": "Like a Rolling Stone", "duracao": "6:13", "numero_faixa": 1},
                    {"titulo": "Tombstone Blues", "duracao": "5:58", "numero_faixa": 2},
                    {"titulo": "It Takes a Lot to Laugh, It Takes a Train to Cry", "duracao": "4:09", "numero_faixa": 3},
                    {"titulo": "From a Buick 6", "duracao": "3:19", "numero_faixa": 4},
                    {"titulo": "Ballad of a Thin Man", "duracao": "5:58", "numero_faixa": 5},
                    {"titulo": "Queen Jane Approximately", "duracao": "5:31", "numero_faixa": 6},
                    {"titulo": "Highway 61 Revisited", "duracao": "3:30", "numero_faixa": 7},
                    {"titulo": "Just Like Tom Thumb's Blues", "duracao": "5:31", "numero_faixa": 8},
                    {"titulo": "Desolation Row", "duracao": "11:21", "numero_faixa": 9},
                ]
            }
        ]
    },
    {
        "artista": "Led Zeppelin",
        "albuns": [
            {
                "titulo": "Led Zeppelin IV",
                "ano": 1971,
                "genero": "Hard Rock / Classic Rock",
                "nota": 10.0,
                "favorito": True,
                "musicas": [
                    {"titulo": "Black Dog", "duracao": "4:54", "numero_faixa": 1},
                    {"titulo": "Rock and Roll", "duracao": "3:40", "numero_faixa": 2},
                    {"titulo": "The Battle of Evermore", "duracao": "5:51", "numero_faixa": 3},
                    {"titulo": "Stairway to Heaven", "duracao": "8:02", "numero_faixa": 4},
                    {"titulo": "Misty Mountain Hop", "duracao": "4:38", "numero_faixa": 5},
                    {"titulo": "Four Sticks", "duracao": "4:44", "numero_faixa": 6},
                    {"titulo": "Going to California", "duracao": "3:31", "numero_faixa": 7},
                    {"titulo": "When the Levee Breaks", "duracao": "7:07", "numero_faixa": 8},
                ]
            },
            {
                "titulo": "Led Zeppelin II",
                "ano": 1969,
                "genero": "Hard Rock / Blues Rock",
                "nota": 9.8,
                "favorito": False,
                "musicas": [
                    {"titulo": "Whole Lotta Love", "duracao": "5:34", "numero_faixa": 1},
                    {"titulo": "What Is and What Should Never Be", "duracao": "4:44", "numero_faixa": 2},
                    {"titulo": "The Lemon Song", "duracao": "6:19", "numero_faixa": 3},
                    {"titulo": "Thank You", "duracao": "4:50", "numero_faixa": 4},
                    {"titulo": "Heartbreaker", "duracao": "4:14", "numero_faixa": 5},
                    {"titulo": "Living Loving Maid (She's Just a Woman)", "duracao": "2:39", "numero_faixa": 6},
                    {"titulo": "Ramble On", "duracao": "4:23", "numero_faixa": 7},
                    {"titulo": "Moby Dick", "duracao": "4:21", "numero_faixa": 8},
                    {"titulo": "Bring It On Home", "duracao": "4:20", "numero_faixa": 9},
                ]
            }
        ]
    },
    {
        "artista": "Capital Inicial",
        "albuns": [
            {
                "titulo": "Acústico MTV",
                "ano": 2000,
                "genero": "Brazilian Rock / Acoustic",
                "nota": 9.6,
                "favorito": True,
                "musicas": [
                    {"titulo": "O Passageiro", "duracao": "4:12", "numero_faixa": 1},
                    {"titulo": "Primeiros Erros (Chove)", "duracao": "4:11", "numero_faixa": 2},
                    {"titulo": "Fogo", "duracao": "4:18", "numero_faixa": 3},
                    {"titulo": "Independência", "duracao": "3:23", "numero_faixa": 4},
                    {"titulo": "Cai a Noite", "duracao": "3:52", "numero_faixa": 5},
                    {"titulo": "Natasha", "duracao": "3:05", "numero_faixa": 6},
                    {"titulo": "Tudo que Vai", "duracao": "3:45", "numero_faixa": 7},
                    {"titulo": "Música Urbana", "duracao": "4:37", "numero_faixa": 8},
                    {"titulo": "Fátima", "duracao": "4:02", "numero_faixa": 9},
                    {"titulo": "Veraneio Vascaína", "duracao": "3:06", "numero_faixa": 10},
                ]
            }
        ]
    },
    {
        "artista": "The Rolling Stones",
        "albuns": [
            {
                "titulo": "Sticky Fingers",
                "ano": 1971,
                "genero": "Classic Rock / Blues Rock",
                "nota": 9.7,
                "favorito": True,
                "musicas": [
                    {"titulo": "Brown Sugar", "duracao": "3:49", "numero_faixa": 1},
                    {"titulo": "Sway", "duracao": "3:51", "numero_faixa": 2},
                    {"titulo": "Wild Horses", "duracao": "5:42", "numero_faixa": 3},
                    {"titulo": "Can't You Hear Me Knocking", "duracao": "7:15", "numero_faixa": 4},
                    {"titulo": "You Gotta Move", "duracao": "2:32", "numero_faixa": 5},
                    {"titulo": "Bitch", "duracao": "3:37", "numero_faixa": 6},
                    {"titulo": "I Got the Blues", "duracao": "3:54", "numero_faixa": 7},
                    {"titulo": "Sister Morphine", "duracao": "5:31", "numero_faixa": 8},
                    {"titulo": "Dead Flowers", "duracao": "4:11", "numero_faixa": 9},
                    {"titulo": "Moonlight Mile", "duracao": "5:56", "numero_faixa": 10},
                ]
            }
        ]
    },
    {
        "artista": "The Beatles",
        "albuns": [
            {
                "titulo": "Abbey Road",
                "ano": 1969,
                "genero": "Classic Rock / Pop Rock",
                "nota": 10.0,
                "favorito": True,
                "musicas": [
                    {"titulo": "Come Together", "duracao": "4:20", "numero_faixa": 1},
                    {"titulo": "Something", "duracao": "3:03", "numero_faixa": 2},
                    {"titulo": "Maxwell's Silver Hammer", "duracao": "3:27", "numero_faixa": 3},
                    {"titulo": "Oh! Darling", "duracao": "3:26", "numero_faixa": 4},
                    {"titulo": "Octopus's Garden", "duracao": "2:51", "numero_faixa": 5},
                    {"titulo": "I Want You (She's So Heavy)", "duracao": "7:47", "numero_faixa": 6},
                    {"titulo": "Here Comes the Sun", "duracao": "3:05", "numero_faixa": 7},
                    {"titulo": "Because", "duracao": "2:45", "numero_faixa": 8},
                    {"titulo": "You Never Give Me Your Money", "duracao": "4:02", "numero_faixa": 9},
                    {"titulo": "Sun King", "duracao": "2:26", "numero_faixa": 10},
                    {"titulo": "Mean Mr. Mustard", "duracao": "1:06", "numero_faixa": 11},
                    {"titulo": "Polythene Pam", "duracao": "1:12", "numero_faixa": 12},
                    {"titulo": "She Came In Through the Bathroom Window", "duracao": "1:57", "numero_faixa": 13},
                    {"titulo": "Golden Slumbers", "duracao": "1:31", "numero_faixa": 14},
                    {"titulo": "Carry That Weight", "duracao": "1:36", "numero_faixa": 15},
                    {"titulo": "The End", "duracao": "2:19", "numero_faixa": 16},
                    {"titulo": "Her Majesty", "duracao": "0:23", "numero_faixa": 17},
                ]
            }
        ]
    }
]

def povoar_banco():
    print("Iniciando o povoamento do banco de dados...")
    
    # Certifica-se de que as tabelas existem
    Base.metadata.create_all(bind=engine)
    
    with Session(engine) as session:
        for item in DADOS_SEED:
            nome_artista = item["artista"]
            
            # Buscar ou criar o Artista
            artista = session.scalars(
                select(models.Artista).where(models.Artista.nome == nome_artista)
            ).first()
            
            if not artista:
                print(f"Cadastrando artista: {nome_artista}")
                artista = models.Artista(nome=nome_artista)
                session.add(artista)
                session.flush() # para obter o id
            else:
                print(f"Artista já cadastrado: {nome_artista}")
                
            for dados_album in item["albuns"]:
                titulo_album = dados_album["titulo"]
                
                # Buscar ou criar o Álbum para este artista
                album = session.scalars(
                    select(models.Album).where(
                        models.Album.titulo == titulo_album,
                        models.Album.artista_id == artista.id
                    )
                ).first()
                
                if not album:
                    print(f"  -> Cadastrando álbum: '{titulo_album}' ({dados_album['ano']})")
                    album = models.Album(
                        titulo=titulo_album,
                        ano=dados_album["ano"],
                        genero=dados_album["genero"],
                        nota=dados_album["nota"],
                        favorito=dados_album["favorito"],
                        artista_id=artista.id
                    )
                    session.add(album)
                    session.flush()
                else:
                    print(f"  -> Álbum já cadastrado: '{titulo_album}'")
                    # Atualizar nota, favorito e gênero se necessário
                    album.ano = dados_album["ano"]
                    album.genero = dados_album["genero"]
                    album.nota = dados_album["nota"]
                    album.favorito = dados_album["favorito"]
                
                # Cadastrar músicas se não existirem no álbum
                for dados_musica in dados_album["musicas"]:
                    titulo_musica = dados_musica["titulo"]
                    
                    musica = session.scalars(
                        select(models.Musica).where(
                            models.Musica.titulo == titulo_musica,
                            models.Musica.album_id == album.id
                        )
                    ).first()
                    
                    if not musica:
                        musica = models.Musica(
                            titulo=titulo_musica,
                            duracao=dados_musica["duracao"],
                            numero_faixa=dados_musica["numero_faixa"],
                            album_id=album.id
                        )
                        session.add(musica)
                    else:
                        # Atualiza duração e faixa caso existam diferenças
                        musica.duracao = dados_musica["duracao"]
                        musica.numero_faixa = dados_musica["numero_faixa"]
                        
        session.commit()
    print("Povoamento concluído com sucesso!")

if __name__ == "__main__":
    try:
        povoar_banco()
    except Exception as e:
        print("\nErro ao conectar e povoar o banco de dados:")
        print(e)
        print("\nATENÇÃO: Se o erro acima for do tipo 'OperationalError' ou 'tenant/user not found',")
        print("verifique se o seu projeto no Supabase está ativo (não pausado).")
        print("Caso esteja pausado, acesse o painel do Supabase e clique em 'Restore project'.")
        sys.exit(1)
