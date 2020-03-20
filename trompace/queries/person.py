# Generate GraphQL queries for queries pertaining to persons objects.
from typing import List

from trompace import QUERY, filter_none_args, make_parameters

QUERY_PERSON = '''Person{parameters}
{{
{fields}
}}'''

QUERY_PERSON_SUBSTRING = '''personBySubstring{parameters}
{{
{fields}
}}'''

default_fields = ["identifier", "name", "publisher", "contributor", "creator", "source", "description", "language"]


# TODO: We only define some basic query fields for now. Potential to add more if we see that they're needed
def query_person(query: str = None, identifier: str = None, contributor: str = None, creator: str = None,
                 source: str = None,
                 first: int = None, offset: int = None, fields: List[str] = None):
    """Returns a query for obtaining Person objects

    Arguments:
        query: perform a substring query on the name field
        identifier: get a Person with this identifier
        contributor: get Person objects from this contributor
        creator: get Person objects from this creator
        source: get Person objects from this source
        first: get the first this many items
        offset: offset search results by this value
        fields: return these fields in the Person objects. Defaults to `trompace.queries.person.default_fields`

    Returns:
        A Person Query string
    """

    if query:
        args = {"query": query,
                "first": first,
                "offset": offset}
        querystr = QUERY_PERSON_SUBSTRING
    else:
        args = {"identifier": identifier,
                "contributor": contributor,
                "creator": creator,
                "source": source,
                "first": first,
                "offset": offset}
        querystr = QUERY_PERSON

    args = filter_none_args(args)

    if fields:
        fields = "\n".join(fields)
    else:
        fields = "\n".join(default_fields)

    parameters = ""
    if args:
        parameters = "({})".format(make_parameters(**args))
    formatted_query = querystr.format(parameters=parameters, fields=fields)
    return QUERY.format(query=formatted_query)
