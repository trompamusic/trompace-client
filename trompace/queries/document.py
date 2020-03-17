# Generate GraphQL queries pertaining to digital document objects.
import json
import os
import asyncio


import trompace.config as config
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException, QueryException
from trompace.queries.templates import query_create
from trompace.constants import SUPPORTED_LANGUAGES
from .. import QUERY

QUERY_DIGITALDOCUMENT = '''DigitalDocument(
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

QUERY_DIGITALDOCUMENT_ALL = '''DigitalDocument
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



def query_document(identifier: str=None, document_name=None, publisher=None, contributor=None, format_=None, creator=None,
                             source=None, description=None, language=None):
    """Returns a query for a digital document object
    Arguments:
        identifier: The unique identifier of the digital document.
        document_name: The name of the digital document.
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
    args = {}

    if identifier:
      args["identifier"] = identifier

    if document_name:
      args["name"] = document_name
    if publisher:
      args["publisher"] = publisher
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
    if description:
      args["description"] = description


    if len(args) == 0:
        return QUERY.format(query=QUERY_DIGITALDOCUMENT_ALL)
    else:
        return query_create(args, QUERY_DIGITALDOCUMENT) 



