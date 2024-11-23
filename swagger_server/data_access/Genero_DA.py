
from swagger_server.models.genero import Genero
from swagger_server.database_setup import db , Genero as db_genero

class Genero_DA:

    def __init__(self) -> None:
        pass

    def create_genre(genre: Genero):
        try:
            new_genre = db_genero(
                nombre=genre.nombre,
                descripcion=genre.descripcion
            )
            db.add(new_genre)
            db.commit()
            return new_genre
        except Exception as e:
            db.rollback()
            print(e)
            return None
        
    def delete_genre(id_genero: int):
        genre = db.query(db_genero).filter(db_genero.id_genero == id_genero).first()
        if genre:
            db.delete(genre)
            db.commit()
            return True
        return False
    def update_genre(id_genero: int, new_genre: Genero):
        genre = db.query(db_genero).filter(db_genero.id_genero == id_genero).first()
        if genre:
            genre.nombre = new_genre.nombre
            genre.descripcion = new_genre.descripcion
            db.commit()
            return genre
        return None
    
    def get_all_genres():
        try:
            genres = db.query(db_genero).all()
            return genres
        except Exception as e:
            print(e)
            return None
        
    def get_genre_by_id(id_genero: int):
        try:
            genre = db.query(db_genero).filter(db_genero.id_genero == id_genero).first()
            return genre
        except Exception as e:
            print(e)
            return None
        
