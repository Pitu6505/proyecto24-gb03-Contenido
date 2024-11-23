import connexion
import six

from swagger_server.models.episodio import Episodio  # noqa: E501
from swagger_server import util
from flask import jsonify
from swagger_server.data_access.Episodio_DA import Episodio_DA



def episodios_get():  # noqa: E501
    """Obtener todos los episodios

     # noqa: E501


    :rtype: List[Episodio]
    """
    try:
        episodios = Episodio_DA.get_all_episodes()
        if episodios is None:
            return jsonify({"error": "No se pudieron obtener los episodios"}), 500
        return jsonify([episodio.to_dict() for episodio in episodios]), 200
    except Exception as e:
        print(f"Error al obtener los episodios: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def episodios_id_episodio_delete(id_episodio):  # noqa: E501
    """Eliminar un episodio

     # noqa: E501

    :param id_episodio: 
    :type id_episodio: int

    :rtype: None
    """
    try:
        result = Episodio_DA.delete_episode(id_episodio)
        if result:
            return jsonify({"message": "Episodio eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Episodio no encontrado"}), 404
    except Exception as e:
        print(f"Error al eliminar el episodio: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def episodios_id_episodio_get(id_episodio):  # noqa: E501
    """Obtener un episodio por ID

     # noqa: E501

    :param id_episodio: 
    :type id_episodio: int

    :rtype: Episodio
    """
    try:
        episodio = Episodio_DA.get_episode_by_id(id_episodio)
        if episodio is None:
            return jsonify({"error": "Episodio no encontrado"}), 404
        return jsonify(episodio.to_dict()), 200
    except Exception as e:
        print(f"Error al obtener el episodio: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def episodios_post(body):  # noqa: E501
    """Crear un nuevo episodio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            body = Episodio.from_dict(connexion.request.get_json())  # noqa: E501
            nuevo_episodio = Episodio_DA.create_episode(body)
            if nuevo_episodio:
                return jsonify({"message": "Episodio creado exitosamente"}), 201
            else:
                return jsonify({"error": "Error al crear el episodio"}), 500
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al crear el episodio: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def episodios_put(body):  # noqa: E501
    """Actualizar un episodio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            body = Episodio.from_dict(connexion.request.get_json())  # noqa: E501
            episodio_actualizado = Episodio_DA.update_episode(body.id_episodio, body)
            if episodio_actualizado:
                return jsonify({"message": "Episodio actualizado exitosamente"}), 200
            else:
                return jsonify({"error": "Episodio no encontrado"}), 404
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al actualizar el episodio: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
