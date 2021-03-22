from trompace.queries.templates import format_query
from trompace import filter_none_args, make_filter


def query_softwareapplication(identifier: str = None, title: str = None, contributor: str = None,
                              creator: str = None, source: str = None, name: str = None,
                              language: str = None, softwareversion: str = None,
                              filter_: dict = None, return_items: list = None):

    """Returns a query for reading an SoftwareApplication from the CE.
    Arguments:
        identifier: return nodes with this identifier
        title: return nodes with this title
        contributor: return nodes with this contributor
        creator: return nodes with this creator
        source: return nodes with this source
        name: return nodes with this name
        language: return nodes with this language
        softwareversion: return nodes with this softwareversion
        filter_: return nodes with this custom filter
        return_items: return these items in the response
    Returns:
        The string for the querying the SoftwareApplication.
    """

    if return_items is None:
        return_items = ["identifier", "creator", "title", "source"]

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "name": name,
        "language": language,
        "softwareVersion": softwareversion
    }
    if filter_:
        args["filter"] = make_filter(filter_)

    args = filter_none_args(args)

    return format_query("SoftwareApplication", args, return_items)
