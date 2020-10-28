# Generate GraphQL queries for queries pertaining to media objects.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


def query_mediaobject(identifier: str = None, creator: str = None, contributor: str = None,
                      encodingformat: str = None, source: str = None, contenturl: str = None, inlanguage:str = None,
                      return_items_list: list = ["identifier", "name"]):

    """Returns a query for querying the database for a media object.
    Arguments:
        identifier: The identifier of the media object in the CE.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing\
         the media object to the web resource. This can be either a name or a base URL.
        encodingformat: A MimeType of the format of object encoded by the media object.
        source: The URL of the web resource to be represented by the node.
        contenturl: The URL of the content encoded by the media object.
        inlanguage: The language of the media object. Currently supported languages are en,es,ca,nl,de,fr.
        return_items_list: A list of item fields that the query must return.
    Returns:
        The string for the quereing the media object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if encodingformat and "/" not in encodingformat:
        raise NotAMimeTypeException(encodingformat)

    args = {
        "identifier": identifier,
        "creator": creator,
        "contributor": contributor,
        "encodingFormat": encodingformat,
        "source": source,
        "contentUrl": contenturl,
        "inLanguage": inlanguage
    }

    args = filter_none_args(args)

    return format_query("MediaObject", args, return_items_list)
