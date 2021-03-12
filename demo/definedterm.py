from trompace.mutations import definedterm, annotation


def main(print_queries: bool, submit_queries: bool):

    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"

    """A closed vocabulary of tags that someone can use"""
    dts = definedterm.create_defined_term_set(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION],
                                              name="Mood")

    dt_happy = definedterm.create_defined_term(creator=admin_vcard,
                                               additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                               termcode="Happy")

    dt_sad = definedterm.create_defined_term(creator=admin_vcard,
                                             additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                             termcode="Sad")

    dts_join_happy = definedterm.defined_term_add_to_defined_term_set(defined_term_set="dts.identifier",
                                                                      defined_term="dt_happy.identifier")
    dts_join_sad = definedterm.defined_term_add_to_defined_term_set(defined_term_set="dts.identifier",
                                                                    defined_term="dt_sad.identifier")

    print("DefinedTerm - Closed Vocabulary")
    if print_queries:
        print(dts)
        print(dt_happy)
        print(dt_sad)
        print(dts_join_happy)
        print(dts_join_sad)

    """A collection of annotation motivations that could be applied to a single item"""

    dts = definedterm.create_defined_term_set(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION],
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/conductor-baton.png",
                                              name="Performance instructions")

    dt_upbow = definedterm.create_defined_term(creator=admin_vcard,
                                               additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                               annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                               broader=annotation.AnnotationSchemaMotivation.commenting.value,
                                               image="https://alastair.trompa-solid.upf.edu/annotation-images/upbow.png",
                                               termcode="Upbow")

    dt_downbow = definedterm.create_defined_term(creator=admin_vcard,
                                                 additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                                 annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                                 broader=annotation.AnnotationSchemaMotivation.commenting.value,
                                                 image="https://alastair.trompa-solid.upf.edu/annotation-images/downbow.png",
                                                 termcode="Downbow")

    dt_arco = definedterm.create_defined_term(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                              annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                              broader=annotation.AnnotationSchemaMotivation.commenting.value,
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/arco.png",
                                              termcode="Arco")

    dt_slur = definedterm.create_defined_term(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                              annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                              broader=annotation.AnnotationSchemaMotivation.commenting.value,
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/slur.png",
                                              termcode="Slur")

    print("DefinedTerm - Motivation Collection")
    if print_queries:
        print(dts)
        print(dt_upbow)
        print(dt_downbow)
        print(dt_arco)
        print(dt_slur)

    if submit_queries:
        dts_id = send_query_and_get_id(dts, "DefinedTermSet")
        dt_upbow_id = send_query_and_get_id(dt_upbow, "DefinedTerm")
        dt_downbow_id = send_query_and_get_id(dt_downbow, "DefinedTerm")
        dt_arco_id = send_query_and_get_id(dt_arco, "DefinedTerm")
        dt_slur_id = send_query_and_get_id(dt_slur, "DefinedTerm")

    dts_join_upbow = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                      defined_term=dt_upbow_id)
    dts_join_downbow = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                        defined_term=dt_downbow_id)
    dts_join_arco = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                     defined_term=dt_arco_id)
    dts_join_slur = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                     defined_term=dt_slur_id)
    print("DefinedTerm - Join to DefinedTermSet")
    if print_queries:
        print(dts_join_upbow)
        print(dts_join_downbow)
        print(dts_join_arco)
        print(dts_join_slur)

    if submit_queries:
        send_query_and_get_id(dts_join_upbow)
        send_query_and_get_id(dts_join_downbow)
        send_query_and_get_id(dts_join_arco)
        send_query_and_get_id(dts_join_slur)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
