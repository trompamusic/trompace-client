# Generate GraphQL queries for queries pertaining to person objects.

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


def query_person(identifier: str = None, contributor: str = None, creator: str = None,
                 source: str = None, language: str = None, format_: str = None,
                 name: str = None, family_name: str = None, given_name: str = None,
                 return_items_list: list = ["identifier", "name"]):

    """Returns a query for retrieving a person or people.

    Arguments:
        identifier: The identifier of the person in the CE.
        contributor: The main URL of the site where the information about the Person was taken from
        creator: The person, organization or service who is creating this Person (e.g. URL of the software)
        source: The URL of the web resource where information about this Person is taken from
        language: The language the metadata is written in.
        format_: The mimetype of the resource indicated by `source`
        name: The name of the person
        family_name: The family name of the person
        given_name: The given name of the person
        return_items_list: A list of item fields that the query must return.

    Returns:
        The string for a person query.
    """

    args = {
        "identifier": identifier,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "language": language,
        "format": format_,
        "name": name,
        "familyName": family_name,
        "givenName": given_name,
    }

    args = filter_none_args(args)

    return format_query("Person", args, return_items_list)
