import asyncio
import configparser
import json

import websockets

from trompace import StringConstant, make_parameters
from trompace.connection import submit_query
from trompace.exceptions import ValueNotFound
from trompace.subscriptions.controlaction import subscription_controlaction_client

INIT_STR = """{"type":"connection_init","payload":{}}"""

property_object = """  propertyObject: [{{potentialActionPropertyIdentifier:"{property_id}",
    nodeIdentifier:"{doc_id}",
    nodeType:DigitalDocument}}]"""

property_value_object = """  propertyValueObject: [{{potentialActionPropertyValueSpecificationIdentifier:"{propertyvalue_id}",
    value:"{output_name}",
    valuePattern:String}}"""

q1 = """mutation{{
RequestControlAction(
  controlAction: {{
{params}
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
    if isinstance(dicty, dict):
        for keys in dicty.keys():
            print("{}: ".format(keys), end="\n ")
            print_dict(dicty[keys])
    else:
        print(dicty)


def get_sub_dict(query):
    payload = {"variables": {},
               "extensions": {},
               # "operationName":StringConstant("null").value,
               "query": query}
    message = {"id": "1",
               "type": "start",
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


async def request_controlaction(req_config_file='req_config1.ini'):
    """
    Request a control action based on the configurations in the req_config_file
    Arguments:
        req_config_file: The ini file with the configuration for the request to be sent.
    Raises:
        ValueNotFound exception if one of the required values for the property or property value specifications is not set.
    """
    config = configparser.ConfigParser()
    config.read(req_config_file)

    entrypoint_id = config['EntryPoint']['ce_id']
    controlaction_id = config['ControlAction']['ce_id']
    num_props = int(config['ControlAction']['numprops'])
    num_pvs = int(config['ControlAction']['numpvs'])
    props = []
    pvss = []
    for i in range(num_props):
        prop_dict = {}
        prop = config['Property{}'.format(i + 1)]
        prop_dict['potentialActionPropertyIdentifier'] = prop['ce_id']
        if prop['value'] == '':
            raise ValueNotFound('potentialActionPropertyIdentifier{}'.format(1 + 1))
        prop_dict['nodeIdentifier'] = prop['value']
        prop_dict['nodeType'] = StringConstant(prop['rangeincludes'])
        # TODO: Right now, assumes that only one value is given.
        prop_params = make_parameters(**prop_dict)
        props.append("{{{}}}".format(prop_params))

    for i in range(num_pvs):
        pvs_dict = {}
        pvs = config['PropertyValueSpecification{}'.format(i + 1)]
        pvs_dict['potentialActionPropertyValueSpecificationIdentifier'] = pvs['ce_id']
        if pvs['value'] == '' and pvs.getboolean('valuerequired'):
            raise ValueNotFound('potentialActionPropertyValueSpecificationIdentifier{}'.format(1 + 1))
        pvs_dict['value'] = pvs['value']
        pvs_dict['valuePattern'] = StringConstant(pvs['valuepattern'])
        pvs_params = make_parameters(**pvs_dict)
        pvss.append("{{{}}}".format(pvs_params))
    param_dict = {"entryPointIdentifier": entrypoint_id, "potentialActionIdentifier": controlaction_id, \
                  "propertyObject": props, "propertyValueObject": pvss}
    params = make_parameters(**param_dict)

    params = params.replace("\\n", "\n").replace("\\", "").replace("\"\"", "\"").replace("\"{", "{").replace("}\"", "}")

    query = q1.format(params=params)

    resp_1 = await submit_query(query)

    output_id = resp_1['data']['RequestControlAction']['identifier']

    # await subscribe_controlaction(control_id)

    status_query = q2.format(control_id=output_id)

    act_status = 'accepted'

    while act_status == 'accepted' or act_status == 'running':
        await asyncio.sleep(1)

        resp_2 = await submit_query(status_query)

        act_status = resp_2['data']['ControlAction'][0]['actionStatus']

        print("Action Status: {}".format(act_status))


async def main(req_config_file='req_config1.ini'):
    await request_controlaction(req_config_file)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
