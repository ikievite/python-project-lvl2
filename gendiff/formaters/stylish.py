

"""module with stylish formater."""


from gendiff.find_diff import ADDED, CHANGED, REMOVED, UNCHANGED
from gendiff.find_diff import NODE_CHILDREN, NODE_NAME, NODE_STATE, NODE_VALUE

INDENT = 4
BADGE_SIZE = 1
BADGE_PADDING = 1
BLANK = ' '
OPEN_BRACE = '{'
CLOSE_BRACE = '}'
diff_line = '{indent}{key}: {value}'
changed_value = ('{indent}- {key}: {removed_value}\n'
                 '{indent}+ {key}: {added_value}'  # noqa: WPS326, WPS318
                 )                   # implicit string concatenation, ignore: extra indentation


def prepare_value(node_value, current_indent):
    """Func encodes value to appropriate format.

    Args:
        node_value: value from node
        current_indent: current indent

    Returns:
        encoded value
    """
    if node_value is True:
        formatted_value = 'true'
    elif node_value is False:
        formatted_value = 'false'
    elif node_value is None:
        formatted_value = 'null'
    elif isinstance(node_value, dict):
        formatted_value = '\n'.join(iter_complex([OPEN_BRACE], node_value, current_indent))
    else:
        formatted_value = node_value
    return formatted_value


def iter_complex(complex_items, complex_value, current_indent):
    """Func prepare output for complex node.

    Args:
        complex_value: value
        current_indent: current indent
        complex_items: list with values, neaded for iteration

    Returns:
        an indented list of values
    """
    newline_indent = current_indent + INDENT * BLANK
    for key, value in complex_value.items():  # noqa: WPS110 # ignore - wrong var name: value
        if isinstance(value, dict):
            complex_items.append(diff_line.format(
                indent=newline_indent,
                key=key,
                value=OPEN_BRACE,
            ))
            iter_complex(complex_items, value, current_indent + INDENT * BLANK)
        else:
            complex_items.append(diff_line.format(
                indent=newline_indent,
                key=key,
                value=value,
            ))
    complex_items.append('{indent}{value}'.format(
        indent=current_indent,
        value=CLOSE_BRACE,
    ))
    return complex_items


def format_line(badge, current_indent, node):
    """Func returns formatted string.

    Args:
        badge: badge
        current_indent: current indent
        node: node

    Returns:
        diff string
    """
    node_value = prepare_value(node[NODE_VALUE], current_indent)
    return diff_line.format(
        key=node[NODE_NAME],
        value=node_value,
        indent='{0}{1}{2}'.format(
            current_indent[:-(BADGE_SIZE + BADGE_PADDING)],
            badge,
            BLANK * BADGE_PADDING,
        ),
    )


def iter_node(nodes, output, depth=1):
    """Func finds and returns diff from list with diff dicts.

    Args:
        nodes: list with diff dicts
        output: list with OPEN_BRACE
        depth: depth

    Returns:
        output string
    """
    for node in sorted(nodes, key=lambda node: node[NODE_NAME]):  # noqa: WPS440 # var overlap
        current_indent = depth * INDENT * BLANK
        children = node.get(NODE_CHILDREN)
        if children:  # noqa: WPS223 # ignore too many `elif` branches: 4 > 3
            output.append(diff_line.format(
                indent=current_indent,
                key=node[NODE_NAME],
                value=OPEN_BRACE,
            ))
            iter_node(children, output, depth + 1)
        elif node[NODE_STATE] == CHANGED:
            output.append(changed_value.format(
                indent=current_indent[:-(BADGE_SIZE + BADGE_PADDING)],
                key=node[NODE_NAME],
                removed_value=prepare_value(node[NODE_VALUE][REMOVED], current_indent),
                added_value=prepare_value(node[NODE_VALUE][ADDED], current_indent),
            ))
        elif node[NODE_STATE] == UNCHANGED:
            badge = ' '
            output.append(format_line(badge, current_indent, node))
        elif node[NODE_STATE] == ADDED:
            badge = '+'
            output.append(format_line(badge, current_indent, node))
        elif node[NODE_STATE] == REMOVED:
            badge = '-'
            output.append(format_line(badge, current_indent, node))
    output.append('{indent}{value}'.format(
        indent=(depth - 1) * INDENT * BLANK,
        value=CLOSE_BRACE,
    ))
    return '\n'.join(output)


def stylish_formater(diff):
    """Func that returns stylish formated diff.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    return iter_node(diff, [OPEN_BRACE])
