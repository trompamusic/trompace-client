# Generate GraphQL queries for mutations pertaining to entry points.

from .templates import mutation_create, mutation_update, mutation_delete
from . import StringConstant

CREATE_ENTRYPOINT = '''CreateEntryPoint(
        {parameters}
        ) {{
          identifier
        }}'''



def mutation_create_entry_point(name: str, contributor: str, subject:str,
                           description: str, creator: str, source:str, language: str, actionPlatform:str, contentType:list, encodingType: list, formatin="html/text", identifier=None):
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
    TODO:
        Assert that content type and encoding type are mimetypes
    """
    assert "/" in formatin, "Please provide a valid mimetype for format"
    assert all("/" in x for x in contentType), "Please provide a valid mimetype for contentType"
    assert all("/" in x for x in encodingType), "Please provide a valid mimetype for encodingType"
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
    return mutation_create(args, CREATE_ENTRYPOINT)


