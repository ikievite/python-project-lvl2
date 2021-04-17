

"""File loader."""


import json

import yaml


def loader(filepath):
    """Func load json or yaml files.

    Args:
        filepath: path to file

    Returns:
        conten of file

    Raises:
        Exception: if wrong file type given
    """
    filepath = filepath.lower()
    try:
        with open(filepath) as f:  # noqa: WPS111 # ignore too short name
            if 'json' in filepath:
                return json.load(f)
            elif 'yaml' in filepath or 'yml' in filepath:
                return yaml.safe_load(f)
            raise Exception('Wrong file type, neither json nor yaml/yml')
    except Exception:  # noqa: WPS329 # ignore allow `except` case
        raise
