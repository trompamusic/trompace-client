# Generate GraphQL queries for mutations pertaining to control actions.

from trompace import StringConstant
from trompace.mutations.templates import mutation_create, mutation_link
from trompace.constants import ActionStatusType
import trompace.exceptions

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


def mutation_create_controlaction(name: str, description: str,
                                  actionstatus: ActionStatusType = ActionStatusType.PotentialActionStatus):
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
