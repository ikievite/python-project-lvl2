

"""module with plain formater."""


from gendiff.find_diff import (
    ADDED, CHANGED, NODE_CHILDREN, NODE_NAME, NODE_STATE, NODE_VALUE, REMOVED,
)


def encode_to_json_type(value):  # noqa: WPS110 # ignore warning about var name
    """Func encodes value to json format.

    Args:
        value: value from node

    Returns:
        encoded value
    """
    if value is True:  # noqa: WPS223 # ignore too many `elif`
        node_value = 'true'
    elif value is False:
        node_value = 'false'
    elif value is None:
        node_value = 'null'
    elif isinstance(value, int):
        node_value = value
    elif isinstance(value, dict):
        node_value = '[complex value]'
    else:
        node_value = "'{0}'".format(value)
    return node_value


def plain_formater(diff):  # noqa: WPS210 # Found too many local variables: 7 > 6
    """Func builds plain output from diff.

    Args:
        diff: list with nodes

    Returns:
        output: formated diff
    """
    output = []

    def iter_node(nodes, parent):  # noqa: WPS430 # ignore warn about nested function
        for node in sorted(nodes, key=lambda node: node[NODE_NAME]):  # noqa: WPS440 # var overlap
            path = [*parent, node[NODE_NAME]]
            joined_path = '.'.join(path)
            children = node.get(NODE_CHILDREN)
            if children:
                iter_node(children, path)
            elif node[NODE_STATE] == CHANGED:
                removed_value = encode_to_json_type(node[NODE_VALUE][REMOVED])
                added_value = encode_to_json_type(node[NODE_VALUE][ADDED])
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
                        joined_path, encode_to_json_type(node[NODE_VALUE]),
                    ))
            elif node[NODE_STATE] == REMOVED:
                output.append("Property '{0}' was removed".format(joined_path))
        return '\n'.join(output)
    return iter_node(diff, [])
