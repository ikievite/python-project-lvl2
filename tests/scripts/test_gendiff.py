''' Tests for gendiff project.'''

from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/diff_flat_1_2.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/flat1.json'
    file2 = 'tests/fixtures/flat2.json'
    assert generate_diff(file1, file2) == expected
