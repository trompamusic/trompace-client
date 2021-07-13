import enum
from typing import Union, List

from trompace import filter_none_args, StringConstant, check_required_args
from trompace.constants import SUPPORTED_LANGUAGES
from trompace.exceptions import UnsupportedLanguageException
from trompace.mutations.itemlist import mutation_create_itemlist, mutation_create_listitem
from trompace.mutations.templates import format_mutation, format_link_mutation

# For making DefinedTerms that are a collection of tags
ADDITIONAL_TYPE_TAG_COLLECTION = "https://vocab.trompamusic.eu/vocab#TagCollection"
ADDITIONAL_TYPE_TAG_COLLECTION_ELEMENT = "https://vocab.trompamusic.eu/vocab#TagCollectionElement"

# For making DefinedTerms that are a collection of annotation motivations
ADDITIONAL_TYPE_MOTIVATION_COLLECTION = "https://vocab.trompamusic.eu/vocab#AnnotationMotivationCollection"
ADDITIONAL_TYPE_MOTIVATION_COLLECTION_ELEMENT = "https://vocab.trompamusic.eu/vocab#AnnotationMotivationCollectionElement"

# For saying that an ItemList is an annotation toolkit
ADDITIONAL_TYPE_ANNOTATION_TOOLKIT = "https://vocab.trompamusic.eu/vocab#AnnotationToolkit"

# For saying that an ItemList is an annotation session
ADDITIONAL_TYPE_ANNOTATION_SESSION = "https://vocab.trompamusic.eu/vocab#AnnotationSession"

OA_ANNOTATION_MOTIVATION_TYPE = "http://www.w3.org/ns/oa#Motivation"


class AnnotationSchemaMotivation(enum.Enum):
    assessing = "http://www.w3.org/ns/oa#assessing"
    bookmarking = "http://www.w3.org/ns/oa#bookmarking"
    classifying = "http://www.w3.org/ns/oa#classifying"
    commenting = "http://www.w3.org/ns/oa#commenting"
    describing = "http://www.w3.org/ns/oa#describing"
    editing = "http://www.w3.org/ns/oa#editing"
    highlighting = "http://www.w3.org/ns/oa#highlighting"
    identifying = "http://www.w3.org/ns/oa#identifying"
    linking = "http://www.w3.org/ns/oa#linking"
    moderating = "http://www.w3.org/ns/oa#moderating"
    questioning = "http://www.w3.org/ns/oa#questioning"
    replying = "http://www.w3.org/ns/oa#replying"
    tagging = "http://www.w3.org/ns/oa#tagging"


def create_annotation_ce_target(creator: str, field: str = None, fragment: str = None):
    """Return a mutation for making an AnnotationCETarget.
    An AnnotationCETarget is a node that can be used for a
    web Annotation (https://www.w3.org/TR/annotation-model)
    as the target field, when the target refers to a node that already exists in the CE

    Arguments:
        creator: a URI to the identity of the user who created this AnnotationCETaraget
        field (optional): the field of the node `target` that contains the URL to the target item
        fragment (optional): If the target is a fragment, the value to be appended to the URL in field

    Returns:
        A GraphQL Mutation to create an AnnotationCETarget in the Trompa CE
    """

    check_required_args(creator=creator)

    params = {"creator": creator,
              "field": field,
              "fragment": fragment}
    params = filter_none_args(params)

    return format_mutation(mutationname="CreateAnnotationCETarget", args=params)


def merge_annotation_target_target(annotationcetarget_id, target_id):
    return format_link_mutation("MergeAnnotationCETargetTarget", annotationcetarget_id, target_id)


def create_annotation_textual_body(creator: str, value: str, format_: str = None, language: str = None):
    """Return a mutation for making an AnnotationTextualBody.
    An AnnotationTextualBody is the main written body of a
    web Annotation (https://www.w3.org/TR/annotation-model).

    Arguments:
        creator: a URI to the identity of the user who created this AnnotationTextualBody
        value: the text for the body of the annotation
        format_: the mimetype that value is formatted in
        language: the language that value is written in

    Returns:
        A GraphQL Mutation to create an AnnotationTextualBody in the Trompa CE
    """

    check_required_args(creator=creator, value=value)

    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    params = {"creator": creator,
              "value": value,
              "format": format_}

    if language is not None:
        params["language"] = StringConstant(language.lower())

    return format_mutation(mutationname="CreateAnnotationTextualBody", args=params)


