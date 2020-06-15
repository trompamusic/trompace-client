# Templates for generating GraphQL queries.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from .. import make_parameters, QUERY
from typing import Dict, Any

from trompace.queries import QUERY
from trompace import make_parameters

QUERY_TEMPLATE = '''{queryname}(
{parameters}
) {{
identifier
name
publisher
contributor
creator
source
description
language
}}'''

QUERY_ALL_TEMPLATE = '''{queryname}{{
identifier
name
publisher
contributor
creator
source
description
language
}}'''



def format_query(queryname: str, args: Dict[str, Any]):
    """Create a query to send to the Contributor Environment.
    Arguments:
        mqueryname: the name of the query to generate
        args: a dictionary of field: value pairs to add to the query.
    Returns:
        A formatted query
    """
    if args:
    	formatted_query = QUERY_TEMPLATE.format(queryname=queryname, parameters=make_parameters(**args))
    else:
    	formatted_query = QUERY_ALL_TEMPLATE.format(queryname=queryname)
    return QUERY.format(query=formatted_query)

