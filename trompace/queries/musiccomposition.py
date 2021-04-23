# Generate GraphQL queries for queries pertaining to music compositions.
from typing import Optional, Union

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate, make_filter
from trompace.constants import SUPPORTED_LANGUAGES


def query_musiccomposition(identifier: str = None, title: str = None, contributor: str = None, creator: str = None,
                           source: str = None, inlanguage: str = None, name: str = None, position: int = None,
                           filter_: dict = None, return_items: Union[list, str] = None):
    """Returns a query for querying the database for a music composition.
    Arguments:
        identifier: The identifier of the music composition in the CE.
        title: The title of the resource indicated by `source`
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing\
                  the music composition to the web resource. This can be either a name or a base URL.
        source: The source URL that an item comes from
        inlanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        name: The name of the music composition.
        position: In the case that this is a movement of a larger work (e.g. a Symphony), the position of this
                  MusicComposition in the larger one.
        filter_: return nodes with this custom filter
        return_items: return these items in the response
    Returns:
        The string for the quereing the music composition.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if return_items is None:
        return_items = ["identifier", "title", "source"]

    if inlanguage and inlanguage not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(inlanguage)

    args = {
        "identifier": identifier,
        "title": title,
        "source": source,
        "contributor": contributor,
        "creator": creator,
        "inLanguage": inlanguage,
        "name": name,
        "position": position
    }
    if filter_:
        args["filter"] = StringConstant(make_filter(filter_))

    args = filter_none_args(args)

    return format_query("MusicComposition", args, return_items)
