import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server import util
from swagger_server.data_access.Actor_DA import Actor_DA
from flask import jsonify



def actores_get():  # noqa: E501
    """Obtener todos los actores

     # noqa: E501


    :rtype: List[Actor]
    """
    try:
        actores = Actor_DA.get_all_actors()
        if actores is None:
            return jsonify({"error": "No se pudieron obtener los actores"}), 500
        return jsonify([actor.to_dict() for actor in actores]), 200
    except Exception as e:
        print(f"Error al obtener los actores: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def actores_id_actor_contenidos_get(id_actor):  # noqa: E501
    """Obtener todos los contenidos asociados a un actor

    Devuelve una lista de contenidos asociados a un actor, dado su ID. # noqa: E501

    :param id_actor: ID del actor para obtener los contenidos asociados
    :type id_actor: int

    :rtype: List[Contenido]
    """
    try:
        contents = Actor_DA.get_contents_by_actor_id(id_actor)
        if contents:
            return jsonify([content.to_dict() for content in contents])
        else:
            return "Actor not found", 404
    except Exception as e:
        return str(e), 500


def actores_id_actor_delete(id_actor):  # noqa: E501
    """Eliminar un actor

     # noqa: E501

    :param id_actor: 
    :type id_actor: int

    :rtype: None
    """
    try:
        result = Actor_DA.delete_actor(id_actor)
        if result:
            return jsonify({"message": "Actor eliminado exitosamente"}), 200
        else:
            return jsonify({"error": "Actor no encontrado"}), 404
    except Exception as e:
        print(f"Error al eliminar el actor: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def actores_id_actor_get(id_actor):  # noqa: E501
    """Obtener un actor por ID

     # noqa: E501

    :param id_actor: 
    :type id_actor: int

    :rtype: Actor
    """
    try:
        actor = Actor_DA.get_actor_by_id(id_actor)
        if actor is None:
            return jsonify({"error": "Actor no encontrado"}), 404
        return jsonify(actor.to_dict()), 200
    except Exception as e:
        print(f"Error al obtener el actor: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500


def actores_post(body):  # noqa: E501
    """Crear un nuevo actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            actor = Actor.from_dict(connexion.request.get_json())  # noqa: E501
            print("Body:")
            print(actor)
            nuevo_actor = Actor_DA.create_actor(actor)
            if nuevo_actor:
                return jsonify({"message": "Actor creado exitosamente"}), 201
            else:
                return jsonify({"error": "Error al crear el actor"}), 500
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al crear el actor: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500




def actores_put(body):  # noqa: E501
    """Actualizar un actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    try:
        if connexion.request.is_json:
            body = Actor.from_dict(connexion.request.get_json())  # noqa: E501
            actor_actualizado = Actor_DA.update_actor(body.id_actor, body)
            if actor_actualizado:
                return jsonify({"message": "Actor actualizado exitosamente"}), 200
            else:
                return jsonify({"error": "Actor no encobntrado"}), 404
        else:
            return jsonify({"error": "El cuerpo de la solicitud no es JSON"}), 400
    except Exception as e:
        print(f"Error al actualizar el actor: {e}")
        return jsonify({"error": "Error interno del servidor"}), 500
