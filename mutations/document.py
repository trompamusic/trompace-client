# Generate GraphQL queries for mutations pertaining to digital document objects.

from . import StringConstant, make_parameters, MUTATION
from .templates import mutation_create, mutation_delete, mutation_update


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
  name
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

DELETE_DIGITAL_DOCUMENT = '''
DeleteDigitalDocument(
  {parameters}
) {{
  identifier
  name
}}
'''


def mutation_create_document(document_name: str, publisher: str, contributor: str, creator: str, source: str, description: str, subject:str, language: str):
    """Returns a mutation for creating a digital document object
    Arguments:
        document_name: The name of the digital document.
        publisher: The person, organization or service responsible for making the artist inofrmation available.
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the artist. 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


    Returns:
        The string for the mutation for creating the document object.
    Raises:
        Assertion error if the input language is not one of the supported languages. 
    """
    return mutation_create(document_name, publisher, contributor, creator, source, description, language, subject, CREATE_DIGITAL_DOCUMENT)

def mutation_update_document(identifier:str, document_name=None, publisher=None, contributor=None, creator=None, source=None, description=None, language=None):
    """Returns a mutation for updating a digital document object.
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

def mutation_delete_document(identifier: str):
    """Returns a mutation for deleting a digital document object based on the identifier.
    Arguments:
        identifier: The unique identifier of the digital document object.
    Returns:
        The string for the mutation for deleting the digital document object based on the identifier.
    """

    return mutation_delete(identifier, DELETE_DIGITAL_DOCUMENT)
