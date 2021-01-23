

"""module with plain formater."""


def isupdated(nodes, node_name):
    """Func checks if the value has been updated.

    Args:
        nodes: list with nodes
        node_name: name of node

    Returns:
        bool value
    """
    node_list = []
    for node in nodes:
        node_list.append(node['name'])
    if node_list.count(node_name) == 2:
        return True


def find_updated_values(nodes, node_name):
    """Func finds updated values.

    Args:
        nodes: list with nodes
        node_name: name of node

    Returns:
        dict with values
    """
    updated = {}
    for node in nodes:
        if node['name'] == node_name:
            if node['type'] == 'complex':
                updated[node['badge']] = '[complex value]'
            else:
                updated[node['badge']] = node['value']
    return updated


def encode_to_json_type(value):  # noqa: WPS110
    """Func encodes value to json format.

    Args:
        value: value from node

    Returns:
        encoded value
    """
    if value is True:
        node_value = 'true'
    elif value is False:
        node_value = 'false'
    elif value is None:
        node_value = 'null'
    elif value == '[complex value]':
        return value
    else:
        node_value = "'{0}'".format(value)
    return node_value


def plain_formater(diff):
    """Func builds plain output from diff.

    Args:
        diff: list with nodes

    Returns:
        output: formated diff
    """
    diff.sort(key=lambda node: node['name'])
    output = []

    def iter_node(nodes, parent):  # noqa: WPS430
        updated_nodes = []
        for node in nodes:  # noqa: WPS426, WPS442
            path = parent.split()
            path.append(node['name'])
            path = '.'.join(path)
            if node['type'] == 'nested':
                node['children'].sort(key=lambda child: child['name'])
                iter_node(node['children'], parent + ' ' + node['name'])  # noqa: WPS336
            elif isupdated(nodes, node['name']):
                if node['name'] not in updated_nodes:
                    updated_nodes.append(node['name'])
                    updated_values = find_updated_values(nodes, node['name'])
                    output.append("Property '{0}' was updated. From {1} to {2}".format(
                        path,
                        encode_to_json_type(updated_values['-']),
                        encode_to_json_type(updated_values['+']),
                    ))
            elif node['badge'] == '+':
                if node['type'] == 'complex':
                    output.append("Property '{0}' was added with value: [complex value]".format(
                        path,
                    ))
                else:
                    output.append("Property '{0}' was added with value: {1}".format(
                        path, encode_to_json_type(node['value']),
                    ))
            elif node['badge'] == '-':
                output.append("Property '{0}' was removed".format(path))
        return '\n'.join(output)
    return iter_node(diff, '')
