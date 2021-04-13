# An annotation session is a collection of annotations of one or more entities that are logically grouped together
from demo.annotation import audio_file_liebestraum, audio_file_pierri_etude
from trompace.mutations import annotation, itemlist


def main(print_queries: bool, submit_queries: bool):
    user_vcard = "https://testuser.trompa-solid.upf.edu/profile/card#me"

    audio1_id = audio_file_liebestraum(print_queries, submit_queries)
    audio2_id = audio_file_pierri_etude(print_queries, submit_queries)

    session = annotation.create_annotation_session(creator=user_vcard, name="Some session")

    print("Annotation session")
    session_id = "session-id"
    if print_queries:
        print(session)
    if submit_queries:
        session_id = send_query_and_get_id(session, "CreateItemList")

    # We have three annotations in this session. One of audio1_id, and two of audio2_id at different points in time
    # For simplicity we don't set any body

    target1 = annotation.create_annotation_ce_target(creator=user_vcard, field="contenturl", fragment="#t=8")
    annotation1 = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.highlighting)

    target2 = annotation.create_annotation_ce_target(creator=user_vcard, field="contenturl")
    annotation2 = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.highlighting)

    target3 = annotation.create_annotation_ce_target(creator=user_vcard, field="contenturl", fragment="#t=15")
    annotation3 = annotation.create_annotation(
        creator=user_vcard,
        motivation=annotation.AnnotationSchemaMotivation.highlighting)

    print("Annotation - Create CE Target and Annotation objects")
    target1_id = "target1-id"
    target2_id = "target2-id"
    target3_id = "target3-id"
    annotation1_id = "annotation1-id"
    annotation2_id = "annotation2-id"
    annotation3_id = "annotation3-id"
    if print_queries:
        print(target1)
        print(target2)
        print(target3)
        print(annotation1)
        print(annotation2)
        print(annotation3)
    if submit_queries:
        target1_id = send_query_and_get_id(target1, "CreateAnnotationCETarget")
        target2_id = send_query_and_get_id(target2, "CreateAnnotationCETarget")
        target3_id = send_query_and_get_id(target3, "CreateAnnotationCETarget")
        annotation1_id = send_query_and_get_id(annotation1, "CreateAnnotation")
        annotation2_id = send_query_and_get_id(annotation2, "CreateAnnotation")
        annotation3_id = send_query_and_get_id(annotation3, "CreateAnnotation")

    # Linking audio to AnnotationCETarget and AnnotationCETarget to Annotation
    target1_audio = annotation.merge_annotation_target_target(target1_id, audio1_id)
    target2_audio = annotation.merge_annotation_target_target(target2_id, audio2_id)
    target3_audio = annotation.merge_annotation_target_target(target3_id, audio2_id)
    annotation1_target = annotation.merge_annotation_targetnode(annotation1_id, target1_id)
    annotation2_target = annotation.merge_annotation_targetnode(annotation2_id, target2_id)
    annotation3_target = annotation.merge_annotation_targetnode(annotation3_id, target3_id)
    print("Annotation - join audio to target and target to annotation")
    if print_queries:
        print(target1_audio)
        print(target2_audio)
        print(target3_audio)
        print(annotation1_target)
        print(annotation2_target)
        print(annotation3_target)
    if submit_queries:
        send_query_and_get_id(target1_audio)
        send_query_and_get_id(target2_audio)
        send_query_and_get_id(target3_audio)
        send_query_and_get_id(annotation1_target)
        send_query_and_get_id(annotation2_target)
        send_query_and_get_id(annotation3_target)

    # Make a container ListItem to add to the Session
    annotation1_item = annotation.create_annotation_session_element(creator=user_vcard)
    annotation2_item = annotation.create_annotation_session_element(creator=user_vcard)
    annotation3_item = annotation.create_annotation_session_element(creator=user_vcard)
    print("Annotation - create ListItem")
    annotation1_item_id = "annotation1-listitem-id"
    annotation2_item_id = "annotation2-listitem-id"
    annotation3_item_id = "annotation3-listitem-id"
    if print_queries:
        print(annotation1_item)
        print(annotation2_item)
        print(annotation3_item)
    if submit_queries:
        annotation1_item_id = send_query_and_get_id(annotation1_item, "CreateListItem")
        annotation2_item_id = send_query_and_get_id(annotation2_item, "CreateListItem")
        annotation3_item_id = send_query_and_get_id(annotation3_item, "CreateListItem")

    # Linking Annotations to ListItems, and add ListItems to the session
    item1_annotation = itemlist.mutation_add_listitem_item(annotation1_item_id, annotation1_id)
    item2_annotation = itemlist.mutation_add_listitem_item(annotation2_item_id, annotation2_id)
    item3_annotation = itemlist.mutation_add_listitem_item(annotation3_item_id, annotation3_id)
    session_item1 = itemlist.mutation_add_itemlist_itemlist_element(session_id, annotation1_item_id)
    session_item2 = itemlist.mutation_add_itemlist_itemlist_element(session_id, annotation2_item_id)
    session_item3 = itemlist.mutation_add_itemlist_itemlist_element(session_id, annotation3_item_id)
    print("Annotation - join annotation to ListItem and and add ListItem to session")
    if print_queries:
        print(item1_annotation)
        print(item2_annotation)
        print(item3_annotation)
        print(session_item1)
        print(session_item2)
        print(session_item3)
    if submit_queries:
        send_query_and_get_id(item1_annotation)
        send_query_and_get_id(item2_annotation)
        send_query_and_get_id(item3_annotation)
        send_query_and_get_id(session_item1)
        send_query_and_get_id(session_item2)
        send_query_and_get_id(session_item3)

    # TODO: Technically no reason that a session could have annotations by multiple people in it


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
