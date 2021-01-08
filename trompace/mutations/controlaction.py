# Generate GraphQL queries for mutations pertaining to control actions.

from trompace import StringConstant
from trompace.mutations.templates import mutation_create, mutation_link, format_link_mutation, format_mutation
from trompace.constants import ActionStatusType
import trompace.exceptions
from typing import List

CREATE_CONTROLACTION = '''CreateControlAction(
        {parameters}
    ) {{
      identifier
    }}'''

ADD_ENTRYPOINT_CONTROLACTION = '''AddThingInterfacePotentialAction(
        from: {{identifier: "{identifier_1}"}}
        to: {{identifier: "{identifier_2}"}}
        ){{
        from {{
        ... on EntryPoint{{
                identifier
        }}
      }}
        to {{
            ... on ControlAction{{
                    identifier
        }}
      }}
    }}'''

UPDATE_CONTROLACTION = """UpdateControlAction(
        {parameters}
    ) {{
      identifier
    }}"""


def mutation_create_controlaction(name: str,
                                  actionstatus: ActionStatusType = ActionStatusType.PotentialActionStatus,
                                  description: str = None):
    """Returns a mutation for creating a ControlAction.
    If an action status is not set, defaults to a PotentialActionStatus
    Arguments:
        name: The name of the ControlAction.
        description: An account of the ControlAction.
        actionstatus: The status of the ControlAction.
    Returns:
        The string for the mutation for creating the ControlAction object.
    """

    if not isinstance(actionstatus, ActionStatusType):
        raise trompace.exceptions.InvalidActionStatusException(actionstatus)

    args = {
        "name": name,
        "description": description,
        "actionStatus": StringConstant(actionstatus)
    }
    return mutation_create(args, CREATE_CONTROLACTION)


def mutation_add_entrypoint_controlaction(entrypoint_id: str, controlaction_id: str):
    """Returns a mutation for adding an entry point object to a control action
    Arguments:
        entrypoint_id: The unique identifier of the entry point.
        controlaction_id: The unique identifier of the control action.
    Returns:
        The string for the mutation for adding an entry point object to a control action
    """

    return mutation_link(entrypoint_id, controlaction_id, ADD_ENTRYPOINT_CONTROLACTION)


def mutation_modify_controlaction(controlaction_id: str, actionstatus: ActionStatusType, error: str = None):
    """Returns a mutation for modifying the status and errors of the ControlAction
    Arguments:
        controlaction_id: The unique identifier of the ControlAction.
        actionstatus: the status to update to.
        error: An error to set if the actionstatus is FailedActionStatus
    Returns:
        The string for the mutation for modifying a ControlAction.
    """

    if not isinstance(actionstatus, ActionStatusType):
        raise trompace.exceptions.InvalidActionStatusException(actionstatus)

    args = {
        "identifier": controlaction_id,
        "actionStatus": StringConstant(actionstatus)
    }
    if error:
        args["error"] = error

    return mutation_create(args, UPDATE_CONTROLACTION)


def mutation_add_propertyvaluespecification_potentialaction(propertyvaluespecification_id: str, controlaction_id: str):
    """Returns a mutation for adding a control action to a property value specification.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        propertyvaluespecification_id: The unique identifier of the property value specification.
    Returns:
        The string for the mutation foradding a control action to a property value specification.
    """
    return format_link_mutation("MergePropertyValueSpecificationPotentialAction", propertyvaluespecification_id, controlaction_id)


def mutation_add_controlaction_additionalproperty(controlaction_id: str, property_id: str):
    """Returns a mutation for adding a control action to a property value specification.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        property_id: The unique identifier of the property.
    Returns:
        The string for the mutation foradding a control action to a property.
    """
    return format_link_mutation("MergeControlActionAdditionalProperty", controlaction_id, property_id)


def mutation_add_controlaction_object(controlaction_id: str, object_id: str):
    """Returns a mutation for adding a control action to an object, either a property value specification or a property
    Arguments:
        controlaction_id: The unique identifier of the control action.
        object_id: The unique identifier of the object (property / property value specification).
    Returns:
        The string for the mutation for adding a control action to an object.
    """
    return format_link_mutation("AddControlActionObject", controlaction_id, object_id)


def mutation_request_controlaction(controlaction_id: str, entrypoint_id: str, properties: list,
                                   propertyValues: list):
    """Returns a mutation for requesting a control action
        controlaction_id: The unique identifier of the control action.
        entrypoint_id: The unique identifier of the entry point linked to this control action
        properties: a list of the properties objects of the control action
        propertyValues: a list of the properties objects of the control action
    Returns:
        The string for the mutation for requesting a control action.
        """
    args = {
        "controlAction": {
            "potentialActionIdentifier": controlaction_id,
            "entryPointIdentifier": entrypoint_id,
            "propertyObject": properties,
            "propertyValueObject": propertyValues
        }
    }
    return format_mutation("RequestControlAction", args)


def mutation_update_controlaction_status(controlaction_id: str, action_status: ActionStatusType):
    """Returns a mutation for updating the status of a control action to an object
    Arguments:
        controlaction_id: The unique identifier of the control action.
        action_status: the action status enum object.
    Returns:
        The string for the mutation for adding a control action to an object.
        """
    args = {
       "identifier": controlaction_id,
       "actionStatus": StringConstant(str(action_status))
    }
    return format_mutation("UpdateControlAction", args)


def mutation_add_actioninterface_result(controlaction_id: str, thing_interface_id: str):
    """Returns a mutation for linking a control action object and a thing interface with the result relation
    Arguments:
        controlaction_id: The unique identifier of the control action.
        thing_interface_id: the unique identifier of a thing interface object
    Returns:
        The string for the mutation for adding a control action to an object.
        """

    return format_link_mutation("AddActionInterfaceResult", controlaction_id, thing_interface_id)
