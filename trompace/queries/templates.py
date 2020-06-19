# Templates for generating GraphQL queries.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from .. import make_parameters, QUERY
from typing import Dict, Any

from trompace.queries import QUERY
from trompace import make_parameters

QUERY_TEMPLATE = '''{queryname}{parameters}
{{
{return_items}
}}'''


def format_query(queryname: str, args: Dict[str, Any], return_items_list: list):
    """Create a query to send to the Contributor Environment.
    Arguments:
        mqueryname: the name of the query to generate
        args: a dictionary of field: value pairs to add to the query.
        return_items_list: A list of items for the query to return.
    Returns:
        A formatted query
    """

    parameters = ""
    if args:
        parameters = "({})".format(make_parameters(**args))
    formatted_query = QUERY_TEMPLATE.format(queryname=queryname, parameters=parameters, return_items="\n".join(return_items_list))
    return QUERY.format(query=formatted_query)
