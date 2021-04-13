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


SESSION_INCLUDES = """
    identifier
    name
    creator
    itemListElement {
      ... on ListItem {
        item {
          ... on Annotation {
            targetNode {
              target {
                __typename
                identifier
              }
            }
          }
        }
      }
    }
"""


ANNOTATION_INCLUDES = """
    targetNode {
      target {
        ... on AudioObject {
          source
        }
      }
    }
    identifier
    motivation
    motivationNode {
      identifier
      broaderMotivation
      title
    }
    bodyNode {
      ... on Annotation {
        identifier
      }
    }
"""


def get_annotation_toolkits_for_user(creator: str):
    return format_query(
        "ItemList",
        {"creator": creator,
         "filter": {
             "additionalType_contains": "https://vocab.trompamusic.eu/vocab#AnnotationToolkit"}
         },
        TOOLKIT_INCLUDES)


def get_annotation_toolkit(identifier: str):
    return format_query("ItemList", {"identifier": identifier}, TOOLKIT_INCLUDES)


def get_session_for_user(creator: str):
    return format_query(
        "ItemList",
        {"creator": creator,
         "filter": {
             "additionalType_contains": "https://vocab.trompamusic.eu/vocab#AnnotationSession"}
         },
        SESSION_INCLUDES)


def get_annotation(identifier: str):
    return format_query("Annotation", {"identifier": identifier}, ANNOTATION_INCLUDES)


def get_annotations_for_target_node(identifier: str):
    """Get all annotations whose target node is given by the identifier"""
    return format_query("Annotation",
                        {"filter": {"targetNode": {"target_in": {"identifier": identifier}}}},
                        ANNOTATION_INCLUDES)


def get_annotations_for_user(creator: str):
    return format_query("Annotation", {"creator": creator}, ANNOTATION_INCLUDES)
