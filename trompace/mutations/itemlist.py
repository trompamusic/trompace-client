from trompace import (docstring_interpolate, filter_none_args,
                      StringConstant, check_required_args)
from trompace.constants import ItemListOrderType
from trompace.mutations.templates import format_mutation, format_link_mutation
import trompace.exceptions

ITEMLIST_ARGS_DOCS = """name: The name of the ItemList object.
        contributor: A person, an organization, or a service responsible
        for contributing the ItemList to the web resource.
        This can be either a name or a base URL.
        itemlistorder: The type of ordering for the list
        (ascending, descending, unordered, ordered)
        description: The description of the ItemList object
        """


@docstring_interpolate("itemlist_args", ITEMLIST_ARGS_DOCS)
def mutation_create_itemlist(contributor: str, name: str = None,
                             itemlistorder: ItemListOrderType =
                             ItemListOrderType.ItemListUnordered,
                             description: str = None):
    """Returns a mutation for creating an ItemList object.

    Arguments:
        {itemlist_args}

    Returns:
        The string for the mutation for creating the ItemList.
    """
    if not isinstance(itemlistorder, ItemListOrderType):
        raise trompace.exceptions.InvalidItemListOrderTypeException(itemlistorder)

    args = {
        "contributor": contributor,
        "name": name,
        "description": description,
        "itemListOrder": StringConstant(itemlistorder)
    }

    args = filter_none_args(args)

    return format_mutation("CreateItemList", args)


@docstring_interpolate("itemlist_args", ITEMLIST_ARGS_DOCS)
def mutation_update_itemlist(identifier: str, contributor: str,
                             name: str = None,
                             itemlistorder: ItemListOrderType =
                             ItemListOrderType.ItemListUnordered,
                             description: str = None):
    """Returns a mutation for updating an ItemList object.

    Arguments:
        identifier: The identifier of the ItemList in the CE to be updated.
        {itemlist_args}

    Returns:
        The string for the mutation for updating the ItemList.
    """
    if not isinstance(itemlistorder, ItemListOrderType):
        raise trompace.exceptions.InvalidItemListOrderTypeException(itemlistorder)

    args = {
        "identifier": identifier,
        "contributor": contributor,
        "name": name,
        "description": description,
        "itemListOrder": StringConstant(itemlistorder)
    }

    args = filter_none_args(args)

    return format_mutation("UpdateItemList", args)


def mutation_delete_itemlist(identifier: str):
    """Returns a mutation for deleting an ItemList object based
    on the identifier.

    Arguments:
        identifier: The unique identifier of the ItemList object.

    Returns:
        The string for the mutation for deleting the ItemList object
        based on the identifier.
    """

    return format_mutation("DeleteItemList", {"identifier": identifier})


LISTITEM_ARGS_DOCS = """name: The name of the ItemList object.
        contributor: A person, an organization, or a service responsible
        for contributing the ItemList to the web resource.
        This can be either a name or a base URL.
        description: The description of the ItemList object
        position: the position of the ItemList
        """


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_create_listitem(contributor: str, name: str = None,
                             description: str = None, position: int = 0):
    """Returns a mutation for creating a ListItem object.

    Arguments:
        {listitem_args}

    Returns:
        The string for the mutation for creating the ListItem.
    """
    args = {
        "contributor": contributor,
        "name": name,
        "description": description,
        "position": position,
    }

    args = filter_none_args(args)

    return format_mutation("CreateListItem", args)


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_update_listitem(identifier, contributor: str, name: str = None,
                             description: str = None, position: int = 0):
    """Returns a mutation for updating a ListItem object.

    Arguments:
        identifier: The identifier of the ListItem in the CE to be
        updated.
        {listitem_args}

    Returns:
        The string for the mutation for updating the ListItem.
    """
    args = {
        "identifier": identifier,
        "contributor": contributor,
        "name": name,
        "description": description,
        "position": position,
    }

    args = filter_none_args(args)

    return format_mutation("UpdateListItem", args)


def mutation_delete_listitem(identifier: str):
    """Returns a mutation for deleting a ListItem object based on the
    identifier.

    Arguments:
        identifier: The unique identifier of the ListItem object.

    Returns:
        The string for the mutation for deleting the ListItem object based
        on the identifier.
    """
    return format_mutation("DeleteListItem", {"identifier": identifier})


def mutation_add_listitem_nextitem(listitem_id: str, nextitem_id: str):
    """Returns a mutation for adding a NextItem to a ListItem object
    based on the identifier.

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        nextitem_id: The unique identifier of the NextItem object.

    Returns:
        The string for the mutation for adding a NextItem to a ListItem object
    based on the identifier.
    """
    check_required_args(listitem_id=listitem_id, nextitem_id=nextitem_id)
    return format_link_mutation("MergeListItemNextItem", listitem_id,
                                nextitem_id)


def mutation_remove_listitem_nextitem(listitem_id: str, nextitem_id: str):
    """Returns a mutation for removing a NextItem to a ListItem object
    based on the identifier.

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        nextitem_id: The unique identifier of the NextItem object.

    Returns:
        The string for the mutation for removing a NextItem to a ListItem
    object based on the identifier.
    """
    check_required_args(listitem_id=listitem_id, nextitem_id=nextitem_id)
    return format_link_mutation("RemoveListItemNextItem", listitem_id,
                                nextitem_id)


def mutation_add_listitem_item(listitem_id: str, item_id: str):
    """Returns a mutation for adding a Item to a ListItem object
    based on the identifier.

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        item_id: The unique identifier of the Item object.

    Returns:
        The string for the mutation for adding a Item to a ListItem object
    based on the identifier.
    """
    check_required_args(listitem_id=listitem_id, item_id=item_id)
    return format_link_mutation("MergeListItemItem", listitem_id, item_id)


def mutation_remove_listitem_item(listitem_id: str, item_id: str):
    """Returns a mutation for removing a Item to a ListItem object
    based on the identifier.

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        item_id: The unique identifier of the Item object.

    Returns:
        The string for the mutation for removing a Item  to a ListItem
    object based on the identifier.
    """
    check_required_args(listitem_id=listitem_id, item_id=item_id)
    return format_link_mutation("RemoveListItemItem", listitem_id, item_id)


def mutation_add_itemlist_itemlist_element(itemlist_id: str, listitem_id: str):
    """Returns a mutation for adding an ListItem in an ItemList object based
    on the identifier.

    Arguments:
        itemlist_id: The unique identifier of the ItemList object.
        listitem_id: The unique identifier of the ListItem object.

    Returns:
        The string for the mutation for adding an ListItem in an ItemList object
        based on the identifier,
    """
    check_required_args(itemlist_id=itemlist_id, listitem_id=listitem_id)
    return format_link_mutation("MergeItemListItemListElement", itemlist_id,
                                listitem_id)


def mutation_remove_itemlist_itemlist_element(itemlist_id: str,
                                              listitem_id: str):
    """Returns a mutation for removing an ListItem in an ItemList object
    based on the identifier.

    Arguments:
        itemlist_id: The unique identifier of the ItemList object.
        listitem_id: The unique identifier of the ListItem object.

    Returns:
        The string for the mutation for removing an ListItem from an ItemList
        object based on the identifier.
    """
    check_required_args(itemlist_id=itemlist_id, listitem_id=listitem_id)
    return format_link_mutation("RemoveItemListItemListElement", itemlist_id,
                                listitem_id)
