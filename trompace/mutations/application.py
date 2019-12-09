# Generate GraphQL queries for mutations pertaining to software applications.

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant

CREATE_APPLICATION = '''CreateSoftwareApplication(
        {parameters}
        ) {{
          identifier
        }}'''


ADD_ENTRYPOINT_APPLICATION = '''AddEntryPointActionApplication(
        from: {{identifier: "{identifier_1}"}}
        to: {{identifier: "{identifier_2}"}}
        ){{
        from {{
                identifier
        }}
        to {{
                identifier
        }}
    }}'''



def mutation_create_application(application_name: str, contributor: str, creator: str, source: str, subject:str,
                           description: str, language: str, formatin = "html", identifier=None):
    """Returns a mutation for creating a software application object
    Arguments:
        application_name: The name of the software application.
        contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
        creator: The person, organization or service responsible for adding the software application.
        source: The URL of the web resource to be represented by the node.
        subject: The subject associated with the application.
        description: An account of the software application.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """
    assert language.lower() in ["en", "es", "ca", "nl", "de", "fr"], "Language {} not supported".format(language)
    # assert "/" in formatin, "Please provide a valid mimetype for format"

    args = {
        "title": application_name,
        "name": application_name,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": formatin,
        "language": StringConstant(language.lower()),
    }
    if identifier:
        args["identifier"] = identifier
    return mutation_create(args, CREATE_APPLICATION)


def mutation_add_entrypoint_application(application_id: str, entrypoint_id: str):
    """Returns a mutation for adding an entry point to an application..
    Arguments:
        application_id: The unique identifier of the application object.
        entrypoint_id: The unique identifier of the entrypoint.
    Returns:
        The string for the mutation for creating a relation between an application and an entry point.
    """

    return mutation_link(entrypoint_id, application_id, ADD_ENTRYPOINT_APPLICATION)


