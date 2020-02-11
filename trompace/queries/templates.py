# Templates for generate GraphQL queries for mutations.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from trompace.exceptions import UnsupportedLanguageException
from . import make_parameters, MUTATION
from ..constants import SUPPORTED_LANGUAGES




def query_create(identifier: str, query_string: str, name=None, publisher=None, contributor=None, creator=None,
                    source=None, subject=None, description=None, language=None, coverage=None, date=None,
                    disambiguatingDescription=None, relation=None, _type=None, _searchScore=None, additionalType=None,
                    alternateName=None, image=None, sameAs=None, url=None, additionalName=None,
                    award=None, birthDate=None, deathDate=None, familyName=None, gender=None, givenName=None,
                    honorificPrefix=None, honorificSuffix=None, jobTitle=None, knowsLanguage=None):
    """Returns a mutation for updating an object.
    Arguments:
        identifier: The unique identifier of the object.
        name (optional): The name of the object.
        publisher (optional): The person, organization or service responsible for making the artist inofrmation available
        contributor (optional): A person, an organization, or a service responsible for contributing the artist to the web resource. This can be either a name or a base URL.
        creator (optional): The person, organization or service who created the thing the web resource is about.
        source (optional): The URL of the web resource to be represented by the node.
        description (optional): An account of the artist.
        language (optional): The language the metadata is written in. Currently supported languages are en,es,ca,nl,de,fr


    Returns:
        The string for the mutation for creating the artist.
    Raises:
        UnsupportedLanguageException if the input language is not one of the supported languages.
    """

    if language and language not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    args = {"identifier": identifier}
    if name:
        args["title"] = name
        args["name"] = name
    if publisher:
        args["publisher"] = publisher
    if contributor:
        args["contributor"] = contributor
    if subject:
        args["subject"] = subject
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

    create_query = query_string.format(parameters=make_parameters(**args))
    return create_query

