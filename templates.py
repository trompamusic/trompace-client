# Templates for mutations



MUTATION = '''
mutation {{
  {mutation}
}}
'''

CREATE_ENTRY_POINT = '''
CreatePerson(
{parameters}
) {{
  identifier
  name
}}

  CreateEntryPoint(
  contributor: {}
  title : {}
  name: {}
  creator: {}
  description: {}
  language: {}
  format: {}
  source: {}
  subject: {}
)
{{
  identifier
  name
}}
'''


def get_wikidata_url(mb_artist):
    # The relation type for artist-url relation type
    wikidata_mb_rel_type = "689870a4-a1e4-4912-b17f-7b2664215698"
    for l in mb_artist.get("url-relation-list", []):
        if l["type-id"] == wikidata_mb_rel_type:
            return l["target"]
    return None


def transform_data_artist(composer_args):
    """Transform data from scraped composers data file"""

    return mutation_artist(**composer_args)


def transform_musicbrainz_artist(mb_artist):
    """Transform a musicbrainz artist to a CreatePerson mutation for the CE"""

    # possible languages: en,es,ca,nl,de,fr

    wikidata_url = get_wikidata_url(mb_artist)
    description = ""
    if wikidata_url:
        description = wikipedia.get_description_for_wikidata(wikidata_url)

    artist_name = mb_artist["name"]
    args = {
        "title": artist_name,
        "name": artist_name,
        "publisher": "https://musicbrainz.org",
        "contributor": "https://musicbrainz.org",
        "creator": "https://musicbrainz.org",
        "source": "https://musicbrainz.org/artist/{}".format(mb_artist["id"]),
        "subject": "artist",
        "description": description,
        "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant("en"),
            }
    return mutation_artist(**args)


def mutation_entrypoint(**kwargs):
    create_person = CREATE_PERSON.format(parameters=make_parameters(**kwargs))
    return MUTATION.format(mutation=create_person)
