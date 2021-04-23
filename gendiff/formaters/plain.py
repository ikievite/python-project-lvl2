

"""module with plain formater."""


from gendiff.find_diff import (
    ADDED, CHANGED, NODE_CHILDREN, NODE_NAME, NODE_STATE, NODE_VALUE, REMOVED,
)
from gendiff.formaters.format_value import encode_to_output


def prepare_value(value):  # noqa: WPS110 # ignore warning about var name
    """Func encodes value to the selected view.

    Args:
        value: value from node

    Returns:
        encoded value
    """
    if isinstance(value, dict):
        node_value = '[complex value]'
    elif isinstance(value, str):
        node_value = "'{0}'".format(value)
    else:
        node_value = encode_to_output(value)
    return node_value


def plain_formater(nodes, output, parent=[]):  # noqa: B006, WPS404 # ignore usong list as arg
    """Func builds plain output from diff.

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
            plain_formater(children, output, path)
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