def create_annotation_motivation(creator: str, title: str, description: str,
                                 broader_schema: AnnotationSchemaMotivation = None,
                                 broader_url: str = None):
    """Return a mutation for making an Annotation motivation
    A custom motivation should be a special case of one of the standard 13 motivations in
    the web annotation vocabulary (https://www.w3.org/TR/annotation-vocab/#named-individuals),
    or a URL pointing to an external motivation

    Arguments:
        creator: a URI to the identity of the user who created this Motivation
        title: a descriptive name for the motivation
        description: a detailed description of the motivation
        broader_schema: a AnnotationSchemaMotivation value describing what this motivation is
           a special case of
        broader_url: a URL to an oa:Motivation describing what this motivation is a special case of
    """
    params = {"creator": creator,
              "title": title,
              "description": description,
              "broaderUrl": broader_url,
              }
    if broader_schema:
        params["broaderMotivation"] = StringConstant(broader_schema.name)
    params = filter_none_args(params)
    return format_mutation(mutationname="CreateAnnotationCEMotivation", args=params)


def create_annotation(creator: str, motivation: AnnotationSchemaMotivation,
                      target_url: str = None, body_url: List[str] = None):
    """Return a mutation for making a web Annotation (https://www.w3.org/TR/annotation-model)

    Arguments:
        creator: a URI to the identity of the user who created this Annotation
        motivation: a AnnotationSchemaMotivation value, or the ID of an AnnotationCEMotivation node
        target_url: if the target is the URL of an external object, the URL
        body_url: if the body is the URL of an external object, the URL

    Returns:
        A GraphQL Mutation to create an Annotation in the Trompa CE
    """

    check_required_args(creator=creator, motivation=motivation)
    params = {"creator": creator,
              "motivation": StringConstant(motivation.name),
              "targetUrl": target_url,
              "bodyUrl": body_url,
              }
    params = filter_none_args(params)

    return format_mutation(mutationname="CreateAnnotation", args=params)


def merge_annotation_targetnode(annotation_id, target_id):
    """
    Join an annotation with an AnnotationCETarget

    Arguments:
        annotation_id: CE Node ID of an Annotation object
        target_id: CE Node ID of an AnnotationCETarget object

    """
    return format_link_mutation("MergeAnnotationTargetNode", annotation_id, target_id)


def merge_annotation_bodytext(annotation_id, textualbody_id):
    """
    Join an annotation with a body described in an AnnotationTextualBody
    Arguments:
        annotation_id: CE Node ID of an Annotation object
        textualbody_id: CE Node ID of an AnnotationTextualBody object

    """
    return format_link_mutation("MergeAnnotationBodyText", annotation_id, textualbody_id)


def merge_annotation_bodynode(annotation_id, node_id):
    """
    Join an annotation with body described in any node in the CE
    Arguments:
        annotation_id: CE Node ID of an Annotation object
        node_id: CE Node ID of any object that implements ThingInterface

    """
    return format_link_mutation("MergeAnnotationBodyNode", annotation_id, node_id)


def merge_annotation_motivationdefinedtermset(annotation_id, definedtermset_id):
    """
    Join an annotation with a DefinedTerm that describes a custom annotation Motivation

    Arguments:
        annotation_id: CE Node ID of an Annotation object
        definedtermset_id: CE Node ID of a DefinedTermSet object which is a more specific annotation Motivation

    Returns:

    """
    return format_link_mutation("MergeAnnotationMotivationDefinedTermSet", annotation_id, definedtermset_id)


def merge_annotation_cemotivation(annotation_id, cemotivation_id):
    """
    Join an annotation with an AnnotationCEMotivation object that describes a custom annotation Motivation

    Arguments:
        annotation_id: CE Node ID of an Annotation object
        cemotivation_id: CE Node ID of a AnnotationCEMotivation object which is a more specific annotation Motivation

    Returns:

    """
    return format_link_mutation("MergeAnnotationMotivationNode", annotation_id, cemotivation_id)


