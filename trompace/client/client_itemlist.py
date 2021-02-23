
from typing import Optional
from trompace import docstring_interpolate
from trompace.config import config
from trompace.connection import submit_query
from trompace.mutations import itemlist as mutations_itemlist
from trompace.constants import ItemListOrderType
from trompace.queries.itemlist import query_listitems
from trompace.exceptions import QueryException, IDNotFoundException


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

    resp = submit_query(mutation)
    result = resp.get("data", {}).get("CreateItemList")

    if result:
        itemlist_id = result["identifier"]
    else:
        raise QueryException(resp['errors'])

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
                                                    description=description,
                                                    position=position)

    resp = submit_query(mutation)
    result = resp.get("data", {}).get("CreateListItem")

    if result:
        element_id = result["identifier"]
    else:
        raise QueryException(resp['errors'])

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
    resp = submit_query(mutation)
    result = resp.get("data", {}).get("MergeItemListItemListElement")
    if not result:
        raise QueryException(resp['errors'])


def merge_listitem_nextitem_nodes(listitem_id: str, nextitem_id: str):
    """Add a NextItem to a ListItem object based on the identifier.
    (https://schema.org/nextItem)

    Arguments:
        listitem_id: The unique identifier of the ListItem object.
        nextitem_id: The unique identifier of the NextItem object.
    """
    mutation = mutations_itemlist.mutation_add_listitem_nextitem(
                                                    listitem_id=listitem_id,
                                                    nextitem_id=nextitem_id)
    resp = submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemNextItem")

    if not result:
        raise QueryException(resp['errors'])


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

    resp = submit_query(mutation)
    result = resp.get("data", {}).get("MergeListItemItem")

    if not result:
        raise QueryException(resp['errors'])


def check_item_nodes(item_ids: list):
    """ Check if Items already exist in the CE

    Arguments:
        item_ids: The list of unique identifiers of the Item objects
    Return:
        Set of identifiers not found
    """
    query = query_listitems(identifiers=item_ids)
    resp = submit_query(query)
    result = resp.get("data", {}).get("ThingInterface")

    not_found = set()
    if not result:
        raise QueryException(resp['errors'])
    elif len(result) != len(item_ids):
        not_found = set(item_ids) - set([item['identifier'] for item in result])

    return not_found


LISTITEM_SEQ_ARGS_DOCS = """listitems: the ListItems objects to create
        ids_mode: the type of Items to create (from ID or from string value)
        contributor: A person, an organization, or a service
        responsible for contributing the ListItem to the web resource.
        This can be either a name or a base URL.
        name: The name of the ListItem object.
        """


@docstring_interpolate("listitem_args", LISTITEM_SEQ_ARGS_DOCS)
def create_sequence_listitem_nodes(listitems: list, ids_mode: bool,
                                   contributor: str, name: str):
    """Create a sequence of ListItem object and return
    the corresponding identifiers.
    (https://schema.org/ListItem)

    Arguments:
        {listitem_args}

    Returns:
       The identifiers of the ListItem objects created.
    """
    if not ids_mode:
        description = [item for item in listitems]
    else:
        description = [None for item in listitems]

    mutation = mutations_itemlist.mutation_sequence_create_listitem(
                                                        listitems=listitems,
                                                        contributor=contributor,
                                                        name=name,
                                                        description=description)
    resp = submit_query(mutation)
    result = resp.get("data", {})

    if len(result.keys()) != len(listitems):
        raise QueryException(resp['errors'])
    else:
        listitems_ids = [result[listalias]['identifier'] for listalias in result]

    return listitems_ids


def merge_sequence_itemlist_itemlistelement_nodes(itemlist_id: str,
                                                  element_ids: list):
    """Add a sequence of ListItem objects to a ItemList object.

    Arguments:
        itemlist_id: The unique identifier of the ItemList object.
        element_ids: The list of unique identifier of the ThingInterface object.
    """
    mutation = mutations_itemlist.mutation_sequence_add_itemlist_itemlist_element(itemlist_id=itemlist_id,
                                                                                  element_ids=element_ids)
    resp = submit_query(mutation)
    result = resp.get("data", {})

    if not result:
        raise QueryException(resp['errors'])
    elif len(result.keys()) != len(element_ids):
        raise QueryException(resp['errors'])


def merge_sequence_listitem_item_nodes(listitem_ids: list, item_ids: list):
    """Add a sequence of Items to a ListItems objects based on the identifiers.
    (https://schema.org/item)

    Arguments:
        listitem_ids: The list of unique identifier of the ListItem object.
        item_ids: The list of unique identifier of the Item object.
    """
    mutation = mutations_itemlist.mutation_sequence_add_listitem_item(listitem_ids=listitem_ids,
                                                                      item_ids=item_ids)
    resp = submit_query(mutation)
    result = resp.get("data", {})

    if not result:
        raise QueryException(resp['errors'])
    elif len(result.keys()) != len(listitem_ids):
        raise QueryException(resp['errors'])


def merge_sequence_listitem_nextitem_nodes(listitem_ids: list):
    """Add a sequence of NextItem to a ListItem objects based on the identifiers.
    (https://schema.org/nextItem)

    Arguments:
        listitem_ids: The list of unique identifiers of the ListItem objects.
    """
    mutation = mutations_itemlist.mutation_sequence_add_listitem_nextitem(listitem_ids=listitem_ids)
    resp = submit_query(mutation)
    result = resp.get("data", {})

    if not result:
        raise QueryException(resp['errors'])


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
    listitems = []
    if values and node_ids:
        raise ValueError("cannot provide both node_ids and values arguments")
    elif values:
        [listitems.append(x) for x in values if x not in listitems]
        ids_mode = False
    elif node_ids:
        not_found = check_item_nodes(node_ids)
        if not_found:
            raise IDNotFoundException(not_found)
        else:
            [listitems.append(x) for x in node_ids if x not in listitems]
            ids_mode = True

    itemlist_id = create_itemlist_node(contributor=contributor,
                                       name=name,
                                       description=description,
                                       ordered=ordered)

    listitems_ids = create_sequence_listitem_nodes(listitems=listitems,
                                                   ids_mode=ids_mode,
                                                   contributor=contributor,
                                                   name=name)

    merge_sequence_itemlist_itemlistelement_nodes(itemlist_id=itemlist_id,
                                                  element_ids=listitems_ids)

    merge_sequence_listitem_nextitem_nodes(listitem_ids=listitems_ids)

    if node_ids:
        merge_sequence_listitem_item_nodes(listitem_ids=listitems_ids,
                                           item_ids=listitems)
