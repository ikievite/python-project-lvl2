

"""gendiff package."""


import argparse
import json


def read_file(filename):
    """Func read json file.

    Args:
        filename: path to file

    Returns:
        conten of file
    """
    with open(filename) as f:
        return json.load(f)


def find_equal_items(file1, file2):
    """Func find equal items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        dict with equal items
    """
    result = []
    for entry in file1.items():
        if entry in file2.items():
            result.append(dict([(' ', (entry))]))
    return result


def find_removed_keys(file1, file2):
    """Func find removed items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        dict with removed items
    """
    result = []
    for key in file1.keys():
        if key not in file2.keys():
            result.append(dict([('-', (key, file1[key]))]))
    return result


def find_added_keys(file1, file2):
    """Func find added items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        dict with added items
    """
    result = []
    for key in file2.keys():
        if key not in file1.keys():
            result.append(dict([('+', (key, file2[key]))]))
    return result


def find_changed_values(file1, file2):
    """Func find equal items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        dict with equal items
    """
    result = []
    for key, value in file1.items():
        if key in file2.keys():
            if value != file2[key]:
                result.append(dict([('-', (key, file1[key]))]))
                result.append(dict([('+', (key, file2[key]))]))
    return result


def generate_diff(file1, file2):
    """Func generate diff of two files.

    Args:
        file1: path to file1
        file2: path to file2

    Returns:
        string with diff
    """
    content1, content2 = read_file(file1), read_file(file2)
    data = []
    data.extend(find_equal_items(content1, content2))
    data.extend(find_removed_keys(content1, content2))
    data.extend(find_changed_values(content1, content2))
    data.extend(find_added_keys(content1, content2))
    result = ['{']
    for item in sorted(data, key=lambda k: list(k.values())[0][0]):
        badge = list(item.keys())[0]
        key, value = list(item.values())[0]
        result.append('  {} {}: {}'.format(badge, key, value))
    result.append('}')
    result = '\n'.join(result)
    return result


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', action='store')
    parser.add_argument('second_file', action='store')
    parser.add_argument(
        '-f', '--format', action='store', help='set format of output',
    )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
