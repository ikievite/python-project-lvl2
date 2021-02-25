

''' Tests for gendiff project.'''

import pytest
from gendiff.scripts.gendiff import generate_diff


test_flat_data = [('tests/fixtures/flat1.json',
                   'tests/fixtures/flat2.json'),
                  ('tests/fixtures/flat1.yaml',
                   'tests/fixtures/flat2.yaml'),
                  ('tests/fixtures/flat1.yml',
                   'tests/fixtures/flat2.yml')]
flat_result = [('tests/fixtures/diff_flat.txt')]


@pytest.mark.parametrize("file1,file2", test_flat_data)
@pytest.mark.parametrize("result", flat_result)
def test_generate_diff_flat(file1, file2, result):
    with open(result) as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2) == expected


def test_generate_diff_flat_stylish():
    with open('tests/fixtures/diff_flat.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/flat1.json'
    file2 = 'tests/fixtures/flat2.json'
    assert generate_diff(file1, file2, 'stylish') == expected


test_nested_data = [('tests/fixtures/nested1.json',
                     'tests/fixtures/nested2.json'),
                    ('tests/fixtures/nested1.yaml',
                     'tests/fixtures/nested2.yaml')]
nested_result = [('tests/fixtures/diff_nested_stylish.txt')]


@pytest.mark.parametrize("file1,file2", test_nested_data)
@pytest.mark.parametrize("result", nested_result)
def test_generate_diff_nested(file1, file2, result):
    with open(result) as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2) == expected


files = [('tests/fixtures/nested1.json',
          'tests/fixtures/nested2.json')]
nested_formaters_results = [('plain', 'tests/fixtures/diff_nested_plain.txt'),
                            ('json', 'tests/fixtures/diff_nested_json_formater.txt')]


@pytest.mark.parametrize("file1,file2", files)
@pytest.mark.parametrize("formater,diff", nested_formaters_results)
def test_generate_diff_nested_formater(file1, file2, formater, diff):
    with open(diff) as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2, formater) == expected


def test_generate_diff_nested_stylish_v2():
    with open('tests/fixtures/diff_nested_stylish2.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested11.json'
    file2 = 'tests/fixtures/nested21.json'
    assert generate_diff(file1, file2) == expected
