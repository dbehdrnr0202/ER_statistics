import json
import os
from ER_apis.ER_api import save_games, game_api

# Model
class Apimodel:
    def save_Api_key(self, key):
        api_key_dic = {"token": key}
        with open("setting/secret.json", "w") as file:
            json.dump(api_key_dic, file)
        print(os.path.isfile("setting/secret.json"))

    def test_Api_key(self):
        if game_api:
            save_games(31460173, 1)
            return os.path.isfile("./datas/Ver10.0_Rank_31460173.json")
        else:
            return False

    def create_folders(self):
        if os.path.exists("setting") == False:
            os.mkdir("setting")
        if os.path.exists("datas") == False:
            os.mkdir("datas")
        if os.path.exists("origin_datas") == False:
            os.mkdir("origin_datas")