

''' Tests for gendiff project.'''


from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_flat_json():
    with open('tests/fixtures/diff_flat.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/flat1.json'
    file2 = 'tests/fixtures/flat2.json'
    assert generate_diff(file1, file2) == expected


def test_generate_diff_flat_yaml():
    with open('tests/fixtures/diff_flat.txt') as f:
        expected_yaml = f.read().strip()
    flat1_yaml = 'tests/fixtures/flat1.yaml'
    flat2_yaml = 'tests/fixtures/flat2.yaml'
    assert generate_diff(flat1_yaml, flat2_yaml) == expected_yaml


def test_generate_diff_flat_yml():
    with open('tests/fixtures/diff_flat.txt') as f:
        expected_yml = f.read().strip()
    flat1_yml = 'tests/fixtures/flat1.yml'
    flat2_yml = 'tests/fixtures/flat2.yml'
    assert generate_diff(flat1_yml, flat2_yml) == expected_yml


def test_generate_diff_flat_stylish():
    with open('tests/fixtures/diff_flat.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/flat1.json'
    file2 = 'tests/fixtures/flat2.json'
    assert generate_diff(file1, file2, 'stylish') == expected


def test_generate_diff_nested_stylish():
    with open('tests/fixtures/diff_nested_stylish.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested1.json'
    file2 = 'tests/fixtures/nested2.json'
    assert generate_diff(file1, file2) == expected


def test_generate_diff_nested_stylish_yaml():
    with open('tests/fixtures/diff_nested_stylish.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested1.yaml'
    file2 = 'tests/fixtures/nested2.yaml'
    assert generate_diff(file1, file2) == expected


def test_generate_diff_nested_plain():
    with open('tests/fixtures/diff_nested_plain.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested1.json'
    file2 = 'tests/fixtures/nested2.json'
    assert generate_diff(file1, file2, 'plain') == expected


def test_generate_diff_nested_json_formater():
    with open('tests/fixtures/diff_nested_json_formater.txt') as f:
        expected = f.read().strip()
    file1 = 'tests/fixtures/nested1.json'
    file2 = 'tests/fixtures/nested2.json'
    assert generate_diff(file1, file2, 'json') == expected
