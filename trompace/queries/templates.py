# Templates for generating GraphQL queries.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from typing import Dict, Any

from trompace.queries import QUERY
from trompace import make_parameters, make_select_query

QUERY_TEMPLATE = '''{queryname}{parameters}
{{
{return_items}
}}'''

QUERY_FILTER_TEMPLATE = '''{queryname}(
filter:{{
{parameters}
}}
)
{{
{return_items}
}}'''

QUERY_ITEMLIST_TEMPLATE = '''{queryname}(
filter:{{
{parameters}
}}
)
{{
identifier
itemListElement{{
    ... on ListItem {{
    identifier
    position
    nextItem{{identifier}}
    }}
}}
}}'''


def format_query(queryname: str, args: Dict[str, Any], return_items_list: list):
    """Create a query to send to the Contributor Environment.
    Arguments:
        queryname: the name of the query to generate
        args: a dictionary of field: value pairs to add to the query.
        return_items_list: A list of items for the query to return.
    Returns:
        A formatted query
    """

    parameters = ""
    if args:
        parameters = "({})".format(make_parameters(**args))
    formatted_query = QUERY_TEMPLATE.format(queryname=queryname, parameters=parameters,
                                            return_items=make_select_query(return_items_list))
    return QUERY.format(query=formatted_query)


def format_filter_query(queryname: str, args: Dict[str, Any], return_items_list: list):
    """Create a query to send to the Contributor Environment.
    Arguments:
        queryname: the name of the query to generate
        args: a dictionary of field: value pairs to add to the query.
        return_items_list: A list of items for the query to return.
    Returns:
        A formatted query
    """

    parameters = ""
    if args:
        parameters = make_parameters(**args)
    formatted_query = QUERY_FILTER_TEMPLATE.format(queryname=queryname, parameters=parameters,
                                                   return_items="\n".join(return_items_list))
    return QUERY.format(query=formatted_query)


def format_itemlist_query(queryname: str, args: Dict[str, Any]):
    """Create a query to send to the Contributor Environment.
    Arguments:
        queryname: the name of the query to generate
        args: a dictionary of field: value pairs to add to the query.
        return_items_list: A list of items for the query to return.
    Returns:
        A formatted query
    """

    parameters = ""
    if args:
        parameters = make_parameters(**args)
    formatted_query = QUERY_ITEMLIST_TEMPLATE.format(queryname=queryname, parameters=parameters)
    return QUERY.format(query=formatted_query)
