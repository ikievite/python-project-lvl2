

"""module with json formater."""


import json


def json_formater(diff):
    """Func returns diff in json format.

    Args:
        diff: list with nodes

    Returns:
        output in json format
    """
    diff.sort(key=lambda node: node['name'])

    def iter_node(nodes):  # noqa: WPS430
        for node in nodes:  # noqa: WPS426, WPS442
            if node['type'] == 'nested':
                node['children'].sort(key=lambda child: child['name'])
                iter_node(node['children'])
        return json.dumps(diff, indent=4)
    return iter_node(diff)
