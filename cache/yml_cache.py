import yaml
from functools import cache

@cache
def get_configs(filename):
    filename= filename.strip()
    with open(f"configs/{filename}.yml") as f:
        config = yaml.safe_load(f)
        return config

