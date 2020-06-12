# Generate GraphQL queries for queries pertaining to media objects.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.queries.templates import format_query
from trompace import StringConstant, _Neo4jDate, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES


def query_mediaobject(identifier: str=None, name: str=None, description: str=None, date: str=None, creator: str=None, contributor: str=None, format_: str=None,\
 encodingFormat: str=None, source: str=None, subject: str=None, contentUrl:str=None, language: str=None, title:str=None):

    """Returns a mutation for creating a media object object
    Arguments:
        identifier: The identifier of the media object in the CE to be updated
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
        title: The title of the page from which the media object information was extracted.  
    Returns:
        The string for the quereing the media object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if format_ and "/" not in format_:
        raise NotAMimeTypeException(format_)


    if encodingFormat and "/" not in encodingFormat:
        raise NotAMimeTypeException(encodingFormat)

    args = {
        "identifier": identifier,
        "name": name,
        "title": title,
        "description": description,
        "creator": creator,
        "contributor": contributor,
        "format": format_,
        "encodingFormat": encodingFormat,
        "source": source,
        "subject": subject,
        "contentUrl": contentUrl,
    }

    if language is not None:
        args["language"] = StringConstant(language.lower())
    if date is not None:
        args["date"] = _Neo4jDate(date)

    args = filter_none_args(args)

    return format_query("MediaObject", args)
