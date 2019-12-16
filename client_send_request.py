import asyncio
import websockets
import json
import sys


from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction_client
from trompace.connection import submit_query


INIT_STR = """{"type":"connection_init","payload":{}}"""

q1 = """mutation{{
RequestControlAction(
  controlAction: {{
  entryPointIdentifier: "{entrypoint_id}", 
    potentialActionIdentifier: "{controlaction_id}",
  propertyObject: [{{potentialActionPropertyIdentifier:"{property_id}",
    nodeIdentifier:"{doc_id}",
    nodeType:DigitalDocument}}],
  propertyValueObject: [{{potentialActionPropertyValueSpecificationIdentifier:"{propertyvalue_id}",
    value:"{output_name}",
    valuePattern:String}}]
  }}) {{
    identifier
        __typename
          }}
          }}
"""

q2 = """query{{ ControlAction(identifier: "{control_id}") {{
    identifier
    description
    actionStatus
    error
    target {{
      title
      __typename
    }}
    result {{
      ... on DigitalDocument {{
        title
        source
        __typename
      }}
      __typename
    }}
    object {{
      ... on PropertyValue {{
        identifier
        title
        value
        nodeValue {{
          ... on DigitalDocument {{
            title
            source
            __typename
          }}
          __typename
        }}
        __typename
      }}
      __typename
    }}
    __typename
  }}
}}"""

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

async def subscribe_controlaction(controlaction_id):
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
    subs = subscription_controlaction_client(controlaction_id)
    print(subs)
    async with websockets.connect(uri, subprotocols=['graphql-ws']) as websocket:
        await websocket.send(INIT_STR)
        async for message in websocket:
            if message == """{"type":"connection_ack"}""":
                is_ok = True
                print("Ack recieved")
                await websocket.send(get_sub_dict(subs))
            elif is_ok:
                print(message)
                # control_id = json.loads(message)["payload"]["data"]["ControlActionRequest"]["identifier"]
                # await handle_control_action(control_id)
                break
            if not is_ok:
                raise Exception("don't have an ack yet")


async def main(entrypoint_id, control_id, property_id, propertyvalue_id, doc_id, output_name):
    request_query = q1.format(entrypoint_id = entrypoint_id, controlaction_id=control_id, property_id=property_id, propertyvalue_id=propertyvalue_id, doc_id=doc_id, output_name=output_name)
    resp_1 = await submit_query(request_query)

    output_id = resp_1['data']['RequestControlAction']['identifier']

    # await subscribe_controlaction(control_id)

    status_query = q2.format(control_id=output_id)


    resp_2 = await submit_query(status_query)

    act_status = {y :{"ID": x['identifier'], "Description": x['description'], 'actionStatus': x['actionStatus'], "Errors": x['error']} for y,x in enumerate(resp_2['data']['ControlAction'])}

    print("Results:")

    print_dict(act_status)


if __name__ == '__main__':
    if len(sys.argv)<2 or sys.argv[1] == '-help' or sys.argv[1] == '--help' or sys.argv[1] == '--h' or sys.argv[1] == '-h':
        print("%s --help or -h or --h or -help to see this menu" % sys.argv[0])
        print("%s --e entrypoint_id control_id property_id propertyvalue_id doc_id output_name" % sys.argv[0])
    elif sys.argv[1] == '-e' or sys.argv[1] == '--e' or sys.argv[1] == '--eval' or sys.argv[1] == '-eval':
        if len(sys.argv)<3:
            print("Please give a hdf5 file to evaluate")
        else:
            entrypoint_id = sys.argv[2]
            control_id = sys.argv[3]
            property_id = sys.argv[4]
            propertyvalue_id = sys.argv[5]
            doc_id = sys.argv[6]
            output_name = sys.argv[7]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(entrypoint_id, control_id, property_id, propertyvalue_id, doc_id, output_name))
