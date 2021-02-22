from trompace.queries.templates import format_query
from trompace import filter_none_args


def query_place(identifier: str = None, title: str = None, contributor: str = None, creator: str = None,
                source: str = None, format_: str = None, name: str = None,
                return_items_list: list = ["identifier", "name"]):

    """Returns a query for retrieving a place or places.

    Arguments:
        identifier: The identifier of the place in the CE.
        title: The title of the resource indicated by `source`
        contributor: The main URL of the site where the information about the Place was taken from
        creator: The person, organization or service who is creating this Place (e.g. URL of the software)
        source: The URL of the web resource where information about this Place is taken from
        format_: The format of ``source``
        name: The name of the place
        return_items_list: A list of fields to return in the query.

    Returns:
        The string for a place query.
    """

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
    }

    args = filter_none_args(args)

    return format_query("Place", args, return_items_list)
