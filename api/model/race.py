import json
import os
from api.service.iracingConnectionService import IRacingAPI


class RaceModel:
    def __init__(self):
        IR_USERNAME = os.getenv('IR_USERNAME')
        IR_ENCODED_PASSWORD = os.getenv('IR_ENCODED_PASSWORD')

        self.message = "Check out my recent races!"
        self.api_instance = IRacingAPI(IR_USERNAME, IR_ENCODED_PASSWORD)
        self.recent_race_list = None
        self.formatted_race_list = {'races': []}
        self.fill_race_info()

    def fill_race_info(self):

        self.recent_race_list = self.api_instance.get_recent_races()
        self.extract_recent_race_info()

    def extract_recent_race_info(self):

        races = self.recent_race_list['races']

        for race in races:

            print("RACE: " + str(race))
            data = {}
            data['series_name'] = race['series_name']
            data['track_name'] = race['track']['track_name']
            data['finish_position'] = race['finish_position']
            data['start_position'] = race['start_position']
            data['incidents'] = race['incidents']

            self.formatted_race_list['races'].append(data)



