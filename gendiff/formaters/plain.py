

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
    for node in nodes:
        if node['name'] == node_name:
            if node['badge'] == '-':
                if node['type'] == 'complex':
                    removed = '[complex value]'
                else:
                    removed = node['value']
            elif node['badge'] == '+':
                if node['type'] == 'complex':
                    added = '[complex value]'
                else:
                    added = node['value']
    return {'removed': removed, 'added': added}


def plain_formater(diff):
    """Func builds plain output from diff.

    Args:
        diff: list with nodes

    Returns:
        output: formated diff
    """
    diff.sort(key=lambda node: node['name'])
    output = []

    def iter_node(nodes, path):  # noqa: WPS430
        updated_nodes = []
        for node in nodes:  # noqa: WPS426, WPS442
            node_path = path + '.' + node['name']  # noqa: WPS336
            node_path = node_path[1:]
            if node['type'] == 'nested':
                node['children'].sort(key=lambda child: child['name'])
                iter_node(node['children'], path + '.' + node['name'])  # noqa: WPS336
            elif isupdated(nodes, node['name']):
                if node['name'] not in updated_nodes:
                    updated_nodes.append(node['name'])
                    updated_values = find_updated_values(nodes, node['name'])
                    output.append("Property '{0}' was updated. From '{1}' to '{2}'".format(
                        node_path, updated_values['removed'], updated_values['added'],
                    ))
            elif node['badge'] == '+':
                if node['type'] == 'complex':
                    output.append("Property '{0}' was added with value: '[complex value]'".format(
                        node_path,
                    ))
                else:
                    output.append("Property '{0}' was added with value: '{1}'".format(
                        node_path, node['value'],
                    ))
            elif node['badge'] == '-':
                output.append("Property '{0}' was removed".format(node_path))
        return '\n'.join(output)
    return iter_node(diff, '')
