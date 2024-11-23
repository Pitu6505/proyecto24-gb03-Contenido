# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.actor import Actor  # noqa: E501
from swagger_server.models.contenido import Contenido  # noqa: E501
from swagger_server.test import BaseTestCase


class TestActorController(BaseTestCase):
    """ActorController integration test stubs"""

    def test_actores_get(self):
        """Test case for actores_get

        Obtener todos los actores
        """
        response = self.client.open(
            '/api/actores',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_id_actor_contenidos_get(self):
        """Test case for actores_id_actor_contenidos_get

        Obtener todos los contenidos asociados a un actor
        """
        response = self.client.open(
            '/api/actores/{id_actor}/contenidos'.format(id_actor=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_id_actor_delete(self):
        """Test case for actores_id_actor_delete

        Eliminar un actor
        """
        response = self.client.open(
            '/api/actores/{id_actor}'.format(id_actor=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_id_actor_get(self):
        """Test case for actores_id_actor_get

        Obtener un actor por ID
        """
        response = self.client.open(
            '/api/actores/{id_actor}'.format(id_actor=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_post(self):
        """Test case for actores_post

        Crear un nuevo actor
        """
        body = Actor()
        response = self.client.open(
            '/api/actores',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_actores_put(self):
        """Test case for actores_put

        Actualizar un actor
        """
        body = Actor()
        response = self.client.open(
            '/api/actores',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
