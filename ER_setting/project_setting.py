from ER_datas.update_game_base_data import update_game_base_data
from ER_apis.ER_api import request_season_info
from ER_setting.apicontroller import Apicontroller
from ER_setting.apimodel import Apimodel
from ER_setting.apiview import Apiview
import dotenv
import os

class ProjectSetting:
    def __init__(self) -> None:        
        self.model = Apimodel()
        self.view = Apiview()
        self.controller = Apicontroller(self.model, self.view)
        
    def make_setting(self):
        self.controller.create_folders()
        self.controller.get_api()
        self.controller.get_test_case()
        self.controller.make_main_py()
        update_game_base_data()
    '''
    def make_env_file(self):
        BS = 16
        NORMAL_MODE_NUMBER = 2
        RANK_MODE_NUMBER = 3
        COBALT_MODE_NUMBER = 6
        OK_RESPONSE=200
        ERROR_RESPONSE_404=404
        ERROR_RESPONSE_429=429
        SEASON_ID = 23
        CHARACTER_FILE_NAME = "./base_datas/Character/Name.json"
        SECRET_FILE_PATH = "./secret.json"
        BASE_DATAS_PATH = "./base_datas/"
        TXT_GAME_BASE_DATA_FILE_NAME = "game_base_data2.txt"
        JSON_GAME_BASE_DATA_FILE_NAME = "game_base_data2.json"
        SECRET_FILE_PATH = "./setting/secret.json"
        BASE_DATAS_PATH = "./base_datas"
        ORIGIN_DATAS_PATH = "./origin_datas"
        TXT_GAME_BASE_DATA_FILE_PATH = "origin_datas/game_base_data.txt"
        TXT_GAME_BASE_DATA_FILE_NAME = "game_base_data.txt"
        RW_EC2_DB_CONNECTION_STRING=""
        READ_EC2_DB_CONNECTION_STRING=""
    '''
    def get_current_season_id_value(self)->int:
        current_season_id = request_season_info(current_season=True).get('seasonID', 0)
        return current_season_id

    def update_env_file(self, modifying_dictionary:dict)->bool:
        env_file = dotenv.find_dotenv()
        if not dotenv.load_dotenv(env_file):
            print("Error: Failed Loading .env File")
            return False
        for key in modifying_dictionary.keys():
            if not dotenv.set_key(env_file, key, str(modifying_dictionary[key]), quote_mode='never'):
                print("Error: Failed modifying .env File")
                return False
        return True
