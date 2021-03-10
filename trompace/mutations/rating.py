from trompace import check_required_args, filter_none_args
from trompace.mutations.templates import format_mutation, format_link_mutation

RATING_DEFINITION_ADDITIONAL_TYPE = "https://vocab.trompamusic.eu/vocab#RatingDefinition"


def create_rating_definition(*, creator: str, bestrating: int, worstrating: int, name: str = None):
    """Return a mutation for making a Rating definition.
    A Rating (https://schema.org/Rating) is an evaluation on a numeric scale.
    A Rating definition describes the structure that a rating can take. It is used so that an annotation
    tool can give a title and present an input according to the correct scale (e.g. 1-5 or 1-100).

    This is a helper method that requires a bestrating and worstrating value and automatically sets
    additionaltype to RATING_DEFINITION_ADDITIONAL_TYPE

    A name is recommended if multiple ratings are going to be shown on the same annotator, but isn't necessary.

    """
    check_required_args(creator=creator, bestrating=bestrating, worstrating=worstrating)

    params = {"creator": creator,
              "name": name,
              "bestRating": bestrating,
              "worstRating": worstrating,
              "additionalType": RATING_DEFINITION_ADDITIONAL_TYPE}

    params = filter_none_args(params)

    return format_mutation(mutationname="CreateRating", args=params)


def create_rating(*, creator: str, bestrating: int, ratingvalue: int = None, worstrating: int = None,
                  ratingexplanation: str = None, additionaltype: str = None):
    """Return a mutation for making a Rating.
    A Rating (https://schema.org/Rating) is an evaluation on a numeric scale.

    Arguments:
        creator: a URI to the identity of the user who created this DefinedTerm
        bestrating: The highest value allowed in this rating system
        ratingvalue: The rating for the content.
        worstrating (optional): The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.
        ratingexplanation (optional): A freeform text box describing why this rating was given
        additionaltype (optional): A schema.org additionalType used to categorise this Rating

    Returns:
        A GraphQL Mutation to create a Rating in the Trompa CE
    """

    check_required_args(creator=creator, bestrating=bestrating, ratingvalue=ratingvalue)

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
