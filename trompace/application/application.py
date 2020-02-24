# Generate GraphQL queries to setup a software application, entrypoint and the associated control action, property and propoerty value specification.
import json
import os

import websockets

import trompace.config as config
from trompace.connection import submit_query, download_file
from trompace.exceptions import QueryException
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction, \
    mutation_modify_controlaction
from trompace.mutations.document import mutation_create_document, mutation_add_digital_document_controlaction
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, \
    mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction


def get_sub_dict(query):
    payload = {"variables": {},
               "extensions": {},
               "query": query}
    message = {"id": "1",
               "type": "start",
               "payload": payload}
    return json.dumps(message)


INIT_STR = """{"type":"connection_init","payload":{}}"""

QUERY_ENTRYPOINT = """query{
  EntryPoint {
    identifier
    title
    description
    contentType
    subject
    potentialAction {
      __typename
      ... on ControlAction {
        identifier
        name
        object {
          __typename
          ... on Property {
            identifier
            title
            description
            rangeIncludes
            __typename
          }
          ... on PropertyValueSpecification {
            identifier
            title
            valueName
            valueRequired
            valuePattern
            description
            defaultValue
            minValue
            maxValue
            stepValue
            __typename
          }
        }
        __typename
      }
    }
    __typename
  }
}
"""
QUERY_CONTROLACTION_ID = """
    query {{
        ControlAction(identifier: "{identifier}") {{
            actionStatus
            identifier
            object {{
                ... on PropertyValue {{
                    value
                    name
                    nodeValue {{
                        ... on DigitalDocument {{
                            format
                            source
                        }}
                    }}
                }}
            }}
        }}
    }}
"""


async def create_entrypointcontrolaction_CE(created_app_id, entrypoint_name, contributor, subject, description_ep,
                                            creator, \
                                            source, language, actionPlatform, contentType, encodingType, formatin,
                                            control_name, description_ca, actionStatus):
    """
    Creates an entry point and control action in the contributor environment and linkss the two to the application.
    Arguments:
        created_app_id: The id of the application that the entry point and control actions should be linked to.
        Entry point arguments:
            entrypoint_name: The name of the entry point.
            source: The URL of the web resource to be represented by the node.
            description: A description of the application.
            formatin: The format of the input files to be used for the application.
            subject: The subject associated with the application.
            contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
            creator: The person, organization or service responsible for adding the software application.
            actionPlatform: The action platform.
            contentType: The content type associated with the entry point, should be a mimetype.
            encodingType: The encoding type associated with the entry point, should be a mimetype.
        Controal Action arguments:
                control_name: the name of the control action.
                actionStatus: The default actionStatus for a newly instantiated ControlAction ‘job'.“


    """

    create_entrypoint_query = mutation_create_entry_point(entrypoint_name, contributor, subject, description_ep,
                                                          creator, \
                                                          source, language, actionPlatform, contentType, encodingType,
                                                          formatin)
    resp = await submit_query(create_entrypoint_query)

    created_ep_id = resp['data']['CreateEntryPoint']['identifier']

    add_entrypoint_query = mutation_add_entrypoint_application(created_app_id, created_ep_id)
    resp = await submit_query(add_entrypoint_query)

    created_control_action = mutation_create_controlaction(control_name, description_ca, actionStatus)
    resp = await submit_query(created_control_action)
    created_ca_id = resp['data']['CreateControlAction']['identifier']

    add_entrypoint_controlaction_query = mutation_add_entrypoint_controlaction(created_ep_id, created_ca_id)
    resp = await submit_query(add_entrypoint_controlaction_query)
    if "errors" in resp.keys():
        raise QueryException(resp['errors'])
    return created_ep_id, created_ca_id


