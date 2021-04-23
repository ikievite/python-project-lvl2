

"""module with stylish formater."""


from gendiff.find_diff import ADDED, CHANGED, REMOVED, UNCHANGED
from gendiff.find_diff import NODE_CHILDREN, NODE_NAME, NODE_STATE, NODE_VALUE
from gendiff.formaters.format_value import encode_to_output

INDENT = 4
BADGE_SIZE = 1
SPACE = 1  # space between badge and key: value
diff_line = '{indent}{key}: {value}'
changed_value = ('{indent}- {key}: {removed_value}\n'
                 '{indent}+ {key}: {added_value}'  # noqa: WPS326, WPS318
                 )                   # implicit string concatenation, ignore: extra indentation


def prepare_value(value, depth):
    """Func encodes value to appropriate format.

    Args:
        value: value from node
        depth: depth

    Returns:
        encoded value
    """
    if isinstance(value, dict):
        node_value = '\n'.join(iter_complex(['{'], value, depth))
    else:
        node_value = encode_to_output(value)
    return node_value


def iter_complex(result, complex_value, depth):
    """Func prepare output for complex node.

    Args:
        complex_value: value
        depth: depth
        result: list with values, neaded for iteration

    Returns:
        an indented list of values
    """
    newline_indent = (depth + 1) * INDENT * ' '
    for key, value in complex_value.items():
        if isinstance(value, dict):
            result.append(diff_line.format(
                indent=newline_indent,
                key=key,
                value='{',
            ))
            iter_complex(result, value, depth + 1)
        else:
            result.append(diff_line.format(
                indent=newline_indent,
                key=key,
                value=value,
            ))
    result.append('{indent}{value}'.format(
        indent=depth * INDENT * ' ',
        value='}',
    ))
    return result


def format_line(badge, depth, node):
    """Func returns formatted string.

    Args:
        badge: badge
        depth: depth
        node: node

    Returns:
        diff string
    """
    current_indent = depth * INDENT * ' '
    value = prepare_value(node[NODE_VALUE], depth)
    return diff_line.format(
        key=node[NODE_NAME],
        value=value,
        indent='{0}{1}{2}'.format(current_indent[:-(BADGE_SIZE + SPACE)], badge, ' ' * SPACE),
    )


def stylish_formater(diff):
    """Func that display diff tree.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    output = ['{']

    def iter_node(nodes, depth):  # noqa: WPS430 # ignore warning about nested function
        for node in sorted(nodes, key=lambda node: node[NODE_NAME]):  # noqa: WPS440 # var overlap
            current_indent = depth * INDENT * ' '
            children = node.get(NODE_CHILDREN)
            if children:  # noqa: WPS223 # ignore too many `elif` branches: 4 > 3
                output.append(diff_line.format(
                    indent=current_indent,
                    key=node[NODE_NAME],
                    value='{',
                ))
                iter_node(children, depth + 1)
            elif node[NODE_STATE] == CHANGED:
                output.append(changed_value.format(
                    indent=current_indent[:-(BADGE_SIZE + SPACE)],
                    key=node[NODE_NAME],
                    removed_value=prepare_value(node[NODE_VALUE][REMOVED], depth),
                    added_value=prepare_value(node[NODE_VALUE][ADDED], depth),
                ))
            elif node[NODE_STATE] == UNCHANGED:
                badge = ' '
                output.append(format_line(badge, depth, node))
            elif node[NODE_STATE] == ADDED:
                badge = '+'
                output.append(format_line(badge, depth, node))
            elif node[NODE_STATE] == REMOVED:
                badge = '-'
                output.append(format_line(badge, depth, node))
        output.append('{indent}{value}'.format(
            indent=(depth - 1) * INDENT * ' ',
            value='}',
        ))
        return '\n'.join(output)
    return iter_node(diff, 1)
