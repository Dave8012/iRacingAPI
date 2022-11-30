from flask_marshmallow import Schema
from marshmallow.fields import Str


class RaceSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ['message',
                  'formatted_race_list']

    message = Str()
    formatted_race_list = Str()
