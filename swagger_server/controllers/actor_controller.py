import connexion
import six

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server import util


def actores_get():  # noqa: E501
    """Obtener todos los actores

     # noqa: E501


    :rtype: List[Actor]
    """
    return 'do some magic!'


def actores_id_actor_contenidos_get(id_actor):  # noqa: E501
    """Obtener todos los contenidos asociados a un actor

    Devuelve una lista de contenidos asociados a un actor, dado su ID. # noqa: E501

    :param id_actor: ID del actor para obtener los contenidos asociados
    :type id_actor: int

    :rtype: List[Contenido]
    """
    return 'do some magic!'


def actores_id_actor_delete(id_actor):  # noqa: E501
    """Eliminar un actor

     # noqa: E501

    :param id_actor: 
    :type id_actor: int

    :rtype: None
    """
    return 'do some magic!'


def actores_id_actor_get(id_actor):  # noqa: E501
    """Obtener un actor por ID

     # noqa: E501

    :param id_actor: 
    :type id_actor: int

    :rtype: Actor
    """
    return 'do some magic!'


def actores_post(body):  # noqa: E501
    """Crear un nuevo actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Actor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def actores_put(body):  # noqa: E501
    """Actualizar un actor

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Actor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
