# Generate GraphQL queries for mutations pertaining to person objects.

from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate
from trompace.constants import SUPPORTED_LANGUAGES, SUPPORTED_GENDER

PERSON_ARGS_DOCS = """title: The title of the resource indicated by `source`
        contributor: The main URL of the site where the information about this Person was taken from
        creator: The person, organization or service who is creating this Person (e.g. URL of the software)
        source: The URL of the web resource where information about this Person is taken from
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        format_: The mimetype of the resource indicated by `source`
        name: The name of the person
        family_name (optional): The family name of the person
        given_name (optional): The given name of the person
        gender (optional): The person's gender
        birth_date (optional): The birth date of the person, formatted as yyyy, yyyy-mm or yyyy-mm-dd
        death_date (optional): The date of death of the person , formatted as yyyy, yyyy-mm or yyyy-mm-dd
        description (optional): A biographical description of the person
        image (optional): URL to an image associated with the person
        publisher (optional): An entity responsible for making the resource available
        honorific_prefix (optional): An honorific prefix.
        honorific_suffix (optional): An honorific suffix.
        job_title (optional): The person's job title."""


@docstring_interpolate("person_args", PERSON_ARGS_DOCS)
def mutation_create_person(*, title: str, contributor: str, creator: str, source: str, format_: str,
                           language: str = None, name: str = None,
                           family_name: str = None, given_name: str = None, gender: str = None,
                           birth_date: str = None, death_date: str = None,
                           description: str = None, image: str = None, publisher: str = None,
                           honorific_prefix: str = None, honorific_suffix: str = None, job_title: str = None):
    """Returns a mutation for creating a Person

    Args:
        {person_args}
    Returns:
        The string for the mutation for creating the person.
    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        ValueError: if ``gender`` is not a value supported by the CE
        NotAMimeTypeException: if ``format_`` is not a valid mimetype.
    """

    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if gender and gender.lower() not in SUPPORTED_GENDER:
        raise ValueError(f"unexpected value for gender: {gender}")

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "familyName": family_name,
        "givenName": given_name,
        "description": description,
        "image": image,
        "publisher": publisher,
        "honorificPrefix": honorific_prefix,
        "honorificSuffix": honorific_suffix,
        "jobTitle": job_title
    }
    if gender is not None:
        args["gender"] = StringConstant(gender.lower())
    if language is not None:
        args["language"] = StringConstant(language.lower())
    if birth_date is not None:
        args["birthDate"] = _Neo4jDate(birth_date)
    if death_date is not None:
        args["deathDate"] = _Neo4jDate(death_date)

    args = filter_none_args(args)

    return format_mutation("CreatePerson", args)


@docstring_interpolate("person_args", PERSON_ARGS_DOCS)
def mutation_update_person(identifier: str, *, title: str = None, contributor: str = None, creator: str = None,
                           source: str = None, language: str = None, format_: str = None, name: str = None,
                           family_name: str = None, given_name: str = None, gender: str = None,
                           birth_date: str = None, death_date: str = None,
                           description: str = None, image: str = None, publisher: str = None,
                           honorific_prefix: str = None, honorific_suffix: str = None, job_title: str = None):
    """Returns a mutation for updating a Person

    Args:
        identifier: The identifier of the person in the CE to be updated
        {person_args}
    Returns:
        The string for the mutation for updating the person.
    Raises:
        UnsupportedLanguageException: if ``language`` is not one of the supported languages.
        ValueError: if ``gender`` is not a value supported by the Ce
        NotAMimeTypeException: if ``format_`` is not a valid mimetype.
    """

    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if gender and gender.lower() not in SUPPORTED_GENDER:
        raise ValueError(f"unexpected value for gender: {gender}")

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
        "familyName": family_name,
        "givenName": given_name,
        "description": description,
        "image": image,
        "publisher": publisher,
        "honorificPrefix": honorific_prefix,
        "honorificSuffix": honorific_suffix,
        "jobTitle": job_title
    }
    if gender is not None:
        args["gender"] = StringConstant(gender.lower())
    if language is not None:
        args["language"] = StringConstant(language.lower())
    if birth_date is not None:
        args["birthDate"] = _Neo4jDate(birth_date)
    if death_date is not None:
        args["deathDate"] = _Neo4jDate(death_date)

    args = filter_none_args(args)

    return format_mutation("UpdatePerson", args)


def mutation_delete_person(identifier: str):
    """Returns a mutation for deleting a Person with the given identifier.

    Args:
        identifier: The identifier of the Person to delete.
    Returns:
        A mutation string to delete a Person
    """

    return format_mutation("DeletePerson", {"identifier": identifier})


def mutation_person_add_exact_match_person(identifier_from: str, identifier_to: str):
    """Returns a mutation for linking two Person objects with skos:exactMatch.

    Args:
        identifier_from: the identifer of the Person to match to
        identifier_to: the identifier of the Person that is an exact match of identifier_from
    Returns: a mutation to make an exactMatch relationship between the Person objects
    """
    return format_link_mutation("MergePersonExactMatch", identifier_from, identifier_to)


def mutation_person_remove_exact_match_person(identifier_from: str, identifier_to: str):
    """Returns a mutation for removing the skos:exactMatch relation between two Person objects

    Args:
        identifier_from: the identifer of the Person to match to
        identifier_to: the identifier of the Person that is an exact match of identifier_from
    Returns: a mutation to remove the exactMatch relationship from the Person objects
    """
    return format_link_mutation("RemovePersonExactMatch", identifier_from, identifier_to)
