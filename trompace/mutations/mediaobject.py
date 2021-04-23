# Generate GraphQL queries for mutations pertaining to media object objects.
from trompace import StringConstant, _Neo4jDate, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation

MEDIAOBJECT_ARGS_DOCS = """name: The name of the media object.
        description: An account of the media object.
        date: The date associated with the media object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the media object to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the media object.
        encodingformat: A MimeType of the format of object encoded by the media object.
        source: The URL of the web resource about this media object. If no such resource is available, use the
                same value as contentUrl.
        subject: The subject of the media object.
        contenturl: The URL of the content encoded by the media object.
        url: 
        license: 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the media object.
        title: The title of the resource indicated by `source`"""


@docstring_interpolate("mediaobject_args", MEDIAOBJECT_ARGS_DOCS)
def mutation_create_media_object(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                 name: str = None, description: str = None, date: str = None,
                                 encodingformat: str = None, embedurl: str = None, url: str = None,
                                 contenturl: str = None, language: str = None, inlanguage: str = None,
                                 license: str = None):
    """Returns a mutation for creating a media object object.

    Arguments:
        {mediaobject_args}

    Returns:
        The string for the mutation for creating the media object.

    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)
    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    if encodingformat is not None and "/" not in encodingformat:
        raise NotAMimeTypeException(encodingformat)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "description": description,
        "encodingFormat": encodingformat,
        "embedUrl": embedurl,
        "url": url,
        "license": license,
        "contentUrl": contenturl,
        "inLanguage": inlanguage,
    }

    if date is not None:
        args["date"] = _Neo4jDate(date)
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreateMediaObject", args)


@docstring_interpolate("mediaobject_args", MEDIAOBJECT_ARGS_DOCS)
def mutation_update_media_object(identifier: str, *, name: str = None, title: str = None, description: str = None,
                                 date: str = None, creator: str = None, contributor: str = None, format_: str = None,
                                 encodingformat: str = None, source: str = None, license: str = None, subject: str = None,
                                 url: str = None, contenturl: str = None, language: str = None, inlanguage:str = None):
    """Returns a mutation for updating a media object object.

    Arguments:
        identifier: The identifier of the media object in the CE to be updated.
        {mediaobject_args}

    Returns:
        The string for the mutation for updating the media object.

    Raises:
        Assertion error if the input language or inLanguage is not one of the supported languages.
    """
    if format_ is not None and "/" not in format_:
        raise NotAMimeTypeException(format_)

    if encodingformat is not None and "/" not in encodingformat:
        raise NotAMimeTypeException(encodingformat)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "identifier": identifier,
        "name": name,
        "title": title,
        "description": description,
        "creator": creator,
        "contributor": contributor,
        "format": format_,
        "encodingFormat": encodingformat,
        "source": source,
        "subject": subject,
        "url": url,
        "contentUrl": contenturl,
        "license": license,
        "inLanguage": inlanguage,
    }
    if date:
        args["date"] = _Neo4jDate(date)
    if language:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMediaObject", args)


def mutation_delete_media_object(identifier: str):
    """Returns a mutation for deleting a media object object based on the identifier.

    Arguments:
        identifier: The unique identifier of the media object object.

    Returns:
        The string for the mutation for deleting the media object object based on the identifier.
    """

    return format_mutation("DeleteMediaObject", {"identifier": identifier})


def mutation_merge_mediaobject_example_of_work(mediaobject_identifier: str, work_identifier: str):
    """Returns a mutation for indicating that a MediaObject is an example of a work
    (https://schema.org/exampleOfWork).

    Arguments:
        mediaobject_identifier: The unique identifier of the media object.
        work_identifier: The unique identifier of the work that the media object is an example of.

    Returns:
        A GraphQL mutation for MergeMediaObjectExampleOfWork.
    """

    return format_link_mutation("MergeMediaObjectExampleOfWork", mediaobject_identifier, work_identifier)


def mutation_remove_mediaobject_example_of_work(mediaobject_identifier: str, work_identifier: str):
    """Returns a mutation for removing that a MediaObject is an example of a work
    (https://schema.org/exampleOfWork).

    Arguments:
        mediaobject_identifier: The unique identifier of the media object.
        work_identifier: The unique identifier of the work that the media object is an example of.

    Returns:
        A GraphQL mutation for RemoveMediaObjectExampleOfWork.
    """

    return format_link_mutation("RemoveMediaObjectExampleOfWork", mediaobject_identifier, work_identifier)


def mutation_merge_media_object_encoding(mediaobject_identifier: str, mediaobject_derivative_identifier: str):
    """Returns a mutation for indicating that a derivative MediaObject *encodes* a primary MediaObject
    (https://schema.org/encoding). For example a transcription of a score is an *encoding* of that score.

    Arguments:
        mediaobject_identifier: The unique identifier of the "main" MediaObject.
        mediaobject_derivative_identifier: The unique identifier of the MediaObject which is the encoding.

    Returns:
        A GraphQL mutation for MergeMediaObjectEncoding.
    """

    return format_link_mutation("MergeMediaObjectEncoding", mediaobject_identifier, mediaobject_derivative_identifier)


def mutation_remove_media_object_encoding(mediaobject_identifier: str, mediaobject_derivative_identifier: str):
    """Returns a mutation for removing that a derivative MediaObject *encodes* a primary MediaObject
    (https://schema.org/encoding).

    Arguments:
        mediaobject_identifier: The unique identifier of the "main" MediaObject.
        mediaobject_derivative_identifier: The unique identifier of the MediaObject which is the encoding.

    Returns:
        A GraphQL mutation for RemoveMediaObjectEncoding.
    """

    return format_link_mutation("RemoveMediaObjectEncoding", mediaobject_identifier, mediaobject_derivative_identifier)


def mutation_merge_media_object_wasderivedfrom(mediaobject_derivative_identifier: str,
                                               mediaobject_source_identifier: str):
    """Returns a mutation for indicating that a MediaObject *was derived from* a primary MediaObject
    (http://www.w3.org/ns/prov#wasDerivedFrom). For example a PDF generated from a MusicXML source file
    was derived from that source file.

    Arguments:
        mediaobject_derivative_identifier: The unique identifier of the MediaObject which is the derivative.
        mediaobject_source_identifier: The unique identifier of the "source" MediaObject.

    Returns:
        A GraphQL mutation for MergeMediaObjectWasDerivedFrom.
    """

    return format_link_mutation("MergeMediaObjectWasDerivedFrom",
                                mediaobject_derivative_identifier,
                                mediaobject_source_identifier)


def mutation_remove_media_object_wasderivedfrom(mediaobject_derivative_identifier: str, mediaobject_source_identifier: str):
    """Returns a mutation for removing that a MediaObject *was derived from* a primary MediaObject
    (http://www.w3.org/ns/prov#wasDerivedFrom).

    Arguments:
        mediaobject_derivative_identifier: The unique identifier of the MediaObject which is the derivative.
        mediaobject_source_identifier: The unique identifier of the "source" MediaObject.

    Returns:
        A GraphQL mutation for RemoveMediaObjectWasDerivedFrom.
    """

    return format_link_mutation("RemoveMediaObjectWasDerivedFrom",
                                mediaobject_derivative_identifier,
                                mediaobject_source_identifier)


def mutation_add_media_object_used(mediaobject_identifier: str, thing_identifier: str):
    """Returns a mutation for indicating that a MediaObject *used* some other thing to create it
    (http://www.w3.org/ns/prov#used). For example an MEI file coverted from musicxml might use
    the verovio software.

    Arguments:
        mediaobject_identifier: The unique identifier of a MediaObject.
        thing_identifier: The unique identifier of some Thing that was used to create the MediaObject.

    Returns:
        A GraphQL mutation for MergeMediaObjectUsed.
    """
    return format_link_mutation("MergeMediaObjectUsed", mediaobject_identifier, thing_identifier)
