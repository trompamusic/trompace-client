# Generate GraphQL queries for mutations pertaining to properties..
from typing import List

from trompace import StringConstant
from .templates import mutation_create, mutation_link, format_link_mutation, format_mutation


def mutation_create_property(title: str, name: str, rangeIncludes: List[StringConstant], description: str = None):
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
        "rangeIncludes": rangeIncludes
    }
    return format_mutation("CreateProperty", args)

def mutation_create_propertyvaluespecification(name: str, defaultValue: str, valueMaxLength: int,
                                               valueMinLength: int, multipleValues: bool, valueName: str,
                                               valuePattern: str, valueRequired: bool, description: str = None):
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
    return format_mutation("CreatePropertyValueSpecification", args)


