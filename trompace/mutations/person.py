# Generate GraphQL queries for mutations pertaining to person objects.
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException
from . import StringConstant
from .templates import mutation_create, mutation_delete
from ..constants import SUPPORTED_LANGUAGES

CREATE_PERSON = '''CreatePerson(
        {parameters}
    ) {{
      identifier
    }}'''

UPDATE_PERSON = '''UpdatePerson(
      {parameters}
    ) {{
      identifier
    }}'''

DELETE_PERSON = '''DeletePerson(
      {parameters}
    ) {{
      identifier
    }}'''


def mutation_create_person(title: str, contributor: str, creator: str, source: str,
                           language: str, format_:str="text/html", name: str=None, description: str=None,
                           image=None, birthDate=None, deathDate=None, familyName=None, givenName=None, gender=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None):
    """Returns a mutation for creating a person object
    Arguments:
        title: The title of the page from which the person information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the person to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        format_: A MimeType of the format of the person, default is "text/html"
        name: The name of the person
        description: An account of the person.
        image (optional): An image associated with the person.
        birthDate (optional): The birth date of the person, currently accepts string, but needs to be chenged to date format.
        deathDate (optional): The date of death of the person, currently accepts string, but needs to be chenged to date format.
        familyName (optional); The family name of the person.
        givenName (optional); The given name of the person.
        gender (optinal): The persons gender.
        honorificPrefix (optional): The person's prefix.
        honorificSuffix (optional): The person's suffix.
        jobTitle (optional): The person's job title.



    Returns:
        The string for the mutation for creating the person.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in formatin:
        raise MimeTypeException(formatin)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "language": StringConstant(language.lower()),
    }
    if description:
        args['description'] = description
    if name:
        args['name'] = name
    if image:
        args["image"] = image
    if birthDate:
        args["birthDate"] = birthDate
    if deathDate:
        args["deathDate"] = deathDate
    if familyName:
        args["familyName"] = familyName
    if gender:
        args["gender"] = gender
    if honorificPrefix:
        args["honorificPrefix"] = honorificPrefix
    if honorificSuffix:
        args["honorificSuffix"] = honorificSuffix
    if jobTitle:
        args["jobTitle"] = jobTitle


    return mutation_create(args, CREATE_PERSON)


def mutation_update_person(identifier: str, title: str=None, contributor: str=None, creator: str=None, source: str=None,
                           language: str=None, name: str=None, description: str=None,
                           image=None, birthDate=None, deathDate=None, familyName=None, givenName=None, gender=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None):
    """Returns a mutation for updating a person object
    Arguments:
        identifier: The identifier of the person in the CE to be updated
        title: The title of the page from which the person information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the person to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        name: The name of the person
        description: An account of the person.
        image: An image associated with the person.
        birthDate: The birth date of the person, currently accepts string, but needs to be chenged to date format.
        deathDate: The date of death of the person, currently accepts string, but needs to be chenged to date format.
        familyName: The family name of the person.
        givenName: The given name of the person.
        gender (optinal): The persons gender.
        honorificPrefix: The person's prefix.
        honorificSuffix: The person's suffix.
        jobTitle: The person's job title.

    Returns:
        The string for the mutation for updating the person.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """
    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in formatin:
        raise MimeTypeException(formatin)

    args = {"identifier": identifier}
    if title:
        args["title"] = title
    if name:
        args["name"] = name
    if contributor:
        args["contributor"] = contributor
    if creator:
        args["creator"] = creator
    if source:
        args["source"] = source
    if language:
        args["language"] = StringConstant(language.lower()),
    if description:
        args['description'] = description
    if name:
        args['name'] = name
    if image:
        args["image"] = image
    if birthDate:
        args["birthDate"] = birthDate
    if deathDate:
        args["deathDate"] = deathDate
    if familyName:
        args["familyName"] = familyName
    if gender:
        args["gender"] = gender
    if honorificPrefix:
        args["honorificPrefix"] = honorificPrefix
    if honorificSuffix:
        args["honorificSuffix"] = honorificSuffix
    if jobTitle:
        args["jobTitle"] = jobTitle

    return mutation_create(args, UPDATE_PERSON)


def mutation_delete_person(identifier: str):
    """Returns a mutation for deleting a person object based on the identifier.
    Arguments:
        identifier: The unique identifier of the person.
    Returns:
        The string for the mutation for deleting the person based on the identifier.
    """

    return mutation_delete(identifier, DELETE_PERSON)
