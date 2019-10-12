# Generate GraphQL queries for mutations pertaining to software applications.

from .templates import mutation_create, mutation_update, mutation_delete, mutation_link
from . import StringConstant, bool_to_str


CREATE_PROPERTY = '''
CreateProperty(
{parameters}
) {{
  identifier
}}
'''

CREATE_PROPERTYVALUESPECIFICATION = '''
CreatePropertyValueSpecification(
{parameters}
) {{
  identifier
}}
'''

ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION  = '''
AddActionInterfaceThingInterfacee(
  from: {{identifier: "{identifier_1}"}}
  to: {{identifier: "{identifier_2}"}}
  field: object
)
{{
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
}}
'''


def mutation_create_property(title: str, name: str, description: str, rangeIncludes: list):
    """Returns a mutation for creating a property
    Arguments:
        name: The name of the property
        description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the Component developer to limit the type of nodes (content types) that can be selected.
    Returns:
        The string for the mutation for creating the property.

    """
    range_inc = []
    for name in rangeIncludes:
        range_inc.append(StringConstant(name))
    args = {
        "title": name,
        "name": name,
        "description": description,
        "rangeIncludes" : StringConstant(str([StringConstant(x) for x in rangeIncludes]))
    }
    return mutation_create(args, CREATE_PROPERTY)

def mutation_create_propertyvaluespecification(name: str, description: str, defaultValue: str, valueMaxLength: int, valueMinLength: int
    , multipleValues: bool, valueName: str, valuePattern: str, valueRequired: bool):
    """Returns a mutation for creating a property
    Arguments:
        name: The name of the property
        description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the Component developer to limit the type of nodes (content types) that can be selected.
    Returns:
        The string for the mutation for creating the property.

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
    """Returns a mutation for adding a digital document as a subject of a composition.
    Arguments:
        controlaction_id: The unique identifier of the control action.
        propertyvaluespecification_id: The unique identifier of the property value specification.
    Returns:
        The string for the mutation for adding the document as a subject of the composition.
    """

    return mutation_link(controlaction_id, propertyvaluespecification_id, ADD_CONTROLACTION_PROPERTYVALUESPECIFICATION)

