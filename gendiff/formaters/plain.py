

"""module with plain formater."""


from gendiff.find_diff import (
    ADDED, CHANGED, NODE_CHILDREN, NODE_NAME, NODE_STATE, NODE_VALUE, REMOVED,
)


def prepare_value(value):  # noqa: WPS110 # ignore warning about var name
    """Func encodes value to the selected view.

    Args:
        value: value from node

    Returns:
        encoded value
    """
    if value is True:  # noqa: WPS223 # ignore warning about too many `elif` branches: 4 > 3
        node_value = 'true'
    elif value is False:
        node_value = 'false'
    elif value is None:
        node_value = 'null'
    elif isinstance(value, dict):
        node_value = '[complex value]'
    elif isinstance(value, str):
        node_value = "'{0}'".format(value)
    else:
        node_value = value
    return node_value


def iter_node(nodes, output, parent=[]):  # noqa: B006, WPS404 # ignore using list as argument
    """Func finds and returns plain diff from list with diff dicts.

    Args:
        nodes: list with nodes
        output: list with diff lines
        parent: parent list

    Returns:
        output: formated diff
    """
    for node in sorted(nodes, key=lambda node: node[NODE_NAME]):  # noqa: WPS440 # var overlap
        path = [*parent, node[NODE_NAME]]
        joined_path = '.'.join(path)
        children = node.get(NODE_CHILDREN)
        if children:
            iter_node(children, output, path)
        elif node[NODE_STATE] == CHANGED:
            removed_value = prepare_value(node[NODE_VALUE][REMOVED])
            added_value = prepare_value(node[NODE_VALUE][ADDED])
            output.append("Property '{0}' was updated. From {1} to {2}".format(
                joined_path,
                removed_value,
                added_value,
            ))
        elif node[NODE_STATE] == ADDED:
            if isinstance(node[NODE_VALUE], dict):
                output.append("Property '{0}' was added with value: [complex value]".format(
                    joined_path,
                ))
            else:
                output.append("Property '{0}' was added with value: {1}".format(
                    joined_path, prepare_value(node[NODE_VALUE]),
                ))
        elif node[NODE_STATE] == REMOVED:
            output.append("Property '{0}' was removed".format(joined_path))
    return '\n'.join(output)


def plain_formater(diff):
    """Func builds plain diff.

    Args:
        diff: list with diff dicts

    Returns:
        output: formated diff
    """
    return iter_node(diff, [])
