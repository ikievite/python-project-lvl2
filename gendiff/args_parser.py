

"""Module that parse arguments."""


import argparse

from gendiff.formaters.format_diff import JSON_VIEW, PLAIN_VIEW, STYLISH_VIEW


def args_parse():
    """Func parses arguments.

    Returns:
        an object holding attributes
    """
    parser = argparse.ArgumentParser(description='Compares two json/yaml files and shows a diff.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        choices=[STYLISH_VIEW, PLAIN_VIEW, JSON_VIEW],
        default=STYLISH_VIEW,
        dest='formater',
        help='set output format (default: "{0}")'.format(STYLISH_VIEW),
    )
    return parser.parse_args()
