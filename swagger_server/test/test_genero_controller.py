# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.models.genero import Genero  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGeneroController(BaseTestCase):
    """GeneroController integration test stubs"""

    def test_generos_get(self):
        """Test case for generos_get

        Obtener todos los géneros
        """
        response = self.client.open(
            '/api/generos',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generos_id_genero_contenidos_get(self):
        """Test case for generos_id_genero_contenidos_get

        Obtener todos los contenidos asociados a un género
        """
        response = self.client.open(
            '/api/generos/{id_genero}/contenidos'.format(id_genero=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generos_id_genero_delete(self):
        """Test case for generos_id_genero_delete

        Eliminar un género
        """
        response = self.client.open(
            '/api/generos/{id_genero}'.format(id_genero=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generos_post(self):
        """Test case for generos_post

        Crear un nuevo género
        """
        body = Genero()
        response = self.client.open(
            '/api/generos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_generos_put(self):
        """Test case for generos_put

        Actualizar un género
        """
        body = Genero()
        response = self.client.open(
            '/api/generos',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
