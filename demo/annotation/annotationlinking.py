# Link together more than one annotation into a "meta" annotation.
# For example, a task may ask for a person to annotate three different characteristics
# of an audio file, but all of those characteristics should be considered as a single annotation.
# We create another annotation, with a custom motivation with skos:broader of oa:Linking
# and make all of the other annotations part of the body of this wrapper annotation
from demo.annotation import audio_file_liebestraum
from demo.definedterm import fixed_vocabulary
from trompace.mutations import annotation


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    vocabulary_ids = fixed_vocabulary(print_queries, submit_queries)
    audio_id = audio_file_liebestraum(print_queries, submit_queries)

    # The annotation target. We're annotating the URL that is at the `source` field of the above audio object
    target = annotation.create_annotation_ce_target(
        creator=user_vcard,
        field="source",
    )
    target_id = "ce-target-id"
    print("AnnotationCETarget")
    if print_queries:
        print(target)
    if submit_queries:
        target_id = send_query_and_get_id(target, "CreateAnnotationCETarget")

    print("Join AnnotationCETarget-Target")
    target_join = annotation.merge_annotation_target_target(target_id, audio_id)
    if print_queries:
        print(target_join)
    if submit_queries:
        send_query_and_get_id(target_join)

    # Annotation 1 - "Happy" tag
    ann1 = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.tagging
    )

    ann1_id = "annotation1-id"
    print("Annotation1")
    if print_queries:
        print(ann1)
    if submit_queries:
        ann1_id = send_query_and_get_id(ann1, "CreateAnnotation")

    # Join the annotation with the AnnotationCETarget
    annotation_target_join = annotation.merge_annotation_targetnode(ann1_id, target_id)
    # Join the annotation with the Body. In this case, the body is the "Happy" DefinedTerm
    # from the DefinedTermSet that we provided
    body_id = vocabulary_ids["dt_happy_id"]
    annotation_body_join = annotation.merge_annotation_bodynode(ann1_id, body_id)

    print("Annotation1 - link to target and body")
    if print_queries:
        print(annotation_target_join)
        print(annotation_body_join)
    if submit_queries:
        send_query_and_get_id(annotation_target_join)
        send_query_and_get_id(annotation_body_join)

    # Annotation 2 - freeform tag
    ann2 = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.tagging
    )

    ann2_id = "annotation2-id"
    print("Annotation2")
    if print_queries:
        print(ann2)
    if submit_queries:
        ann2_id = send_query_and_get_id(ann2, "CreateAnnotation")

    # The annotation text body
    body = annotation.create_annotation_textual_body(
        creator=user_vcard,
        value="favourite-song",  # the tag
        format_="text/plain",
        language="en"
    )
    body_id = "text-body-id"
    print("AnnotationTextualBody")
    if print_queries:
        print(body)
    if submit_queries:
        body_id = send_query_and_get_id(body, "CreateAnnotationTextualBody")

    # Join the annotation with the AnnotationCETarget and body. Note that we can use the same
    # target as we know that all annotations are of the same thing
    annotation_target_join = annotation.merge_annotation_targetnode(ann2_id, target_id)
    annotation_body_join = annotation.merge_annotation_bodynode(ann2_id, body_id)

    print("Annotation1 - link to target and body")
    if print_queries:
        print(annotation_target_join)
        print(annotation_body_join)
    if submit_queries:
        send_query_and_get_id(annotation_target_join)
        send_query_and_get_id(annotation_body_join)

    # Linking Annotation, this joins together the two previous annotations into a third one
    # Make a custom motivation which describes what this linking represents
    custom_motivation = annotation.create_annotation_motivation(
        creator=user_vcard, title="Music scholars feedback grouping",
        description="This motivation groups together 4 different annotations into a single meta-annotation"
                    "which represents the full description of a recording by a user",
        broader_schema=annotation.AnnotationSchemaMotivation.linking)
    custom_motivation_id = "custom-motivation-id"
    print("Linking Annotation - create Motivation")
    if print_queries:
        print(custom_motivation)
    if submit_queries:
        custom_motivation_id = send_query_and_get_id(custom_motivation, "CreateAnnotationCEMotivation")

    ann_link = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.linking
    )

    ann_link_id = "annotation2-id"
    print("Linking Annotation")
    if print_queries:
        print(ann2)
    if submit_queries:
        ann_link_id = send_query_and_get_id(ann_link, "CreateAnnotation")

    # Add the custom motivation as the motivation of the linking annotation
    link_annotation_target_join = annotation.merge_annotation_targetnode(ann_link_id, target_id)
    link_annotation_motivation_join = annotation.merge_annotation_cemotivation(ann_link_id, custom_motivation_id)

    # Add the two prior annotations as the body of the linking annotation
    link_annotation_body1_join = annotation.merge_annotation_bodynode(ann_link_id, ann1_id)
    link_annotation_body2_join = annotation.merge_annotation_bodynode(ann_link_id, ann2_id)

    print("Linking Annotation - join with target, motivation, and bodies")
    if print_queries:
        print(link_annotation_target_join)
        print(link_annotation_motivation_join)
        print(link_annotation_body1_join)
        print(link_annotation_body2_join)
    if submit_queries:
        send_query_and_get_id(link_annotation_target_join)
        send_query_and_get_id(link_annotation_motivation_join)
        send_query_and_get_id(link_annotation_body1_join)
        send_query_and_get_id(link_annotation_body2_join)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)

