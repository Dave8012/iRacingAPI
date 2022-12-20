from flask import Flask
from flasgger import Swagger
from api.route.license import license_api
from api.route.race import race_api


app = Flask(__name__)

app.config['SWAGGER'] = {
    'title': 'iRacing API Docs',
}
swagger = Swagger(app)

# Initialize Config
app.config.from_pyfile('config.py')
app.register_blueprint(license_api, url_prefix='/license')
app.register_blueprint(race_api, url_prefix='/race')


