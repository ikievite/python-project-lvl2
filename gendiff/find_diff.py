

"""module finds diff from two files."""


ADDED = 'ADDED'
REMOVED = 'REMOVED'
CHANGED = 'CHANGED'
UNCHANGED = 'UNCHANGED'
NODE_NAME = 'name'
NODE_STATE = 'state'
NODE_VALUE = 'value'
NODE_CHILDREN = 'children'


def find_diff(dict1, dict2):
    """Func find diff items.

    Args:
        dict1: content of first file
        dict2: content of second file

    Returns:
        list with diff items
    """
    diff = []
    for key in set(dict1) & set(dict2):
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if value1 == value2:
            diff.append({
                NODE_NAME: key,
                NODE_STATE: UNCHANGED,
                NODE_VALUE: value2,
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                NODE_NAME: key,
                NODE_STATE: UNCHANGED,
                NODE_CHILDREN: find_diff(value1, value2),
            })
        else:
            diff.append({
                NODE_NAME: key,
                NODE_STATE: CHANGED,
                NODE_VALUE: {REMOVED: value1, ADDED: value2},
            })
    for added_key in set(dict2) - set(dict1):
        diff.append({
            NODE_NAME: added_key,
            NODE_STATE: ADDED,
            NODE_VALUE: dict2.get(added_key),
        })
    for removed_key in set(dict1) - set(dict2):
        diff.append({
            NODE_NAME: removed_key,
            NODE_STATE: REMOVED,
            NODE_VALUE: dict1.get(removed_key),
        })
    return diff
