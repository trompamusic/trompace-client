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
                             ItemListOrderType.unordered,
                             description: str = None):
    """Returns a mutation for creating an itemlist object.

    Arguments:
        {itemlist_args}

    Returns:
        The string for the mutation for creating the itemlist.
    """
    if not isinstance(itemlistorder, ItemListOrderType):
        raise trompace.exceptions.InvalidItemListOrderTyException(
                                                            itemlistorder)

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
                             ItemListOrderType.unordered,
                             description: str = None):
    """Returns a mutation for updating an itemlist object.

    Arguments:
        identifier: The identifier of the itemlist in the CE to be updated.
        {itemlist_args}

    Returns:
        The string for the mutation for updating the itemlist.
    """
    if not isinstance(itemlistorder, ItemListOrderType):
        raise trompace.exceptions.InvalidItemListOrderTyException(
                                                                itemlistorder)

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
    """Returns a mutation for deleting an itemlist object based
    on the identifier.

    Arguments:
        identifier: The unique identifier of the itemlist object.

    Returns:
        The string for the mutation for deleting the itemlist object
        based on the identifier.
    """

    return format_mutation("DeleteItemList", {"identifier": identifier})


LISTITEM_ARGS_DOCS = """name: The name of the ItemList object.
        contributor: A person, an organization, or a service responsible
        for contributing the ItemList to the web resource.
        This can be either a name or a base URL.
        description: The description of the ItemList object
        """


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_create_listitem(contributor: str, name: str = None,
                             description: str = None):
    """Returns a mutation for creating a listitem object.

    Arguments:
        {listitem_args}

    Returns:
        The string for the mutation for creating the itemlist.
    """
    args = {
        "contributor": contributor,
        "name": name,
        "description": description,
    }

    args = filter_none_args(args)

    return format_mutation("CreateListItem", args)


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_update_listitem(identifier, contributor: str, name: str = None,
                             description: str = None):
    """Returns a mutation for updating a listitem_args object.

    Arguments:
        identifier: The identifier of the listitem_args in the CE to be
        updated.
        {listitem_args}

    Returns:
        The string for the mutation for updating the listitem_args.
    """
    args = {
        "identifier": identifier,
        "contributor": contributor,
        "name": name,
        "description": description,
    }

    args = filter_none_args(args)

    return format_mutation("UpdateListItem", args)


def mutation_delete_listitem(identifier: str):
    """Returns a mutation for deleting a listitem object based on the
    identifier.

    Arguments:
        identifier: The unique identifier of the listitem object.

    Returns:
        The string for the mutation for deleting the listitem object based
        on the identifier.
    """
    return format_mutation("DeleteListItem", {"identifier": identifier})


def mutation_add_itemlist_itemlist_element(identifier_1: str,
                                           identifier_2: str):
    """Returns a mutation for adding an item in an itemlist object based
    on the identifier.

    Arguments:
        identifier_1: The unique identifier of the itemlist object.
        identifier_2: The unique identifier of the listitem object.

    Returns:
        The string for the mutation for adding an item in an itemlist object
        based on the identifier,
    """
    check_required_args(identifier_1=identifier_1, identifier_2=identifier_2)
    return format_link_mutation("MergeItemListItemListElement", identifier_1,
                                identifier_2)


def mutation_remove_itemlist_itemlist_element(identifier_1: str,
                                              identifier_2: str):
    """Returns a mutation for removing an item in an itemlist object
    based on the identifier.

    Arguments:
        identifier_1: The unique identifier of the itemlist object.
        identifier_2: The unique identifier of the listitem object.

    Returns:
        The string for the mutation for removing an item from an itemlist
        object based on the identifier.
    """
    check_required_args(identifier_1=identifier_1, identifier_2=identifier_2)
    return format_link_mutation("RemoveItemListItemListElement", identifier_1,
                                identifier_2)

# AddListItemItem-> if you have a ListItem, it points to a Thing called 'item'
