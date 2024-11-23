from swagger_server.models.contenido import Contenido
from swagger_server.database_setup import db, Contenido as db_contenido, Actor, Genero


class Contenido_DA:

    def __init__(self) -> None:
        pass

    #Si da fallo cambiar esto
    def create_content(content: Contenido):
        try:
            new_content = db_contenido(
                
                titulo=content.titulo,
                descripcion=content.descripcion,
                fecha_lanzamiento =content.fecha_lanzamiento,
                duracion=content.duracion,
                tipo=content.tipo,
                stream_url=content.stream_url,
                portada_url = content.portada_url,
                trailer_url = content.trailer_url,

            )
            print("new_content")
            print(new_content)
            db.add(new_content)
            db.commit()

             # Add actors and genres
            if content.id_actores:
                for actor_id in content.id_actores:
                    actor = db.query(Actor).get(actor_id)
                    if actor:
                        new_content.actores.append(actor)

            if content.id_generos:
                for genero_id in content.id_generos:
                    genero = db.query(Genero).get(genero_id)
                    if genero:
                        new_content.generos.append(genero)

            db.commit()
            return new_content

        except Exception as e:
            db.rollback()
            print(e)
            return None

    def delete_content(id_contenido: int):
        content = db.query(db_contenido).filter(db_contenido.id_contenido == id_contenido).first()
        if content:
            db.delete(content)
            db.commit()
            return True
        return False

    def update_content(id: int, new_content: Contenido):
         content = db.query(db_contenido).filter(db_contenido.id_contenido == id).first()
         if content:
            content.titulo = new_content.titulo
            content.descripcion = new_content.descripcion
            content.fecha_lanzamiento= new_content.fecha_lanzamiento
            content.duracion = new_content.duracion
            content.tipo = new_content.tipo
            content.stream_url = new_content.stream_url
            content.portada_url = new_content.portada_url
            content.trailer_url = new_content.trailer_url
              # Update actors and genres
            content.actores = []
            if new_content.id_actores:
                    for actor_id in new_content.id_actores:
                        actor = db.query(Actor).get(actor_id)
                        if actor:
                            content.actores.append(actor)

            content.generos = []
            if new_content.id_generos:
                    for genero_id in new_content.id_generos:
                        genero = db.query(Genero).get(genero_id)
                        if genero:
                            content.generos.append(genero)
            db.commit()
            return content
         return None
     
    def get_all_contents():
        try:
            contents = db.query(db_contenido).all()
            print(contents)
            return contents
        except Exception as e:
            print(e)
            return None
        
    def get_content_by_id(id_contenido: int):
        try:
            content = db.query(db_contenido).filter(db_contenido.id_contenido == id_contenido).first()
            return content
        except Exception as e:
            print(e)
            return None

    def filter_contents(titulo=None, nombre_actor=None, nombre_genero=None):
        try:
            query = db.query(db_contenido)

            if titulo:
                query = query.filter(db_contenido.titulo.ilike(f'%{titulo}%'))

            if nombre_actor:
                query = query.join(db_contenido.actores).filter(Actor.nombre.ilike(f'%{nombre_actor}%'))

            if nombre_genero:
                query = query.join(db_contenido.generos).filter(Genero.nombre.ilike(f'%{nombre_genero}%'))

            contents = query.all()
            return contents
        except Exception as e:
            print(e)
            return None