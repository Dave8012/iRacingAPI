from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.race import RaceModel
from api.schema.race import RaceSchema

race_api = Blueprint('race', __name__)


@race_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Recent Races',
            'schema': RaceSchema
        }
    }
})
def get_race_info():
    """
    Endpoint to return recent race information
    ---
    """
    result = RaceModel()
    return RaceSchema().dump(result), 200
