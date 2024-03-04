import sys
# View
class Apiview:
    def get_Api_key(self):
        if len(sys.argv) == 2:
            return sys.argv[1]
        elif len(sys.argv) > 2:
            print("다시 입력해주세요.")
            sys.exit()
        else:
            return input("키를 입력해주세요:")

    def show_result(self, result):
        print(result)