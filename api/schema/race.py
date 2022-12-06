from flask_marshmallow import Schema
from marshmallow.fields import Str, Dict, List, Raw


class RaceSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ['message',
                  'race_list']

    message = Str()
    race_list = Raw()
