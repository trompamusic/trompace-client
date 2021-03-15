# Perform an annotation by ranking an item
from demo.annotation import audio_file_liebestraum
from demo.definedterm import fixed_vocabulary
from trompace.mutations import annotation, rating


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"


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
        motivation=annotation.AnnotationSchemaMotivation.assessing
    )

    ann_id = "annotation-id"
    print("Annotation")
    if print_queries:
        print(ann)
    if submit_queries:
        ann_id = send_query_and_get_id(ann, "CreateAnnotation")

    # Make a rating
    user_rating = rating.create_rating(
        creator=user_vcard,
        bestrating=10,
        worstrating=1,
        ratingvalue=8
    )
    print("Rating")
    rating_id = "rating-id"
    if print_queries:
        print(user_rating)
    if submit_queries:
        rating_id = send_query_and_get_id(user_rating, "CreateRating")

    # Join the annotation with the AnnotationCETarget
    annotation_target_join = annotation.merge_annotation_targetnode(ann_id, target_id)
    # Join the annotation with the Body. In this case, the body is the Rating that we just made
    annotation_body_join = annotation.merge_annotation_bodynode(ann_id, rating_id)

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
