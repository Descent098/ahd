import os                             # Used primarily to validate paths
from configparser import ConfigParser # Used to serialize and de-serialize legacy config files

# Third-party dependencies
import yaml
import colored                        # Used to colour terminal output

def migrate_config():
    """Migrates pre V0.5.0 configs to the new standard"""

    # Configuration file locations
    CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}ahd.yml"
    OLD_CONFIG_FILE_PATH = f"{os.path.dirname(__file__)}{os.sep}.ahdconfig"
    if os.path.isfile(OLD_CONFIG_FILE_PATH):
        print(f"{colored.fg(1)}Old Configuration file found in {OLD_CONFIG_FILE_PATH} automatically migrating to version 0.5.0+{colored.fg(15)}")
        with open(OLD_CONFIG_FILE_PATH, "r") as old_config_file:
            old_config = ConfigParser()
            old_config.readfp(old_config_file)
            old_config = dict(old_config)
            del(old_config['DEFAULT'])
        for section in old_config:
            old_config[section] = {"command": old_config[section]["command"], "paths":old_config[section]["paths"]}
        new_config = {}
        new_config["macros"] = old_config
        with open(CONFIG_FILE_PATH, "w") as new_config_file:
            yaml.dump(new_config, new_config_file, default_flow_style=False)
        del old_config

        valid = False
        while not valid:
            remove_legacy = input("Would you like to remove the old configuration file (y or n)?")
            if remove_legacy.lower().startswith("y"):
                os.remove(OLD_CONFIG_FILE_PATH)
            elif remove_legacy.lower().startswith("n"):
                return True
            else:
                print("Please enter Y to remove config or N to not")
                continue


    else: # If no legacy configs are present
        return False