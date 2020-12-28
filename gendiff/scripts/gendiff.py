

"""gendiff package."""


import argparse
from pprint import pprint

from gendiff.loader import loader


def find_diff2(file1, file2):
    """Func find diff items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        list with diff items
    """
    diff = []
    for key in file1:
        item = {}
        if key in file2:
            value1 = file1[key]
            value2 = file2[key]
            if value1 == value2:
                item['name'] = key
                item['badge'] = ' '
                if isinstance(value1, dict) and isinstance(value2, dict):
                    item['type'] = 'nested'
                    item['value'] = find_diff2(value1, value2)
                    diff.append(item)
                else:
                    item['type'] = 'flat'
                    item['value'] = value1
                    diff.append(item)
            else:
                item['name'] = key
                if isinstance(value1, dict) and isinstance(value2, dict):
                    item['badge'] = ' '
                    item['type'] = 'nested'
                    item['value'] = find_diff2(value1, value2)
                    diff.append(item)
                else:
                    item['badge'] = '-'
                    item['type'] = 'flat'
                    item['value'] = value1
                    diff.append(item)
                    item = {}
                    item['name'] = key
                    item['type'] = 'flat'
                    item['badge'] = '+'
                    item['value'] = value2
                    diff.append(item)
        elif key not in file2:
            item['name'] = key
            item['badge'] = '-'
            item['type'] = 'flat'
            item['value'] = file1[key]
            diff.append(item)
    for key in file2:
        item = {}
        if key not in file1:
            item['name'] = key
            item['badge'] = '+'
            item['type'] = 'flat'
            item['value'] = file2[key]
            diff.append(item)
    return diff


def stylish_formater(diff, level=1):
    """
    """
    '''
    for element in diff:
        if element['type'] == 'flat':
            print('  {0} {1}: {2}'.format(element['badge'], element['name'], element['value']))
        elif element['type'] == 'nested':
            print('  {0} {1}: {2}'.format(element['badge'], element['name'], '{'))
            stylish_formater(element['value'])
    '''


def generate_diff(file1, file2):  # noqa: WPS210
    """Func generate diff of two files.

    Args:
        file1: path to file1
        file2: path to file2

    Returns:
        string with diff
    """
    content1, content2 = loader(file1), loader(file2)
    diff = find_diff2(content1, content2)
    #pprint(diff)
    print('\n'.join(stylish_formater(diff)))

    '''
    output = ['{']
    for element in sorted(diff, key=lambda key_of_item: list(key_of_item.values())[0][0]):  # noqa: WPS221, E501
        for badge, diff_values in element.items():
            output.append('  {0} {1}: {2}'.format(badge, diff_values[0], diff_values[1]))
    output.append('}')
    '''


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument(
        '-f', '--format', action='store', help='set format of output',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)  # noqa: WPS421
    # stylish_formater2(diff)


if __name__ == '__main__':
    main()
