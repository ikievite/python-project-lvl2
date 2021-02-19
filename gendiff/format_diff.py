

"""module that returns formated diff."""


from gendiff.formaters.json import json_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.stylish import stylish_formater

CHOICE_STYLISH = 'stylish'
CHOICE_PLAIN = 'plain'
CHOICE_JSON = 'json'


def format_diff(diff, formater):
    """Func returns formated diff.

    Args:
        diff: dict with diff between two files
        formater: that chosen by user

    Returns:
        string with formated diff

    Raises:
        Exception: if wrong formater given
    """
    try:  # noqa: WPS229
        if formater == CHOICE_STYLISH:
            return stylish_formater(diff)
        elif formater == CHOICE_PLAIN:
            return plain_formater(diff)
        elif formater == CHOICE_JSON:
            return json_formater(diff)
        raise Exception("unsupported formater type '{}'".format(formater))  # noqa: P101
    except Exception as e:  # noqa: WPS111
        print('Exception: ' + str(e))  # noqa: WPS421, WPS336
        raise
