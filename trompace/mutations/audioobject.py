from trompace import StringConstant, _Neo4jDate, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation

AUDIOOBJECT_ARGS_DOCS = """name: The name of the audio object.
        description: An account of the audio object.
        date: The date associated with the audio object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the audio object to the web resource.
                     This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the audio object.
        encodingformat: A MimeType of the format of object encoded by the audio object.
        source: The URL of the web resource about this audio object. If no such resource is available, use the
                same value as contentUrl.
        subject: The subject of the audio object.
        contenturl: The URL of the content encoded by the audio object.
        url:
        license:
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inlanguage: The language of the audio object.
        title: The title of the resource indicated by `source`"""


@docstring_interpolate("audioobject_args", AUDIOOBJECT_ARGS_DOCS)
def mutation_create_audioobject(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                name: str = None, description: str = None, date: str = None,
                                encodingformat: str = None, embedurl: str = None, url: str = None,
                                contenturl: str = None, language: str = None, inlanguage: str = None,
                                license: str = None, subject: str = None):
    """Returns a mutation for creating a AudioObject.

    Arguments:
        {audioobject_args}

    Returns:
        The string for the mutation for creating the AudioObject.

    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
        ValueError if a required argument is None
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
        "subject": subject
    }

    if date is not None:
        args["date"] = _Neo4jDate(date)
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreateAudioObject", args)


@docstring_interpolate("audioobject_args", AUDIOOBJECT_ARGS_DOCS)
def mutation_update_audioobject(identifier: str, *, name: str = None, title: str = None, description: str = None,
                                date: str = None, creator: str = None, contributor: str = None,
                                format_: str = None, encodingformat: str = None, source: str = None, license: str = None,
                                subject: str = None, contenturl: str = None, language: str = None, inlanguage: str = None):
    """Returns a mutation for updating a AudioObject.

    Arguments:
        identifier: The identifier of the AudioObject in the CE to be updated.
        {audioobject_args}

    Returns:
        The string for the mutation for updating the AudioObject.

    Raises:
        Assertion error if the input language or inlanguage is not one of the supported languages.
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
        "contentUrl": contenturl,
        "license": license,
        "inLanguage": inlanguage,
    }
    if date:
        args["date"] = _Neo4jDate(date)
    if language:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateAudioObject", args)


def mutation_delete_audioobject(identifier: str):
    """Returns a mutation for deleting a AudioObject based on the identifier.

    Arguments:
        identifier: The unique identifier of the AudioObject.

    Returns:
        The string for the mutation for deleting the AudioObject based on the identifier.
    """

    return format_mutation("DeleteAudioObject", {"identifier": identifier})


def mutation_merge_audioobject_encoding(audioobject_identifier: str, audiobject_derivative_identifier: str):
    """Returns a mutation for indicating that a derivative AudioObject *encodes* a primary AudioObject
    (https://schema.org/encoding). For example a transcription of a score is an *encoding* of that score.

    Arguments:
        audiobject_identifier: The unique identifier of the "main" AudioObject.
        audiobject_derivative_identifier: The unique identifier of the AudioObject which is the encoding.

    Returns:
        A GraphQL mutation for MergeAudioObjectEncoding.
    """

    return format_link_mutation("MergeAudioObjectEncoding", audioobject_identifier, audiobject_derivative_identifier)


def mutation_remove_audioobject_encoding(audioobject_identifier: str, audiobject_derivative_identifier: str):
    """Returns a mutation for removing that a derivative AudioObject *encodes* a primary AudioObject
    (https://schema.org/encoding). For example a transcription of a score is an *encoding* of that score.

    Arguments:
        audiobject_identifier: The unique identifier of the "main" AudioObject.
        audiobject_derivative_identifier: The unique identifier of the AudioObject which is the encoding.

    Returns:
        A GraphQL mutation for RemoveAudioObjectEncoding.
    """
    return format_link_mutation("RemoveAudioObjectEncoding", audioobject_identifier, audiobject_derivative_identifier)


def mutation_merge_audioobject_exampleofwork(audioobject_identifier: str, work_identifier: str):
    """Returns a mutation for indicating that a AudioObject is an example of a work
    (https://schema.org/exampleOfWork).

    Arguments:
        audioobject_identifier: The unique identifier of the AudioObject.
        work_identifier: The unique identifier of the work that the AudioObject is an example of.

    Returns:
        A GraphQL mutation for MergeAudioObjectExampleOfWork.
    """

    return format_link_mutation("MergeAudioObjectExampleOfWork", audioobject_identifier, work_identifier)


def mutation_remove_audioobject_exampleofwork(audioobject_identifier: str, work_identifier: str):
    """Returns a mutation for removing that a AudioObject is an example of a work
    (https://schema.org/exampleOfWork).

    Arguments:
        audio_object_identifier: The unique identifier of the AudioObject.
        work_identifier: The unique identifier of the work that the AudioObject is an example of.

    Returns:
        A GraphQL mutation for RemoveAudioObjectExampleOfWork.
    """

    return format_link_mutation("RemoveAudioObjectExampleOfWork", audioobject_identifier, work_identifier)
