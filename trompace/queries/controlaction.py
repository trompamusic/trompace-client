from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES

QUERY_CONTROLACTION_ID = """
    query {{
        ControlAction(identifier: "{identifier}") {{
            actionStatus
            identifier
            wasDerivedFrom{{
                identifier
            }}
            object {{
                identifier
                ... on PropertyValue {{
                    wasDerivedFrom {{
                      identifier
                    }}               
                    value
                    name
                    title
                    nodeValue {{
                            ... on AudioObject {{
                               contentUrl
                              }}
                            ... on MediaObject {{
                               contentUrl
                              }}
                            ... on VideoObject {{
                               contentUrl
                              }}
                            ... on DigitalDocument {{
                               source
                              }}                       
                            format
                            
                    }}
                }}
            }}
        }}
    }}
"""


def query_controlaction(identifier: str):

    """Returns a query for querying the database for a controlaction object.
    Arguments:
        identifier: The identifier of the control action in the CE.
    Returns:
        The string for the quereing the control action.
    """
    query_ca = QUERY_CONTROLACTION_ID.format(identifier=identifier)
    return query_ca

def query_controlaction_filter(filter: str, return_items_list: list = ["identifier", "name"]):

    """Returns a query for querying the database for a controlaction object given a specific filter.
    Arguments:
        identifier: The identifier of the control action in the CE.
    Returns:
        The string for the quereing the control action.
    """
    query_ca = format_query("ControlAction", filter, return_items_list)
    return query_ca