''' Tests for gendiff project.'''

from gendiff.scripts.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/diff_flat_json.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/flat1.json'
    file2 = 'tests/fixtures/flat2.json'
    assert generate_diff(file1, file2) == expected

    with open('tests/fixtures/diff_flat_yaml.txt') as f:
        expected_yaml = f.read().strip()
    flat1_yaml = 'tests/fixtures/flat1.yaml'
    flat2_yaml = 'tests/fixtures/flat2.yaml'
    flat1_yml = 'tests/fixtures/flat1.yml'
    flat2_yml = 'tests/fixtures/flat2.yml'
    assert generate_diff(flat1_yaml, flat2_yaml) == expected_yaml
    assert generate_diff(flat1_yml, flat2_yml) == expected_yaml

    with open('tests/fixtures/diff_nested_json.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested1.json'
    file2 = 'tests/fixtures/nested2.json'
    assert generate_diff(file1, file2) == expected_yaml
