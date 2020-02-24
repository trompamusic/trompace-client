# Generate GraphQL queries for mutations pertaining to persons/artists objects.
from trompace.exceptions import UnsupportedLanguageException, MimeTypeException
from . import StringConstant, _Neo4jDate
from .templates import mutation_create, mutation_update, mutation_delete
from ..constants import SUPPORTED_LANGUAGES

CREATE_PERSON = '''CreatePerson(
        {parameters}
    ) {{
      identifier
    }}'''

UPDATE_PERSON = '''UpdatePerson(
      {parameters}
    ) {{
      identifier
    }}'''

DELETE_PERSON = '''DeletePerson(
      {parameters}
    ) {{
      identifier
    }}'''


def mutation_create_artist(artist_name: str, publisher: str, contributor: str, creator: str, source: str,
                           description: str, language: str, formatin="text/html", coverage=None, date=None,
                           disambiguatingDescription=None, relation=None, _type=None, _searchScore=None,
                           additionalType=None, alternateName=None, image=None, sameAs=None, url=None,
                           additionalName=None,
                           award=None, birthDate=None, deathDate=None, familyName=None, gender=None, givenName=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None, knowsLanguage=None):
    """Returns a mutation for creating a person object
    Arguments:
        artist_name: The name of the artist
        publisher: The person, organization or service responsible for making the artist inofrmation available
        contributor: A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator: The person, organization or service who created the thing the web resource is about.
        sourcer: The URL of the web resource to be represented by the node.
        description: An account of the artist.
        language: The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr
        coverage (optional): The spatial or temporal topic of the resource, the spatial applicability of the resource, or the jurisdiction under which the resource is relevant.
        date (optional): A point in time associated with an event in the lifecycle of the resource. Must be in ‘YYYY’, ‘YYYY-MM’ or ‘YYYY-MM-DD’ format.
        disambiguatingDescription (optional): An alternate description of the artist, particularlly to distinguish from other similar artists.
        relation (optional): A related resource. Any web resource can be used as a relation.
        _type (optional): The RDF type URI of the node.
        _searchScore (optional): Unknown, ask Alastair.
        additionalType (optional): An additional type for the node.
        alternateName (optional): Alternate name of the artist.
        image (optional): An image associated with the artist.
        sameAs (optional): A schema.org property, defined as the URL of a reference Web page that unambiguously indicates the item's identity.
        url (optional): An additional URL for the artist.
        additionalName (optional): An additional name for the artist.
        award (optional): Awards won the artist?
        birthDate (optional): The birth date of the artist, currently accepts string, but needs to be chenged to date format.
        deathDate (optional): The date of death of the artist, currently accepts string, but needs to be chenged to date format.
        familyName (optional); The family name of the artist.
        gender (optinal): The artists gender.
        honorificPrefix (optional): The artist's prefix.
        honorificSuffix (optional): The artist's suffix.
        jobTitle (optional): The artist's job title.
        knowsLanguage (optional): The language known by the artist.



    Returns:
        The string for the mutation for creating the artist.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    if "/" not in formatin:
        raise MimeTypeException(formatin)

    args = {
        "title": artist_name,
        "name": artist_name,
        "publisher": publisher,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "subject": "artist",
        "description": description,
        "format": formatin,
        "language": StringConstant(language.lower()),
    }
    if coverage:
        args["coverage"] = coverage
    if date:
        args["date"] = _Neo4jDate(date)
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
        args["birthDate"] = _Neo4jDate(birthDate)
    if deathDate:
        args["deathDate"] = _Neo4jDate(deathDate)
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

    return mutation_create(args, CREATE_PERSON)


def mutation_update_artist(identifier: str, artist_name=None, publisher=None, contributor=None, creator=None,
                           source=None, description=None, language=None, coverage=None, date=None,
                           disambiguatingDescription=None, relation=None, _type=None, _searchScore=None,
                           additionalType=None, alternateName=None, image=None, sameAs=None, url=None,
                           additionalName=None,
                           award=None, birthDate=None, deathDate=None, familyName=None, gender=None, givenName=None,
                           honorificPrefix=None, honorificSuffix=None, jobTitle=None, knowsLanguage=None):
    """Returns a mutation for updating a person object
    Arguments:
        identifier: The unique identifier of the artist
        artist_name (optional): The name of the artist
        publisher (optional): The person, organization or service responsible for making the artist inofrmation available.
        contributor (optional): A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator (optional): The person, organization or service who created the thing the web resource is about.
        sourcer (optional): The URL of the web resource to be represented by the node.
        description (optional): An account of the artist.
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr.
        coverage (optional): The spatial or temporal topic of the resource, the spatial applicability of the resource, or the jurisdiction under which the resource is relevant.
        date (optional): A point in time associated with an event in the lifecycle of the resource. Must be in ‘YYYY’, ‘YYYY-MM’ or ‘YYYY-MM-DD’ format.
        disambiguatingDescription (optional): An alternate description of the artist, particularlly to distinguish from other similar artists.
        relation (optional): A related resource. Any web resource can be used as a relation.
        _type (optional): The RDF type URI of the node.
        _searchScore (optional): Unknown, ask Alastair.
        additionalType (optional): An additional type for the node.
        alternateName (optional): Alternate name of the artist.
        image (optional): An image associated with the artist.
        sameAs (optional): A schema.org property, defined as the URL of a reference Web page that unambiguously indicates the item's identity.
        url (optional): An additional URL for the artist.
        additionalName (optional): An additional name for the artist.
        award (optional): Awards won the artist?
        birthDate (optional): The birth date of the artist, currently accepts string, but needs to be chenged to date format.
        deathDate (optional): The date of death of the artist, currently accepts string, but needs to be chenged to date format.
        familyName (optional); The family name of the artist.
        gender (optinal): The artists gender.
        honorificPrefix (optional): The artist's prefix.
        honorificSuffix (optional): The artist's suffix.
        jobTitle (optional): The artist's job title.
        knowsLanguage (optional): The language known by the artist.

    Returns:
        The string for the mutation for updating the artist.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    return mutation_update(identifier, UPDATE_PERSON, artist_name, publisher, contributor, creator, source, description,
                           language)


def mutation_delete_artist(identifier: str):
    """Returns a mutation for deleting a person object based on the identifier.
    Arguments:
        identifier: The unique identifier of the artist.
    Returns:
        The string for the mutation for deleting the artist based on the identifier.
    """

    return mutation_delete(identifier, DELETE_PERSON)
