

"""module that returns formated diff."""


from gendiff.formaters.json import json_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.stylish import stylish_formater


def format_diff(diff, formater):
    """Func returns formated diff.

    Args:
        diff: dict with diff between two files
        formater: that chosen by user

    Returns:
        string with formated diff
    """
    if formater == 'stylish':
        return stylish_formater(diff)
    elif formater == 'plain':
        return plain_formater(diff)
    elif formater == 'json':
        return json_formater(diff)
