import connexion
import six

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.models.genero import Genero  # noqa: E501
from swagger_server import util


def generos_get():  # noqa: E501
    """Obtener todos los géneros

     # noqa: E501


    :rtype: List[Genero]
    """
    return 'do some magic!'


def generos_id_genero_contenidos_get(id_genero):  # noqa: E501
    """Obtener todos los contenidos asociados a un género

    Devuelve una lista de contenidos asociados a un género, dado su ID. # noqa: E501

    :param id_genero: ID del género para obtener los contenidos asociados
    :type id_genero: int

    :rtype: List[Contenido]
    """
    return 'do some magic!'


def generos_id_genero_delete(id_genero):  # noqa: E501
    """Eliminar un género

    Elimina un género por su ID. # noqa: E501

    :param id_genero: ID del género a eliminar
    :type id_genero: int

    :rtype: None
    """
    return 'do some magic!'


def generos_post(body):  # noqa: E501
    """Crear un nuevo género

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Genero.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def generos_put(body):  # noqa: E501
    """Actualizar un género

    Actualiza los datos de un género existente. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Genero
    """
    if connexion.request.is_json:
        body = Genero.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
