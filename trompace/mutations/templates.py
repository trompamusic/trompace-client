# Templates for generating GraphQL queries for mutations.

from typing import Dict, Any

from trompace import make_parameters
from trompace.mutations import MUTATION


MUTATION_TEMPLATE = '''{mutationname}(
{parameters}
) {{
identifier
}}'''


MUTATION_ALIAS_TEMPLATE = '''{mutationalias}: {mutationname}(
{parameters}
) {{
identifier
}}'''


LINK_MUTATION_TEMPLATE = '''{mutationname}(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
  ) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
  }}'''


LINK_MUTATION_ALIAS_TEMPLATE = '''{mutationalias}: {mutationname}(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
  ) {{
    from {{
      identifier
    }}
    to {{
      identifier
    }}
  }}'''


def format_sequence_link_mutation(mutations: list):
    """Create a mutation link sequence  to send to the Contributor Environment.
    Arguments:
        mutations: a list of mutations [(mutationalias, mutationname, args),...]
    Returns:
        A formatted mutation sequence
    """
    formatted_mutations = []
    for mutation in mutations:
        mutationalias, mutationname, args = mutation
        identifier_1, identifier_2 = args
        formatted_mutation = create_alias_link_mutation(mutationalias=mutationalias, mutationname=mutationname, identifier_1=identifier_1, identifier_2=identifier_2)
        formatted_mutations.append(formatted_mutation)

    return MUTATION.format(mutation="\n".join(formatted_mutations))


def create_alias_link_mutation(mutationalias: str, mutationname: str, identifier_1: str, identifier_2: str):
    """Create a mutation link alias to send to the Contributor Environment.
    Arguments:
        mutationalias: the alias of the mutation to generate
        mutationname: the name of the mutation to generate
        identifier_1: The unique identifier of the first object.
        identifier_2: The unique identifier of the second object.
    Returns:
        A mutation string
    """
    return LINK_MUTATION_ALIAS_TEMPLATE.format(mutationalias=mutationalias, mutationname=mutationname, identifier_1=identifier_1, identifier_2=identifier_2)


def format_sequence_mutation(mutations: list):
    """Create a mutation sequence to send to the Contributor Environment.
    Arguments:
        mutations: a list of mutations [(mutationalias, mutationname, args),...]
    Returns:
        A formatted mutation sequence
    """
    formatted_mutations = []
    for mutation in mutations:
        mutationalias, mutationname, args = mutation
        formatted_mutation = create_alias_mutation(mutationalias=mutationalias, mutationname=mutationname, args=args)
        formatted_mutations.append(formatted_mutation)

    return MUTATION.format(mutation="\n".join(formatted_mutations))


def create_alias_mutation(mutationalias: str, mutationname: str, args: Dict[str, Any]):
    """Create a mutation alias to send to the Contributor Environment.
    Arguments:
        mutationalias: the alias of the mutation to generate
        mutationname: the name of the mutation to generate
        args: a dictionary of field: value pairs to add to the mutation
    Returns:
        A mutation string
    """
    return MUTATION_ALIAS_TEMPLATE.format(mutationalias=mutationalias, mutationname=mutationname, parameters=make_parameters(**args))


def format_alias_mutation(mutationalias: str, mutationname: str, args: Dict[str, Any]):
    """Create a mutation to send to the Contributor Environment.
    Arguments:
        mutationalias: the alias of the mutation to generate
        mutationname: the name of the mutation to generate
        args: a dictionary of field: value pairs to add to the mutation
    Returns:
        A formatted mutation
    """
    formatted_mutation = MUTATION_ALIAS_TEMPLATE.format(mutationalias=mutationalias, mutationname=mutationname, parameters=make_parameters(**args))
    return MUTATION.format(mutation=formatted_mutation)


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


def format_link_mutation(mutationname: str, identifier_1: str, identifier_2: str):
    """Create a mutation with link between two identifiers to send to the Contributor Environment.
    Arguments:
        mutationname: the name of the mutation to generate
        identifier_1: The unique identifier of the first object.
        identifier_2: The unique identifier of the second object.
    Returns:
        A formatted mutation
    """
    return MUTATION.format(mutation=LINK_MUTATION_TEMPLATE.format(mutationname=mutationname, identifier_1=identifier_1,
                                                                  identifier_2=identifier_2))


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
