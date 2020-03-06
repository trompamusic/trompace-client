# Templates for generate GraphQL queries for mutations.

# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property
from trompace.exceptions import UnsupportedLanguageException
from . import make_parameters, MUTATION, StringConstant, _Neo4jDate
from ..constants import SUPPORTED_LANGUAGES


def mutation_create(args, mutation_string: str):
    """Returns a mutation for creating an object.
    Arguments:
        args: a dictionary of arguments for the template. The fucntion calling this function is responsible for validating the arguments.

    Returns:
        The string for the mutation for creating the object.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)


def mutation_update(identifier: str, mutation_string: str, name=None, publisher=None, contributor=None, creator=None,
                    source=None, description=None, language=None, coverage=None, date=None,
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
    if creator:
        args["creator"] = creator
    if source:
        args["source"] = source
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


def mutation_link(identifier_1: str, identifier_2: str, mutation_string: str):
    """Returns a mutation for linking two objects based on their identifiers.
    Arguments:
        identifier_1: The unique identifier of the first object.
        identifier_2: The unique identifier of the second object.
    Returns:
        The string for the mutation for the link.
    """

    broad_match_mutation = mutation_string.format(identifier_1=identifier_1, identifier_2=identifier_2)
    return MUTATION.format(mutation=broad_match_mutation)
