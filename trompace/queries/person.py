# Generate GraphQL queries for mutations pertaining to persons/artists objects.
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException
from . import StringConstant
from .templates import query_create
from ..constants import SUPPORTED_LANGUAGES

QUERY_PERSON = '''query {{
  Person(
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
  }}
}}'''

QUERY_PERSON_ALL = '''query {
  Person
  {
    identifier
    name
    publisher
    contributor
    creator
    source
    description
    language
  }
}'''


def query_artist(identifier: str=None, artist_name=None, publisher=None, contributor=None, creator=None, subject=None,
                             source=None, description=None, language=None):
    """Returns a query for a personobject
    Arguments:
        identifier: The unique identifier of the person.
        document_name: The name of the person.
        publisher: The person, organization or service responsible for making the artist information available.
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource.
            This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        source: The URL of the web resource to be represented by the node.
        description: An account of the artist.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


    Returns:
        The string for the mutation for creating the document object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if all(v is None for v in locals().values()):
        return QUERY_PERSON_ALL
    else:
        return query_create(identifier, QUERY_PERSON, artist_name, publisher, contributor, creator, subject,
                                 source, description, language)

        
