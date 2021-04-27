

''' Tests for module loader.'''


import pytest
from gendiff.loader import load_content


def test_loader():
    with pytest.raises(Exception) as excinfo:
        load_content('tests/fixtures/nested2')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Wrong file type, neither json nor yaml/yml"
