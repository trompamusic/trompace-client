# Perform annotations using a fixed vocabulary of terms
from demo.annotation import audio_file_liebestraum
from demo.definedterm import fixed_vocabulary
from trompace.mutations import annotation


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    # Our vocabulary
    vocabulary_ids = fixed_vocabulary(print_queries, submit_queries)

    audio_id = audio_file_liebestraum(print_queries, submit_queries)

    # The annotation target. We're annotating the URL that is at the `source` field of the above audio object
    target = annotation.create_annotation_ce_target(
        creator=user_vcard,
        field="source",  # we want to annotate the URL that is at the 'source' field of the AudioObject node
        # Optionally, set the 'fragment' parameter to annotate a time range in the file
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

    # The annotation
    ann = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.tagging
    )

    ann_id = "annotation-id"
    print("Annotation")
    if print_queries:
        print(ann)
    if submit_queries:
        ann_id = send_query_and_get_id(ann, "CreateAnnotation")

    # Join the annotation with the AnnotationCETarget
    annotation_target_join = annotation.merge_annotation_targetnode(ann_id, target_id)
    # Join the annotation with the Body. In this case, the body is the "Happy" DefinedTerm
    # from the DefinedTermSet that we provided
    body_id = vocabulary_ids["dt_happy_id"]
    annotation_body_join = annotation.merge_annotation_bodynode(ann_id, body_id)

    print("Annotation - link to target and body")
    if print_queries:
        print(annotation_target_join)
        print(annotation_body_join)
    if submit_queries:
        send_query_and_get_id(annotation_target_join)
        send_query_and_get_id(annotation_body_join)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
