from ER_setting.project_setting import ProjectSetting
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument(
    "--u", help="Want to update .env file values?", type=bool, default=True
)
if __name__=="__main__":
    project_setting = ProjectSetting()
    project_setting.make_setting()
    if argument_parser.parse_args().u:
        project_setting.update_env_file(
            modifying_dictionary={
                "SEASON_ID":project_setting.get_current_season_id_value()
            }
        )