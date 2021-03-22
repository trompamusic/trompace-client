# An annotation toolkit is a collection of annotation types that can be applied to annotations
# This could include Rating Definitions or DefinedTermSets

from trompace.mutations import definedterm, annotation, rating


def main(print_queries: bool, submit_queries: bool):
    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"

    definition = rating.create_rating_definition(
        creator=admin_vcard,
        bestrating=10,
        worstrating=1,
        name="Overal performance"
    )

    dts = definedterm.create_defined_term_set(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION],
                                              name="Mood")

    dt_happy = definedterm.create_defined_term(creator=admin_vcard,
                                               additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                               termcode="Happy")

    dt_sad = definedterm.create_defined_term(creator=admin_vcard,
                                             additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                             termcode="Sad")

    if submit_queries:
        definition_id = send_query_and_get_id(definition, "DefinedTermSet")
        dts_id = send_query_and_get_id(dts, "DefinedTermSet")
        dt_happy_id = send_query_and_get_id(dt_happy, "DefinedTerm")
        dt_sad_id = send_query_and_get_id(dt_sad, "DefinedTerm")

        dts_join_happy = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                          defined_term=dt_happy_id)
        dts_join_sad = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                        defined_term=dt_sad_id)








if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)