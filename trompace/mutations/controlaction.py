# Generate GraphQL queries for mutations pertaining to software applications.

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant


CREATE_CONTROLACTION = '''
CreateControlAction(
{parameters}
) {{
  identifier
  description
  actionStatus
}}
'''


ADD_ENTRYPOINT_CONTROLACTION = '''
AddThingInterfacePotentialAction(
  from: {{identifier: "{identifier_1}"}}
  to: {{identifier: "{identifier_2}"}}
)
{{
    from {{
    ... on EntryPoint{{
            identifier
    }}
  }}
  to {{
    ... on ControlAction{{
            identifier
    }}
  }}
}}
'''


def mutation_create_controlaction(name: str, description: str, actionStatus: str, identifier=None, language=None, subject=None):
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
    # assert language.lower() in ["en", "es", "ca", "nl", "de", "fr"], "Language {} not supported".format(language)

    args = {
        "name": name,
        "description": description,
        "actionStatus" : StringConstant(actionStatus.lower())
    }
    return mutation_create(args, CREATE_CONTROLACTION)

def mutation_add_entrypoint_controlaction(entrypoint_id: str, controlaction_id: str):
    """Returns a mutation for adding a digital document as a subject of a composition.
    Arguments:
        document_id: The unique identifier of the digital document object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for adding the document as a subject of the composition.
    """

    return mutation_link(entrypoint_id, controlaction_id, ADD_ENTRYPOINT_CONTROLACTION)

