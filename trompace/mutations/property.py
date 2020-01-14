# Generate GraphQL queries for mutations pertaining to properties..
from typing import List

from . import StringConstant
from .templates import mutation_create, mutation_link

CREATE_PROPERTY = '''CreateProperty(
        {parameters}
        ) {{
      identifier
    }}'''

CREATE_PROPERTYVALUESPECIFICATION = '''CreatePropertyValueSpecification(
        {parameters}
        ) {{
      identifier
    }}'''

ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION = '''AddActionInterfaceThingInterface(
    from: {{identifier: "{identifier_1}", type: ControlAction}}
    to: {{identifier: "{identifier_2}", type: PropertyValueSpecification}}
    field: object
    ){{
        from {{
            __typename
      }}
      to {{
           __typename
           ... on PropertyValueSpecification{{
            identifier
        }}
      }}
    }}'''

ADD_CONTROLACTION_PROPERTY = '''AddActionInterfaceThingInterface(
    from: {{identifier: "{identifier_1}", type: ControlAction}}
    to: {{identifier: "{identifier_2}", type: Property}}
    field: object
    ){{
        from {{
            __typename
      }}
      to {{
           __typename 
           ... on Property{{  
            identifier
        }}
      }}
    }}'''


def mutation_create_property(title: str, name: str, description: str, rangeIncludes: List[StringConstant]):
    """Returns a mutation for creating a property
    Arguments:
        title: The title of the property
        name: The name of the property
        description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the Component developer to limit the type of nodes (content types) that can be selected.
    Returns:
        The string for the mutation for creating the property.

    """
    # import pdb;pdb.set_trace()
    args = {
        "title": title,
        "name": name,
        "description": description,
        "rangeIncludes": rangeIncludes
    }
    return mutation_create(args, CREATE_PROPERTY)


def mutation_create_propertyvaluespecification(name: str, description: str, defaultValue: str, valueMaxLength: int,
                                               valueMinLength: int
                                               , multipleValues: bool, valueName: str, valuePattern: str,
                                               valueRequired: bool):
    """Returns a mutation for creating a property value specification
    Each PropertyValueSpecification defines a scalar input parameter that the Component user should be prompted with when preparing
    the request for an algorithm process job. There are numerous properties that can be used to set requirements, type and limits for a scalar parameter.
    With these properties, a Component developer can set up the input field for this parameter.
    Arguments:
        name: The name of the property value specification.
        description: An account of the property
        defaultValue: the default value to use for the property value specification.
        valueMaxLength: The maximum length of the value.
        valueMinLength: The minimum length of the value.
        multipleValues: A boolean that states if multiple values are accepted or not.
        valueName: The name of the value.
        valuePattern: The format of the value.
        valueRequired: A boolean stating if the value is required or not.
    Returns:
        The string for the mutation for creating the property value specification.

    """

    args = {
        "name": name,
        "title": name,
        "description": description,
        "defaultValue": defaultValue,
        "valueMaxLength": valueMaxLength,
        "valueMinLength": valueMinLength,
        "multipleValues": multipleValues,
        "valueName": valueName,
        "valuePattern": StringConstant(valuePattern),
        "valueRequired": valueRequired
    }
    return mutation_create(args, CREATE_PROPERTYVALUESPECIFICATION)


def mutation_add_controlaction_propertyvaluespecification(controlaction_id: str, propertyvaluespecification_id: str):
    """Returns a mutation for adding a control action to a property value specification.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        propertyvaluespecification_id: The unique identifier of the property value specification.
    Returns:
        The string for the mutation foradding a control action to a property value specification.
    """

    return mutation_link(controlaction_id, propertyvaluespecification_id, ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION)


def mutation_add_controlaction_property(controlaction_id: str, property_id: str):
    """Returns a mutation for adding a control action to a property value specification.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        property_id: The unique identifier of the property.
    Returns:
        The string for the mutation foradding a control action to a property.
    """

    return mutation_link(controlaction_id, property_id, ADD_CONTROLACTION_PROPERTY)
