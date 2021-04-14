

"""module with stylish formater."""


from gendiff.find_diff import ADDED, CHANGED, REMOVED, UNCHANGED

indent = 4
diff_line = '{indent}{key}: {value}'
changed_value = ('{indent}- {key}: {removed_value}\n'
                 '{indent}+ {key}: {added_value}'  # noqa: WPS326, WPS318
                 )                   # implicit string concatenation, ignore: extra indentation


def encode_to_json_type(value, depth):
    """Func encodes value to json format.

    Args:
        value: value from node
        depth: depth

    Returns:
        encoded value
    """
    if value is True:
        node_value = 'true'
    elif value is False:
        node_value = 'false'
    elif value is None:
        node_value = 'null'
    elif isinstance(value, dict):
        node_value = '\n'.join(iter_complex(['{'], value, depth))
    else:
        return value
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
    newline_indent = (depth + 1) * indent * ' '
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
        indent=depth * indent * ' ',
        value='}',
    ))
    return result


def stylish_formater(diff):
    """Func that display diff tree.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    output = ['{']

    def iter_node(nodes, depth):  # noqa: WPS430 # ignore warning about nested function
        for node in sorted(nodes, key=lambda node: node['name']):  # noqa: WPS440 # var overlap
            current_indent = depth * indent * ' '
            if 'children' in node.keys():  # noqa: WPS223 # ignore quantity `elif` branches
                output.append(diff_line.format(
                    indent=current_indent,
                    key=node['name'],
                    value='{',
                ))
                iter_node(node['children'], depth + 1)
            elif node['state'] == CHANGED:
                output.append(changed_value.format(
                    indent=current_indent[:-2],
                    key=node['name'],
                    removed_value=encode_to_json_type(node['value'][REMOVED], depth),
                    added_value=encode_to_json_type(node['value'][ADDED], depth),
                ))
            else:
                if node['state'] == UNCHANGED:  # noqa: WPS513 # implicit `elif`
                    badge = ' '
                elif node['state'] == ADDED:
                    badge = '+'
                elif node['state'] == REMOVED:
                    badge = '-'
                value = encode_to_json_type(node['value'], depth)
                output.append(diff_line.format(
                    key=node['name'],
                    value=value,
                    indent='{0}{1} '.format(current_indent[:-2], badge),
                ))
        output.append('{indent}{value}'.format(
            indent=(depth - 1) * indent * ' ',
            value='}',
        ))
        return '\n'.join(output)
    return iter_node(diff, 1)
