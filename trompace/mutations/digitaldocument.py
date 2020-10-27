# Generate GraphQL queries for mutations pertaining to digital document objects.
from trompace import StringConstant, docstring_interpolate, filter_none_args
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from .templates import format_mutation
from ..constants import SUPPORTED_LANGUAGES


DIGITALDOCUMENT_ARGS_DOCS = """title: The title of the resource indicated by `source`
        contributor: The main URL of the site where the information about this DigitalDocument was taken from
        creator: The person, organization or service who is creating this DigitalDocument (e.g. URL of the software)
        source: The URL of the web resource where information about this DigitalDocument is taken from
        format_: The mimetype of the resource indicated by `source`
        subject (optional): The subject of the music composition.
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        description (optional): An account of the music composition.
"""


@docstring_interpolate("digitaldocument_args", DIGITALDOCUMENT_ARGS_DOCS)
def mutation_create_digitaldocument(*, title: str, contributor: str, creator: str, source: str, format_: str,
                                    subject: str = None, language: str = None, description: str = None):
    """Returns a mutation for creating a digital document object.

    Arguments:
        {digitaldocument_args}

    Returns:
        The string for the mutation for creating the digital document.

    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
        NotAMimeTypeException: if ``format_`` is not a valid mimetype.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(format_)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "subject": subject,
        "description": description,
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("CreateDigitalDocument", args)


@docstring_interpolate("digitaldocument_args", DIGITALDOCUMENT_ARGS_DOCS)
def mutation_update_digitaldocument(identifier: str, *, title: str = None, contributor: str = None,
                                    creator: str = None, source: str = None, format_: str = None,
                                    subject: str = None, language: str = None, description: str = None):
    """Returns a mutation for updating a digital document object.

    Arguments:
        identifier: The identifier of the media object in the CE to be updated.
        {digitaldocument_args}

    Returns:
        The string for the mutation for creating the artist.

    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "subject": subject,
        "description": description
    }
    if language is not None:
        args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateDigitalDocument", args)


def mutation_delete_digitaldocument(identifier: str):
    """Returns a mutation for deleting a digital document object based on the identifier.

    Arguments:
        identifier: The unique identifier of the digital document object.

    Returns:
        The string for the mutation for deleting the digital document object based on the identifier.
    """

    return format_mutation("DeleteDigitalDocument", {"identifier": identifier})
