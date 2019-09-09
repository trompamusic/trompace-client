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




def mutation_artist(artist_name: str, artist_id: str, description: str):
    """Returns a mutation for creating a person object
    Arguments:
        str artist_name: The name of the artist
        str artist_if: The musicbraniz id of the artist
        str description: The relavent description of the artist

    Returns:
        The string for the mutation for creating the artist.
    Raises:
        None
    """
    args = {
        "title": artist_name,
        "name": artist_name,
        "publisher": "https://musicbrainz.org",
        "contributor": "https://musicbrainz.org",
        "creator": "https://musicbrainz.org",
        "source": "https://musicbrainz.org/artist/{}".format(artist_id),
        "subject": "artist",
        "description": description,
        "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant("en"),
            }
    create_person = CREATE_PERSON.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_person)


