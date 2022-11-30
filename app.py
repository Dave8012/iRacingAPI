from flask import Flask
from flasgger import Swagger
from api.route.info import info_api


def create_app():
    app = Flask(__name__)

    app.config['SWAGGER'] = {
        'title': 'iRacing API Docs',
    }
    swagger = Swagger(app)

    # Initialize Config
    app.config.from_pyfile('config.py')
    app.register_blueprint(info_api, url_prefix='/info')

    return app


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
