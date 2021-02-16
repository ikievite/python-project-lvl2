

"""module with stylish formater."""


amount_of_indent = 2
base_indent = ' ' * amount_of_indent


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
    else:
        return value
    return node_value


def diff_line(depth, node):
    """Func generates line.

    Args:
        depth: level of indentation
        node: dict with diff data

    Returns:
        line
    """
    badge = node['badge']
    key = node['name']
    indent = base_indent * depth
    if node['type'] == 'flat':
        value = encode_to_json_type(node['value'])
    else:
        value = '{'
    return '{base_indent}{indent}{badge} {key}: {value}'.format(
        base_indent=base_indent, indent=indent, badge=badge, key=key, value=value,
    )


def iter_complex(result, complex_node, depth):  # noqa: WPS430, WPS442
    """Func prepare output for complex node.

    Args:
        result: list with output
        complex_node: value of node
        depth: level of indentation

    Returns:
        list with stylish complex output
    """
    for node_key, node_value in complex_node.items():
        diff_comlex_line = '    {indent}  {key}: {value}'
        complex_indent = base_indent * depth + base_indent
        if isinstance(node_value, dict):
            result.append(diff_comlex_line.format(
                indent=complex_indent, key=node_key, value='{',
            ))
            iter_complex(result, node_value, depth + amount_of_indent)
        else:
            result.append(diff_comlex_line.format(
                indent=complex_indent, key=node_key, value=node_value,
            ))
    result.append('{0}{1}{2}'.format(base_indent, complex_indent, '}'))
    return result


def stylish_formater(diff):
    """Func that display diff tree.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    output = ['{']

    def iter_node(nodes, depth):  # noqa: WPS430
        nodes.sort(key=lambda entry: entry['name'])
        indent = depth * base_indent
        for node in nodes:  # noqa: WPS426
            if node['type'] == 'nested':
                output.append(diff_line(depth, node))
                iter_node(node['children'], depth + amount_of_indent)
            elif node['type'] == 'complex':
                output.append(diff_line(depth, node))
                output.extend(iter_complex([], node['value'], depth))
            elif node['type'] == 'flat':
                output.append(diff_line(depth, node))
        output.append('{0}{1}'.format(indent, '}'))
        return '\n'.join(output)
    return iter_node(diff, 0)
