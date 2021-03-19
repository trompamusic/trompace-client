from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation
from trompace import StringConstant, _Neo4jDate, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES


MUSICGROUP_ARGS_DOCS = """title: The title of the resource indicated by `source`
        contributor: The main URL of the site where the information about this MusicGroup was taken from
        creator: The MusicGroup, organization or service who is creating this MusicGroup (e.g. URL of the software)
        source: The URL of the web resource where information about this MusicGroup is taken from
        format_: The mimetype of the resource indicated by `source`
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        name (optional): The name of the MusicGroup
        founding_date (optional): The date that this organization was founded, formatted as yyyy, yyyy-mm or yyyy-mm-dd
        disolution_date (optional): The date that this organization was dissolved, formatted as yyyy, yyyy-mm or yyyy-mm-dd
        description (optional): A description of the MusicGroup
        image (optional): URL to an image associated with the MusicGroup
        publisher (optional): An entity responsible for making the resource available"""


@docstring_interpolate("musicgroup_args", MUSICGROUP_ARGS_DOCS)
def mutation_create_musicgroup(*, title: str, contributor: str, creator: str, source: str, format_: str,
                               language: str = None, name: str = None,
                               founding_date: str = None, disolution_date: str = None,
                               description: str = None, image: str = None, publisher: str = None):
    """Returns a mutation for creating a MusicGroup

    Args:
        {musicgroup_args}
    Returns:
        The string for the mutation for creating the musicgroup.
    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        NotAMimeTypeException: if ``format_`` is not a valid mimetype.
    """

    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)
    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "description": description,
        "image": image,
        "publisher": publisher,
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())
    if founding_date is not None:
        args["foundingDate"] = _Neo4jDate(founding_date)
    if disolution_date is not None:
        args["disolutionDate"] = _Neo4jDate(disolution_date)

    args = filter_none_args(args)

    return format_mutation("CreateMusicGroup", args)


@docstring_interpolate("musicgroup_args", MUSICGROUP_ARGS_DOCS)
def mutation_update_musicgroup(identifier: str, *, title: str = None, contributor: str = None, creator: str = None,
                               source: str = None, format_: str = None, language: str = None, name: str = None,
                               founding_date: str = None, disolution_date: str = None,
                               description: str = None, image: str = None, publisher: str = None):
    """Returns a mutation for updating a MusicGroup

    Args:
        identifier: The identifier of the musicgroup in the CE to be updated
        {musicgroup_args}
    Returns:
        The string for the mutation for updating the musicgroup.
    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        ValueError: if ``gender`` is not a value supported by the Ce
        NotAMimeTypeException: if ``format_`` is not a valid mimetype.
    """

    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if format_ and "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "description": description,
        "image": image,
        "publisher": publisher,
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())
    if founding_date is not None:
        args["foundingDate"] = _Neo4jDate(founding_date)
    if disolution_date is not None:
        args["disolutionDate"] = _Neo4jDate(disolution_date)

    args = filter_none_args(args)

    return format_mutation("UpdateMusicGroup", args)


def mutation_delete_musicgroup(identifier: str):
    """Returns a mutation for deleting a MusicGroup with the given identifier.

    Args:
        identifier: The identifier of the MusicGroup to delete.
    Returns:
        A mutation string to delete a MusicGroup
    """

    return format_mutation("DeleteMusicGroup", {"identifier": identifier})


def mutation_musicgroup_add_exact_match_musicgroup(identifier_from: str, identifier_to: str):
    """Returns a mutation for linking two MusicGroup objects with skos:exactMatch.

    Args:
        identifier_from: the identifer of the MusicGroup to match to
        identifier_to: the identifier of the MusicGroup that is an exact match of identifier_from
    Returns: a mutation to make an exactMatch relationship between the MusicGroup objects
    """
    return format_link_mutation("MergeMusicGroupExactMatch", identifier_from, identifier_to)


def mutation_musicgroup_remove_exact_match_musicgroup(identifier_from: str, identifier_to: str):
    """Returns a mutation for removing the skos:exactMatch relation between two MusicGroup objects

    Args:
        identifier_from: the identifer of the MusicGroup to match to
        identifier_to: the identifier of the MusicGroup that is an exact match of identifier_from
    Returns: a mutation to remove the exactMatch relationship from the MusicGroup objects
    """
    return format_link_mutation("RemoveMusicGroupExactMatch", identifier_from, identifier_to)


def mutation_add_musicgroup_member(identifier_from: str, identifier_to: str):
    """Returns a mutation for linking a Person object with an MusicGroup object.

    Args:
        identifier_from: the identifer of the Person to match to
        identifier_to: the identifier of the MusicGroup to which Person belong
    Returns: a mutation for linking a Person object with an MusicGroup object
    """
    return format_link_mutation("MergeMusicGroupMember", identifier_from, identifier_to)
