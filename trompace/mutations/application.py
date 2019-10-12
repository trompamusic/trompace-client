# Generate GraphQL queries for mutations pertaining to software applications.

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant

CREATE_APPLICATION = '''
CreateSoftwareApplication(
{parameters}
) {{
  identifier
}}
'''


ADD_ENTRYPOINT_APPLICATION = '''
AddEntryPointEntryActionApplication(
  from: {{identifier: "{identifier_1}"}}
  to: {{identifier: "{identifier_2}"}}
)
{{
    from {{
            identifier
            name
  }}
  to {{
            identifier
            name

  }}
}}
'''



def mutation_create_application(application_name: str, contributor: str, creator: str, source: str, subject:str,
                           description: str, language: str, identifier=None):
    """Returns a mutation for creating a software application object
    Arguments:
        application_name: The name of the software application.
        contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
        creator: The person, organization or service responsible for adding the software application.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the software application.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """
    assert language.lower() in ["en", "es", "ca", "nl", "de", "fr"], "Language {} not supported".format(language)

    args = {
        "title": application_name,
        "name": application_name,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": "html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant(language.lower()),
    }
    return mutation_create(args, CREATE_APPLICATION)



def mutation_add_entrypoint_application(application_id: str, entrypoint_id: str):
    """Returns a mutation for adding an entry point to an application..
    Arguments:
        application_id: The unique identifier of the application object.
        entrypoint_id: The unique identifier of the entrypoint.
    Returns:
        The string for the mutation for creating a relation between an application and an entry point.
    """

    return mutation_link(application_id, entrypoint_id, ADD_ENTRYPOINT_APPLICATION)


