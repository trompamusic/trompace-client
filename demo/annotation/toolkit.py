# An annotation toolkit is a collection of annotation types that can be applied to annotations
# This could include Rating Definitions or DefinedTermSets
from demo.definedterm import fixed_vocabulary
from trompace.mutations import definedterm, annotation, itemlist, rating


def main(print_queries: bool, submit_queries: bool):
    admin_vcard = "https://alastair.trompa-solid.upf.edu/profile/card#me"

    # A vocabulary, this is two tags "Happy and "Sad"
    vocabulary_ids = fixed_vocabulary(print_queries, submit_queries)
    dts_id = vocabulary_ids["dts_id"]

    # A 'template' of the rating that we're using. This can be used to show a graphical widget,
    # and also as a common template that can be used to join together multiple annotations
    rating_definition = rating.create_rating_definition(creator=admin_vcard, worstrating=0, bestrating=10)
    rating_definition_id = "rating-definition-id"
    print("Rating (definition)")
    if print_queries:
        print(rating_definition)
    if submit_queries:
        rating_definition_id = send_query_and_get_id(rating_definition, "CreateRating")

    # A plain textbox that can be used to make an annotation with motivation oa:commenting
    commenting_motivation = "http://www.w3.org/ns/oa#commenting"

    # Make our toolkit - this is an itemlist with a special additionalType
    # TODO: Currently we're making queries manually. Should have related methods in trompace.client
    #  to wrap up the complexity in making multiple queries

    toolkit = annotation.create_annotation_toolkit(
        creator=admin_vcard, name="Creatve feedback annotation",
        description="A set of annotations that I like to use when giving feedback to people")

    toolkit_item_vocabulary = annotation.create_annotation_toolkit_element(creator=admin_vcard)

    toolkit_item_rating = annotation.create_annotation_toolkit_element(creator=admin_vcard)

    toolkit_item_motivation = annotation.create_annotation_toolkit_element(
        creator=admin_vcard,
        itemurl=commenting_motivation
    )

    itemlist_id = "itemlist-id"
    listitem_vocab_id = "listitem-vocab-id"
    listitem_rating_id = "listitem-rating-id"
    listitem_motivation_id = "listitem-motivation-id"
    print("Toolkit - ItemList and ListItems")
    if print_queries:
        print(toolkit)
        print(toolkit_item_vocabulary)
        print(toolkit_item_rating)
        print(toolkit_item_motivation)
    if submit_queries:
        itemlist_id = send_query_and_get_id(toolkit, "CreateItemList")
        listitem_vocab_id = send_query_and_get_id(toolkit_item_vocabulary, "CreateListItem")
        listitem_rating_id = send_query_and_get_id(toolkit_item_rating, "CreateListItem")
        listitem_motivation_id = send_query_and_get_id(toolkit_item_motivation, "CreateListItem")

    # Join toolkit items with the thing that they point to
    join_vocab = itemlist.mutation_add_listitem_item(listitem_vocab_id, dts_id)
    join_rating = itemlist.mutation_add_listitem_item(listitem_rating_id, rating_definition_id)
    print("Toolkit - join ListItems with item")
    if print_queries:
        print(join_vocab)
        print(join_rating)
    if submit_queries:
        send_query_and_get_id(join_vocab)
        send_query_and_get_id(join_rating)

    # Join the toolkit items to the toolkit
    add_vocab = itemlist.mutation_add_itemlist_itemlist_element(itemlist_id, listitem_vocab_id)
    add_rating = itemlist.mutation_add_itemlist_itemlist_element(itemlist_id, listitem_rating_id)
    add_motivation = itemlist.mutation_add_itemlist_itemlist_element(itemlist_id, listitem_motivation_id)

    print("Toolkit - add ListItems to ItemList")
    if print_queries:
        print(add_vocab)
        print(add_rating)
        print(add_motivation)
    if submit_queries:
        send_query_and_get_id(add_vocab)
        send_query_and_get_id(add_rating)
        send_query_and_get_id(add_motivation)


if __name__ == '__main__':
    from demo import args, send_query_and_get_id

    main(args.args.print, args.args.submit)
