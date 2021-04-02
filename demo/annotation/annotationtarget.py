# Make annotations with different types of targets
from demo.annotation import audio_file_pierri_etude
from trompace.mutations import annotation


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    # An annotation where the target is a specific field of an existing node.
    # For simplicity we don't have a body
    audio_id = audio_file_pierri_etude(print_queries, submit_queries)

    # The annotation target. We're annotating the URL that is at the `source` field of the above audio object
    target = annotation.create_annotation_ce_target(
        creator=user_vcard,
        field="source",  # we want to annotate the URL that is at the 'source' field of the AudioObject node
        fragment="t=10,20"  # only annotate 10 seconds of audio from 10sec - 20sec
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

    print("Annotation - link to target")
    if print_queries:
        print(annotation_target_join)
    if submit_queries:
        send_query_and_get_id(annotation_target_join)

    # An annotation where the target is an actual node in the CE (not the item at a field)
    # The annotation target. We're annotating the URL that is at the `source` field of the above audio object
    ann_target = annotation.create_annotation_ce_target(
        creator=user_vcard  # no field or fragment set
    )

    ann_target_id = "ce-target-id"
    print("AnnotationCETarget - no field")
    if print_queries:
        print(ann_target)
    if submit_queries:
        ann_target_id = send_query_and_get_id(ann_target, "CreateAnnotationCETarget")

    print("Join AnnotationCETarget-Target")
    # Here, the target field of the AnnotationCETarget object is the previous annotation object
    ann_target_join = annotation.merge_annotation_target_target(ann_target_id, ann_id)
    if print_queries:
        print(ann_target_join)
    if submit_queries:
        send_query_and_get_id(ann_target_join)

    # A new annotation, this one is an annotation about the _other_ annotation
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

    print("Annotation - link to target")
    if print_queries:
        print(annotation_target_join)
    if submit_queries:
        send_query_and_get_id(annotation_target_join)

    # Annotation target 3: external target
    # This style of annotation doesn't need an AnnotationCETarget object, because the target isn't in the CE
    ann = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.tagging,
        target_url="https://example.com/audio.mp3"
    )

    print("Annotation - external URL target")
    if print_queries:
        print(ann)
    if submit_queries:
        send_query_and_get_id(ann, "CreateAnnotation")


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
