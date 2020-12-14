from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES

QUERY_CONTROLACTION_ID = """
    query {{
        ControlAction(identifier: "{identifier}") {{
            actionStatus
            identifier
            object {{
                ... on PropertyValue {{
                    value
                    name
                    title
                    nodeValue {{
                        ... on DigitalDocument {{
                            format
                            source
                        }}
                    }}
                }}
            }}
        }}
    }}
"""


def query_controlaction(identifier: str = None):

    """Returns a query for querying the database for a controlaction object.
    Arguments:
        identifier: The identifier of the media object in the CE.

        The string for the quereing the media object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    query_ca = QUERY_CONTROLACTION_ID.format(identifier=identifier)
    return query_ca
