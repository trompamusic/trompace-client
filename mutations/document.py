from . import StringConstant, make_parameters, MUTATION
from .templates import mutation_create


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


def mutation_create_document(document_name: str, publisher: str, contributor: str, creator: str, source: str, description: str, subject:str, language: str):
    """Returns a mutation for creating a digital document object
    Arguments:
        artist_name: The name of the digital document.
        publisher: The person, organization or service responsible for making the artist inofrmation available.
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
    return mutation_create(document_name, publisher, contributor, creator, source, description, language, subject, CREATE_DIGITAL_DOCUMENT)

def mutation_update_document(identifier:str, document_name=None, publisher=None, contributor=None, creator=None, source=None, description=None, language=None):
    """Returns a mutation for updating a person object
    Arguments:
        identifier: The unique identifier of the digital document.
        document_name (optional): The name of the digital document.
        publisher (optional): The person, organization or service responsible for making the artist inofrmation available.
        contributor (optional): A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator (optional): The person, organization or service who created the document that the web resource is about.
        sourcer (optional): The URL of the web resource to be represented by the node.
        description (optional): An account of the artist. 
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr.
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages. 
    """

    return mutation_update(identifier, UPDATE_DIGITAL_DOCUMENT, document_name, publisher, contributor, creator, source, description, language)


def get_query_remove_document_composition(composition_id, document_id):
    query = REMOVE_DIGITAL_DOCUMENT_SUBJECT_OF_COMPOSITION.format(document_id=document_id, composition_id=composition_id)
    return MUTATION.format(mutation=query)


def transform_data_create_document(document_args):
    create_digital_document = CREATE_DIGITAL_DOCUMENT.format(parameters=make_parameters(**document_args))
    return MUTATION.format(mutation=create_digital_document)


def transform_data_update_document(document_args):
    update_digital_document = UPDATE_DIGITAL_DOCUMENT.format(parameters=make_parameters(**document_args))
    return MUTATION.format(mutation=update_digital_document)
