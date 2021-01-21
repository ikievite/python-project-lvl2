

"""module finds diff from two files."""


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
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': ' ',
                        'children': find_diff(value1, value2),
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': ' ',
                        'value': value1,
                    })
            elif value1 != value2:
                if isinstance(value1, dict) and isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': ' ',
                        'children': find_diff(value1, value2),
                    })
                elif isinstance(value1, dict):
                    if len(value1) == 1:
                        diff.append({
                            'name': key,
                            'type': 'complex',
                            'badge': '-',
                            'value': value1,
                        })
                    else:
                        diff.append({
                            'name': key,
                            'type': 'nested',
                            'badge': '-',
                            'children': value1,
                        })
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '+',
                        'value': value2,
                    })
                elif isinstance(value2, dict):
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': value1,
                    })
                    diff.append({
                        'name': key,
                        'type': 'nested',
                        'badge': '+',
                        'children': value2,
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': value1,
                    })
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '+',
                        'value': value2,
                    })
        elif key not in file2.keys():
            if isinstance(file1[key], dict):
                if len(file1[key]) == 1:
                    diff.append({
                        'name': key,
                        'type': 'flat',
                        'badge': '-',
                        'value': file1[key],
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'complex',
                        'badge': '-',
                        'value': file1[key],
                    })
            else:
                diff.append({
                    'name': key,
                    'type': 'flat',
                    'badge': '-',
                    'value': file1[key],
                })
    for key in file2.keys():  # noqa: WPS440
        if key not in file1:
            if isinstance(file2.get(key), dict):
                if len(file2[key]) == 1:
                    diff.append({
                        'name': key,
                        'type': 'complex',
                        'badge': '+',
                        'value': file2[key],
                    })
                else:
                    diff.append({
                        'name': key,
                        'type': 'complex',
                        'badge': '+',
                        'value': file2[key],
                    })
            else:
                diff.append({
                    'name': key,
                    'type': 'flat',
                    'badge': '+',
                    'value': file2[key],
                })
    return diff
