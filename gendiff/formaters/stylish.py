

"""module with stylish formater."""


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
    if node['type'] == 'flat':
        value = encode_to_json_type(node['value'])
    else:
        value = '{'
    return '  {indent}{badge} {key}: {value}'.format(
        indent='  '*depth, badge=badge, key=key, value=value,
    )


def stylish_formater(diff):
    """Func that display diff tree.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    diff.sort(key=lambda entry: entry['name'])
    output = ['{']

    def iter_node(nodes, depth):  # noqa: WPS430
        for node in nodes:  # noqa: WPS426
            if node['type'] == 'nested':
                node['children'].sort(key=lambda child: child['name'])
                output.append(diff_line(depth, node))
                iter_node(node['children'], depth + 2)

            elif node['type'] == 'complex':
                output.append(diff_line(depth, node))

                def iter_complex(complex_node, depth):  # noqa: WPS430, WPS442
                    for node_key, node_value in complex_node.items():
                        diff_comlex_line = '      {indent}  {key}: {value}'
                        if isinstance(node_value, dict):
                            output.append(diff_comlex_line.format(
                                indent='  '*depth, key=node_key, value='{',
                            ))
                            iter_complex(node_value, depth + 2)
                        else:
                            output.append(diff_comlex_line.format(
                                indent='  '*depth, key=node_key, value=node_value,
                            ))
                    output.append('    {0}{1}'.format('  '*depth, '}'))
                iter_complex(node['value'], depth)
            elif node['type'] == 'flat':
                output.append(diff_line(depth, node))
        output.append('{0}{1}'.format('  '*depth, '}'))
        return '\n'.join(output)
    return iter_node(diff, 0)
