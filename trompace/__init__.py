import datetime
import json
from datetime import date
import logging

logger = logging.getLogger(__file__)


def docstring_interpolate(name, values):
    """Interpolate a variable into a function's docstring.
    Use to prevent duplication of documentation in `create` and `update` methods."""
    def _decorator(func):
        args = {name: values}
        if func.__doc__:
            func.__doc__ = func.__doc__.format(**args)
        return func

    return _decorator


def filter_none_args(args):
    """Filter a dictionary and only return items where the value is not None
    A StringConstant with a value of None is also counted as an empty value"""
    return {k: v for k, v in args.items() if v is not None}


def check_required_args(**kwargs):
    for arg, val in kwargs.items():
        if val is None:
            raise ValueError(f"required argument '{arg}' must not be None")


class StringConstant:
    """Some values in GraphQL are constants, not strings, and so they shouldn't
    be encoded or have quotes put around them. Use this to represent a constant
    and it won't be quoted in the query"""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value


def encode_list(thelist, encoder):
    for item in thelist:
        if isinstance(item, StringConstant):
            yield item.value
        elif isinstance(item, dict):
            yield "{" + make_parameters(**item) + "}"
        else:
            yield encoder.encode(item)


def make_filter(args: dict):
    assert len(args) == 1
    encoder = json.JSONEncoder()
    parts = ["{"]
    for k, v in args.items():
        parts.append(k + ":")
        if isinstance(v, dict):
            parts.append(make_filter(v))
        else:
            parts.append(encoder.encode(v))
    parts.append("}")
    return " ".join(parts)


def make_select_query(args) -> str:
    parts = []
    for a in args:
        if isinstance(a, str):
            parts.append(a)
        elif isinstance(a, dict):
            assert len(a) == 1
            for k, v in a.items():
                assert isinstance(v, list) or isinstance(v, dict)
                parts.append(k + "{")
                if isinstance(v, list):
                    parts.append(make_select_query(v))
                elif isinstance(v, dict):
                    parts.append(make_select_query([v]))
                parts.append("}")
        elif isinstance(a, list):
            parts.extend(a)
    return "\n".join(parts)


def make_parameters(**kwargs):
    """Convert query parameters to the graphql format.
    This creates a formatted string of parameters and values suitable to be passed to a graphql
    mutation or query. It has a special-case for String constants (that are represented without
    quotes around them) and lists.
    String constants in a list are supported, but only to one level deep.
    This method does no validation of parameter names.
    Arguments:
         **kwargs: a mapping of field names to values
    Returns:
        A string representation of the graphql parameters
    """
    encoder = json.JSONEncoder()
    parts = []
    for k, v in kwargs.items():
        if isinstance(v, StringConstant):
            value = v.value
        elif isinstance(v, datetime.datetime):
            value = f"{{formatted: {encoder.encode(v.isoformat())}}}"
        elif isinstance(v, list):
            value = "[{}]".format(", ".join(item for item in encode_list(v, encoder)))
        elif isinstance(v, dict):
            value = "{" + make_parameters(**v) + "}"
        else:
            value = encoder.encode(v)
        parts.append("{}: {}".format(k, value))
    return "\n        ".join(parts)


class _Neo4jDate(StringConstant):
    """The _Neo4jDate is used for Date values. It will be added as
    StringConstant in the GraphQL. The date will be formatted as:
        { year:[int] [month: [int] day: [int]] }

    The constructor argument can be a date, a list of dateparts [year, month,
    day] or a year. The month and day in the list of dateparts are optional.
    All dateparts should be of type int."""

    def __init__(self, value):
        if isinstance(value, str) and "-" in value:
            value = value.split("-")
        if isinstance(value, date):
            self.value = "{{ year: {0} month: {1} day: {2} }}".format(value.year, value.month, value.day)
        elif isinstance(value, list):
            date_parts = ['year', 'month', 'day']
            date_str = ""
            for i in range(min(len(date_parts), len(value))):
                # cast to int incase the value is a string - remove a leading 0 so that it's not
                # interpreted as octal
                date_str += "{0}: {1} ".format(date_parts[i], int(value[i]))
            self.value = "{{ {0}}}".format(date_str)
        else:
            self.value = "{{ year: {0} }}".format(value)


QUERY = '''query {{
  {query}
}}'''
