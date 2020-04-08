import datetime

import pytz

from trompace import filter_none_args
from trompace.mutations.templates import format_mutation


def create_rating(creator: str, ratingvalue: int, bestrating: int, *, worstrating: int = None,
                  additionaltype: str = None):
    """Return a mutation for making a Rating.
    A Rating (https://schema.org/Rating) is an evaluation on a numeric scale,

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTerm
        ratingvalue: The rating for the content
        bestrating: The highest value allowed in this rating system
        worstrating: The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.
        additionaltype: A schema.org additionalType used to categorise this Rating

    Returns:
        A GraphQL Mutation to create a Rating in the Trompa CE
    """
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"creator": creator,
              "ratingValue": ratingvalue,
              "bestRating": bestrating,
              "worstRating": worstrating,
              "additionalType": additionaltype,
              "created": utcnow}

    params = filter_none_args(params)

    return format_mutation(mutationname="CreateRating", args=params)


def update_rating(identifier: str, *, creator: str = None, ratingvalue: int = None, bestrating: int = None,
                  worstrating: int = None, additionaltype: str = None):
    utcnow = datetime.datetime.now(pytz.UTC)

    params = {"identifier": identifier,
              "creator": creator,
              "ratingValue": ratingvalue,
              "bestRating": bestrating,
              "worstRating": worstrating,
              "additionalType": additionaltype,
              "modified": utcnow}

    params = filter_none_args(params)
    return format_mutation(mutationname="UpdateRating", args=params)


def delete_rating(identifier: str):
    """Return a mutation for deleting a Rating.

    Arguments:
        identifier: The identifier of the Rating to delete

    Returns:
        A GraphQL Mutation to delete a Rating from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteRating", args=params)
