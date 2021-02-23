

"""File loader."""


import json

import yaml


def loader(filename):
    """Func load json or yaml files.

    Args:
        filename: path to file

    Returns:
        conten of file

    Raises:
        Exception: if wrong file type given
    """
    filename = filename.lower()
    try:
        if 'json' in filename:
            with open(filename) as json_file:
                return json.load(json_file)
        elif 'yaml' in filename or 'yml' in filename:
            with open(filename) as yaml_file:
                return yaml.safe_load(yaml_file)
        else:
            raise Exception('Wrong file type, neither json nor yaml/yml')
    except Exception:  # noqa: WPS329
        raise
