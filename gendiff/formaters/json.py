

"""module with json formater."""


import json


def json_formater(diff):
    """Func returns diff in json format.

    Args:
        diff: list with nodes

    Returns:
        output in json format
    """
    def iter_node(nodes):  # noqa: WPS430
        nodes.sort(key=lambda entry: entry['name'])
        for node in nodes:  # noqa: WPS426, WPS442
            if node['type'] == 'nested':
                iter_node(node['children'])
        return json.dumps(diff, indent=4)
    return iter_node(diff)
