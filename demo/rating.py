from trompace.mutations import rating


def main(print_queries: bool, submit_queries: bool):

    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    definition = rating.create_rating(
        creator=admin_vcard,
        bestrating=10,
        worstrating=1,
        additionaltype=rating.RATING_DEFINITION_ADDITIONAL_TYPE
    )

    print("\nRating - Definition\n")
    if print_queries:
        print(definition)

    actual_rating = rating.create_rating(
        creator=user_vcard,
        bestrating=10,
        worstrating=1,
        ratingvalue=8
    )

    print("\nRating\n")
    if print_queries:
        print(actual_rating)

    # Link rating
    rating_definition_id = "4d38adc9-ff6d-4709-bcf5-f67fef867456"
    actual_rating_id = "787e7dc4-9a77-4b26-9d30-61a4909fbc07"
    merge_ratings = rating.rating_add_was_derived_from_rating(actual_rating_id, rating_definition_id)

    print("\nLink Rating with Rating Definition\n")
    if print_queries:
        print(merge_ratings)


if __name__ == '__main__':
    from demo import args
    main(args.args.print, args.args.submit)
