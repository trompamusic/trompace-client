# Generate GraphQL queries for mutations pertaining to music composition objects.
from trompace import StringConstant, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation


MUSICCOMPOSITION_ARGS_DOCS = """title: The title of the resource indicated by `source`
        contributor: The main URL of the site where the information about this MusicComposition was taken from
        creator: The person, organization or service who is creating this MusicComposition (e.g. URL of the software)
        source: The URL of the web resource where information about this MusicComposition is taken from
        format_: The mimetype of the resource indicated by `source`
        subject: The subject of the music composition.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inlanguage: The language of the music composition.
        name: The name of the music composition.
        description: An account of the music composition.
        position: In the case that this is a movement of a larger work (e.g. a Symphony), the position of this
                  MusicComposition in the larger one.
"""


@docstring_interpolate("musiccomposition_args", MUSICCOMPOSITION_ARGS_DOCS)
def mutation_create_music_composition(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                      subject: str = None, language: str = None, inlanguage: str = None,
                                      name: str = None, description: str = None, position: int = None):
    """Returns a mutation for creating a music composition object

    Args:
        {musiccomposition_args}

    Returns:
        The string for the mutation for creating the music composition.

    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        NotAMimeTypeException: if ``format_`` is not a valid mimetype
    """
    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)
    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "format": format_,
        "subject": subject,
        "source": source,
        "inLanguage": inlanguage,
        "name": name,
        "description": description,
        "position": position
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreateMusicComposition", args)


@docstring_interpolate("musiccomposition_args", MUSICCOMPOSITION_ARGS_DOCS)
def mutation_update_music_composition(identifier: str, *, title: str = None, contributor: str = None, creator: str = None,
                                      source: str = None, format_: str = None,
                                      subject: str = None, language: str = None, inlanguage: str = None,
                                      name: str = None, description: str = None, position: int = None):
    """Returns a mutation for updating a MusicComposition object.
    
    Args:
        identifier: The identifier of the MusicComposition in the CE to be updated
        {musiccomposition_args}

    Returns:
        The string for the mutation for updating the music composition.
    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        NotAMimeTypeException: if ``format_`` is not a valid mimetype
    """

    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if format_ and "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {"identifier": identifier,
            "title": title,
            "contributor": contributor,
            "creator": creator,
            "subject": subject,
            "source": source,
            "inLanguage": inlanguage,
            "format": format_,
            "name": name,
            "description": description,
            "position": position
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMusicComposition", args)


def mutation_delete_music_composition(identifier: str):
    """Returns a mutation for deleting a MusicComposition.

    Args:
        identifier: The identifier of the MusicComposition.
    Returns:
        The string for the mutation for deleting the music composition object based on the identifier.
    """

    return format_mutation("DeleteMusicComposition", {"identifier": identifier})


def mutation_merge_music_composition_included_composition(main_identifier, part_identifier):
    """Returns a mutation for adding a MusicComposition as an included composition of another MusicComposition
    (https://schema.org/includedComposition). For example, the first movement of a composition could be
    represented as an includedComposition of a main symphony.

    Args:
        main_identifier: The identifier of a main MusicComposition.
        part_identifier: The identifier of a MusicComposition which is an included part of the main MusicComposition.
    """
    return format_link_mutation("MergeMusicCompositionIncludedComposition", main_identifier, part_identifier)


def mutation_remove_music_composition_included_composition(main_identifier, part_identifier):
    """Returns a mutation for removing a MusicComposition as an included composition of another MusicComposition
    (https://schema.org/includedComposition).

    Args:
        main_identifier: The identifier of a main MusicComposition.
        part_identifier: The identifier of a MusicComposition which is an included part of the main MusicComposition.
    """
    return format_link_mutation("RemoveMusicCompositionIncludedComposition", main_identifier, part_identifier)


def mutation_merge_music_composition_has_part(main_identifier, part_identifier):
    """Returns a mutation for adding a MusicComposition as a part of another MusicComposition
    (https://schema.org/hasPart). For example, the first movement of a composition could be
    represented as a hasPart of a main symphony.

    Args:
        main_identifier: The identifier of a main MusicComposition.
        part_identifier: The identifier of a MusicComposition which is a part of the main MusicComposition.
    """
    return format_link_mutation("MergeMusicCompositionHasPart", main_identifier, part_identifier)


