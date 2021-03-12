# A basic annotation of an object which has a free-form text tag

from trompace.mutations import annotation, audioobject


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    # A file that we're annotating
    audio = audioobject.mutation_create_audioobject(
        name="Liebestraum No. 3",
        title="Liebestraum No. 3",
        creator="https://github.com/trompamusic/audio-annotator",
        contributor="https://mtg.upf.edu/",
        source="https://trompa-mtg.upf.edu/data/anno-component-test/SMC_005.wav",
        format_="audio/wav",
        encodingformat="audio/wav",
        contenturl="https://trompa-mtg.upf.edu/data/anno-component-test/SMC_005.wav"
    )

    audio_id = "audio-node-id"
    print("AudioObject")
    if print_queries:
        print(audio)
    if submit_queries:
        audio_id = send_query_and_get_id(audio, "CreateAudioObject")

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

    # The annotation target. We're annotating the URL that is at the `source` field of the above audio object
    target = annotation.create_annotation_ce_target(
        creator=user_vcard,
        field="source",  # we want to annotate the URL that is at the 'source' field of the AudioObject node
        # Optionally, set the 'fragment' parameter to annotate a time range in the file
    )

    target_id = "text-body-id"
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

    # Join the annotation with the AnnotationCETarget, and the Body
    annotation_target_join = annotation.merge_annotation_targetnode(ann_id, target_id)
    annotation_body_join = annotation.merge_annotation_bodytext(ann_id, body_id)

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