def update_annotation_ce_target(identifier: str, target: str = None, field: str = None, fragment: str = None):
    """Return a mutation for updating an AnnotationCETarget.

    Returns:
        A GraphQL Mutation to update an AnnotationCETarget in the Trompa CE
    """
    check_required_args(identifier=identifier)
    params = {"identifier": identifier,
              "target": target,
              "field": field,
              "fragment": fragment}
    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateAnnotationCETarget", args=params)


def update_annotation_textual_body(identifier: str, value: str = None, format_: str = None, language: str = None):
    """Return a mutation for updating an AnnotationTextualBody.

    Returns:
        A GraphQL Mutation to update an AnnotationTextualBody in the Trompa CE
    """
    check_required_args(identifier=identifier)
    if language and language.lower() not in SUPPORTED_LANGUAGES:
        raise UnsupportedLanguageException(language)

    params = {"identifier": identifier,
              "value": value,
              "format": format_}
    params = filter_none_args(params)

    if language is not None:
        params["language"] = StringConstant(language.lower())

    return format_mutation(mutationname="UpdateAnnotationTextualBody", args=params)


def update_annotation_motivation(identifier: str, creator: str, title: str, description: str,
                                 broader_schema: AnnotationSchemaMotivation = None,
                                 broader_url: str = None):
    """Return a mutation for updating an Annotation motivation

    """
    check_required_args(identifier=identifier)
    params = {"identifier": identifier,
              "creator": creator,
              "title": title,
              "description": description,
              "broaderUrl": broader_url,
              }
    if broader_schema:
        params["broaderMotivation"] = StringConstant(broader_schema.name)
    params = filter_none_args(params)
    return format_mutation(mutationname="UpdateAnnotationCEMotivation", args=params)


def update_annotation(identifier: str, target: str = None, motivation: Union[AnnotationSchemaMotivation, str] = None,
                      body: str = None, creator: str = None):
    """Return a mutation for updating an Annotation.

    Returns:
        A GraphQL Mutation to create an Annotation in the Trompa CE
    """
    check_required_args(identifier=identifier)
    params = {"identifier": identifier,
              "target": target,
              "motivation": motivation,
              "body": body,
              "creator": creator}
    params = filter_none_args(params)

    return format_mutation(mutationname="UpdateAnnotation", args=params)


def delete_annotation_ce_target(identifier: str):
    """Return a mutation for deleting an AnnotationCETarget.

    Arguments:
        identifier: The identifier of the AnnotationCETarget to delete

    Returns:
        A GraphQL Mutation to delete an AnnotationCETarget from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteAnnotationCETarget", args=params)


def delete_annotation_textual_body(identifier: str):
    """Return a mutation for deleting an AnnotationTextualBody.

    Arguments:
        identifier: The identifier of the AnnotationTextualBody to delete

    Returns:
        A GraphQL Mutation to delete an AnnotationTextualBody from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteAnnotationTextualBody", args=params)


def delete_annotation_motivation(identifier: str):
    """Return a mutation for deleting an AnnotationCEMotivation.

    Arguments:
        identifier: The identifier of the AnnotationCEMotivation to delete

    Returns:
        A GraphQL Mutation to delete an AnnotationCEMotivation from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="UpdateAnnotationCEMotivation", args=params)


def delete_annotation(identifier: str):
    """Return a mutation for deleting an Annotation.

    Arguments:
        identifier: The identifier of the Annotation to delete

    Returns:
        A GraphQL Mutation to delete an Annotation from the Trompa CE
    """
    params = {"identifier": identifier}
    return format_mutation(mutationname="DeleteAnnotation", args=params)


def create_annotation_toolkit(creator: str, name: str, description: str = None):
    # TODO: Not sure what to do about ordering
    return mutation_create_itemlist(name=name, creator=creator, description=description,
                                    additionaltype=[ADDITIONAL_TYPE_ANNOTATION_TOOLKIT])


def create_annotation_toolkit_element(creator: str, name: str = None, itemurl: str = None):
    return mutation_create_listitem(creator=creator, name=name, itemurl=itemurl)


def create_annotation_session(creator: str, name: str, description: str = None):
    return mutation_create_itemlist(name=name, creator=creator, description=description,
                                    additionaltype=[ADDITIONAL_TYPE_ANNOTATION_SESSION])


def create_annotation_session_element(creator: str):
    # To add an annotation to an annotation session we don't need any additional information
    #  in the ListItem, it's just a basic container
    return mutation_create_listitem(creator=creator)
