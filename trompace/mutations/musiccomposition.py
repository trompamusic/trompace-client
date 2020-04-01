# Generate GraphQL queries for mutations pertaining to music composition objects.
from trompace.exceptions import UnsupportedLanguageException, NotAMimeTypeException
from trompace.mutations.templates import format_mutation
from trompace import StringConstant, _Neo4jDate, filter_none_args
from trompace.constants import SUPPORTED_LANGUAGES

ADD_MUSIC_COMPOSITION_BROAD_MATCH = '''AddMusicCompositionBroadMatch(
    from: {{identifier: "{identifier_1}" }}
    to: {{identifier: "{identifier_2}" }}
  ) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
  }}'''

REMOVE_MUSIC_COMPOSITION_BROAD_MATCH = '''RemoveMusicCompositionBroadMatch(
    from: {{identifier: "{identifier_1}" }}
    to: {{identifier: "{identifier_2}" }}
  ) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
  }}'''

ADD_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION = '''AddDMusicCompositionExampleOfWork(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
}}'''

MERGE_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION = '''MergeMusicCompositionExampleOfWork(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
}}'''

REMOVE_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION = '''RemoveMusicCompositionExampleOfWork(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
}}'''



ADD_MUSIC_COMPOSITION_TO_CONTROL_ACTION_MUTATION = """AddActionInterfaceThingInterface (
            from: {{identifier: "{identifier_2}", type: ControlAction}}
            to: {{identifier: "{identifier_1}", type: MusicComposition}}
            field: result
        ) {{
            from {{
                __typename
            }}
            to {{
                __typename
            }}
        }}"""


def mutation_create_music_composition(title: str, contributor: str, creator: str, source: str,
                           language: str, inLanguage:str, formatin:str="text/html", name: str=None, description: str=None):
    """Returns a mutation for creating a music composition object
    Arguments:
        title: The title of the page from which the music composition information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the music composition to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        formatin: A MimeType of the format of the page describing the music composition, default is "text/html"
        name: The name of the music composition.
        description: An account of the music composition.


    Returns:
        The string for the mutation for creating the music composition.
    Raises:
        UnsupportedLanguageException if the input language or inLanguage is not one of the supported languages.
    """
    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if inLanguage not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(inLanguage)

    if "/" not in formatin:
        raise NotAMimeTypeException(formatin)

    args = {
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "format": formatin,
        "language": StringConstant(language.lower()),
        "inLanguage": StringConstant(inLanguage.lower()),
    }
    if name:
        args["name"] = name
    if description:
        args["description"] = description

    args = filter_none_args(args)

    return format_mutation("CreateMusicComposition", args)


def mutation_update_music_composition(identifier: str, title: str=None, contributor: str=None, creator: str=None, source: str=None,
                           language: str=None, inLanguage:str=None, format_:str=None, name: str=None, description: str=None):
    """Returns a mutation for updating a music composition object.
    Arguments:
        title: The title of the page from which the music composition information was extracted.      
        contributor: A person, an organization, or a service responsible for contributing the music composition to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        source: The URL of the web resource to be represented by the node.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        inLanguage: The language of the music composition. Currently supported languages are en,es,ca,nl,de,fr
        format_: A MimeType of the format of the page describing the music composition, default is "text/html"
        name: The name of the music composition.
        description: An account of the music composition.
    Returns:
        The string for the mutation for updating the music composition.
    Raises:
        Assertion error if the input language or inLanguage is not one of the supported languages.
    """
        


    args = {"identifier": identifier}
    if title:
        args["title"] = title
    if contributor:
        args["contributor"] = contributor
    if creator:
        args["creator"] = creator
    if source:
        args["source"] = source
    if language:
        if language not in SUPPORTED_LANGUAGES:
            raise UnsupportedLanguageException(language)
        else:
            args["language"] = StringConstant(language.lower())
    if inLanguage:
        if inLanguage not in SUPPORTED_LANGUAGES:
            raise UnsupportedLanguageException(inLanguage)
        else:
            args["inLanguage"] = StringConstant(inLanguage.lower())
    if format_:
        args["format"] = format_
    if name:
        args["name"] = name
    if description:
        args["description"] = description
    args = filter_none_args(args)

    return format_mutation("UpdateMusicComposition", args)



def mutation_delete_music_composition(identifier: str):
    """Returns a mutation for deleting a music composition object based on the identifier.
    Arguments:
        identifier: The unique identifier of the music composition object.
    Returns:
        The string for the mutation for deleting the music composition object based on the identifier.
    """

    return mutation_delete("DeleteMusicComposition", {"identifier": identifier})


def mutation_add_broad_match_music_composition(from_identifier: str, to_identifier: str):
    """Returns a mutation for creating a broad match between two music comosition objects.
    Arguments:
        from_identifier: The unique identifier of the digital document object from which to create the broad match.
        to_identifier: The unique identifier of the digital document object to which the broad match should be created.
    Returns:
        The string for the mutation for creating the broad match between the two documents.
    """

    return mutation_link(from_identifier, to_identifier, ADD_MUSIC_COMPOSITION_BROAD_MATCH)


def mutation_remove_broad_match_music_composition(from_identifier: str, to_identifier: str):
    """Returns a mutation for removing a broad match between two music composition objects.
    Arguments:
        from_identifier: The unique identifier of the music composition object from which to remove the broad match.
        to_identifier: The unique identifier of the digital document object to which the broad match should be removed.
    Returns:
        The string for the mutation for removing the broad match between the music compositions.
    """

    return mutation_link(from_identifier, to_identifier, REMOVE_MUSIC_COMPOSITION_BROAD_MATCH)


def mutation_add_music_composition_work_example_composition(music_composition_id: str, composition_id: str):
    """Returns a mutation for adding a music composition as an example of a composition.
    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for adding the music composition as an example of the composition.
    """

    return mutation_link(music_composition_id, composition_id, ADD_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION)


def mutation_merge_music_composition_work_example_composition(music_composition_id: str, composition_id: str):
    """Returns a mutation for merging a music composition as an example of a composition.
    Merging means that the connection will be added only if it does not exist.

    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for merging the music composition as an example of the composition.
    """

    return mutation_link(music_composition_id, composition_id, MERGE_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION)


def mutation_remove_music_composition_work_example_composition(music_composition_id: str, composition_id: str):
    """Returns a mutation for removing a music composition as an example of a composition.
    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for removing the music composition as an example of the composition.
    """

    return mutation_link(music_composition_id, composition_id, REMOVE_MUSIC_COMPOSITION_WORK_EXAMPLE_COMPOSITION)


def mutation_add_music_composition_controlaction(music_composition_id: str, controlaction_id: str):
    """Returns a mutation for adding a music composition to a control action.
    Arguments:
        music_composition_id: The unique identifier of the music composition object.
        composition_id: The unique identifier of the composition object.
    Returns:
        The string for the mutation for adding the music composition to the control action. 
    """

    return mutation_link(music_composition_id, controlaction_id, ADD_MUSIC_COMPOSITION_TO_CONTROL_ACTION_MUTATION)