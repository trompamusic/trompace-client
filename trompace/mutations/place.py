from trompace import StringConstant, check_required_args, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import NotAMimeTypeException, UnsupportedLanguageException
from trompace.mutations.templates import format_mutation, format_link_mutation

PLACE_ARGS_DOCS = """name: The name of the place object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the place to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the place.
        source: The URL of the web resource about this place.
        title: The title of the resource indicated by `source`"""


@docstring_interpolate("place_args", PLACE_ARGS_DOCS)
def mutation_create_place(*, title: str, contributor: str, creator: str, source: str, format_: str,
                          name: str = None, language: str = None):
    """Returns a mutation for creating a place object.

    Arguments:
        {place_args}

    Returns:
        The string for the mutation for creating the place.
    """
    check_required_args(title=title, contributor=contributor, creator=creator, source=source, format_=format_)
    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreatePlace", args)


@docstring_interpolate("place_args", PLACE_ARGS_DOCS)
def mutation_update_place(identifier: str, *, name: str = None, title: str = None,
                          creator: str = None, contributor: str = None,
                          format_: str = None, source: str = None, language: str = None):
    """Returns a mutation for updating a place object.

    Arguments:
        identifier: The identifier of the place in the CE to be updated.
        {place_args}

    Returns:
        The string for the mutation for updating the place.

    """
    if format_ is not None and "/" not in format_:
        raise NotAMimeTypeException(format_)

    if language is not None and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {
        "identifier": identifier,
        "name": name,
        "title": title,
        "creator": creator,
        "contributor": contributor,
        "format": format_,
        "source": source,
    }
    if language:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdatePlace", args)


def mutation_delete_place(identifier: str):
    """Returns a mutation for deleting a place object based on the identifier.

    Arguments:
        identifier: The unique identifier of the place object.

    Returns:
        The string for the mutation for deleting the place object based on the identifier.
    """

    return format_mutation("DeletePlace", {"identifier": identifier})


def mutation_merge_person_birthplace(person_identifier: str, place_identifier: str):
    """Returns a mutation for adding a place as the place of birth of a person.

    Arguments:
        person_identifier: The unique identifier of the person object.
        place_identifier: The unique identifier of the place where the person was born.

    Returns:
        The string for the mutation for merging a place as the birth place of a person.
    """

    return format_link_mutation("MergePersonBirthPlace", person_identifier, place_identifier)


def mutation_remove_person_birthplace(person_identifier: str, place_identifier: str):
    """Returns a mutation for removing a place as the place of birth of a person.

    Arguments:
        person_identifier: The unique identifier of the person object.
        place_identifier: The unique identifier of the place where the person was born.

    Returns:
        The string for the mutation for removing a place as the birth place of a person.
    """

    return format_link_mutation("RemovePersonBirthPlace", person_identifier, place_identifier)


def mutation_merge_person_deathplace(person_identifier: str, place_identifier: str):
    """Returns a mutation for adding a place as the place of death of a person.

    Arguments:
        person_identifier: The unique identifier of the person.
        place_identifier: The unique identifier of the place where the person died.

    Returns:
        The string for the mutation for merging a place as the place of death of a person.
    """

    return format_link_mutation("MergePersonDeathPlace", person_identifier, place_identifier)


def mutation_remove_person_deathplace(person_identifier: str, place_identifier: str):
    """Returns a mutation for removing a place as the place of death of a person.

    Arguments:
        person_identifier: The unique identifier of the person.
        place_identifier: The unique identifier of the place where the person died.

    Returns:
        The string for the mutation for removing a place as the place of death of a person.
    """

    return format_link_mutation("RemovePersonDeathPlace", person_identifier, place_identifier)
