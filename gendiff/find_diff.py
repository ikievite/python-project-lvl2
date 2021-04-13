

"""module finds diff from two files."""


ADDED = 'ADDED'
REMOVED = 'REMOVED'
CHANGED = 'CHANGED'
UNCHANGED = 'UNCHANGED'


def find_diff(dict1, dict2):
    """Func find diff items.

    Args:
        dict1: content of first file
        dict2: content of second file

    Returns:
        list with diff items
    """
    diff = []

    for key in dict2.keys():
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key in dict1.keys():
            if value1 == value2:
                diff.append({
                    'name': key,
                    'state': UNCHANGED,
                    'value': value2,
                })
            elif isinstance(value1, dict) and isinstance(value2, dict):
                diff.append({
                    'name': key,
                    'state': UNCHANGED,
                    'children': find_diff(value1, value2),
                })
            else:
                diff.append({
                    'name': key,
                    'state': CHANGED,
                    'value': {REMOVED: value1, ADDED: value2},
                })
        else:
            diff.append({
                'name': key,
                'state': ADDED,
                'value': value2,
            })
    for key in dict1.keys():  # noqa: WPS440 # ignore var overlap
        value1 = dict1.get(key)
        if key not in dict2.keys():
            diff.append({
                'name': key,
                'state': REMOVED,
                'value': value1,
            })

    return diff
