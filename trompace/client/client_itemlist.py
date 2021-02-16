
from trompace.config import config
from trompace.connection import submit_query
from trompace.mutations.itemlist import *
from trompace.constants import ItemListOrderType



def create_itemlist_node(contributor = contributor, name = name, 
                         description = description, ordered = ordered):
    """
    """
    itemlistorder = ItemListOrderType.ItemListUnordered
    if ordered:
        itemlistorder = ItemListOrderType.ItemListOrderAscending

    mutation = mutation_create_itemlist(contributor = contributor,
                                        name = name,
                                        itemlistorder = itemlistorder,
                                        description = description)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("CreateItemList")

    if result:
        itemlist_id = resp["data"]["CreateItemList"]["identifier"]
    else:
        # Raise Error
        pass

    return itemlist_id


def create_listitem_node(contributor = contributor, name = name, 
                         description = description, position = position):
    """
    """
    mutation = mutation_create_listitem(contributor = contributor, 
                                        name = name,
                                        description = value, 
                                        position = position)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("CreateListItem")

    if result:
        element_id = resp["data"]["CreateItemList"]["identifier"]
    else:
        # Raise Error
        pass

    return element_id


def merge_itemlist_itemlistelement_nodes(itemlist_id = itemlist_id, 
                                         element_id = element_id):
    """
    """
    mutation = mutation_add_itemlist_itemlist_element(itemlist_id = itemlist_id, 
                                                      element_id = element_id)
    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeItemListItemListElement")

    if not result:
        # Raise Error
        pass


def merge_listitem_nextitem_nodes(listitem_id = previousItemId, 
                                  nextitem_id = element_id):
    """
    """
    mutation = mutation_add_listitem_nextitem(listitem_id = previousItemId, 
                                              nextitem_id = element_id)
    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemNextItem")

    if not result:
        # Raise Error
        pass


def merge_listitem_item_nodes(listitem_id = listitem_id, item_id = item_id):
    """
    """
    mutation =  mutation_add_listitem_item(listitem_id = listitem_id, 
                                           item_id = item_id)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemItem")

    if not result:
        # Raise Error
        pass


def create_itemlist(contributor: str, name: str, description: str, 
                    node_ids: list = None, values: list = None, ordered: bool):
    """
    Main function
    """
    if values:
        listitems = values
    elif node_ids:
        listitems = node_ids

    itemlist_id = create_itemlist_node(contributor = contributor, name = name, 
                                       description = description, ordered = ordered):

    position = 0
    previous_item_id = None
    for item in listitems:
        if values:
            description = item

        listitem_id = create_listitem_node(contributor = contributor, name = name, 
                                           description = description, position = position):

        merge_itemlist_itemlistelement_nodes(itemlist_id = itemlist_id, element_id = listitem_id)

        if node_ids:
            merge_listitem_item_nodes(listitem_id = listitem_id, item_id = item)

        if previous_item_id:
            merge_listitem_nextitem_nodes(listitem_id = previous_item_id, nextitem_id = listitem_id)

        previous_item_id = listitem_id
        position += 1
