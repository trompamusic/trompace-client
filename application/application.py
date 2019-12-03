# Generate GraphQL queries to setup a software application, entrypoint and the associated control action, property and propoerty value specification.

from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluepsecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from .connection import submit_query

async def create_application(application_name: str, subject: str, description: str, source:str, formatin: str, actionStatus: str, actionPlatform:str, contentType:list,\
 encodingType: list,property_title: str, property_name: str, property_description: str, rangeIncludes: list,\
 value_name: str, value_description: str, defaultValue: str, valueMaxLength: int, valueMinLength: int , multipleValues: bool,\
  valueName: str, valuePattern: str, valueRequired: bool, language: str="en", contributor:str="UPF", creator:str= "www.upf.edu" ):

    """
    Creates an application on the Contributor Environment, with the associated entry point, control action, property object and property value specification.
    Arguments:
        application_name: The name of the application, will be re-used for the control action and entry point for now.
        source: The URL of the web resource to be represented by the node.
        description: A description of the application, will be re-used for the control action and entry point for now. 
        formatin: The format of the input files to be used for the application.
        subject: The subject associated with the application, will be re-used for control action and entry point for now. 
        actionStatus: The default actionStatus for a newly instantiated ControlAction ‘job'.
        actionPlatform: The action platform.
        contentType: The content type associated with the entry point, should be a mimetype.
        encodingType: The encoding type associated with the entry point, should be a mimetype.
        property_title: The title of the property
        property_name: The name of the property
        property_description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the Component developer to limit the type of nodes (content types) that can be selected.
        value_name: The name of the property value specification.
        value_description: An account of the property
        defaultValue: the default value to use for the property value specification.
        valueMaxLength: The maximum length of the value.
        valueMinLength: The minimum length of the value.
        multipleValues: A boolean that states if multiple values are accepted or not.
        valueName: The name of the value.
        valuePattern: The format of the value.
        valueRequired: A boolean stating if the value is required or not. 

        contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
        creator: The person, organization or service responsible for adding the software application.
    Returns:
	    The identifiers for the created application, entrypoint, control action template, property and property values sepcification.

    TODO:
	    Extend for multiple control actions, properties and property value specifications.

    """
    create_application_query = mutation_create_application(application_name, contributor, creator, source, subject, description, language, formatin)
    resp = await submit_query(create_application_query)
    #Check if response is OK or error
    created_app_id = resp['data']['CreateSoftwareApplication']['identifier']
    create_entrypoint_query = mutation_create_entry_point(application_name, contributor, subject, description, creator, source, language, actionPlatform, contentType, encodingType, formatin)
    resp = await submit_query(create_entrypoint_query)
    #Check if response is OK or error
    created_ep_id = resp['data']['CreateEntryPoint']['identifier']
    add_entrypoint_query = mutation_add_entrypoint_application(created_app_id, created_ep_id)
    resp = await submit_query(add_entrypoint_query)
    #Check if response is OK or error
    created_control_action = mutation_create_controlaction(application_name, description, actionStatus)
    resp = await submit_query(created_control_action)
    #Check if response is OK or error
    created_ca_id = resp['data']['CreateControlAction']['identifier']
    add_entrypoint_controlaction_query = mutation_add_entrypoint_controlaction(created_ep_id, created_ca_id)
    resp = await submit_query(add_entrypoint_controlaction_query)

    create_property_query = mutation_create_property(property_title, property_name, property_description, rangeIncludes)
    resp = await submit_query(create_property_query)

    created_property_id = resp['data']['CreateProperty']['identifier']
    add_controlaction_property_query = mutation_add_controlaction_property(created_ca_id, created_property_id)

    resp = await submit_query(add_controlaction_property_query)

    create_propertyvaluespecification_query = mutation_create_propertyvaluespecification(value_name, value_description, defaultValue, valueMaxLength, valueMinLength\
    	, multipleValues, valueName, valuePattern, valueRequired)

    resp = await submit_query(create_propertyvaluespecification_query)
    created_propertyvaluespec_id = resp['data']['CreatePropertyValueSpecification']['identifier']
    add_propertyvalue_controlaction_query= mutation_add_controlaction_propertyvaluepsecification(created_ca_id, created_propertyvaluespec_id)
    resp = await submit_query(add_propertyvalue_controlaction_query)

    print(resp)

    return created_app_id, created_ep_id, created_ca_id, created_property_id, created_propertyvaluespec_id








if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # subs = subscription_controlaction(32)
    # query = get_sub_dict(subs)
    import pdb;pdb.set_trace()





