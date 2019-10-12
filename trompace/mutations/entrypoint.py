# Generate GraphQL queries for mutations pertaining to software applications.

from .templates import mutation_create, mutation_update, mutation_delete
from . import StringConstant

CREATE_ENTRYPOINT = '''
CreateEntryPoint(
{parameters}
) {{
  identifier
}}
'''



def mutation_create_entry_point(name: str, contributor: str, subject:str,
                           description: str, creator: str, source:str, language: str, actionPlatform:str, contentType:list, encodingType: list, identifier=None):
    """Returns a mutation for creating a software application object
    Arguments:
        artist_name: The name of the artist
        publisher: The person, organization or service responsible for making the artist inofrmation available
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the artist.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """
    args = {
        "title": name,
        "name": name,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": "html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant(language.lower()),
        "actionPlatform": actionPlatform,
        "contentType": contentType, 
        "encodingType": encodingType
    }
    return mutation_create(args, CREATE_ENTRYPOINT)


