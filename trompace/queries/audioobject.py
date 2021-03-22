from trompace.queries.templates import format_query
from trompace import filter_none_args, make_filter


def query_audioobject(identifier: str = None, title: str = None, contributor: str = None,
                      creator: str = None, source: str = None, format_: str = None, name: str = None,
                      date: str = None, encodingformat: str = None,
                      embedurl: str = None, url: str = None, contenturl: str = None, language: str = None,
                      inlanguage: str = None, license_: str = None, filter_: dict = None,
                      return_items: list = None):

    """Returns a query for reading an AudioObject from the CE.
    Arguments:
        identifier: return nodes with this identifier
        title: return nodes with this title
        contributor: return nodes with this contributor
        creator: return nodes with this creator
        source: return nodes with this source
        format_: return nodes with this format
        name: return nodes with this name
        date: return nodes with this date
        encodingformat: return nodes with this encodingFormat
        embedurl: return nodes with this embedUrl
        url: return nodes with this url
        contenturl: return nodes with this contentUrl
        language: return nodes with this language
        inlanguage: return nodes with this inLanguage
        license_: return nodes with this license
        filter_: return nodes with this custom filter
        return_items: return these items in the response
    Returns:
        The string for the querying the media object.
    """

    if return_items is None:
        return_items = ["identifier", "creator", "title", "source"]

    args = {
        "identifier": identifier,
        "title": title,
        "contributor": contributor,
        "creator": creator,
        "source": source,
        "format": format_,
        "name": name,
        "date": date,
        "encodingFormat": encodingformat,
        "embedUrl": embedurl,
        "url": url,
        "contentUrl": contenturl,
        "language": language,
        "inLanguage": inlanguage,
        "license": license_
    }
    if filter_:
        args["filter"] = make_filter(filter_)

    args = filter_none_args(args)

    return format_query("AudioObject", args, return_items)
