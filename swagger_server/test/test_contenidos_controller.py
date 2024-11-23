# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.models.contenidos_body import ContenidosBody  # noqa: E501
from swagger_server.models.contenidos_body1 import ContenidosBody1  # noqa: E501
from swagger_server.models.episodio import Episodio  # noqa: E501
from swagger_server.models.genero import Genero  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContenidosController(BaseTestCase):
    """ContenidosController integration test stubs"""

    def test_contenidos_filtrar_get(self):
        """Test case for contenidos_filtrar_get

        Filtrar contenidos por nombre, actor y género
        """
        query_string = [('titulo', 'titulo_example'),
                        ('nombre_actor', 'nombre_actor_example'),
                        ('nombre_genero', 'nombre_genero_example')]
        response = self.client.open(
            '/api/contenidos/filtrar',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_get(self):
        """Test case for contenidos_get

        Obtener todos los contenidos
        """
        response = self.client.open(
            '/api/contenidos',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_id_contenido_actores_get(self):
        """Test case for contenidos_id_contenido_actores_get

        Obtener todos los actores asociados a un contenido
        """
        response = self.client.open(
            '/api/contenidos/{id_contenido}/actores'.format(id_contenido=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_id_contenido_delete(self):
        """Test case for contenidos_id_contenido_delete

        Eliminar un contenido
        """
        response = self.client.open(
            '/api/contenidos/{id_contenido}'.format(id_contenido=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_id_contenido_episodios_get(self):
        """Test case for contenidos_id_contenido_episodios_get

        Obtener todos los episodios asociados a un contenido
        """
        response = self.client.open(
            '/api/contenidos/{id_contenido}/episodios'.format(id_contenido=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_id_contenido_generos_get(self):
        """Test case for contenidos_id_contenido_generos_get

        Obtener todos los géneros asociados a un contenido
        """
        response = self.client.open(
            '/api/contenidos/{id_contenido}/generos'.format(id_contenido=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_id_contenido_get(self):
        """Test case for contenidos_id_contenido_get

        Obtener un contenido por ID
        """
        response = self.client.open(
            '/api/contenidos/{id_contenido}'.format(id_contenido=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_post(self):
        """Test case for contenidos_post

        Crear un nuevo contenido con actores y géneros
        """
        body = ContenidosBody1()
        response = self.client.open(
            '/api/contenidos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contenidos_put(self):
        """Test case for contenidos_put

        Actualizar un contenido con actores y géneros asociados
        """
        body = ContenidosBody()
        response = self.client.open(
            '/api/contenidos',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
