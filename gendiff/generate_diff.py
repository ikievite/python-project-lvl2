

"""Module that generate diff between two dicts."""


from gendiff.find_diff import find_diff
from gendiff.format_diff import format_diff
from gendiff.loader import loader


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
