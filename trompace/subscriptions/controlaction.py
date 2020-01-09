# Generate GraphQL queries for mutations pertaining to control actions.

from .templates import subscription_create
from . import StringConstant

CONTROL_ACTION_SUBSCRIPTION = '''ControlActionRequest(
        {parameters}
    ) {{
      identifier
    }}'''

CONTROL_ACTION_SUBSCRIPTION_CLIENT = '''ControlActionMutation(
        {parameters}
    ) {{
      identifier
    }}'''


def subscription_controlaction(identifier: str):
    """Returns a mutation for creating a control action object
    Arguments:
        name: The name of the cvontrol action.
        description: An account of the control action.
        actionStatus: The default actionStatus for a newly instantiated ControlAction ‘job'.
    Returns:
        The string for the mutation for creating the control action object.

    """

    args = {
        "entryPointIdentifier": identifier,
    }
    return subscription_create(args, CONTROL_ACTION_SUBSCRIPTION)


def subscription_controlaction_client(identifier: str):
    """Returns a mutation for creating a control action object
    Arguments:
        name: The name of the cvontrol action.
        description: An account of the control action.
        actionStatus: The default actionStatus for a newly instantiated ControlAction ‘job'.
    Returns:
        The string for the mutation for creating the control action object.

    """

    args = {
        "identifier": identifier,
    }
    return subscription_create(args, CONTROL_ACTION_SUBSCRIPTION_CLIENT)
