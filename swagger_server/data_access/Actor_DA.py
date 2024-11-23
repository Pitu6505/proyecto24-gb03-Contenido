from hmac import new
from swagger_server.models.actor import Actor
from swagger_server.database_setup import db , Actor as db_actor

class Actor_DA:

    def __init__(self) -> None:
        pass

    def create_actor(actor: Actor):
        try:
            new_actor = db_actor(
                nombre=actor.nombre,
                apellidos=actor.apellidos,
                fecha_nac=actor.fecha_nac,
                imagen_url=actor.imagen_url,
                descripcion=actor.descripcion
            )
            db.add(new_actor)
            db.commit()
            return actor
        except Exception as e:
            db.rollback()
            print(e)
            return None
        
    def delete_actor(id: int):
        actor = db.query(db_actor).filter(db_actor.id_actor == id).first()
        if actor:
            db.delete(actor)
            db.commit()
            return True
        return False
        
    def update_actor(id: int, new_actor: Actor):
        actor = db.query(db_actor).filter(db_actor.id_actor == id).first()
        if actor:
            
                actor.nombre = new_actor.nombre
                actor.apellidos = new_actor.apellidos
                actor.fecha_nac = new_actor.fecha_nac
                actor.imagen_url = new_actor.imagen_url
                actor.descripcion = new_actor.descripcion
                db.commit()
                return actor
        return None
    
    def get_all_actors():
        try:
            actors = db.query(db_actor).all()
            return actors
        except Exception as e:
            print(e)
            return None
        
    def get_actor_by_id(id: int):
        try:
            actor = db.query(db_actor).filter(db_actor.id_actor == id).first()
            return actor
        except Exception as e:
            print(e)
            return None
        
    def get_contents_by_actor_id(id_actor: int):
        try:
            actor = db.query(db_actor).filter(db_actor.id_actor == id_actor).first()
            if actor:
                return actor.contenidos
            return None
        except Exception as e:
            print(e)
            return None
            