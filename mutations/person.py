# GEnerate GraphQL queries for mutations.


from . import StringConstant, make_parameters, MUTATION
from .templates import mutation_create, mutation_update


CREATE_PERSON = '''
CreatePerson(
{parameters}
) {{
  identifier
  name
}}
'''

UPDATE_PERSON = '''
UpdatePerson(
  {parameters}
) {{
  identifier
  relation
}}
'''


def mutation_create_artist(artist_name: str, publisher: str, contributor: str, creator: str, source: str, description: str, language: str):
    """Returns a mutation for creating a person object
    Arguments:
        str artist_name: The name of the artist
        str publisher: The person, organization or service responsible for making the artist inofrmation available
        str contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        str creator: The person, organization or service who created the thing the web resource is about.
        srt sourcer: The URL of the web resource to be represented by the node.
        str description: An account of the artist. 
        str language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages. 
    """

    return mutation_create(artist_name, publisher, contributor, creator, source, description, language, "artist", CREATE_PERSON)

def mutation_update_artist(identifier:str, artist_name = None, publisher= None, contributor= None, creator= None, source= None, description= None, language= None):
    """Returns a mutation for updating a person object
    Arguments:
        str identifier: The unique identifier of the artist
        str artist_name: The name of the artist, OPTIONAL.
        str publisher: The person, organization or service responsible for making the artist inofrmation available, OPTIONAL.
        str contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL, OPTIONAL.
        str creator: The person, organization or service who created the thing the web resource is about, OPTIONAL.
        srt sourcer: The URL of the web resource to be represented by the node, OPTIONAL.
        str description: An account of the artist, OPTIONAL. 
        str language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr, OPTIONAL


    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages. 
    """

    return mutation_update(identifier, UPDATE_PERSON, artist_name, publisher, contributor, creator, source, description, language)