async def create_property_CE(property_title, property_name, property_description, rangeIncludes, created_ca_id):
    """
    Creates a property in the contributor environment and links it to the control action.
    Argument:
        created_ca_id: The contributor environment id of the control action to link the property to.
        property_title: The title of the property
        property_name: The name of the property
        property_description: An account of the property
        rangeIncludes: accepts an array of possible node types for this content reference and can be used by the \
        Component developer to limit the type of nodes (content types) that can be selected.
    """

    create_property_query = mutation_create_property(property_title, property_name, property_description, rangeIncludes)
    resp = await submit_query(create_property_query)

    created_property_id = resp['data']['CreateProperty']['identifier']
    add_controlaction_property_query = mutation_add_controlaction_property(created_ca_id, created_property_id)

    resp = await submit_query(add_controlaction_property_query)

    return created_property_id


async def create_propertyvalue_CE(created_ca_id, value_name, value_description, defaultValue, valueMaxLength,
                                  valueMinLength \
                                  , multipleValues, valueName, valuePattern, valueRequired):
    """
    Creates a property value specification in the controbutor environment and liks it to the control action.
    Arguments:
        created_ca_id: The contributor environment id of the control action to link the property value specification object to.
        value_name: The name of the property value specification.
        value_description: An account of the property
        defaultValue: the default value to use for the property value specification.
        valueMaxLength: The maximum length of the value.
        valueMinLength: The minimum length of the value.
        multipleValues: A boolean that states if multiple values are accepted or not.
        valueName: The name of the value.
        valuePattern: The format of the value.
        valueRequired: A boolean stating if the value is required or not.
    """

    create_propertyvaluespecification_query = mutation_create_propertyvaluespecification(value_name, value_description,
                                                                                         defaultValue, valueMaxLength,
                                                                                         valueMinLength \
                                                                                         , multipleValues, valueName,
                                                                                         valuePattern, valueRequired)

    resp = await submit_query(create_propertyvaluespecification_query)

    created_propertyvaluespec_id = resp['data']['CreatePropertyValueSpecification']['identifier']
    add_propertyvalue_controlaction_query = mutation_add_controlaction_propertyvaluespecification(created_ca_id,
                                                                                                  created_propertyvaluespec_id)
    resp = await submit_query(add_propertyvalue_controlaction_query)
    return created_propertyvaluespec_id


async def create_application_CE(application_name: str, subject: str, description: str, source: str, formatin: str, \
                                language: str = "en", contributor: str = "UPF", creator: str = "www.upf.edu"):
    """
    Creates an application on the Contributor Environment and returns the identifier.
    Arguments:
        application_name: The name of the application.
        source: The URL of the web resource to be represented by the node.
        description: A description of the application.
        formatin: The format of the input files to be used for the application.
        subject: The subject associated with the application.
        contributor: A person, an organization, or a service responsible for adding the software application. This can be either a name or a base URL.
        creator: The person, organization or service responsible for adding the software application.
    Returns:
        The identifiers for the created application.

    """
    create_application_query = mutation_create_application(application_name, contributor, creator, source, subject,
                                                           description, language, formatin)
    resp = await submit_query(create_application_query)

    created_app_id = resp['data']['CreateSoftwareApplication']['identifier']
    return created_app_id


async def subscribe_controlaction(entrypoint_id, command_line, num_properties, num_propertyvalues):
    """
    Sends a subscribtion request for the control action pertaining to the input control_id.
    Establishes a websockets connection with the GraphQl database and waits for calls to the application linked to the control action
    Arguments:
        entrypoint_id: the identifier for the entry point linked to the control action to subscribe to.
        command_line: The command line command for the application, must adhere to the standards proposed.
        num_properties: The number of properties related to the control action.
        num_propertyvalues: The number of property values related to the control action.
    """
    websocket_port = config.websocket_port
    print(websocket_port)
    is_ok = False
    subs = subscription_controlaction(entrypoint_id)
    async with websockets.connect(websocket_port, subprotocols=['graphql-ws']) as websocket:
        await websocket.send(INIT_STR)
        async for message in websocket:
            if message == """{"type":"connection_ack"}""":
                is_ok = True
                print("Ack recieved")
                await websocket.send(get_sub_dict(subs))
            elif is_ok:
                print("Message recieved, processesing")
                control_id = json.loads(message)["payload"]["data"]["ControlActionRequest"]["identifier"]
                await handle_control_action(control_id, command_line, num_properties, num_propertyvalues)
                break
            if not is_ok:
                raise Exception("don't have an ack yet")


