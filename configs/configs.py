import os.path

import yaml


# Load the YAML file
def load_config_values(module_name):
    file_path = os.path.join(os.getenv("PWD"), 'configs', module_name, "test_aut-qa.yml")
    with open(file_path, 'r') as file:
        locators = yaml.safe_load(file)
    return dict(locators)
