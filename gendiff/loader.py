

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
        with open(filename) as f:  # noqa: WPS111 # ignore too short name
            if 'json' in filename:
                return json.load(f)
            elif 'yaml' in filename or 'yml' in filename:
                return yaml.safe_load(f)
            raise Exception('Wrong file type, neither json nor yaml/yml')
    except Exception:  # noqa: WPS329 # ignore allow `except` case
        raise
