# Generate GraphQL queries for mutations pertaining to properties..

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant, bool_to_str


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

ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION  = '''AddActionInterfaceThingInterface(
    from: {{identifier: "{identifier_1}"}}
    to: {{identifier: "{identifier_2}"}}
    field: object
    ){{
        from {{
            --typename
      }}
      to {{
           --typename 
           ... on PropertyValueSpecification{{  
            identifier
            name
        }}
      }}
    }}'''


def mutation_create_property(title: str, name: str, description: str, rangeIncludes: list):
    """Returns a mutation for creating a property
    Arguments:
        title: The title of the property
        name: The name of the property
        description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the Component developer to limit the type of nodes (content types) that can be selected.
    Returns:
        The string for the mutation for creating the property.

    """
    args = {
        "title": title,
        "name": name,
        "description": description,
        "rangeIncludes" : StringConstant(str([StringConstant(x) for x in rangeIncludes]))
    }
    return mutation_create(args, CREATE_PROPERTY)

def mutation_create_propertyvaluespecification(name: str, description: str, defaultValue: str, valueMaxLength: int, valueMinLength: int
    , multipleValues: bool, valueName: str, valuePattern: str, valueRequired: bool):
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
        "defaultValue" : defaultValue,
        "valueMaxLength": valueMaxLength,
        "valueMinLength": valueMinLength,
        "multipleValues": bool_to_str(multipleValues),
        "valueName": valueName,
        "valuePattern": StringConstant(valuePattern),
        "valueRequired": bool_to_str(valueRequired)
    }
    return mutation_create(args, CREATE_PROPERTYVALUESPECIFICATION)

def mutation_add_controlaction_propertyvaluepsecification(controlaction_id: str, propertyvaluespecification_id: str):
    """Returns a mutation for adding a control action to a property value specification.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        propertyvaluespecification_id: The unique identifier of the property value specification.
    Returns:
        The string for the mutation foradding a control action to a property value specification.
    """

    return mutation_link(controlaction_id, propertyvaluespecification_id, ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION)

