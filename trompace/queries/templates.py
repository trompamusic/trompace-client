# Templates for generate GraphQL queries for mutations.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from trompace.exceptions import UnsupportedLanguageException
from .. import make_parameters, QUERY
from ..constants import SUPPORTED_LANGUAGES




def query_create(args, query_string: str):
    """Returns a mutation for creating an object.
    Arguments:
        args: a dictionary of arguments for the template. The fucntion calling this function is responsible for validating the arguments.

    Returns:
        The string for the mutation for creating the object.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    create_query = query_string.format(parameters=make_parameters(**args))
    return QUERY.format(query=create_query)

