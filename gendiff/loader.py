

"""File loader."""


import json

import yaml


def loader(filename):
    """Func load json or yaml files.

    Args:
        filename: path to file

    Returns:
        conten of file
    """
    if filename.endswith('json'):
        with open(filename) as json_file:
            return json.load(json_file)
    elif filename.endswith('yaml') or filename.endswith('yml'):
        with open(filename) as yaml_file:
            return yaml.safe_load(yaml_file)
