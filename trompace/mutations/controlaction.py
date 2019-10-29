# Generate GraphQL queries for mutations pertaining to control actions.

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant


CREATE_CONTROLACTION = '''CreateControlAction(
        {parameters}
    ) {{
      identifier
      description
      actionStatus
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


def mutation_create_controlaction(name: str, description: str, actionStatus: str):
    """Returns a mutation for creating a control action object
    Arguments:
        name: The name of the cvontrol action.
        description: An account of the control action.
        actionStatus: The default actionStatus for a newly instantiated ControlAction ‘job'.
    Returns:
        The string for the mutation for creating the control action object.

    """

    args = {
        "name": name,
        "description": description,
        "actionStatus" : StringConstant(actionStatus.lower())
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

