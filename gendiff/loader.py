

"""File loader."""


import json
import pathlib

import yaml


class BadFileType(Exception):
    """A class to represent wrong file tyle."""

    pass  # noqa: WPS420, WPS604 # ignore wrong keyword: ipass, ncorrect node inside `class` body


def loader(filepath):
    """Func load json or yaml files.

    Args:
        filepath: path to file

    Returns:
        conten of file

    Raises:
         BadFileType: if wrong file type given
    """
    file_extention = pathlib.Path(filepath).suffix.lower()
    with open(filepath) as f:  # noqa: WPS111 # ignore too short name
        if file_extention == '.json':
            return json.load(f)
        elif file_extention == '.yaml' or file_extention == '.yml':  # noqa: WPS514 # implicit `in`
            return yaml.safe_load(f)
        raise BadFileType('Wrong file type, neither json nor yaml/yml')
