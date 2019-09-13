# Templates for generate GraphQL queries for mutations.

from . import StringConstant, make_parameters, MUTATION


def mutation_create(name: str, publisher: str, contributor: str, creator: str, source: str, description: str, language: str, subject:str, mutation_string: str, coverage=None, date=None,
    disambiguatingDescription=None, relation=None, _type=None, _searchScore=None, additionalType=None, alternateName=None, image=None, sameAs=None, url=None, additionalName=None,
    award=None, birthDate=None, deathDate=None, familyName=None, gender=None, givenName=None, honorificPrefix=None, honorificSuffix=None, jobTitle=None, knowsLanguage=None):
    """Returns a mutation for creating an object.
    Arguments:
        name: The name of the object.
        publisher: The person, organization or service responsible for making the artist inofrmation available
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the artist. 
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr

    Returns:
        The string for the mutation for creating the object.
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
    if date:
        args["date"] = date
    if disambiguatingDescription:
        args["disambiguatingDescription"] = disambiguatingDescription
    if relation:
        args["relation"] = relation
    if _type:
        args["type"] = _type
    if _searchScore:
        args["_searchScore"] = _searchScore
    if additionalType:
        args["additionalType"] = additionalType
    if alternateName:
        args["alternateName"] = alternateName
    if image:
        args["image"] = image
    if sameAs:
        args["sameAs"] = sameAs
    if url:
        args["url"] = url
    if additionalName:
        args["additionalName"] = additionalName
    if award:
        args["award"] = award
    if birthDate:
        args["birthDate"] = birthDate
    if deathDate:
        args["deathDate"] = deathDate
    if familyName:
        args["familyName"] = familyName
    if gender:
        args["gender"] = gender
    if honorificPrefix:
        args["honorificPrefix"] = honorificPrefix
    if honorificSuffix:
        args["honorificSuffix"] = honorificSuffix
    if jobTitle:
        args["jobTitle"] = jobTitle
    if knowsLanguage:
        args["knowsLanguage"] = knowsLanguage

    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)

def mutation_update(identifier: str, mutation_string: str, name = None, publisher = None, contributor = None, creator = None, source = None, description = None, language = None, coverage=None, date=None,
    disambiguatingDescription=None, relation=None, _type=None, _searchScore=None, additionalType=None, alternateName=None, image=None, sameAs=None, url=None, additionalName=None,
    award=None, birthDate=None, deathDate=None, familyName=None, gender=None, givenName=None, honorificPrefix=None, honorificSuffix=None, jobTitle=None, knowsLanguage=None):
    """Returns a mutation for updating an object.
    Arguments:
        identifier: The unique identifier of the object.
        name (optional): The name of the object.
        publisher (optional): The person, organization or service responsible for making the artist inofrmation available
        contributor (optional): A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator (optional): The person, organization or service who created the thing the web resource is about.
        sourcer (optional): The URL of the web resource to be represented by the node.
        description (optional): An account of the artist. 
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


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
    if coverage:
        args["coverage"] = coverage
    if date:
        args["date"] = date
    if disambiguatingDescription:
        args["disambiguatingDescription"] = disambiguatingDescription
    if relation:
        args["relation"] = relation
    if _type:
        args["type"] = _type
    if _searchScore:
        args["_searchScore"] = _searchScore
    if additionalType:
        args["additionalType"] = additionalType
    if alternateName:
        args["alternateName"] = alternateName
    if image:
        args["image"] = image
    if sameAs:
        args["sameAs"] = sameAs
    if url:
        args["url"] = url
    if additionalName:
        args["additionalName"] = additionalName
    if award:
        args["award"] = award
    if birthDate:
        args["birthDate"] = birthDate
    if deathDate:
        args["deathDate"] = deathDate
    if familyName:
        args["familyName"] = familyName
    if gender:
        args["gender"] = gender
    if honorificPrefix:
        args["honorificPrefix"] = honorificPrefix
    if honorificSuffix:
        args["honorificSuffix"] = honorificSuffix
    if jobTitle:
        args["jobTitle"] = jobTitle
    if knowsLanguage:
        args["knowsLanguage"] = knowsLanguage
        
    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)

def mutation_delete(identifier: str, mutation_string: str):
    """Returns a mutation for deleting an object
    Arguments:
        identifier: The unique identifier of the object.
    Returns:
        The string for the mutation for creating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages. 
    """

    args = {"identifier": identifier}

    delete_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=delete_mutation)