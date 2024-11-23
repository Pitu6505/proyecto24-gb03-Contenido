# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.episodio import Episodio  # noqa: E501
from swagger_server.test import BaseTestCase


class TestEpisodiosController(BaseTestCase):
    """EpisodiosController integration test stubs"""

    def test_episodios_get(self):
        """Test case for episodios_get

        Obtener todos los episodios
        """
        response = self.client.open(
            '/api/episodios',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_episodios_id_episodio_delete(self):
        """Test case for episodios_id_episodio_delete

        Eliminar un episodio
        """
        response = self.client.open(
            '/api/episodios/{id_episodio}'.format(id_episodio=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_episodios_id_episodio_get(self):
        """Test case for episodios_id_episodio_get

        Obtener un episodio por ID
        """
        response = self.client.open(
            '/api/episodios/{id_episodio}'.format(id_episodio=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_episodios_post(self):
        """Test case for episodios_post

        Crear un nuevo episodio
        """
        body = Episodio()
        response = self.client.open(
            '/api/episodios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_episodios_put(self):
        """Test case for episodios_put

        Actualizar un episodio
        """
        body = Episodio()
        response = self.client.open(
            '/api/episodios',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
