

''' Tests for gendiff project.'''

import pytest
from gendiff.format_diff import format_diff


def test_format_diff_jsonlike_formater():
    with pytest.raises(Exception):
        format_diff({}, 'jsonlike')
