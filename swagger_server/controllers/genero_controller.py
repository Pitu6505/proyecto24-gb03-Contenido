import connexion
import six

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.models.genero import Genero  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Genero_DA import Genero_DA
from flask import jsonify, request



def generos_get():  # noqa: E501
    """Obtener todos los géneros

     # noqa: E501


    :rtype: List[Genero]
    """
    try:
        generos = Genero_DA.get_all_genres()
        if generos is None:
            return jsonify({"error": "No se pudieron obtener los géneros"}), 500
        return jsonify([genero.to_dict() for genero in generos]), 200
    except Exception as e:
        print(f"Error al obtener los géneros: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def generos_id_genero_contenidos_get(id_genero):  # noqa: E501
    """Obtener todos los contenidos asociados a un género

    Devuelve una lista de contenidos asociados a un género, dado su ID. # noqa: E501

    :param id_genero: ID del género para obtener los contenidos asociados
    :type id_genero: int

    :rtype: List[Contenido]
    """
    try:
        genre = Genero_DA.get_genre_by_id(id_genero)
        if genre:
            contents = genre.contenidos
            return jsonify([content.to_dict() for content in contents])
        else:
            return "Genre not found", 404
    except Exception as e:
        return str(e), 500


def generos_id_genero_delete(id_genero):  # noqa: E501
    """Eliminar un género

    Elimina un género por su ID. # noqa: E501

    :param id_genero: ID del género a eliminar
    :type id_genero: int

    :rtype: None
    """
    try:
        result = Genero_DA.delete_genre(id_genero)
        if result:
            return jsonify({"message": "Género eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Género no encontrado"}), 404
    except Exception as e:
        print(f"Error al eliminar el género: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def generos_post(body):  # noqa: E501
    """Crear un nuevo género

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            body = Genero.from_dict(connexion.request.get_json())  # noqa: E501
            nuevo_genero = Genero_DA.create_genre(body)
            if nuevo_genero:
                return jsonify({"message": "Género creado exitosamente"}), 201
            else:
                return jsonify({"error": "Error al crear el género"}), 500
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al crear el género: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def generos_put(body):  # noqa: E501
    """Actualizar un género

    Actualiza los datos de un género existente. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Genero
    """
    try:
        if connexion.request.is_json:
            body = Genero.from_dict(connexion.request.get_json())  # noqa: E501
            genero_actualizado = Genero_DA.update_genre(body.id_genero, body)
            if genero_actualizado:
                return jsonify({"message": "Género actualizado exitosamente"}), 200
            else:
                return jsonify({"error": "Género no encontrado"}), 404
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al actualizar el género: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
