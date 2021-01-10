

"""gendiff package."""


import argparse

from gendiff.loader import loader


def find_diff(file1, file2):
    """Func find diff items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        list with diff items
    """
    diff = []
    for key in file1.keys():
        if key in file2:
            value1 = file1.get(key)
            value2 = file2.get(key)
            if value1 == value2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': ' ',
                        'children': find_diff(value1, value2),
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': ' ',
                        'value': value1,
                    })
            elif value1 != value2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': ' ',
                        'children': find_diff(value1, value2),
                    })
                elif isinstance(value1, dict):
                    if len(value1) == 1:
                        diff.append({
                            'name': key,
                            'type': 'flat',
                            'badge': '-',
                            'value': value1,
                        })
                    else:
                        diff.append({
                            'name': key,
                            'type': 'nested',
                            'badge': '-',
                            'children': value1,
                        })
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '+',
                        'value': value2,
                    })
                elif isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': value1,
                    })
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': '+',
                        'children': value2,
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': value1,
                    })
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '+',
                        'value': value2,
                    })
        elif key not in file2.keys():
            if isinstance(file1[key], dict):
                if len(file1[key]) == 1:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': file1[key],
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': '-',
                        'children': file1[key],
                    })
            else:
                diff.append({
                    'name': key,
                    'type': 'flat',
                    'badge': '-',
                    'value': file1[key],
                })
    for key in file2.keys():  # noqa: WPS440
        if key not in file1:
            if isinstance(file2.get(key), dict):
                if len(file2[key]) == 1:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '+',
                        'value': file2[key],
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': '+',
                        'children': file2[key],
                    })
            else:
                diff.append({
                    'name': key,
                    'type': 'flat',
                    'badge': '+',
                    'value': file2[key],
                })
    return diff


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
        if isinstance(nodes, dict):
            for node_key, node_value in nodes.items():
                if isinstance(node_value, dict):
                    output.append('  {0}  {1}: {2}'.format('  '*depth, node_key, '{'))
                    iter_node(node_value, depth + 2)
                else:
                    output.append('  {0}  {1}: {2}'.format('  '*depth, node_key, node_value))
        else:
            for element in nodes:  # noqa: WPS426
                if element['type'] == 'flat':
                    if isinstance(element['value'], dict):
                        output.append('  {0}{1} {2}: {3}'.format(
                            '  '*depth, element['badge'], element['name'], '{',
                        ))
                        output.append('      {0}  {1}: {2}'.format(
                            '  '*depth,
                            list(element['value'])[0],
                            list(element['value'].values())[0],
                        ))
                        output.append('    {0}{1}'.format('  '*depth, '}'))
                    else:
                        output.append('  {0}{1} {2}: {3}'.format(
                            '  '*depth, element['badge'], element['name'], element['value'],
                        ))
                elif element['type'] == 'nested':
                    if isinstance(element['children'], list):
                        element['children'].sort(key=lambda child: child['name'])
                    output.append('  {0}{1} {2}: {3}'.format(
                        '  '*depth, element['badge'], element['name'], '{',
                    ))
                    iter_node(element['children'], depth + 2)
        output.append('{0}{1}'.format('  '*depth, '}'))
        return '\n'.join(output)
    return iter_node(diff, 0)


def generate_diff(file1, file2, formater='stylish'):  # noqa: WPS210
    """Func generate diff of two files.

    Args:
        file1: path to file1
        file2: path to file2
        formater: format for output

    Returns:
        string with diff
    """
    content1, content2 = loader(file1), loader(file2)
    diff = find_diff(content1, content2)
    if formater == 'stylish':
        return stylish_formater(diff)


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Compares two json/yaml files and shows a diff.')
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument(
        '-f', '--format', action='store', default='stylish', required=False,
        dest='formater', help='set output format (default: "stylish")',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.formater)

    print(diff)  # noqa: WPS421


if __name__ == '__main__':
    main()
