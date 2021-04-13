from trompace.queries.templates import format_query

TOOLKIT_INCLUDES = """
    additionalType
    identifier
    name
    itemListElement {
      ... on ListItem {
        identifier
        name
        itemUrl
        item {
          __typename
          identifier
          ... on DefinedTermSet {
            name
            additionalType
            hasDefinedTerm {
              identifier
              broaderUrl
              broaderMotivation
              termCode
              image
            }
          }
          ... on Rating {
            name
            worstRating
            bestRating
          }
        }
      }
    }
"""


def get_annotation_toolkits_for_user(creator: str):
    return format_query("ItemList", {"creator": creator}, TOOLKIT_INCLUDES)


def get_annotation_toolkit(identifier: str):
    return format_query("ItemList", {"identifier": identifier}, TOOLKIT_INCLUDES)
