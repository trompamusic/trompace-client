# Generate GraphQL queries for mutations pertaining to media object objects.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation, format_link_mutation
from trompace import StringConstant, _Neo4jDate, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES


def mutation_create_media_object(name: str, description: str, date: str, creator: str, contributor: str, format_: str, encodingFormat: str, source: str, subject: str, \
    conrtentUrl:str, language: str, title:str=None):

    """Returns a mutation for creating a media object object
    Arguments:
        name: The name of the media object.  
        description: An account of the media object.
        date: The date associated with the media object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the media object to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the media object.
        encodingFormat: A MimeType of the format of object encoded by the media object.
        source: The URL of the web resource to be represented by the node.
        subject: The subject of the media object.
        contentUrl: The URL of the content encoded by the media object. 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the media object. Currently supported languages are en,es,ca,nl,de,fr
        title: The title of the page from which the media object information was extracted.  
    Returns:
        The string for the mutation for creating the media object.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in format_:
        raise NotAMimeTypeException(formatin)

    if "/" not in encodingFormat:
        raise NotAMimeTypeException(encodingFormat)

    args = {
        "title": title,
        "description": description,
        "date": _Neo4jDate(date),
        "creator": creator,
        "contributor": contributor,
        "format": format_,
        "encodingFormat": encodingFormat,
        "source": source,
        "subject": subject,
        "contentUrl": contentUrl
        "language": StringConstant(language.lower()),
    }
    if title:
        args["title"] = title


    args = filter_none_args(args)

    return format_mutation("CreateMediaObject", args)


def mutation_update_media_object(identifier: str, name: str=None, title:str=None, description: str=None, date: str=None, creator: str=None, contributor: str=None,\
    format_: str=None, encodingFormat: str=None, source: str=None, subject: str=None, conrtentUrl:str=None, language: str=None):
    """Returns a mutation for updating a media object object.
    Arguments:
        name: The name of the media object.  
        description: An account of the media object.
        date: The date associated with the media object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the media object to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the media object.
        encodingFormat: A MimeType of the format of object encoded by the media object.
        source: The URL of the web resource to be represented by the node.
        subject: The subject of the media object.
        contentUrl: The URL of the content encoded by the media object. 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the media object. Currently supported languages are en,es,ca,nl,de,fr
        title: The title of the page from which the media object information was extracted.  
    Returns:
        The string for the mutation for updating the media object.
    Raises:
        Assertion error if the input language or inLanguage is not one of the supported languages.
    """
        


    args = {"identifier": identifier}
    if name:
        args["name"] = name
    if title:
        args["title"] = title
    if description:
        args["description"] = description
    if date:
        args["date"] = _Neo4jDate(date)
    if creator:
        args["creator"] = creator
    if contributor:
        args["contributor"] = contributor
    if format_:
        if "/" not in format_:
            raise NotAMimeTypeException(formatin)
        else:
            args["format"] = format_
    if encodingFormat:
        if "/" not in encodingFormat:
            raise NotAMimeTypeException(encodingFormat)
        else:
            args["encodingFormat"] = encodingFormat
    if contentUrl:
        args["contentUrl"] = encodingFormat 
    if subject:
        args["subject"] = subject
    if source:
        args["source"] = source
    if language:
        if language not in SUPPORTED_LANGUAGES:
            raise UnsupportedLanguageException(language)
        else:
            args["language"] = StringConstant(language.lower())

    args = filter_none_args(args)

    return format_mutation("UpdateMediaObject", args)



def mutation_delete_media_object(identifier: str):
    """Returns a mutation for deleting a media object object based on the identifier.
    Arguments:
        identifier: The unique identifier of the media object object.
    Returns:
        The string for the mutation for deleting the media object object based on the identifier.
    """

    return format_mutation("DeleteMediaObject", {"identifier": identifier})




def mutation_merge_media_object_work_example(media_object_identifier: str, work_identifier: str):
    """Returns a mutation for creating merging a media object as an example of a work.
    Arguments:
        media_object_identifier: The unique identifier of the media object.
        work_identifier: The unique identifier of the work that the media object is an example of.
    Returns:
        The string for the mutation for merging a media object as an example of the work.
    """

    return format_link_mutation("MergeMediaObjectExampleOfWork", media_object_identifier, work_identifier)


def mutation_reomve_media_object_work_example(media_object_identifier: str, work_identifier: str):
    """Returns a mutation for creating removing a media object as an example of a work.
    Arguments:
        media_object_identifier: The unique identifier of the media object.
        work_identifier: The unique identifier of the work that the media object is an example of.
    Returns:
        The string for the mutation for removing a media object as an example of the work.
    """

    return format_link_mutation("RemoveMediaObjectExampleOfWork", media_object_identifier, work_identifier)


def mutation_merge_media_object_work_example(media_object_identifier_1: str, media_object_identifier_2: str):
    """Returns a mutation for creating merging a media object as an encoding of another media object
    Arguments:
        media_object_identifier_1: The unique identifier of the media object that is encoding the other.
        media_object_identifier_2: The unique identifier of the media object being encoded.
    Returns:
        The string for the mutation for merging a media object as an encoding of another media object. 
    """

    return format_link_mutation("MergeMediaObjectEncoding", media_object_identifier_1, media_object_identifier_2)


def mutation_remove_media_object_work_example(media_object_identifier_1: str, media_object_identifier_2: str):
    """Returns a mutation for creating removing a media object as an encoding of another media object
    Arguments:
        media_object_identifier_1: The unique identifier of the media object that is encoding the other.
        media_object_identifier_2: The unique identifier of the media object being encoded.
    Returns:
        The string for the mutation for removing a media object as an encoding of another media object. 
    """

    return format_link_mutation("RemoveMediaObjectEncoding", media_object_identifier_1, media_object_identifier_2)

