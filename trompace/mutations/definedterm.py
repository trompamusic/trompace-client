from typing import List

from trompace import check_required_args, filter_none_args
from trompace.mutations import MUTATION
from trompace.mutations.templates import format_mutation, format_link_mutation

ADD_DEF_TERM_DEF_TERMSET = '''AddDefinedTermSetHasDefinedTerm (
    from: {{identifier: "{defined_term_set_id}"}}
    to: {{identifier: "{defined_term_id}"}}
) {{
    from {{
        __typename
    }}
    to {{
        __typename
    }}
}}'''


def _verify_additional_type(additionaltype):
    """Check that the input to additionaltype is a list of strings.
    If it is empty, raise ValueError
    If it is a string, convert it to a list of strings."""
    if additionaltype is None:
        return None

    if isinstance(additionaltype, str):
        additionaltype = [additionaltype]
    if len(additionaltype) == 0:
        raise ValueError("additionaltype must be a non-empty list")
    return additionaltype


def create_defined_term_set(*, creator: str, name: str, additionaltype: List[str], image: str = None):
    """Return a mutation for making a DefinedTermSet.
    A DefinedTermSet (https://schema.org/DefinedTermSet) is a group of defined terms, e.g. categories or labels.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTermSet
        name: the name of this DefinedTermSet
        additionaltype: A list of schema.org additionalTypes used to categorise this DefinedTermSet
        image (optional): an image to describe this DefinedTermSet

    Returns:
        A GraphQL Mutation to create a DefinedTermSet in the Trompa CE
    """

    check_required_args(creator=creator, name=name, additionaltype=additionaltype)
    additionaltype = _verify_additional_type(additionaltype)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "name": name,
              "image": image}
    params = filter_none_args(params)
    return format_mutation(mutationname="CreateDefinedTermSet", args=params)


def create_defined_term(*, creator: str, termcode: str, additionaltype: List[str],
                        broader: str = None, image: str = None):
    """Return a mutation for making a DefinedTerm.
    A DefinedTerm (https://schema.org/DefinedTerm) is a word, name, acronym, phrase, etc. with a formal definition.
    It is part of a DefinedTermSet.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTerm
        termcode: The name of this term
        additionaltype: A list of schema.org additionalTypes used to categorise this DefinedTerm
        broader (optional): a type to be related with skos:broader
        image (optional): an image to describe this DefinedTerm

    Returns:
        A GraphQL Mutation to create a DefinedTerm in the Trompa CE
    """
    check_required_args(creator=creator, termcode=termcode, additionaltype=additionaltype)
    additionaltype = _verify_additional_type(additionaltype)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "termCode": termcode,
              "broader": broader,
              "image": image}
    params = filter_none_args(params)

    return format_mutation(mutationname="CreateDefinedTerm", args=params)


def update_defined_term_set(identifier: str, *, creator: str = None, name: str = None,
                            additionaltype: List[str] = None, image: str = None):
    """Return a mutation for updating a DefinedTermSet.

    TODO: Copy arguments from create_

    Returns:
        A GraphQL Mutation to update a DefinedTermSet in the Trompa CE
    """

    additionaltype = _verify_additional_type(additionaltype)
    params = {"identifier": identifier,
              "creator": creator,
              "name": name,
              "additionalType": additionaltype,
              "image": image}

    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateDefinedTermSet", args=params)


def update_defined_term(identifier: str, *, creator: str = None, termcode: str = None,
                        additionaltype: List[str] = None, broader: str = None, image: str = None):
    """Return a mutation for updating a DefinedTerm.

    TODO: Copy arguments from create_

    Returns:
        A GraphQL Mutation to update a DefinedTerm in the Trompa CE
    """

    additionaltype = _verify_additional_type(additionaltype)
    params = {"identifier": identifier,
              "creator": creator,
              "termCode": termcode,
              "additionalType": additionaltype,
              "broader": broader,
              "image": image}

    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateDefinedTerm", args=params)


def delete_defined_term_set(identifier: str):
    """Return a mutation for deleting a DefinedTermSet.

    Arguments:
        identifier: The identifier of the DefinedTermSet to delete

    Returns:
        A GraphQL Mutation to delete a DefinedTermSet from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteDefinedTermSet", args=params)


def delete_defined_term(identifier: str):
    """Return a mutation for deleting a DefinedTermSet.

    Arguments:
        identifier: The identifier of the DefinedTerm to delete

    Returns:
        A GraphQL Mutation to delete a DefinedTerm from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteDefinedTerm", args=params)


def defined_term_add_to_defined_term_set(*, defined_term_set: str, defined_term: str):
    """Return a mutation for adding a DefinedTerm to a DefinedTermSet.

    Arguments:
        defined_term_set: The identifier of the DefinedTermSet to add to
        defined_term: The identifier of the DefinedTermSet to add

    Returns:
        A GraphQL Mutation to add a DefinedTerm to the DefinedTermSet
    """
    return format_link_mutation("MergeDefinedTermSetHasDefinedTerm", defined_term_set, defined_term)

# TODO: Remove a term from termset - just delete it?
