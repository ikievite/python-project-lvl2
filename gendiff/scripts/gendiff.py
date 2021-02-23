

"""gendiff package."""


import argparse

from gendiff.loader import loader
from gendiff.find_diff import find_diff
from gendiff.format_diff import format_diff
from gendiff.format_diff import CHOICE_STYLISH, CHOICE_PLAIN, CHOICE_JSON


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
    return format_diff(diff, formater)


def main():
    """Run main func."""
    parser = argparse.ArgumentParser(description='Compares two json/yaml files and shows a diff.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', choices=[CHOICE_STYLISH, CHOICE_PLAIN, CHOICE_JSON],
        default=CHOICE_STYLISH,  # noqa: WPS317
        dest='formater', help='set output format (default: "{0}")'.format(CHOICE_STYLISH),
    )
    args = parser.parse_args()
    try:  # noqa: WPS229
        diff = generate_diff(args.first_file, args.second_file, args.formater)

        print(diff)  # noqa: WPS421
    except Exception as e:  # noqa: WPS111
        print('Exception: {0}'.format(str(e)))  # noqa: WPS421


if __name__ == '__main__':
    main()
