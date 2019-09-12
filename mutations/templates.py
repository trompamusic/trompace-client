from . import StringConstant, make_parameters, MUTATION


def mutation_create(name: str, publisher: str, contributor: str, creator: str, source: str, description: str, language: str, subject:str, mutation_string: str,
 coverage=None, date=None, disambiguatingDescription=None, identifier=None, relation=None, rights=None, type=None, alternateName=None, image=None, sameAs=None, url=None):
    """Returns a mutation for creating a digital document object
    Arguments:
        str artist_name: The name of the digital document
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
        "title": name,
        "name": name,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": subject,
        "description": description,
        "format": "text/html",  # an artist doesn't have a mimetype, use the mimetype of the source (musicbrainz page)
        "language": StringConstant(language.lower()),
            }
    if coverage:
        args["coverage"] = coverage

    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)

def mutation_update(identifier: str, mutation_string: str, name = None, publisher = None, contributor = None, creator = None, source = None, description = None, language = None):
    """Returns a mutation for creating a digital document object
    Arguments:
        str artist_name: The name of the digital document
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

    if language:

      assert language.lower() in ["en","es","ca","nl","de","fr"], "Language {} not supported".format(language)
    
    args = {"identifier": identifier}
    if name:
      args["title"] = name
      args["name"] = name
    if publisher:
      args["publisher"] = publisher
    if contributor:
      args["contributor"] = contributor
    if creator:
      args["creator"] = creator
    if source:
      args["source"] = source


    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)

# def main():
#   print(mutation_update("aiaiaia", UPDATE_PERSON, publisher = "booboo"))

# if __name__ == '__main__':
#     main()