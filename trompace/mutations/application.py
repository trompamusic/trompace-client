# Generate GraphQL queries for mutations pertaining to software applications.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace import StringConstant, filter_none_args
from .templates import mutation_create, mutation_link
from ..constants import SUPPORTED_LANGUAGES

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


def mutation_create_application(*, name: str, contributor: str, creator: str, source: str, title: str = None,
                                subject: str = None, language: str = None, description: str = None, format_: str = None,
                                softwareversion: str = None):
    """Returns a mutation for creating a software application object
    Arguments:
        name: The name of the software application.
        title: the html title of the page at `source`
        contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
        creator: The person, organization or service responsible for adding the software application.
        source: The URL of the web resource to be represented by the node.
        subject: The subject associated with the application.
        description: An account of the software application.
        language: The language of the page at `source`. Currently supported languages are en,es,ca,nl,de,fr
        softwareversion: the version of the software
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
        NotAMimeTypeException if format_ is not a valid mimetype.
    """

    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)
    if format_ and "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "name": name,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "title": title,
        "subject": subject,
        "description": description,
        "format": format_,
        "softwareVersion": softwareversion
    }
    if language:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)
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
