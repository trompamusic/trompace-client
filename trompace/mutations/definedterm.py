import datetime

import pytz

from trompace import filter_none_args
from trompace.mutations import MUTATION
from trompace.mutations.templates import format_mutation

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


def create_defined_term_set(creator: str, name: str, additionaltype: str):
    """Return a mutation for making a DefinedTermSet.
    A DefinedTermSet (https://schema.org/DefinedTermSet) is a group of defined terms, e.g. categories or labels.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTermSet
        name: the name of this DefinedTermSet
        additionaltype: A schema.org additionalType used to categorise this DefinedTermSet

    Returns:
        A GraphQL Mutation to create a DefinedTermSet in the Trompa CE
    """
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "name": name,
              "created": utcnow}
    return format_mutation(mutationname="CreateDefinedTermSet", args=params)


def create_defined_term(creator: str, termcode: str, additionaltype: str):
    """Return a mutation for making a DefinedTerm.
    A DefinedTerm (https://schema.org/DefinedTerm) is a word, name, acronym, phrase, etc. with a formal definition.
    It is part of a DefinedTermSet.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTerm
        termcode: The name of this term
        additionaltype: A schema.org additionalType used to categorise this DefinedTerm

    Returns:
        A GraphQL Mutation to create a DefinedTerm in the Trompa CE
    """
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"additionalType": additionaltype,
              "creator": creator,
              "termCode": termcode,
              "created": utcnow}
    return format_mutation(mutationname="CreateDefinedTerm", args=params)


def update_defined_term_set(identifier: str, *, creator: str = None, name: str = None):
    """Return a mutation for updating a DefinedTermSet.

    TODO: Copy arguments from create_

    Returns:
        A GraphQL Mutation to update a DefinedTermSet in the Trompa CE
    """
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"identifier": identifier,
              "creator": creator,
              "name": name,
              "modified": utcnow}

    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateDefinedTermSet", args=params)


def update_defined_term(identifier: str, creator: str = None, termcode: str = None):
    """Return a mutation for updating a DefinedTerm.

    TODO: Copy arguments from create_

    Returns:
        A GraphQL Mutation to update a DefinedTerm in the Trompa CE
    """
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"identifier": identifier,
              "creator": creator,
              "termCode": termcode,
              "modified": utcnow}

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


def defined_term_add_to_defined_term_set(defined_term_set: str, defined_term: str):
    """Return a mutation for adding a DefinedTerm to a DefinedTermSet.

    Arguments:
        defined_term_set: The identifier of the DefinedTermSet to add to
        defined_term: The identifier of the DefinedTermSet to add

    Returns:
        A GraphQL Mutation to add a DefinedTerm to the DefinedTermSet
    """
    params = {"defined_term_set_id": defined_term_set,
              "defined_term_id": defined_term}
    add_dts_dt = ADD_DEF_TERM_DEF_TERMSET.format(**params)
    return MUTATION.format(mutation=add_dts_dt)


# TODO: Remove a term from termset - just delete it?
