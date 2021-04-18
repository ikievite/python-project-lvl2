

"""module that returns formated diff."""


from gendiff.formaters.json import json_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.stylish import stylish_formater

STYLISH_VIEW = 'stylish'
PLAIN_VIEW = 'plain'
JSON_VIEW = 'json'


def format_diff(diff, formater):
    """Func returns formated diff.

    Args:
        diff: dict with diff between two files
        formater: that chosen by user

    Returns:
        string with formated diff
    """
    if formater == STYLISH_VIEW:
        return stylish_formater(diff)
    elif formater == PLAIN_VIEW:
        return plain_formater(diff)
    elif formater == JSON_VIEW:
        return json_formater(diff)
