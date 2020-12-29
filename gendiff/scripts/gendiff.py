

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
        entry = {}
        entry['name'] = key
        if key in file2:
            value1 = file1.get(key)
            value2 = file2.get(key)
            if value1 == value2:
                entry['badge'] = ' '  # noqa: WPS204
                if isinstance(value1, dict) and isinstance(value2, dict):
                    entry['type'] = 'nested'  # noqa: WPS204
                    entry['value'] = find_diff(value1, value2)  # noqa: WPS204
                    diff.append(entry)  # noqa: WPS204
                else:
                    entry['type'] = 'flat'
                    entry['value'] = value1
                    diff.append(entry)
            elif value1 != value2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    entry['badge'] = ' '
                    entry['type'] = 'nested'
                    entry['value'] = find_diff(value1, value2)
                    diff.append(entry)
                else:
                    entry['badge'] = '-'
                    entry['type'] = 'flat'
                    entry['value'] = value1
                    diff.append(entry)
                    entry = {}
                    entry['name'] = key
                    entry['type'] = 'flat'
                    entry['badge'] = '+'
                    entry['value'] = value2
                    diff.append(entry)
        elif key not in file2.keys():
            entry['badge'] = '-'
            entry['type'] = 'flat'
            entry['value'] = file1[key]
            diff.append(entry)
    for key in file2.keys():
        entry = {}
        if key not in file1:
            entry['name'] = key
            entry['badge'] = '+'
            entry['type'] = 'flat'
            entry['value'] = file2[key]
            diff.append(entry)
    return diff


def stylish_formater(diff):
    """Func that display diff tree.

    Args:
        diff: list with diff dicts

    Returns:
        output string
    """
    output = ['{']

    def iter_node(nodes, depth):  # noqa: WPS430
        for element in nodes:
            if element['type'] == 'flat':
                output.append('  {0}{1} {2}: {3}'.format(
                    '  '*depth, element['badge'], element['name'], element['value'],
                ))
            elif element['type'] == 'nested':
                output.append('  {0}{1} {2}: {3}'.format(
                    '  '*depth, element['badge'], element['name'], '{',
                ))
                iter_node(element['value'], depth + 2)
        output.append('{0} {1}'.format('  '*depth, '}'))
        return '\n'.join(output)
    return iter_node(diff, 0)


def generate_diff(file1, file2):  # noqa: WPS210
    """Func generate diff of two files.

    Args:
        file1: path to file1
        file2: path to file2

    Returns:
        string with diff
    """
    content1, content2 = loader(file1), loader(file2)
    return find_diff(content1, content2)

    # sorted(diff, key=lambda key_of_item: list(key_of_item.values())[0][0])  # noqa: E800


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument(
        '-f', '--format', action='store', help='set format of output',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(stylish_formater(diff))  # noqa: WPS421


if __name__ == '__main__':
    main()
