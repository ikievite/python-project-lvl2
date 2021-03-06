

''' Tests for gendiff project.'''

import pytest
from gendiff.formaters.format_diff import format_diff


def test_format_diff_jsonlike_formater():
    with pytest.raises(Exception) as excinfo:
        format_diff({}, 'jsonlike')
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Wrong formater: 'jsonlike'"
