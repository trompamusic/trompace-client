name = "subscriptions"

import json


class StringConstant:
    """Some values in GraphQL are constants, not strings, and so they shouldn't
    be encoded or have quotes put around them. Use this to represent a constant
    and it won't be quoted in the query"""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class ListConstant:
    """Some values in GraphQL are constants, not strings, and so they shouldn't
    be encoded or have quotes put around them. Use this to represent a  list of 
    constants and it won't be quoted in the query"""

    def __init__(self, values):
        self.values = [StringConstant(x) for x in values]


def BoolConstant(in_bool: bool):
    """ Converts a boolean value to a constant string value."""
    if in_bool:
        return StringConstant('true')
    else:
        return StringConstant('false')


def make_parameters(**kwargs):
    """Convert mutation query parameters from dictionary to string format.
    """
    encoder = json.JSONEncoder()
    parts = []
    for k, v in kwargs.items():
        if isinstance(v, StringConstant):
            value = v.value
        elif isinstance(v, ListConstant):
            value = v.values
        else:
            value = encoder.encode(v)
        parts.append("{}: {}".format(k, value))
    return "\n        ".join(parts)


SUBSCRIPTION = '''subscription {{
  {subscription}
}}'''
