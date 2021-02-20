

"""module finds diff from two files."""


FLAT_TYPE = 'flat'
NESTED_TYPE = 'nested'
COMPLEX_TYPE = 'complex'
UNCHANGED_BADGE = ' '
ADDED_BADGE = '+'
REMOVED_BADGE = '-'


def find_diff(file1, file2):
    """Func find diff items.

    Args:
        file1: content of first file
        file2: content of second file

    Returns:
        list with diff items
    """
    diff = []
    for key in file1.keys():
        if key in file2:
            value1 = file1.get(key)
            value2 = file2.get(key)
            if value1 == value2:
                diff.append({
                    'name': key,
                    'type': FLAT_TYPE,
                    'badge': UNCHANGED_BADGE,
                    'value': value1,
                })
            elif value1 != value2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': NESTED_TYPE,
                        'badge': UNCHANGED_BADGE,
                        'children': find_diff(value1, value2),
                    })
                elif isinstance(value1, dict):
                    if len(value1) == 1:
                        diff.append({
                            'name': key,
                            'type': COMPLEX_TYPE,
                            'badge': REMOVED_BADGE,
                            'value': value1,
                        })
                    diff.append({
                        'name': key,
                        'type': FLAT_TYPE,
                        'badge': ADDED_BADGE,
                        'value': value2,
                    })
                elif isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': FLAT_TYPE,
                        'badge': REMOVED_BADGE,
                        'value': value1,
                    })
                    if len(value2) == 1:
                        diff.append({
                            'name': key,
                            'type': COMPLEX_TYPE,
                            'badge': ADDED_BADGE,
                            'value': value2,
                        })
                else:
                    diff.append({
                        'name': key,
                        'type': FLAT_TYPE,
                        'badge': REMOVED_BADGE,
                        'value': value1,
                    })
                    diff.append({
                        'name': key,
                        'type': FLAT_TYPE,
                        'badge': ADDED_BADGE,
                        'value': value2,
                    })
        elif key not in file2.keys():
            if isinstance(file1[key], dict):
                diff.append({
                    'name': key,
                    'type': COMPLEX_TYPE,
                    'badge': REMOVED_BADGE,
                    'value': file1[key],
                })
            else:
                diff.append({
                    'name': key,
                    'type': FLAT_TYPE,
                    'badge': REMOVED_BADGE,
                    'value': file1[key],
                })
    for key in file2.keys():  # noqa: WPS440
        if key not in file1:
            if isinstance(file2.get(key), dict):
                diff.append({
                    'name': key,
                    'type': COMPLEX_TYPE,
                    'badge': ADDED_BADGE,
                    'value': file2[key],
                })
            else:
                diff.append({
                    'name': key,
                    'type': FLAT_TYPE,
                    'badge': ADDED_BADGE,
                    'value': file2[key],
                })
    return diff
