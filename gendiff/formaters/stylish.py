

"""module with stylish formater."""


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
                output.append('  {0}{1} {2}: {3}'.format(
                    '  '*depth, node['badge'], node['name'], '{',
                ))
                iter_node(node['children'], depth + 2)

            elif node['type'] == 'complex':
                output.append('  {0}{1} {2}: {3}'.format(
                    '  '*depth, node['badge'], node['name'], '{',
                ))

                def iter_complex(node, depth):  # noqa: WPS430, WPS442
                    for node_key, node_value in node.items():
                        if isinstance(node_value, dict):
                            output.append('      {0}  {1}: {2}'.format(
                                '  '*depth, node_key, '{',
                            ))
                            iter_complex(node_value, depth + 2)
                        else:
                            output.append('      {0}  {1}: {2}'.format(
                                '  '*depth, node_key, node_value,
                            ))
                    output.append('    {0}{1}'.format('  '*depth, '}'))
                iter_complex(node['value'], depth)
            elif node['type'] == 'flat':
                output.append('  {0}{1} {2}: {3}'.format(
                    '  '*depth, node['badge'], node['name'], node['value'],
                ))
        output.append('{0}{1}'.format('  '*depth, '}'))
        return '\n'.join(output)
    return iter_node(diff, 0)
