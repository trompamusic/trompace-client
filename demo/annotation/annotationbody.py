# Make annotations with different types of bodies

from trompace.mutations import annotation


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    # An annotation requires a target, but we omit it from this demo.

    # An annotation whose body is an external URL
    ann_url = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.describing,
        body_url=["https://trompamusic.eu/something", "http://example.com/somethingelse"]
    )

    ann_url_id = "annotation-id"
    print("Annotation - url body")
    if print_queries:
        print(ann_url)
    if submit_queries:
        ann_url_id = send_query_and_get_id(ann_url, "CreateAnnotation")

    # An annotation whose body is some text
    body = annotation.create_annotation_textual_body(
        creator=user_vcard,
        value="if the <i>format</i> field is set correctly, the value of the <b>textualbody</b> can even be html!",
        format_="text/html",
        language="en"
    )

    body_id = "text-body-id"
    print("AnnotationTextualBody")
    if print_queries:
        print(body)
    if submit_queries:
        body_id = send_query_and_get_id(body, "CreateAnnotationTextualBody")

    ann_text = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.commenting
    )

    ann_text_id = "annotation-id"
    print("Annotation - Textual body")
    if print_queries:
        print(ann_text)
    if submit_queries:
        ann_text_id = send_query_and_get_id(ann_text, "CreateAnnotation")

    # Join the annotation with the and the Body
    annotation_text_body_join = annotation.merge_annotation_bodytext(ann_text_id, body_id)

    print("Annotation - link to body")
    if print_queries:
        print(annotation_text_body_join)
    if submit_queries:
        send_query_and_get_id(annotation_text_body_join)

    # An annotation whose body is another node in the CE. In this case, the previous annotation
    ann_node = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.linking
    )
    ann_node_id = "annotation-id"
    print("Annotation - node body")
    if print_queries:
        print(ann_node)
    if submit_queries:
        ann_node_id = send_query_and_get_id(ann_node, "CreateAnnotation")

    # Join the annotation with the and the Body
    annotation_node_body_join = annotation.merge_annotation_bodynode(ann_node_id, ann_text_id)

    print("Annotation - link to body")
    if print_queries:
        print(annotation_node_body_join)
    if submit_queries:
        send_query_and_get_id(annotation_node_body_join)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
