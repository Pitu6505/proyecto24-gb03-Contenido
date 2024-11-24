#!/usr/bin/env python3

import connexion

from swagger_server.database_setup import Base, engine
from swagger_server import encoder


def main():
    Base.metadata.create_all(engine)
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Microservicio de Contenido'}, pythonic_params=True)
    app.run(port=8081, debug=True)


if __name__ == '__main__':
    main()