async def handle_control_action(identifier, command_line, properties, property_values):
    """
    A function to handle a control action request.
    Arguments:
        identifier: the identifier for the entry point.
        command_line: The command line associated with the application associated with the entry point,
        properties: A list of required properties.
        property_values: A list of required property values.
    """

    properties, property_values = await get_control_action_id(identifier, properties, property_values)

    query_modify_ca = mutation_modify_controlaction(identifier, "running")
    resp = await submit_query(query_modify_ca)

    input_paths = []

    format_dict = {"PropertyValue{}".format(x + 1): property_values[y] for x, y in enumerate(property_values)}

    for i, pro in enumerate(properties, 1):
        # TODO: Assert that the format of the file matches the required format.

        input_url = properties[pro]['source']
        out_path = "./{}".format(input_url.split("/")[-1])

        await download_file(input_url, out_path)
        input_paths.append(out_path)
        format_dict['Property{}'.format(i)] = os.path.abspath(out_path)

        print("Downloaded File {}".format(out_path))

    os.system(command_line.format(**format_dict))

    # TODO: How to get the right output file name (possibly one of the property value specifications) and the right source path?

    create_doc_query = mutation_create_document(property_values['outputName'], "UPF", "IPF", "www.upf.edu",
                                                "./dummy_path",
                                                "output of test algorithm", "test subject", "en")
    resp = await submit_query(create_doc_query)
    created_doc_id = resp['data']['CreateDigitalDocument']['identifier']

    query_add_doc = mutation_add_digital_document_controlaction(created_doc_id, identifier)

    resp = await submit_query(query_add_doc)

    print(resp)

    query_modify_ca = mutation_modify_controlaction(identifier, "complete")
    resp = await submit_query(query_modify_ca)
    print(resp)


async def get_control_all_actions():
    """
    Submits a query to get all control actions, entry points and associated property and property value specifications.
    """
    resp = await submit_query(QUERY_ENTRYPOINT)

    entry_point_ids = {y: {"Id": x['identifier'], "Description": x['description'],
                           x['potentialAction'][0]['__typename'] + "_id": x['potentialAction'][0]['identifier'] \
        , x['potentialAction'][0]['__typename'] + "_name": x['potentialAction'][0]['name'] \
        , x['potentialAction'][0]['__typename'] + "_properties": {z['__typename'] + '_id': z['identifier'] for z in
                                                                  x['potentialAction'][0]['object']}} \
                       for y, x in enumerate(resp['data']['EntryPoint'])}

    print("Found the following actions: ")

    print_dict(entry_point_ids)


async def get_control_action_id(control_id, properties, property_values):
    """
    Get property and property value objects for the control action to be handeled.

    Arguments:
        control_id: The identifier of the control action.
        properties: A list of property names required
        property_values: A list of property value names.
    TODO:
        Add optional values using valueRequired.
    """
    query_ca = QUERY_CONTROLACTION_ID.format(identifier=control_id)
    resp = await submit_query(query_ca)
    op_pro = {}
    op_pvs = {}

    objects = resp['data']['ControlAction'][0]['object']
    for ob in objects:
        if ob['name'] in properties:
            op_pro[ob['name']] = ob['nodeValue']
        elif ob['name'] in property_values:
            op_pvs[ob['name']] = ob['value']
        else:
            raise ValueNotFound(ob['name'])
    for pro in properties:
        if pro not in op_pro.keys():
            raise ValueNotFound(pro)
    for pro in property_values:
        if pro not in op_pvs.keys():
            raise ValueNotFound(pro)

    return op_pro, op_pvs
