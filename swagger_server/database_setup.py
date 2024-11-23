from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import class_mapper
from datetime import datetime



# Crear una clase base para las tablas
Base = declarative_base()

contenido_actor_association = Table('contenido_actor', Base.metadata,
    Column('id_contenido', Integer, ForeignKey('Contenido.id_contenido')),
    Column('id_actor', Integer, ForeignKey('actor.id_actor'))
)

contenido_genero_association = Table('contenido_genero', Base.metadata,
    Column('id_contenido', Integer, ForeignKey('Contenido.id_contenido')),
    Column('id_genero', Integer, ForeignKey('genero.id_genero'))
)

class Contenido(Base):
    __tablename__ = 'Contenido'

    id_contenido = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    tipo = Column(String, nullable=False)  # Ej. "pelicula", "serie", etc.
    fecha_lanzamiento = Column(DateTime, default=datetime.utcnow)
    duracion = Column(Integer, nullable=True)  # Duración en minutos
    trailer_url = Column(String, nullable=True)
    portada_url = Column(String, nullable=True)
    stream_url = Column(String, nullable=True)

    actores = relationship('Actor', secondary=contenido_actor_association, back_populates='contenidos')
    generos = relationship('Genero', secondary=contenido_genero_association, back_populates='contenidos')
    episodios = relationship('Episodio', back_populates='contenido')

    def to_dict(self):
        return {
            "id_contenido": self.id_contenido,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "tipo": self.tipo,
            "fecha_lanzamiento": self.fecha_lanzamiento,
            "duracion": self.duracion,
            "trailer_url": self.trailer_url,
            "portada_url": self.portada_url,
            "stream_url": self.stream_url,
            "actores": [actor.to_dict() for actor in self.actores],
            "generos": [genero.to_dict() for genero in self.generos]
        }
    
class Episodio(Base):
    __tablename__ = 'episodio'
    
    id_episodio = Column(Integer, primary_key=True, autoincrement=True)
    id_contenido = Column(Integer, ForeignKey('Contenido.id_contenido'), nullable=False)
    num_temporada = Column(Integer, nullable=False)
    num_episodio = Column(Integer, nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    duracion = Column(Integer, nullable=True)  # Duración en minutos
    stream_url = Column(String, nullable=True)
    
    contenido = relationship("Contenido", back_populates="episodios")

    def to_dict(self):
        return {
            "id_episodio": self.id_episodio,
            "id_contenido": self.id_contenido,
            "num_temporada": self.num_temporada,
            "num_episodio": self.num_episodio,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "duracion": self.duracion,
            "stream_url": self.stream_url
        }    

class Genero(Base):
    __tablename__ = 'genero'
    
    id_genero = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)

    contenidos = relationship('Contenido', secondary=contenido_genero_association, back_populates='generos')

    def to_dict(self):
        return {
            "id_genero": self.id_genero,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }
    


class Actor(Base):
    __tablename__ = 'actor'
    
    id_actor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellidos = Column(String, nullable=False)
    fecha_nac = Column(Date, nullable=True)
    imagen_url = Column(String, nullable=True)
    descripcion = Column(String, nullable=True)
    contenidos = relationship('Contenido', secondary=contenido_actor_association, back_populates='actores')

    def to_dict(self):
        return {
            "id_actor": self.id_actor,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "fecha_nac": self.fecha_nac,
            "imagen_url": self.imagen_url,
            "descripcion": self.descripcion
        }

engine = create_engine('sqlite:///database.db')
# Crear todas las tablas en la base de datos
#Base.metadata.create_all(engine)
# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
db = Session()