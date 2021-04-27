

"""Module that generate diff between two dicts."""


from gendiff.find_diff import find_diff
from gendiff.formaters.format_diff import STYLISH_VIEW, format_diff
from gendiff.loader import load_content


def generate_diff(file1, file2, formater=STYLISH_VIEW):
    """Func generate diff of two files.

    Args:
        file1: path to file1
        file2: path to file2
        formater: format for output

    Returns:
        string with diff
    """
    content1, content2 = load_content(file1), load_content(file2)
    diff = find_diff(content1, content2)
    return format_diff(diff, formater)
