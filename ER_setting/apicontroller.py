import os
from ER_apis.ER_api import save_games
import sys
# Controller
class Apicontroller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def create_folders(self):
        self.model.create_folders()

    def get_api(self):
        while True:
            Api_key = self.view.get_Api_key()
            self.model.save_Api_key(Api_key)
            if self.model.test_Api_key():
                os.remove("./datas/Ver10.0_Rank_31460173.json")
                self.view.show_result("입력되었습니다.")
                break
            else:
                self.view.show_result("잘못된 키가 입력되었습니다.")
                sys.exit()

    def get_test_case(self):
        save_games(31131392, 1)
        save_games(31130633, 1)

    def make_main_py(self):
        main = open("main.py", "w")
        main.close()