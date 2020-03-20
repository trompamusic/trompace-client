# Generate GraphQL queries for queries pertaining to persons objects.
from trompace.exceptions import UnsupportedLanguageException
from trompace import QUERY
from .templates import query_create
from ..constants import SUPPORTED_LANGUAGES

QUERY_PERSON = '''Person(
  {parameters}
  )
  {{
    identifier
    name
    publisher
    contributor
    creator
    source
    description
    language
  }}'''

QUERY_PERSON_ALL = '''Person
  {
    identifier
    name
    publisher
    contributor
    creator
    source
    description
    language
  }'''


def query_person(identifier: str=None, title: str=None, contributor: str=None, creator: str=None, source: str=None,
                           language: str=None, format_:str=None, name: str=None, description: str=None,
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
        image: An image associated with the person.
        birthDate : The birth date of the person, currently accepts string, but needs to be chenged to date format.
        deathDate : The date of death of the person, currently accepts string, but needs to be chenged to date format.
        familyName ; The family name of the person.
        givenName ; The given name of the person.
        gender : The persons gender.
        honorificPrefix : The person's prefix.
        honorificSuffix : The person's suffix.
        jobTitle: The person's job title.


    Returns:
        The string for the mutation for creating the document object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)
    args ={}

    if identifier:
      args["identifier"] = identifier

    if title:
      args["title"] = title
    if contributor:
      args["contributor"] = contributor
    if creator:
      args["creator"] = creator
    if source:
      args["source"] = source
    if language:
      args["language"] = language
    if format_:
      args["format"] = format_
    if name:
      args["name"] = name
    if description:
      args["description"] = description
    if image:
      args["image"] = image
    if birthDate:
      args["birthDate"] = birthDate
    if deathDate:
      args["deathDate"] = deathDate
    if familyName:
      args["familyName"] = familyName
    if givenName:
      args["givenName"] = givenName
    if gender:
      args["gender"] = gender
    if honorificPrefix:
      args["honorificPrefix"] = honorificPrefix
    if honorificSuffix:
      args["honorificSuffix"] = honorificSuffix
    if jobTitle:
      args["jobTitle"] = jobTitle

    if len(args) == 0:
        return QUERY.format(query=QUERY_PERSON_ALL)
    else:
        return query_create(args, QUERY_PERSON)
