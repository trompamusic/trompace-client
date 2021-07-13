from typing import List

from trompace import StringConstant, check_required_args, filter_none_args, docstring_interpolate
from trompace.mutations import _verify_additional_type, annotation
from trompace.mutations.templates import format_mutation, format_link_mutation


DEFINEDTERMSET_ARGS_DOCS = """creator: a URI to the identity of the user who created this DefinedTermSet (:dcterms:`creator`)
        name: the name of this DefinedTermSet (:schema:`name`)
        additionaltype: A list of schema.org additionalTypes used to categorise this DefinedTermSet (:schema:`additionalType`)
        broader_url (optional): a type to be related with :skos:`broader`
        broader_schema (optional): an annotation motivation to be related with :skos:`broader`
        image (optional): an image to describe this DefinedTermSet (:schema:`image`)
"""


@docstring_interpolate("definedtermset_args", DEFINEDTERMSET_ARGS_DOCS)
def create_defined_term_set(*, creator: str, name: str, additionaltype: List[str], broader_url: str = None,
                            broader_schema: annotation.AnnotationSchemaMotivation = None, image: str = None):
    """Return a mutation for making a DefinedTermSet.
    A :schema:`DefinedTermSet` is a group of defined terms, e.g. categories or labels.

    Arguments:
        {definedtermset_args}

    Returns:
        A GraphQL Mutation to create a DefinedTermSet in the Trompa CE
    """

    check_required_args(creator=creator, name=name, additionaltype=additionaltype)
    additionaltype = _verify_additional_type(additionaltype)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "name": name,
              "broaderUrl": broader_url,
              "image": image}
    if broader_schema is not None:
        params["broaderMotivation"] = StringConstant(broader_schema.name)
    params = filter_none_args(params)
    return format_mutation(mutationname="CreateDefinedTermSet", args=params)


DEFINEDTERM_ARGS_DOCS = """creator: a URI to the identity of the user who created this DefinedTerm (:dcterms:`creator`)
        termcode: The name of this term
        additionaltype: A list of schema.org additionalTypes used to categorise this DefinedTerm (:schema:`additionalType`)

        image (optional): an image to describe this DefinedTerm (:schema:`image`)
"""


@docstring_interpolate("definedterm_args", DEFINEDTERM_ARGS_DOCS)
def create_defined_term(*, creator: str, termcode: str, additionaltype: List[str], image: str = None):
    """Return a mutation for making a DefinedTerm.
    A :schema:`DefinedTerm` is a word, name, acronym, phrase, etc. with a formal definition.
    It is part of a DefinedTermSet.

    Arguments:
        {definedterm_args}

    Returns:
        A GraphQL Mutation to create a DefinedTerm in the Trompa CE
    """
    check_required_args(creator=creator, termcode=termcode, additionaltype=additionaltype)
    additionaltype = _verify_additional_type(additionaltype)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "termCode": termcode,
              "image": image}

    params = filter_none_args(params)

    return format_mutation(mutationname="CreateDefinedTerm", args=params)


@docstring_interpolate("definedtermset_args", DEFINEDTERMSET_ARGS_DOCS)
def update_defined_term_set(identifier: str, *, creator: str = None, name: str = None,
                            additionaltype: List[str] = None, broader_url: str = None,
                            broader_schema: annotation.AnnotationSchemaMotivation = None,
                            image: str = None):
    """Return a mutation for updating a DefinedTermSet.

    Arguments:
        identifier: The identifier of the DefinedTermSet in the CE to be updated (:dcterms:`identifier`).
        {definedtermset_args}

    Returns:
        A GraphQL Mutation to update a DefinedTermSet in the Trompa CE
    """

    additionaltype = _verify_additional_type(additionaltype)
    params = {"identifier": identifier,
              "creator": creator,
              "name": name,
              "additionalType": additionaltype,
              "broaderUrl": broader_url,
              "image": image}
    if broader_schema is not None:
        params["broaderMotivation"] = StringConstant(broader_schema.name)
    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateDefinedTermSet", args=params)


@docstring_interpolate("definedterm_args", DEFINEDTERM_ARGS_DOCS)
def update_defined_term(identifier: str, *, creator: str = None, termcode: str = None,
                        additionaltype: List[str] = None, image: str = None):
    """Return a mutation for updating a DefinedTerm.

    Arguments:
        identifier: The identifier of the DefinedTerm in the CE to be updated (:dcterms:`identifier`).
        {definedterm_args}

    Returns:
        A GraphQL Mutation to update a DefinedTerm in the Trompa CE
    """

    additionaltype = _verify_additional_type(additionaltype)
    params = {"identifier": identifier,
              "creator": creator,
              "termCode": termcode,
              "additionalType": additionaltype,
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
