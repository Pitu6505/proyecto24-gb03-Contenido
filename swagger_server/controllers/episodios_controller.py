import connexion
import six

from swagger_server.models.episodio import Episodio  # noqa: E501
from swagger_server import util


def episodios_get():  # noqa: E501
    """Obtener todos los episodios

     # noqa: E501


    :rtype: List[Episodio]
    """
    return 'do some magic!'


def episodios_id_episodio_delete(id_episodio):  # noqa: E501
    """Eliminar un episodio

     # noqa: E501

    :param id_episodio: 
    :type id_episodio: int

    :rtype: None
    """
    return 'do some magic!'


def episodios_id_episodio_get(id_episodio):  # noqa: E501
    """Obtener un episodio por ID

     # noqa: E501

    :param id_episodio: 
    :type id_episodio: int

    :rtype: Episodio
    """
    return 'do some magic!'


def episodios_post(body):  # noqa: E501
    """Crear un nuevo episodio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Episodio.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def episodios_put(body):  # noqa: E501
    """Actualizar un episodio

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Episodio.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
