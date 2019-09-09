# GEnerate GraphQL queries for mutations.


from __init__ import StringConstant, make_parameters, MUTATION


CREATE_PERSON = '''
CreatePerson(
{parameters}
) {{
  identifier
  name
}}
'''

UPDATE_PERSON = '''
UpdatePerson(
  {parameters}
) {{
  identifier
  relation
}}
'''


def mutation_create_artist(artist_name: str, publisher: str, contributor: str, creator: str, source: str, description: str, language: str):
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
        "title": artist_name,
        "name": artist_name,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": "artist",
        "description": description,
        "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant(language.lower()),
            }
    create_person = CREATE_PERSON.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_person)

# def mutation_modify_artist(artist_name = None: str, publisher = None: str, contributor = None: str, creator = None: str, source = None: str, description = None: str, language = None: str):
#     """Returns a mutation for creating a person object
#     Arguments:
#         str artist_name: The name of the artist
#         str publisher: The person, organization or service responsible for making the artist inofrmation available
#         str contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
#         str creator: The person, organization or service who created the thing the web resource is about.
#         srt sourcer: The URL of the web resource to be represented by the node.
#         str description: An account of the artist. 
#         str language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


#     Returns:
#         The string for the mutation for creating the artist.
#     Raises:
#         Assertion error if the input language is not one of the supported languages. 
#     """

#     assert language.lower() in ["en","es","ca","nl","de","fr"], "Language {} not supported".format(language)
    
#     args = {
#         "title": artist_name,
#         "name": artist_name,
#         "publisher": publisher,
#         "contributor": contributor,
#         "creator": creator,
#         "source": source,
#         "subject": "artist",
#         "description": description,
#         "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
#         "language": StringConstant(language.lower()),
#             }
#     create_person = CREATE_PERSON.format(parameters=make_parameters(**args))
#     return MUTATION.format(mutation=create_person)
