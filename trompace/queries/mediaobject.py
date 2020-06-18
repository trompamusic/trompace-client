# Generate GraphQL queries for queries pertaining to media objects.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES

MEDIAOBJECT_ARGS_DOCS = """identifier: The identifier of the media object in the CE.
        name: The name of the media object.
        description: An account of the media object.
        date: The date associated with the media object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the media object to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the media object.
        encodingFormat: A MimeType of the format of object encoded by the media object.
        source: The URL of the web resource to be represented by the node.
        subject: The subject of the media object.
        contentUrl: The URL of the content encoded by the media object.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the media object. Currently supported languages are en,es,ca,nl,de,fr
        title: The title of the resource indicated by `source`"""


@docstring_interpolate("mediaobject_args", MEDIAOBJECT_ARGS_DOCS)
def query_mediaobject(identifier: str=None, creator: str=None, contributor: str=None,\
 encodingFormat: str=None, source: str=None, contentUrl:str=None, return_items_list: list=None):

    """Returns a query for querying the database for a media object.
    Arguments:
        {mediaobject_args}
    Returns:
        The string for the quereing the media object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """



    if encodingFormat and "/" not in encodingFormat:
        raise NotAMimeTypeException(encodingFormat)
        
    if not return_items_list:
        return_items_list = ["identifier", "name"]
    args = {
        "identifier": identifier,
        "creator": creator,
        "contributor": contributor,
        "encodingFormat": encodingFormat,
        "source": source,
        "contentUrl": contentUrl,
    }

    args = filter_none_args(args)

    return format_query("MediaObject", args, return_items_list)
