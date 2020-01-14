# Templates for generate GraphQL queries for mutations.

from . import make_parameters, SUBSCRIPTION


# To be added EntryPoint, ControlAction, PropertyValueSpecification and Property

def subscription_create(args, subscription_string: str):
    """Returns a subscription for creating an object.
    Arguments:
		args: a dictionary of arguments for the template. The fucntion calling this function is responsible for validating the arguments.

    Returns:
        The string for the mutation for creating the object.
    Raises:
        Assertion error if the input language is not one of the supported languages.
    """

    create_subscription = subscription_string.format(parameters=make_parameters(**args))
    return SUBSCRIPTION.format(subscription=create_subscription)
