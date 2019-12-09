# Generate GraphQL queries for mutations pertaining to musical compositions and works related objects.
from .exceptions import UnsupportedLanguageException
from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant
from ..constants import SUPPORTED_LANGUAGES

CREATE_MUSIC_COMPOSITION = '''CreateMusicComposition(
        {parameters}
    ) {{
      identifier
  }}'''

UPDATE_MUSIC_COMPOSITION = '''UpdateMusicComposition(
        {parameters}
    ) {{
      identifier
  }}'''

DELETE_MUSIC_COMPOSITION = '''DeleteMusicComposition(
    {parameters}
    ) {{
      identifier
  }}'''

ADD_COMPOSITION_AUTHOR = '''AddCreativeWorkInterfaceLegalPerson(
  from: {{identifier: "{identifier_1}" type:MusicComposition}}
  to: {{identifier: "{identifier_2}" type: Person}}
  field: author 
  )
  {{
      from {{
          ... on CreativeWork {{
              identifier
      }}
    }}
    to {{
          ... on Person {{
              identifier
      }}
    }}
  }}'''

REMOVE_COMPOSITION_AUTHOR = '''RemoveCreativeWorkInterfaceLegalPerson(
  from: {{identifier: "{identifier_1}" type:MusicComposition}}
  to: {{identifier: "{identifier_2}" type: Person}}
  field: author 
  )
  {{
      from {{
          ... on CreativeWork {{
              identifier
      }}
    }}
    to {{
          ... on Person {{
              identifier
      }}
    }}
  }}'''


def mutation_create_composition(composition_name: str, publisher: str, contributor: str, creator: str, source: str,
                                description: str, subject: str, language: str, formatin="text/html"):
    """Returns a mutation for creating a digital document object
    Arguments:
        comosition_name: The name of the comnposition.
        publisher: The person, organization or service responsible for making the artist inofrmation available.
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the artist.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr.


    Returns:
        The string for the mutation for creating the artist.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    assert "/" in formatin, "Please provide a valid mimetype for format"

    args = {
        "title": composition_name,
        "name": composition_name,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": formatin,
        "language": StringConstant(language.lower()),
    }
    return mutation_create(args, CREATE_MUSIC_COMPOSITION)


def mutation_update_composition(identifier: str, composition_name=None, publisher=None, contributor=None, creator=None,
                                source=None, description=None, language=None):
    """Returns a mutation for updating a person object
    Arguments:
        identifier: The unique identifier of the composition.
        composition_name (optional): The name of the composition.
        publisher (optional): The person, organization or service responsible for making the artist inofrmation available.
        contributor (optional): A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator (optional): The person, organization or service who created the composition that the web resource is about.
        sourcer (optional): The URL of the web resource to be represented by the node.
        description (optional): An account of the artist.
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr.
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    return mutation_update(identifier, UPDATE_MUSIC_COMPOSITION, composition_name, publisher, contributor, creator,
                           source, description, language)


def mutation_delete_composition(identifier: str):
    """Returns a mutation for deleting a person object based on the identifier.
    Arguments:
        identifier: The unique identifier of the artist.
    Returns:
        The string for the mutation for deleting the artist based on the identifier.
    """

    return mutation_delete(identifier, DELETE_MUSIC_COMPOSITION)


def mutation_add_composition_author(composition_id: str, composer_id: str):
    """Returns a mutation for adding an artist object as the composer of a composition.
    Arguments:
        composition_id: The unique identifier of the composition object.
        composer_id: The unique identifier of the artist object for the composer of the composition.
    Returns:
        The string for the mutation for adding the artist object as the composer of the composition.
    """

    return mutation_link(composition_id, composer_id, ADD_COMPOSITION_AUTHOR)


def mutation_remove_composition_author(composition_id: str, composer_id: str):
    """Returns a mutation for removing an artist object as the composer of a composition.
    Arguments:
        composition_id: The unique identifier of the composition object.
        composer_id: The unique identifier of the artist object for the composer of the composition.
    Returns:
        The string for the mutation for removing the artist object as the composer of the composition.
    """

    return mutation_link(composition_id, composer_id, REMOVE_COMPOSITION_AUTHOR)
