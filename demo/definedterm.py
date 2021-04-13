
from trompace.mutations import definedterm, annotation
from demo import send_query_and_get_id


def fixed_vocabulary(print_queries: bool, submit_queries: bool):
    """A closed vocabulary of tags that someone can use"""

    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"

    dts = definedterm.create_defined_term_set(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION],
                                              name="Mood")

    dts_id = "definedtermset-id"
    print("DefinedTermSet")
    if print_queries:
        print(dts)
    if submit_queries:
        dts_id = send_query_and_get_id(dts, "CreateDefinedTermSet")

    dt_happy = definedterm.create_defined_term(creator=admin_vcard,
                                               additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                               termcode="Happy")

    dt_sad = definedterm.create_defined_term(creator=admin_vcard,
                                             additionaltype=[annotation.ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT],
                                             termcode="Sad")

    dt_happy_id = "definedterm-happy-id"
    dt_sad_id = "definedterm-sad-id"
    print("DefinedTerms")
    if print_queries:
        print(dt_happy)
        print(dt_sad)
    if submit_queries:
        dt_happy_id = send_query_and_get_id(dt_happy, "CreateDefinedTerm")
        dt_sad_id = send_query_and_get_id(dt_sad, "CreateDefinedTerm")

    dts_join_happy = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                      defined_term=dt_happy_id)
    dts_join_sad = definedterm.defined_term_add_to_defined_term_set(defined_term_set=dts_id,
                                                                    defined_term=dt_sad_id)

    print("Join DefinedTerm to DefinedTermSet")
    if print_queries:
        print(dts_join_happy)
        print(dts_join_sad)
    if submit_queries:
        send_query_and_get_id(dts_join_happy)
        send_query_and_get_id(dts_join_sad)

    return {"dts_id": dts_id,
            "dt_happy_id": dt_happy_id,
            "dt_sad_id": dt_sad_id}


def motivation_collection(print_queries: bool, submit_queries: bool):
    """A collection of annotation motivations that could be applied to a single item"""
    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"

    dts = definedterm.create_defined_term_set(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION],
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/conductor-baton.png",
                                              name="Performance instructions")

    dt_upbow = definedterm.create_defined_term(creator=admin_vcard,
                                               additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                               annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                               broader_schema=annotation.AnnotationSchemaMotivation.commenting,
                                               image="https://alastair.trompa-solid.upf.edu/annotation-images/upbow.png",
                                               termcode="Upbow")

    dt_downbow = definedterm.create_defined_term(creator=admin_vcard,
                                                 additionaltype=[
                                                     annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                     annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                                 broader_schema=annotation.AnnotationSchemaMotivation.commenting,
                                                 image="https://alastair.trompa-solid.upf.edu/annotation-images/downbow.png",
                                                 termcode="Downbow")

    dt_arco = definedterm.create_defined_term(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                              annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                              broader_schema=annotation.AnnotationSchemaMotivation.commenting,
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/arco.png",
                                              termcode="Arco")

    dt_slur = definedterm.create_defined_term(creator=admin_vcard,
                                              additionaltype=[annotation.ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT,
                                                              annotation.OA_ANNOTATION_MOTIVATION_TYPE],
                                              broader_schema=annotation.AnnotationSchemaMotivation.commenting,
                                              image="https://alastair.trompa-solid.upf.edu/annotation-images/slur.png",
                                              termcode="Slur")

    print("DefinedTerm - Motivation Collection")
    dts_id = "dts-id"
    dt_upbow_id = "dt-upbow-id"
    dt_downbow_id = "dt-downbow-id"
    dt_arco_id = "dt-arco-id"
    dt_slur_id = "dt-slur-id"
    if print_queries:
        print(dts)
        print(dt_upbow)
        print(dt_downbow)
        print(dt_arco)
        print(dt_slur)

    if submit_queries:
        dts_id = send_query_and_get_id(dts, "CreateDefinedTermSet")
        dt_upbow_id = send_query_and_get_id(dt_upbow, "CreateDefinedTerm")
        dt_downbow_id = send_query_and_get_id(dt_downbow, "CreateDefinedTerm")
        dt_arco_id = send_query_and_get_id(dt_arco, "CreateDefinedTerm")
        dt_slur_id = send_query_and_get_id(dt_slur, "CreateDefinedTerm")

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

    return {
        "dts_id": dts_id,
        "dt_upbow_id": dt_upbow_id,
        "dt_downbow_id": dt_downbow_id,
        "dt_slur_id": dt_slur_id,
        "dt_arco_id": dt_arco_id,
    }


def main(print_queries: bool, submit_queries: bool):

    fixed_vocabulary(print_queries, submit_queries)
    motivation_collection(print_queries, submit_queries)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
