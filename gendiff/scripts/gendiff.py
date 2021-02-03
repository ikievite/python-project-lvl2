

"""gendiff package."""


import argparse

from gendiff.formaters.json import json_formater
from gendiff.formaters.plain import plain_formater
from gendiff.formaters.stylish import stylish_formater
from gendiff.loader import loader
from gendiff.find_diff import find_diff


def generate_diff(file1, file2, formater='stylish'):
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
    elif formater == 'plain':
        return plain_formater(diff)
    elif formater == 'json':
        return json_formater(diff)


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Compares two json/yaml files and shows a diff.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', choices=['stylish', 'plain', 'json'],
        default='stylish',  # noqa: WPS317
        dest='formater', help='set output format (default: "stylish")',
    )
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.formater)

    print(diff)  # noqa: WPS421


if __name__ == '__main__':
    main()
