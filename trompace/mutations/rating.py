import datetime

import pytz

from trompace import check_required_args, filter_none_args
from trompace.mutations.templates import format_mutation, format_link_mutation

RATING_DEFINITION_ADDITIONAL_TYPE = "https://vocab.trompamusic.eu/vocab#RatingDefinition"


def create_rating(*, creator: str, bestrating: int, ratingvalue: int = None, worstrating: int = None,
                  ratingexplanation: str = None, additionaltype: str = None):
    """Return a mutation for making a Rating.
    A Rating (https://schema.org/Rating) is an evaluation on a numeric scale.

    If you want to create a template rating for other people to follow, set additionatype to
    RATING_DEFINITION_ADDITIONAL_TYPE.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTerm
        bestrating: The highest value allowed in this rating system
        ratingvalue: The rating for the content. Must be set if ``additionaltype`` is not
          ``https://vocab.trompamusic.eu/vocab#RatingDefinition``
        worstrating (optional): The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.
        ratingexplanation (optional): A freeform text box describing why this rating was given
        additionaltype (optional): A schema.org additionalType used to categorise this Rating

    Returns:
        A GraphQL Mutation to create a Rating in the Trompa CE
    """

    args = {"creator": creator,
            "bestrating": bestrating}
    # Only check that ratingvalue is present if we're not making a Rating definition
    if additionaltype != RATING_DEFINITION_ADDITIONAL_TYPE:
        args["ratingvalue"] = ratingvalue

    check_required_args(**args)

    params = {"creator": creator,
              "ratingValue": ratingvalue,
              "bestRating": bestrating,
              "worstRating": worstrating,
              "ratingExplanation": ratingexplanation,
              "additionalType": additionaltype}

    params = filter_none_args(params)

    return format_mutation(mutationname="CreateRating", args=params)


def update_rating(identifier: str, *, creator: str = None, ratingvalue: int = None, bestrating: int = None,
                  worstrating: int = None, ratingexplanation: str = None, additionaltype: str = None):

    params = {"identifier": identifier,
              "creator": creator,
              "ratingValue": ratingvalue,
              "bestRating": bestrating,
              "worstRating": worstrating,
              "ratingExplanation": ratingexplanation,
              "additionalType": additionaltype}

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


def rating_add_was_derived_from_rating(rating_id: str, original_rating_id: str):
    """Generate a mutation to link two ratings with the prov:wasDerivedFrom relation

    Arguments:
        rating_id: the id of the new rating
        original_rating_id: the id of the original rating from which rating_id was derived

    Returns:
        A GraphQL Mutation for MergeRatingWasDerivedFrom
    """

    return format_link_mutation("MergeRatingWasDerivedFrom", rating_id, original_rating_id)


def rating_remove_was_derived_from_rating(rating_id: str, original_rating_id: str):
    """Generate a mutation to remove the prov:wasDerivedFrom relation between two ratings

    Arguments:
        rating_id: the id of the new rating
        original_rating_id: the id of the original rating from which rating_id was derived

    Returns:
        A GraphQL Mutation for RemoveRatingWasDerivedFrom
    """

    return format_link_mutation("RemoveRatingWasDerivedFrom", rating_id, original_rating_id)
