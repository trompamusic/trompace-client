from trompace import docstring_interpolate
from trompace.constants import ItemListOrderType
from trompace.mutations.templates import format_mutation

ITEMLIST_ARGS_DOCS = """name: The name of the ItemList object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the ItemList to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the ItemList.
        source: The URL of the web resource about this ItemList.
        title: The title of the resource indicated by `source`
        numTracks: The number of tracks in the ItemList
        """


@docstring_interpolate("itemlist_args", ITEMLIST_ARGS_DOCS)
def mutation_create_itemlist(*, title: str, contributor: str, creator: str, source: str, format_: str,
                             name: str = None, item_list_order: ItemListOrderType = None, ):
    """Returns a mutation for creating an itemlist object.

    Arguments:
        {itemlist_args}

    Returns:
        The string for the mutation for creating the itemlist.
    """


@docstring_interpolate("itemlist_args", ITEMLIST_ARGS_DOCS)
def mutation_update_itemlist(identifier: str):
    """Returns a mutation for updating an itemlist object.

    Arguments:
        identifier: The identifier of the itemlist in the CE to be updated.
        {itemlist_args}

    Returns:
        The string for the mutation for updating the itemlist.
    """


def mutation_delete_itemlist(identifier: str):
    """Returns a mutation for deleting an itemlist object based on the identifier.

    Arguments:
        identifier: The unique identifier of the itemlist object.

    Returns:
        The string for the mutation for deleting the itemlist object based on the identifier.
    """

    return format_mutation("DeleteItemList", {"identifier": identifier})


LISTITEM_ARGS_DOCS = """name: The name of the ListItem object.
        creator: The person, organization or service who created the thing the web resource is about.
        contributor: A person, an organization, or a service responsible for contributing the ListItem to the web resource. This can be either a name or a base URL.
        format_: A MimeType of the format of the page describing the ListItem.
        source: The URL of the web resource about this ListItem.
        title: The title of the resource indicated by `source`
        numTracks: The number of tracks in the ListItem
        """


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_create_listitem():
    """Returns a mutation for creating an listitem object.

    Arguments:
        {listitem_args}

    Returns:
        The string for the mutation for creating the itemlist.
    """


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def mutation_update_listitem(identifier):
    """Returns a mutation for updating an listitem_args object.

    Arguments:
        identifier: The identifier of the listitem_args in the CE to be updated.
        {itemlist_args}

    Returns:
        The string for the mutation for updating the listitem_args.
    """


def mutation_delete_listitem(identifier: str):
    """Returns a mutation for deleting an listitem object based on the identifier.

    Arguments:
        identifier: The unique identifier of the listitem object.

    Returns:
        The string for the mutation for deleting the listitem object based on the identifier.
    """

    return format_mutation("DeleteListItem", {"identifier": identifier})


# AddListItemItem -> if you have a ListItem, it points to a Thing called 'item'

# AddItemListItemListElement -> Add either a Thing or a ListItem to an ItemList


def mutation_add_itemlist_itemlist_element():
    pass


def mutation_remove_itemlist_itemlist_element():
    pass

