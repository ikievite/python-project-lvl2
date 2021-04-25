

"""module that encode value to appropriate viev."""


def encode_to_output(value):  # noqa: WPS110 # ignore warning wrong variable name: value
    """Func encodes value to the selected view.

    Args:
        value: value from node

    Returns:
        encoded value
    """
    if value is True:
        node_value = 'true'
    elif value is False:
        node_value = 'false'
    elif value is None:
        node_value = 'null'
    else:
        node_value = value
    return node_value
