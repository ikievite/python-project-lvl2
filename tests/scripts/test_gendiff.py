

''' Tests for gendiff project.'''

import json
import pytest
from gendiff.scripts.gendiff import generate_diff
from gendiff.find_diff import NODE_NAME


test_flat_data = [('tests/fixtures/flat1.json',
                   'tests/fixtures/flat2.json',
                   'tests/fixtures/diff_flat.txt'),
                  ('tests/fixtures/flat1.yaml',
                   'tests/fixtures/flat2.yaml',
                   'tests/fixtures/diff_flat.txt'),
                  ('tests/fixtures/flat1.yml',
                   'tests/fixtures/flat2.yml',
                   'tests/fixtures/diff_flat.txt'),
                  ('tests/fixtures/nested1.json',
                   'tests/fixtures/nested2.json',
                   'tests/fixtures/diff_nested_stylish.txt'),
                  ('tests/fixtures/nested1.yaml',
                   'tests/fixtures/nested2.yaml',
                   'tests/fixtures/diff_nested_stylish.txt'),
                  ('tests/fixtures/nested11.json',
                   'tests/fixtures/nested21.json',
                   'tests/fixtures/diff_nested_stylish2.txt')]


@pytest.mark.parametrize("file1,file2,diff", test_flat_data)
def test_generate_diff_flat_new(file1, file2, diff):
    with open(diff) as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2) == expected


test_data_with_formaters = [('tests/fixtures/nested1.json',
                             'tests/fixtures/nested2.json',
                             'plain',
                             'tests/fixtures/diff_nested_plain.txt'),
                            ('tests/fixtures/nested1.json',
                             'tests/fixtures/nested2.json',
                             'stylish',
                             'tests/fixtures/diff_nested_stylish.txt')]


@pytest.mark.parametrize("file1,file2,formater,diff", test_data_with_formaters)
def test_generate_diff_with_formater(file1, file2, formater, diff):
    with open(diff) as f:
        expected = f.read().strip()
    assert generate_diff(file1, file2, formater) == expected


def convert_to_dict(nodes):
    result = {}
    for node in nodes:
        result.update({node[NODE_NAME]: node})
    return result


test_data_for_json_formater = [('tests/fixtures/nested1.json',
                                'tests/fixtures/nested2.json',
                                'json',
                                'tests/fixtures/diff_nested_json_formater.txt')]


@pytest.mark.skip(reason='to do')
@pytest.mark.parametrize("file1,file2,formater,diff", test_data_for_json_formater)
def test_generate_diff_json_formater(file1, file2, formater, diff):
    with open(diff) as f:
        json_diff = json.load(f)
    expected = convert_to_dict(json_diff)
    assert convert_to_dict(json.loads(generate_diff(file1, file2, formater))) == expected
