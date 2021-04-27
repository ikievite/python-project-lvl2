

"""Module that parse arguments."""


import argparse

from gendiff.formaters.format_diff import JSON_VIEW, PLAIN_VIEW, STYLISH_VIEW


def prepare_args_parser():
    """Func creates parser and adds arguments.

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


def args_parse():
    """Func returns parser and arguments.

    Returns:
        parser and arguments.
    """
    return prepare_args_parser()
