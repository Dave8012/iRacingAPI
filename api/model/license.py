import os
from api.service.iracingConnectionService import IRacingAPI


class LicenseModel:
    def __init__(self):
        IR_USERNAME = os.getenv('IR_USERNAME')
        IR_ENCODED_PASSWORD = os.getenv('IR_ENCODED_PASSWORD')

        self.message = "Check out my stats!"
        self.api_instance = IRacingAPI(IR_USERNAME, IR_ENCODED_PASSWORD)
        self.road_safety_rating = None
        self.road_irating = None
        self.oval_safety_rating = None
        self.oval_irating = None
        self.fill_license_info()

    def fill_license_info(self):

        member_info_json = self.api_instance.get_member_info()

        # Extracting JSON data
        license_json = member_info_json["licenses"]
        oval_info = license_json["oval"]
        road_info = license_json["road"]

        # Setting values
        self.oval_safety_rating = oval_info["safety_rating"]
        self.oval_irating = oval_info["irating"]
        self.road_safety_rating = road_info["safety_rating"]
        self.road_irating = road_info["irating"]