def mutation_remove_music_composition_has_part(main_identifier, part_identifier):
    """Returns a mutation for removing a MusicComposition as a part of another MusicComposition
    (https://schema.org/hasPart).

    Args:
        main_identifier: The identifier of a main MusicComposition.
        part_identifier: The identifier of a MusicComposition which is a part of the main MusicComposition.
    """
    return format_link_mutation("RemoveMusicCompositionHasPart", main_identifier, part_identifier)


def mutation_merge_music_composition_composer(composition_identifier, person_identifier):
    """Returns a mutation for adding a Person as the composer of a MusicComposition
    (https://schema.org/composer).

    Args:
        composition_identifier: The identifier of a MusicComposition.
        person_identifier: The identifier of a Person who composed the MusicComposition.
    """
    return format_link_mutation("MergeMusicCompositionComposer", composition_identifier, person_identifier)


def mutation_remove_music_composition_composer(composition_identifier, person_identifier):
    """Returns a mutation for removing a Person as the composer of a MusicComposition
    (https://schema.org/composer).

    Args:
        composition_identifier: The identifier of a MusicComposition.
        person_identifier: The identifier of a Person who composed the MusicComposition.
    """
    return format_link_mutation("RemoveMusicCompositionComposer", composition_identifier, person_identifier)


def mutation_merge_music_composition_exact_match(from_identifier, to_identifier):
    """Returns a mutation for indicating that two MusicComposition objects represent the same composition
    (http://www.w3.org/2004/02/skos/core#exactMatch).

    Args:
        from_identifier: The identifier of one MusicComposition.
        to_identifier: The identifier of another MusicComposition.
    """
    return format_link_mutation("MergeMusicCompositionExactMatch", from_identifier, to_identifier)


def mutation_remove_music_composition_exact_match(from_identifier, to_identifier):
    """Returns a mutation for removing two MusicComposition representing the same composition
    (http://www.w3.org/2004/02/skos/core#exactMatch).

    Args:
        from_identifier: The identifier of one MusicComposition.
        to_identifier: The identifier of another MusicComposition.
    """
    return format_link_mutation("RemoveMusicCompositionExactMatch", from_identifier, to_identifier)


def mutation_merge_music_composition_work_example(music_composition_id: str, creativework_id: str):
    """Returns a mutation for adding a CreativeWork as an example of a MusicComposition
    (https://schema.org/workExample).

    Args:
        music_composition_id: The identifier of a MusicComposition.
        creativework_id: The identifier of a CreativeWork which is an example of the MusicComposition.
    """

    return format_link_mutation("MergeMusicCompositionWorkExample", music_composition_id, creativework_id)


def mutation_remove_music_composition_work_example(music_composition_id: str, creativework_id: str):
    """Returns a mutation for removing a CreativeWork as an example of a MusicComposition
    (https://schema.org/workExample).

    Args:
        music_composition_id: The identifier of a MusicComposition.
        creativework_id: The identifier of a CreativeWork which is an example of the MusicComposition.
    """

    return format_link_mutation("RemoveMusicCompositionWorkExample", music_composition_id, creativework_id)

def mutation_merge_music_composition_recorded_as(music_composition_id: str, music_recording_id: str):
    """Returns a mutation for adding a MusicRecording as an recording of a MusicComposition
    (https://schema.org/recordedAs).

    Args:
        music_composition_id: The identifier of a MusicComposition.
        music_recording_id: The identifier of a MusicRecording which is a recording of the MusicComposition.
    """

    return format_link_mutation("MergeMusicCompositionRecordedAs", music_composition_id, music_recording_id)


def mutation_remove_music_composition_recorded_as(music_composition_id: str, music_recording_id: str):
    """Returns a mutation for removing a MusicRecording as a recording of a MusicComposition.
    (https://schema.org/recordedAs).

    Args:
        music_composition_id: The identifier of a MusicComposition.
        music_recording_id: The identifier of a MusicRecording which is a recording of the MusicComposition.
    """

    return format_link_mutation("RemoveMusicCompositionRecordedAs", music_composition_id, music_recording_id)
