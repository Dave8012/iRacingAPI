import json
import os
from api.service.iracingConnectionService import IRacingAPI


class RaceModel:
    def __init__(self):
        IR_USERNAME = os.getenv('IR_USERNAME')
        IR_ENCODED_PASSWORD = os.getenv('IR_ENCODED_PASSWORD')

        self.message = "Information about the last 10 races"
        self.api_instance = IRacingAPI(IR_USERNAME, IR_ENCODED_PASSWORD)
        self.recent_race_list = None
        self.race_list = None
        self.fill_race_info()

    def fill_race_info(self):

        self.recent_race_list = self.api_instance.get_recent_races()
        self.extract_recent_race_info()

    def extract_recent_race_info(self):

        parsed_races = []
        recent_race_list = self.recent_race_list["races"]

        for race in recent_race_list:

            data = {
                "series_name": race["series_name"],
                "track_name": race["track"]["track_name"],
                "finish_position": race["finish_position"],
                "start_position": race["start_position"],
                "incidents": race["incidents"]
            }

            parsed_races.append(data)

        self.race_list = parsed_races



