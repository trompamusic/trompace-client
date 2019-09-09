from __init__ import StringConstant, make_parameters, MUTATION



# We say that 2 different scores of the same thing are a broad match
ADD_DIGITAL_DOCUMENT_BROAD_MATCH = '''
AddDigitalDocumentBroadMatch(
  from: {{identifier: "{from_document_id}" }}
  to: {{identifier: "{to_document_id}" }}
) {{
  from {{
    identifier
  }}
  to {{
    identifier
  }}
}}
'''

REMOVE_DIGITAL_DOCUMENT_BROAD_MATCH = '''
RemoveDigitalDocumentBroadMatch(
  from: {{identifier: "{from_document_id}" }}
  to: {{identifier: "{to_document_id}" }}
) {{
  from {{
    identifier
  }}
  to {{
    identifier
  }}
}}
'''

ADD_DIGITAL_DOCUMENT_SUBJECT_OF_COMPOSITION = '''
AddThingInterfaceCreativeWorkInterface(
    from: {{identifier: "{document_id}" type:DigitalDocument}}
    to: {{identifier: "{composition_id}" type:MusicComposition}}
    field: subjectOf
) {{
    from {{
      __typename
    }}
    to {{
      __typename
    }}
}}
'''

REMOVE_DIGITAL_DOCUMENT_SUBJECT_OF_COMPOSITION = '''
RemoveThingInterfaceCreativeWorkInterface(
    from: {{identifier: "{document_id}" type:DigitalDocument}}
    to: {{identifier: "{composition_id}" type:MusicComposition}}
    field: subjectOf
) {{
    from {{
      __typename
    }}
    to {{
      __typename
    }}
}}
'''

CREATE_DIGITAL_DOCUMENT = '''
CreateDigitalDocument(
  {parameters}
) {{
  identifier
  relation
}}
'''

UPDATE_DIGITAL_DOCUMENT = '''
UpdateDigitalDocument(
  {parameters}
) {{
  identifier
  relation
}}
'''


def get_query_add_document_broad_match(from_document_id, to_document_id):
    query = ADD_DIGITAL_DOCUMENT_BROAD_MATCH.format(from_document_id=from_document_id, to_document_id=to_document_id)
    return MUTATION.format(mutation=query)


def get_query_remove_document_broad_match(from_document_id, to_document_id):
    query = REMOVE_DIGITAL_DOCUMENT_BROAD_MATCH.format(from_document_id=from_document_id, to_document_id=to_document_id)
    return MUTATION.format(mutation=query)


def mutation_create_document(document_name: str, publisher: str, contributor: str, creator: str, source: str, description: str, language: str):
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

    assert language.lower() in ["en","es","ca","nl","de","fr"], "Language {} not supported".format(language)
    
    args = {
        "title": document_name,
        "name": document_name,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": "artist",
        "description": description,
        "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant(language.lower()),
            }

    create_digital_document = CREATE_DIGITAL_DOCUMENT.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_digital_document)


def get_query_remove_document_composition(composition_id, document_id):
    query = REMOVE_DIGITAL_DOCUMENT_SUBJECT_OF_COMPOSITION.format(document_id=document_id, composition_id=composition_id)
    return MUTATION.format(mutation=query)


def transform_data_create_document(document_args):
    create_digital_document = CREATE_DIGITAL_DOCUMENT.format(parameters=make_parameters(**document_args))
    return MUTATION.format(mutation=create_digital_document)


def transform_data_update_document(document_args):
    update_digital_document = UPDATE_DIGITAL_DOCUMENT.format(parameters=make_parameters(**document_args))
    return MUTATION.format(mutation=update_digital_document)
