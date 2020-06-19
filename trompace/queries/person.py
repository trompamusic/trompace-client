# Generate GraphQL queries for queries pertaining to person objects.

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


def query_person(identifier: str = None, contributor: str = None, creator: str = None,
                    source: str = None, language: str = None, format_: str = None,
                    name: str = None, family_name: str = None, given_name: str = None,
                    return_items_list: list = ["identifier", "name"]):

    """Returns a query for querying the database for a person object.
    Arguments:
        identifier: The identifier of the person in the CE.
        contributor: The main URL of the site where the information about this Person was taken from
        source: The URL of the web resource where information about this Person is taken from
        name: The name of the person
        family_name: The family name of the person
        given_name: The given name of the person
        return_item_list: A list of item fields that the query must return.
    Returns:
        The string for the mutation for creating the person.
    Raises:
        UnsupportedLanguageException if `language` is not one of the supported languages.
        NotAMimeTypeException if `format_` is not a valid mimetype.
    """


    args = {
        "identifier": identifier,
        "contributor": contributor,
        "source": source,
        "name": name,
        "familyName": family_name,
        "givenName": given_name,
    }

    args = filter_none_args(args)

    return format_query("Person", args, return_items_list)
