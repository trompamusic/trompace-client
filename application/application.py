# Generate GraphQL queries to setup a software application, entrypoint and the associated control action, property and propoerty value specification.
import asyncio
import websockets
import json
import numpy as np


from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction, mutation_modify_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from trompace.mutations.document import mutation_create_document, mutation_add_digital_document_controlaction
from .connection import submit_query, download_file
from trompace.subscriptions.controlaction import subscription_controlaction


from essentia.streaming import VectorInput, FrameCutter, Chromagram
from essentia import Pool, run
from essentia.standard import MonoLoader

def chroma(filename, fs=44100, frame_size=32768):
    audio = MonoLoader(filename=filename)()
    hop_size = frame_size // 2
    vectorinput = VectorInput(audio)
    framecutter = FrameCutter(frameSize=frame_size, hopSize=hop_size)
    chromagram = Chromagram(sampleRate=fs)
    pool = Pool()
    vectorinput.data >> framecutter.signal
    framecutter.frame >> chromagram.frame
    chromagram.chromagram >> (pool, 'chromagram')
    run(vectorinput)
    return pool['chromagram']

def print_dict(dicty):
    if isinstance(dicty,dict):
        for keys in dicty.keys():
            print("{}: ".format(keys), end ="\n ")
            print_dict(dicty[keys])
    else:
        print(dicty)
def get_sub_dict(query):
    payload = {"variables":{},
    "extensions": {},
    # "operationName":StringConstant("null").value,
    "query": query}
    message = {"id":"1",
    "type":"start",
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
async def dummy_function(inputs):
    return inputs


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
    add_propertyvalue_controlaction_query= mutation_add_controlaction_propertyvaluespecification(created_ca_id, created_propertyvaluespec_id)
    resp = await submit_query(add_propertyvalue_controlaction_query)

    print(resp)

    return created_app_id, created_ep_id, created_ca_id, created_property_id, created_propertyvaluespec_id


async def subscribe_controlaction(entrypoint_id):
    """
    Sends a subscribtion request for the control action pertaining to the input control_id.
    Establishes a websockets connection with the GraphQl database and waits for calls to the application linked to the control action
    Arguments:
        entrypoint_id: the identifier for the entry point linked to the control action to subscribe to.
    TODO:
        set uri in the config file instead of hardcoded here.
        I
    """
    uri = "ws://127.0.0.1:4000/graphql"
    is_ok = False
    subs = subscription_controlaction(entrypoint_id)
    async with websockets.connect(uri, subprotocols=['graphql-ws']) as websocket:
        await websocket.send(INIT_STR)
        async for message in websocket:
            if message == """{"type":"connection_ack"}""":
                is_ok = True
                print("Ack recieved")
                await websocket.send(get_sub_dict(subs))
            elif is_ok:
                print("Message recieved, processesing")
                control_id = json.loads(message)["payload"]["data"]["ControlActionRequest"]["identifier"]
                await handle_control_action(control_id)
                break
            if not is_ok:
                raise Exception("don't have an ack yet")


async def handle_control_action(identifier):
    """
    A function to handle a control action request, for now, just a plceholder, needs to be adapted to fit any function
    """

    input_url, output_name = await get_control_action_id(identifier)
    query_modify_ca = mutation_modify_controlaction(identifier, "running")
    resp = await submit_query(query_modify_ca)
    await download_file(input_url, "./"+input_url.split("/")[-1])
    print("Downloaded File")
    #This part should be changed

    chroma_output = chroma("./"+input_url.split("/")[-1])
    np.save("./"+output_name, chroma_output)

    create_doc_query = mutation_create_document(output_name, "UPF", "IPF", "www.upf.edu", "./"+output_name,
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

    entry_point_ids = {y: {"Id": x['identifier'], "Description": x['description'], x['potentialAction'][0]['__typename']+"_id": x['potentialAction'][0]['identifier']\
    , x['potentialAction'][0]['__typename']+"_name": x['potentialAction'][0]['name']\
        , x['potentialAction'][0]['__typename']+"_properties": {z['__typename']+'_id': z['identifier'] for z in x['potentialAction'][0]['object']}}\
        for y,x in enumerate(resp['data']['EntryPoint'])}

    print("Found the following actions: ")

    print_dict(entry_point_ids)


async def get_control_action_id(control_id):
    """
    Get document from control action id
    """
    query_ca = QUERY_CONTROLACTION_ID.format(identifier=control_id)
    resp = await submit_query(query_ca)
    ob = resp['data']['ControlAction'][0]['object']

    if isinstance(ob[0]['nodeValue'], dict):
        input_url = ob[0]['nodeValue']['source']
        output_name = ob[1]['value']
    else:
        input_url = ob[1]['nodeValue']['source']
        output_name = ob[0]['value']
    return input_url, output_name




