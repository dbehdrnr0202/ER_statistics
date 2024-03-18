import json
import os
from glob import glob
import itertools
import re


class Tier:
    def __init__(self) -> None:
        with open("./handmadeDB/TierMMRCost/V15/Tier.json", "r", encoding="utf-8") as f:
            self.tier_DB = json.load(f)
        self.tier_DB.pop("name")
        self.tier_names = [name for [name, _, _, _] in self.tier_DB.values()]

    def tier_name(self, mmr: int = 0) -> str:
        for name, start, end, cost in self.tier_DB.values():
            if start <= mmr < end:
                return name
        return name

    def tier_cost(self, n) -> int:
        """n can tier name or mmrBefore"""
        if isinstance(n, str):
            for name, start, end, cost in self.tier_DB.values():
                if n == name:
                    return cost
            return cost
        else:
            for name, start, end, cost in self.tier_DB.values():
                if start <= n < end:
                    return cost
            cost += ((n - start) // end) * 2
            return cost
            print("int")
        # for tier_name,start,end,cost in self.tier_DB.values():
        #     if tier_name==name:
        #         return cost
        # return name


class GameDB:
    def __init__(
        self,
        types: list = ["Colbalt", "Normal", "Rank"],
        major_version: int = ["*"],
        minor_version: int = ["*"],
        root_dir: str = "",
    ) -> None:

        self.game_list = []
        self.dir_list = []
        self.root_dir = os.environ.get("GAME_DB", "./datas")
        if root_dir:
            self.root_dir = root_dir
        if root_dir:
            self.root_dir = root_dir

        cases = list(itertools.product(major_version, minor_version, types))
        for major_ver, minor_ver, type_name in cases:
            self.dir_list += glob(
                f"{self.root_dir}/Ver{major_ver}.{minor_ver}_{type_name}*"
            )
        self.game_list = [re.split("[_.]", file)[-2] for file in self.dir_list]


class GameType:
    def __init__(self) -> None:
        with open("./handmadeDB/game_type.json", "r", encoding="utf-8") as f:
            self.type_num = json.load(f)

        self.num_type = {}
        for key, value in self.type_num.items():
            self.num_type[value] = key


class GameVerson:
    def __init__(self) -> None:
        file_name = "./setting/game_version.json"
        with open(file_name, "r", encoding="utf-8") as f:
            lastest_version = json.load(f)
        self.major = lastest_version.get("CURRENT_GAME_MAJOR_VERSION", 0)
        self.minor = lastest_version.get("CURRENT_GAME_MINOR_VERSION", 0)
        pass
