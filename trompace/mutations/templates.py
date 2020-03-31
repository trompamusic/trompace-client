# Templates for generating GraphQL queries for mutations.
from typing import Dict, Any

from trompace.mutations import MUTATION
from trompace import make_parameters


MUTATION_TEMPLATE = '''{mutationname}(
{parameters}
) {{
identifier
}}'''


def format_mutation(mutationname: str, args: Dict[str, Any]):
    """Create a mutation to send to the Contributor Environment.
    Arguments:
        mutationname: the name of the mutation to generate
        args: a dictionary of field: value pairs to add to the mutation
    Returns:
        A formatted mutation
    """

    formatted_mutation = MUTATION_TEMPLATE.format(mutationname=mutationname, parameters=make_parameters(**args))
    return MUTATION.format(mutation=formatted_mutation)


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


def mutation_update(args, mutation_string: str):
    """Returns a mutation for updating an object
    Arguments:
        args: a dictionary of arguments for the template. The fucntion calling this function is responsible for validating the arguments.
    Returns:
        The string for the mutation for updating the object.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    create_mutation = mutation_string.format(parameters=make_parameters(**args))
    return MUTATION.format(mutation=create_mutation)


def mutation_delete(identifier: str, mutation_string: str):
    """Returns a mutation for deleting an object
    Arguments:
        identifier: The unique identifier of the object.
    Returns:
        The string for the mutation for creating the object.
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