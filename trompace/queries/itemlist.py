# Generate GraphQL queries for queries pertaining to media objects.
from trompace.queries.templates import format_filter_query, format_itemlist_query
from trompace import StringConstant, _Neo4jDate, filter_none_args, docstring_interpolate


def query_listitems(identifiers: list = None, return_items_list: list = ["identifier"]):

    """Returns a query for querying the database for a ThingInterface object.
    Arguments:
        identifiers: The list of identifiers of the ThingInterfaces object in the CE.
        return_items_list: A list of item fields that the query must return.
    Returns:
        The string for the quereing the ThingInterface object.
    """

    args = {
        "identifier_in": identifiers,
    }

    args = filter_none_args(args)

    return format_filter_query("ThingInterface", args, return_items_list)


def query_itemlist(identifier: str):

    """Returns a query for querying the database for a ItemList object.
    Arguments:
        identifier: The identifier of the ItemList object in the CE.
    Returns:
        The string for the quereing the ItemList object.
    """

    args = {
        "identifier_in": identifier,
    }

    args = filter_none_args(args)

    return format_itemlist_query("ItemList", args)
