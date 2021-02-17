
from typing import Optional
from trompace import docstring_interpolate
from trompace.config import config
from trompace.connection import submit_query
from trompace.mutations import itemlist as mutations_itemlist
from trompace.constants import ItemListOrderType


ITEMLIST_ARGS_DOCS = """contributor: A person, an organization, or a service
        responsible for contributing the ItemList to the web resource.
        name: The name of the ItemList object.
        description: The description of the ItemList object
        ordered: The type of ordering for the list (ascending, descending,
        unordered, ordered)
        """


@docstring_interpolate("itemlist_args", ITEMLIST_ARGS_DOCS)
def create_itemlist_node(contributor: str, name: str, description: str = None,
                         ordered: bool = False):
    """Create a ItemList object and return the corresponding identifier.
    (https://schema.org/ItemList)

    Arguments:
        {itemlist_args}

    Returns:
        The identifier of the ItemList object created
    """
    itemlistorder = ItemListOrderType.ItemListUnordered
    if ordered:
        itemlistorder = ItemListOrderType.ItemListOrderAscending

    mutation = mutations_itemlist.mutation_create_itemlist(
                                        contributor=contributor,
                                        name=name,
                                        itemlistorder=itemlistorder,
                                        description=description)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("CreateItemList")

    if result:
        itemlist_id = result["identifier"]
    else:
        # Raise Error
        pass

    return itemlist_id


LISTITEM_ARGS_DOCS = """contributor: A person, an organization, or a service
        responsible for contributing the ListItem to the web resource.
        This can be either a name or a base URL.
        name: The name of the ListItem object.
        description: The description of the ItemList object
        position: the position of the ListItem
        """


@docstring_interpolate("listitem_args", LISTITEM_ARGS_DOCS)
def create_listitem_node(contributor: str, name: str, description: str = None,
                         position: Optional[int] = None):
    """Create a ListItem object and return the corresponding identifier.
    (https://schema.org/ListItem)

    Arguments:
        {listitem_args}

    Returns:
       The identifier of the ListItem object created
    """
    mutation = mutations_itemlist.mutation_create_listitem(
                                                    contributor=contributor,
                                                    name=name,
                                                    description=value,
                                                    position=position)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("CreateListItem")

    if result:
        element_id = result["identifier"]
    else:
        # Raise Error
        pass

    return element_id


def merge_itemlist_itemlistelement_nodes(itemlist_id: str, element_id: str):
    """Add a ThingInterface in an ItemList object based on the identifiers.
    (https://schema.org/itemListElement)

    Arguments:
        itemlist_id: The unique identifier of the ItemList object.
        element_id: The unique identifier of the ThingInterface object.
    """
    mutation = mutations_itemlist.mutation_add_itemlist_itemlist_element(
                                                    itemlist_id=itemlist_id,
                                                    element_id=element_id)
    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeItemListItemListElement")

    if not result:
        # Raise Error
        pass


def merge_listitem_nextitem_nodes(listitem_id: str, nextitem_id: str):
    """Add a NextItem to a ListItem object based on the identifier.
    (https://schema.org/nextItem)

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        nextitem_id: The unique identifier of the NextItem object.
    """
    mutation = mutations_itemlist.mutation_add_listitem_nextitem(
                                                    listitem_id=previousItemId,
                                                    nextitem_id=element_id)
    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemNextItem")

    if not result:
        # Raise Error
        pass


def merge_listitem_item_nodes(listitem_id: str, item_id: str):
    """Add an Item to a ListItem object based on the identifier.
    (https://schema.org/item)

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        item_id: The unique identifier of the Item object.
    """
    mutation = mutations_itemlist.mutation_add_listitem_item(
                                                    listitem_id=listitem_id,
                                                    item_id=item_id)

    resp = trompace.connection.submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemItem")

    if not result:
        # Raise Error
        pass


MAINCREATE_ARGS_DOCS = """contributor: A person, an organization, or a service
        responsible for contributing the ItemList to the web resource.
        This can be either a name or a base URL.
        name: The name of the ItemList object.
        description: The description of the ItemList object
        position: the position of the ListItem
        ordered: The type of ordering for the list (ascending, descending,
        unordered, ordered)
        node_ids: set of node identifiers to be added to ItemList as ListItem
        values: set of values to be added to ItemList as ListItem
        """


@docstring_interpolate("maincreate_args", MAINCREATE_ARGS_DOCS)
def create_itemlist(contributor: str, name: str, description: str,
                    ordered: bool, node_ids: list = None, values: list = None):
    """ Main function to create a ItemList object and related ListItem objects
    based on the input values or node identifiers.

    Arguments:
        {maincreate_args}

    """
    if values and node_ids:
        # Raise Error
        pass
    elif values:
        listitems = values
        ids_mode = False
    elif node_ids:
        listitems = node_ids
        ids_mode = True

    itemlist_id = create_itemlist_node(contributor=contributor,
                                       name=name,
                                       description=description,
                                       ordered=ordered)

    previous_item_id = None
    for position, item in enumerate(listitems):

        listitem_descr = None
        if not ids_modes:
            listitem_descr = item

        listitem_id = create_listitem_node(contributor=contributor,
                                           name=name,
                                           description=listitem_descr,
                                           position=position)

        merge_itemlist_itemlistelement_nodes(itemlist_id=itemlist_id,
                                             element_id=listitem_id)

        if ids_modes:
            merge_listitem_item_nodes(listitem_id=listitem_id, item_id=item)

        if previous_item_id:
            merge_listitem_nextitem_nodes(listitem_id=previous_item_id,
                                          nextitem_id=listitem_id)

        previous_item_id = listitem_id
