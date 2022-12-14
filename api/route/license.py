from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.model.license import LicenseModel
from api.schema.license import LicenseSchema

license_api = Blueprint('license', __name__)


@license_api.route('/')
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Welcome to my iRacing stats API',
            'schema': LicenseSchema
        }
    }
})
def get_license_info():
    """
    Endpoint to return license/rating information
    ---
    """
    result = LicenseModel()
    return LicenseSchema().dump(result), 200
