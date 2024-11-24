from hmac import new
from swagger_server.models.episodio import Episodio
from swagger_server.database_setup import db , Episodio as db_episodio

class Episodio_DA:
    
        def __init__(self) -> None:
            pass
    
        def create_episode(episode: Episodio):
            try:
                new_episode = db_episodio(
                    id_contenido=episode.id_contenido,
                    num_temporada=episode.num_temporada,
                    num_episodio=episode.num_episodio,
                    titulo=episode.titulo,
                    descripcion=episode.descripcion,
                    duracion=episode.duracion,
                    stream_url=episode.stream_url
                )
                print(new_episode)
                db.add(new_episode)
                db.commit()
                return episode
            except Exception as e:
                db.rollback()
                print(e)
                return None
            
        def delete_episode(id: int):
            episode = db.query(db_episodio).filter(db_episodio.id_episodio == id).first()
            if episode:
                db.delete(episode)
                db.commit()
                return True
            return False
            
        def update_episode(id: int, new_episode: Episodio):
            episode = db.query(db_episodio).filter(db_episodio.id_episodio == id).first()
            if episode:

                episode.id_contenido = new_episode.id_contenido
                episode.num_temporada = new_episode.num_temporada
                episode.num_episodio = new_episode.num_episodio
                episode.titulo = new_episode.titulo
                episode.descripcion = new_episode.descripcion
                episode.duracion = new_episode.duracion
                episode.stream_url = new_episode.stream_url
                db.commit()
                return episode
            return None
        
        def get_all_episodes():
            try:
                episodes = db.query(db_episodio).all()
                return episodes
            except Exception as e:
                print(e)
                return None
            
        def get_episode_by_id(id: int):
            try:
                episode = db.query(db_episodio).filter(db_episodio.id_episodio == id).first()
                return episode
            except Exception as e:
                print(e)
                return None
            
        def get_episodes_by_content_id(id_contenido: int):
            try:
                episodes = db.query(db_episodio).filter(db_episodio.id_contenido == id_contenido).all()
                return episodes
            except Exception as e:
                print(e)
                return None