

"""module with json formater."""


import json


def json_formater(diff):
    """Func returns diff in json format.

    Args:
        diff: list with nodes

    Returns:
        output in json format
    """
    return json.dumps(diff, indent=4)
