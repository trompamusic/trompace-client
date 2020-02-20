# Generate GraphQL queries for mutations pertaining to persons/artists objects.
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException
from . import StringConstant
from .templates import mutation_create, mutation_update, mutation_delete
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


def mutation_create_artist(title: str, contributor: str, creator: str, source: str,
                           language: str, formatin:str="text/html", name: str=None, description: str=None,
                           image=None, sameAs=None, birthDate=None, deathDate=None, familyName=None, givenName=None, gender=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None):
    """Returns a mutation for creating a person object
    Arguments:
        title: The title of the page from which the artist information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        formatin: A MimeType of the format of the artist, default is "text/html"
        name: The name of the artist
        description: An account of the artist.
        image (optional): An image associated with the artist.
        birthDate (optional): The birth date of the artist, currently accepts string, but needs to be chenged to date format.
        deathDate (optional): The date of death of the artist, currently accepts string, but needs to be chenged to date format.
        familyName (optional); The family name of the artist.
        givenName (optional); The given name of the artist.
        gender (optinal): The artists gender.
        honorificPrefix (optional): The artist's prefix.
        honorificSuffix (optional): The artist's suffix.
        jobTitle (optional): The artist's job title.



    Returns:
        The string for the mutation for creating the artist.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in formatin:
        raise MimeTypeException(formatin)

    args = {
        "title": title,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": formatin,
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


def mutation_update_artist(identifier: str, title: str, contributor: str, creator: str, source: str,
                           language: str, formatin:str="text/html", name: str=None, description: str=None,
                           image=None, sameAs=None, birthDate=None, deathDate=None, familyName=None, givenName=None, gender=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None):
    """Returns a mutation for updating a person object
    Arguments:
        title: The title of the page from which the artist information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        formatin: A MimeType of the format of the artist, default is "text/html"
        name: The name of the artist
        description: An account of the artist.
        image (optional): An image associated with the artist.
        birthDate (optional): The birth date of the artist, currently accepts string, but needs to be chenged to date format.
        deathDate (optional): The date of death of the artist, currently accepts string, but needs to be chenged to date format.
        familyName (optional); The family name of the artist.
        givenName (optional); The given name of the artist.
        gender (optinal): The artists gender.
        honorificPrefix (optional): The artist's prefix.
        honorificSuffix (optional): The artist's suffix.
        jobTitle (optional): The artist's job title.

    Returns:
        The string for the mutation for updating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    return mutation_update(identifier, UPDATE_PERSON, artist_name, publisher, contributor, creator, source, description,
                           language)


def mutation_delete_artist(identifier: str):
    """Returns a mutation for deleting a person object based on the identifier.
    Arguments:
        identifier: The unique identifier of the artist.
    Returns:
        The string for the mutation for deleting the artist based on the identifier.
    """

    return mutation_delete(identifier, DELETE_PERSON)
