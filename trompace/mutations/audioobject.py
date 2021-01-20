# Generate GraphQL queries for mutations pertaining to audio object objects.
from trompace import StringConstant, _Neo4jDate, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation

AUDIOOBJECT_ARGS_DOCS = """name: The name of the audio object.
        description: An account of the audio object.
        date: The date associated with the audio object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the audio object to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the audio object.
        encodingFormat: A MimeType of the format of object encoded by the audio object.
        source: The URL of the web resource about this audio object. If no such resource is available, use the
                same value as contentUrl.
        subject: The subject of the audio object.
        contentUrl: The URL of the content encoded by the audio object.
        url: 
        license: 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the audio object.
        title: The title of the resource indicated by `source`"""


@docstring_interpolate("audioobject_args", AUDIOOBJECT_ARGS_DOCS)
def mutation_create_audio_object(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                 name: str = None, description: str = None, date: str = None,
                                 encodingFormat: str = None, embedurl: str = None, url: str = None,
                                 contentUrl: str = None, language: str = None, inlanguage: str = None,
                                 license: str = None, subject: str = None):
    """Returns a mutation for creating a audo object object.

    Arguments:
        {audioobject_args}

    Returns:
        The string for the mutation for creating the audio object.

    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)
    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    if encodingFormat is not None and "/" not in encodingFormat:
        raise NotAMimeTypeException(encodingFormat)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "description": description,
        "encodingFormat": encodingFormat,
        "embedUrl": embedurl,
        "url": url,
        "license": license,
        "contentUrl": contentUrl,
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
def mutation_update_audio_object(identifier: str, *, name: str = None, title: str = None, description: str = None,
                                 date: str = None, creator: str = None, contributor: str = None,
                                 format_: str = None, encodingFormat: str = None, source: str = None, license: str = None,
                                 subject: str = None, contentUrl: str = None, language: str = None, inlanguage:str = None):
    """Returns a mutation for updating a audio object object.

    Arguments:
        identifier: The identifier of the audio object in the CE to be updated.
        {audioobject_args}

    Returns:
        The string for the mutation for updating the audio object.

    Raises:
        Assertion error if the input language or inLanguage is not one of the supported languages.
    """
    if format_ is not None and "/" not in format_:
        raise NotAMimeTypeException(format_)

    if encodingFormat is not None and "/" not in encodingFormat:
        raise NotAMimeTypeException(encodingFormat)

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
        "encodingFormat": encodingFormat,
        "source": source,
        "subject": subject,
        "contentUrl": contentUrl,
        "license": license,
        "inLanguage": inlanguage,
    }
    if date:
        args["date"] = _Neo4jDate(date)
    if language:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateAudioObject", args)


def mutation_delete_audio_object(identifier: str):
    """Returns a mutation for deleting a audio object object based on the identifier.

    Arguments:
        identifier: The unique identifier of the audio object object.

    Returns:
        The string for the mutation for deleting the audio object object based on the identifier.
    """

    return format_mutation("DeleteAudioObject", {"identifier": identifier})



def mutation_remove_audio_object_work_example(audio_object_identifier: str, work_identifier: str):
    """Returns a mutation for creating removing a audio object as an example of a work.

    Arguments:
        audio_object_identifier: The unique identifier of the audio object.
        work_identifier: The unique identifier of the work that the audio object is an example of.

    Returns:
        The string for the mutation for removing a audio object as an example of the work.
    """

    return format_link_mutation("RemoveAudioObjectExampleOfWork", audio_object_identifier, work_identifier)


def mutation_merge_audio_object_encoding(audio_object_identifier_1: str, audio_object_identifier_2: str):
    """Returns a mutation for creating merging a audio object as an encoding of another audio object.

    Arguments:
        audio_object_identifier_1: The unique identifier of the audio object that is encoding the other.
        audio_object_identifier_2: The unique identifier of the audio object being encoded.

    Returns:
        The string for the mutation for merging a audio object as an encoding of another audio object.
    """

    return format_link_mutation("MergeAudioObjectEncoding", audio_object_identifier_1, audio_object_identifier_2)


def mutation_remove_audio_object_encoding(audio_object_identifier_1: str, audio_object_identifier_2: str):
    """Returns a mutation for creating removing a audio object as an encoding of another audio object.

    Arguments:
        audio_object_identifier_1: The unique identifier of the audio object that is encoding the other.
        audio_object_identifier_2: The unique identifier of the audio object being encoded.

    Returns:
        The string for the mutation for removing a audio object as an encoding of another audio object.
    """

    return format_link_mutation("RemoveAudioObjectEncoding", audio_object_identifier_1, audio_object_identifier_2)


# link AudioObject to Work (step 5)
def mutation_merge_audio_object_work_example(audio_object_identifier: str, work_identifier: str):
    """Returns a mutation for creating merging a audio object as an example of a work.

    Arguments:
        audio_object_identifier: The unique identifier of the audio object.
        work_identifier: The unique identifier of the work that the audio object is an example of.

    Returns:
        The string for the mutation for merging a audio object as an example of the work.
    """

    return format_link_mutation("MergeAudioObjectExampleOfWork", audio_object_identifier, work_identifier)