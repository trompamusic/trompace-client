from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation
from trompace import StringConstant, _Neo4jDate, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


MUSICRECORDING_ARGS_DOCS = """name: The name of the MusicRecording object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the MusicRecording to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the MusicRecording.
        source: The URL of the web resource about this MusicRecording.
        title: The title of the resource indicated by `source`
        """


@docstring_interpolate("musicrecording_args", MUSICRECORDING_ARGS_DOCS)
def mutation_create_musicrecording(*, name: str = None, title: str,  description: str, contributor: str, creator: str, source: str,
                                   format_: str, encodingformat: str = None, subject: str = None, language: str = None, date: str = None):
    """Returns a mutation for creating a MusicRecording object.
    https://schema.org/MusicRecording

    Arguments:
        {musicrecording_args}

    Returns:
        The string for the mutation for creating the MusicRecording.
    """
    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "name": name,
        "title": title,
        "description": description,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "encodingFormat": encodingformat,
        "subject": subject
    }

    if language is not None:
        args["language"] = StringConstant(language.lower())
    if date is not None:
        args["date"] = _Neo4jDate(date)

    args = filter_none_args(args)

    return format_mutation("CreateMusicRecording", args)


@docstring_interpolate("musicrecording_args", MUSICRECORDING_ARGS_DOCS)
def mutation_update_musicrecording(identifier: str, *, title: str = None, contributor: str = None,
                                   creator: str = None, source: str = None, encodingformat: str = None,
                                   format_: str = None, name: str = None, language: str = None,
                                   description: str = None, date: str = None, subject: str = None):
    """Returns a mutation for updating a MusicRecording object.
    https://schema.org/MusicRecording

    Arguments:
        identifier: The identifier of the MusicRecording in the CE to be updated
        {musicrecording_args}

    Returns:
        The string for the mutation for updating the MusicRecording.
    """
    if format_ is not None and "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "description": description,
        "encodingFormat": encodingformat,
        "subject": subject
    }

    if date is not None:
        args["date"] = _Neo4jDate(date)
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMusicRecording", args)


def mutation_delete_musicrecording(identifier: str):
    """Returns a mutation for deleting a MusicRecording object based on the identifier.
    https://schema.org/MusicRecording

    Arguments:
        identifier: The unique identifier of the MusicRecording object.

    Returns:
        The string for the mutation for deleting the MusicRecording object based on the identifier.
    """

    return format_mutation("DeleteMusicRecording", {"identifier": identifier})


def mutation_merge_music_recording_audio(recording_identifier, audio_identifier):
    """Returns a mutation for adding a Audio object to a MusicRecording object.
    (https://schema.org/workExample).

    Args:
        recording_identifier: The identifier of a MusicRecording.
        audio_identifier: The identifier of a AudioObject linked to a MusicRecording.

    Returns:
        The string for the mutation for adding a Audio object to a MusicRecording object.
    """
    return format_link_mutation("MergeMusicRecordingAudio", recording_identifier, audio_identifier)


def mutation_remove_music_recording_audio(recording_identifier, audio_identifier):
    """Returns a mutation for removing a Audio object to a MusicRecording object.
    (https://schema.org/workExample).

    Args:
        recording_identifier: The identifier of a MusicRecording.
        audio_identifier: The identifier of a AudioObject linked to a MusicRecording.

    Returns:
        The string for the mutation for removing a Audio object to a MusicRecording object.
    """
    return format_link_mutation("RemoveMusicRecordingAudio", recording_identifier, audio_identifier)
