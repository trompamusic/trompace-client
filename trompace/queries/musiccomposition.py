# Generate GraphQL queries for queries pertaining to music compositions.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


def query_musiccomposition(identifier: str = None, title: str = None, contributor: str = None, creator: str = None, inlanguage: str = None,
							name: str = None, position: int = None, return_items_list: list = ["identifier", "name"]):

    """Returns a query for querying the database for a music composition.
    Arguments:
        identifier: The identifier of the music composition in the CE.
        title: The title of the resource indicated by `source`
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing\
                  the music composition to the web resource. This can be either a name or a base URL.
        inlanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        name: The name of the music composition.
        position: In the case that this is a movement of a larger work (e.g. a Symphony), the position of this
                  MusicComposition in the larger one.
        return_item_list: A list of item fields that the query must return.
    Returns:
        The string for the quereing the music composition.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if inlanguage and inlanguage not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(inlanguage)

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "inLanguage": inlanguage,
        "name": name,
        "position": position
    }

    args = filter_none_args(args)

    return format_query("MusicComposition", args, return_items_list)
