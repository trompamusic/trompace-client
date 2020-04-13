# Generate GraphQL queries for mutations pertaining to music composition objects.
from trompace import StringConstant, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation


def mutation_create_music_composition(title: str, contributor: str, creator: str, subject: str, source: str,
                                      language: str, inLanguage: str, format_: str = "text/html", name: str = None,
                                      description: str = None):
    """Returns a mutation for creating a music composition object
    Arguments:
        title: The title of the page from which the music composition information was extracted.
        contributor: A person, an organization, or a service responsible for contributing the music composition to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        subject: The subject of the music composition.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        format_: A MimeType of the format of the page describing the music composition, default is "text/html"
        name: The name of the music composition.
        description: An account of the music composition.


    Returns:
        The string for the mutation for creating the music composition.
    Raises:
        UnsupportedLanguageException if the input language or inLanguage is not one of the supported languages.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if inLanguage and inLanguage not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(inLanguage)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "format": format_,
        "subject": subject,
        "source": source,
        "language": StringConstant(language.lower()),
        "inLanguage": inLanguage,
        "name": name,
        "description": description
    }

    args = filter_none_args(args)

    return format_mutation("CreateMusicComposition", args)


def mutation_update_music_composition(identifier: str, title: str = None, contributor: str = None, creator: str = None,
                                      subject: str = None, source: str = None,
                                      language: str = None, inLanguage: str = None, format_: str = None,
                                      name: str = None, description: str = None):
    """Returns a mutation for updating a music composition object.
    Arguments:
        title: The title of the page from which the music composition information was extracted.
        contributor: A person, an organization, or a service responsible for contributing the music composition to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        subject: The subject of the music composition.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        format_: A MimeType of the format of the page describing the music composition, default is "text/html"
        name: The name of the music composition.
        description: An account of the music composition.
    Returns:
        The string for the mutation for updating the music composition.
    Raises:
        Assertion error if the input language or inLanguage is not one of the supported languages.
    """

    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if inLanguage and inLanguage not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(inLanguage)

    if format_ and "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {"identifier": identifier,
            "title": title,
            "contributor": contributor,
            "creator": creator,
            "subject": subject,
            "source": source,
            "inLanguage": inLanguage,
            "format": format_,
            "name": name,
            "description": description}

    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMusicComposition", args)


def mutation_delete_music_composition(identifier: str):
    """Returns a mutation for deleting a music composition object based on the identifier.
    Arguments:
        identifier: The unique identifier of the music composition object.
    Returns:
        The string for the mutation for deleting the music composition object based on the identifier.
    """

    return format_mutation("DeleteMusicComposition", {"identifier": identifier})


def mutation_add_broad_match_music_composition(from_identifier: str, to_identifier: str):
    """Returns a mutation for creating a broad match between two music comosition objects.
    Arguments:
        from_identifier: The unique identifier of the digital document object from which to create the broad match.
        to_identifier: The unique identifier of the digital document object to which the broad match should be created.
    Returns:
        The string for the mutation for creating the broad match between the two documents.
    """

    return format_link_mutation("AddMusicCompositionBroadMatch", from_identifier, to_identifier)


def mutation_remove_broad_match_music_composition(from_identifier: str, to_identifier: str):
    """Returns a mutation for removing a broad match between two music composition objects.
    Arguments:
        from_identifier: The unique identifier of the music composition object from which to remove the broad match.
        to_identifier: The unique identifier of the digital document object to which the broad match should be removed.
    Returns:
        The string for the mutation for removing the broad match between the music compositions.
    """

    return format_link_mutation("RemoveMusicCompositionBroadMatch", from_identifier, to_identifier)


def mutation_merge_music_composition_work_example_composition(music_composition_id: str, composition_id: str):
    """Returns a mutation for merging a music composition as an example of a composition.
    Merging means that the connection will be added only if it does not exist.

    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for merging the music composition as an example of the composition.
    """

    return format_link_mutation("MergeMusicCompositionExampleOfWork", music_composition_id, composition_id)


def mutation_remove_music_composition_work_example_composition(music_composition_id: str, composition_id: str):
    """Returns a mutation for removing a music composition as an example of a composition.
    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for removing the music composition as an example of the composition.
    """

    return format_link_mutation("RemoveMusicCompositionExampleOfWork", music_composition_id, composition_id)
