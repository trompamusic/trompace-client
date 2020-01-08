# Generate GraphQL queries for mutations pertaining to entry points.
from typing import List
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException
from .templates import mutation_create, mutation_update, mutation_delete
from . import StringConstant
from ..constants import SUPPORTED_LANGUAGES

CREATE_ENTRYPOINT = '''CreateEntryPoint(
        {parameters}
        ) {{
          identifier
        }}'''


def mutation_create_entry_point(name: str, contributor: str, subject: str,
                                description: str, creator: str, source: str, language: str, actionPlatform: str,
                                contentType: List, encodingType: list, formatin="text/html", identifier=None):
    """Returns a mutation for creating an entry point object
    Arguments:
        name: The name of the entry point.
        contributor: A person, an organization, or a service responsible for contributing the aentry point to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the entry point is about.
        source: The URL of the web resource to be represented by the node.
        description: An account of the entry point..
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr.
        actionPlatform: The action platform.
        contentType: The content type associated with the entry point, should be a mimetype.
        encodingType: The encoding type associated with the entry point, should be a mimetype.
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)
    if "/" not in formatin:
        raise MimeTypeException(formatin)
    if not all("/" in x for x in contentType):
        missing_list = [x for x in contentType if "/" not in x]
        raise MimeTypeException(missing_list)
    if not all("/" in x for x in encodingType):
        missing_list = [x for x in encodingType if "/" not in x]
        raise MimeTypeException(missing_list)

    args = {
        "title": name,
        "name": name,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": formatin,
        "language": StringConstant(language.lower()),
        "actionPlatform": actionPlatform,
        "contentType": contentType,
        "encodingType": encodingType
    }
    if identifier:
        args["identifier"] = identifier
    return mutation_create(args, CREATE_ENTRYPOINT)
