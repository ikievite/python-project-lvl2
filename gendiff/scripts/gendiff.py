

"""gendiff package."""


import argparse
from pprint import pprint

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
    common = list(file1.keys() & file2.keys())
    removed = list(file1.keys() - file2.keys())
    added = list(file2.keys() - file1.keys())
    for key in common:
        if file1[key] == file2[key]:
            diff.append({' ': {key: file1[key]}})
    for key in common:
        value1 = file1[key]
        value2 = file2[key]
        if value1 != value2:
            if isinstance(value1, dict) and isinstance(value2, dict):
                diff.append({' ': {key: find_diff(value1, value2)}})
            else:
                diff.append({'-': {key: value1}})
                diff.append({'+': {key: value2}})
    for key in removed:
        diff.append({'-': {key: file1[key]}})
    for key in added:
        diff.append({'+': {key: file2[key]}})
    return diff


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
    '''
    diff = []
    diff.extend(find_equal_items(content1, content2))
    diff.extend(find_removed_keys(content1, content2))
    diff.extend(find_changed_values(content1, content2))
    diff.extend(find_added_keys(content1, content2))
    output = ['{']
    for element in sorted(diff, key=lambda key_of_item: list(key_of_item.values())[0][0]):  # noqa: WPS221, E501
        for badge, diff_values in element.items():
            output.append('  {0} {1}: {2}'.format(badge, diff_values[0], diff_values[1]))
    output.append('}')
    return '\n'.join(output)
    return output
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
    pprint(generate_diff(args.first_file, args.second_file))  # noqa: WPS421


if __name__ == '__main__':
    main()
