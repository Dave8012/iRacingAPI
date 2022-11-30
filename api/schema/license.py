from flask_marshmallow import Schema
from marshmallow.fields import Str, Float, Integer


class LicenseSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ['message',
                  'road_safety_rating',
                  'road_irating',
                  'oval_safety_rating',
                  'oval_irating']

    message = Str()
    road_safety_rating = Float()
    road_irating = Integer()
    oval_safety_rating = Float()
    oval_irating = Integer()
