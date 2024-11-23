import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.models.contenidos_body import ContenidosBody  # noqa: E501
from swagger_server.models.contenidos_body1 import ContenidosBody1  # noqa: E501
from swagger_server.models.episodio import Episodio  # noqa: E501
from swagger_server.models.genero import Genero  # noqa: E501
from swagger_server.data_access.Contenido_DA import Contenido_DA
from swagger_server.data_access.Episodio_DA import Episodio_DA

from flask import jsonify
from swagger_server import util


def contenidos_filtrar_get(titulo=None, nombre_actor=None, nombre_genero=None):  # noqa: E501
    """Filtrar contenidos por nombre, actor y género

    Devuelve una lista de contenidos que coincidan con el nombre, actor o género especificado. # noqa: E501

    :param titulo: Nombre o título parcial del contenido a buscar
    :type titulo: str
    :param nombre_actor: Nombre del actor para filtrar los contenidos asociados a dicho actor
    :type nombre_actor: str
    :param nombre_genero: Nombre del género para filtrar los contenidos asociados a dicho género
    :type nombre_genero: str

    :rtype: List[Contenido]
    """
    try:
        contents = Contenido_DA.filter_contents(titulo, nombre_actor, nombre_genero)
        if contents:
            return jsonify([content.to_dict() for content in contents]), 200
        return jsonify({"message": "No contents found"}), 404
    except Exception as e:
        return str(e), 500


def contenidos_get():  # noqa: E501
    """Obtener todos los contenidos

     # noqa: E501


    :rtype: List[Contenido]
    """
    try:
        contenidos = Contenido_DA.get_all_contents()
        print(contenidos)
        return [contenido.to_dict() for contenido in contenidos]
    except Exception as e:
        print("Error al obtener los contenidos")
        return "Error", 500


def contenidos_id_contenido_actores_get(id_contenido):  # noqa: E501
    """Obtener todos los actores asociados a un contenido

    Devuelve una lista de actores asociados al contenido especificado por su ID. # noqa: E501

    :param id_contenido: ID del contenido para el cual se desean obtener los actores asociados
    :type id_contenido: int

    :rtype: List[Actor]
    """
    try:
        content = Contenido_DA.get_content_by_id(id_contenido)
        if content:
            return jsonify([actor.to_dict() for actor in content.actores]), 200
        return jsonify({"message": "Content not found"}), 404
    except Exception as e:
        return str(e), 500


def contenidos_id_contenido_delete(id_contenido):  # noqa: E501
    """Eliminar un contenido

     # noqa: E501

    :param id_contenido: 
    :type id_contenido: int

    :rtype: None
    """
    try:
        contenido = Contenido_DA.get_content_by_id(id_contenido)
        if contenido:
            # Eliminar episodios asociados
            episodios = Episodio_DA.get_episodes_by_content_id(id_contenido)
            for episodio in episodios:
                Episodio_DA.delete_episode(episodio.id_episodio)
            
            # Eliminar el contenido
            Contenido_DA.delete_content(id_contenido)
            return "Contenido y episodios asociados eliminados", 200
        return "Contenido no encontrado", 404
    except Exception as e:
        print(f"Error al eliminar el contenido: {e}")
        return "Error interno del servidor", 500


def contenidos_id_contenido_episodios_get(id_contenido):  # noqa: E501
    """Obtener todos los episodios asociados a un contenido

    Devuelve una lista de episodios asociados al contenido especificado por su ID. # noqa: E501

    :param id_contenido: ID del contenido para el cual se desean obtener los episodios asociados
    :type id_contenido: int

    :rtype: List[Episodio]
    """
    try:
        content = Contenido_DA.get_content_by_id(id_contenido)
        if content:
            return jsonify([episodio.to_dict() for episodio in content.episodios]), 200
        return jsonify({"message": "Content not found"}), 404
    except Exception as e:
        return str(e), 500


def contenidos_id_contenido_generos_get(id_contenido):  # noqa: E501
    """Obtener todos los géneros asociados a un contenido

    Devuelve una lista de géneros asociados al contenido especificado por su ID. # noqa: E501

    :param id_contenido: ID del contenido para el cual se desean obtener los géneros asociados
    :type id_contenido: int

    :rtype: List[Genero]
    """
    try:
        content = Contenido_DA.get_content_by_id(id_contenido)
        if content:
            return jsonify([genero.to_dict() for genero in content.generos]), 200
        return jsonify({"message": "Content not found"}), 404
    except Exception as e:
        return str(e), 500


def contenidos_id_contenido_get(id_contenido):  # noqa: E501
    """Obtener un contenido por ID

     # noqa: E501

    :param id_contenido: 
    :type id_contenido: int

    :rtype: Contenido
    """
    content = Contenido_DA.get_content_by_id(id_contenido)
    if content:
        return jsonify(content.to_dict()), 200
    return jsonify({"message": "Content not found"}), 404


def contenidos_post(body):  # noqa: E501
    """Crear un nuevo contenido con actores y géneros

    Crea un contenido nuevo y asocia múltiples actores y géneros. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Contenido
    """
    if not body:
        return jsonify({"message": "Invalid input"}), 400
    content = ContenidosBody.from_dict(body)
    new_content = Contenido_DA.create_content(content)
    if new_content:
        return jsonify(new_content.to_dict()), 201
    return jsonify({"message": "Error creating content"}), 500

def contenidos_put(body):  # noqa: E501
    """Actualizar un contenido con actores y géneros asociados"""
    
    if not body:
        return jsonify({"message": "Invalid input"}), 400
    
    # Asegurarse de manejar body como dict
    if isinstance(body, bytes):
        body_dict = json.loads(body.decode('utf-8'))
    elif isinstance(body, dict):
        body_dict = body
    else:
        return jsonify({"message": "Invalid input format"}), 400
    
    # Obtener ID del contenido
    id_contenido = body_dict.get('id_contenido')
    if not id_contenido:
        return jsonify({"message": "id_contenido is required"}), 400
    
    # Convertir a objeto del modelo
    content = ContenidosBody1.from_dict(body_dict)  # Asegúrate de que este método funcione correctamente
    
    # Llamar al DA para actualizar
    updated_content = Contenido_DA.update_content(id_contenido, content)
    
    if updated_content:
        return jsonify(updated_content.to_dict()), 200
    else:
        return jsonify({"message": "Content not found"}), 404