import asyncio
import websockets
import json

from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluepsecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from application.connection import submit_query
from application.application import create_application

INIT_STR = """{"type":"connection_init","payload":{}}"""

QUERY = '''{"id":"1","type":"start","payload":{"variables":{},"extensions":{},"operationName":null,"query":'''

pq_1 = """query{
  ControlAction {
    identifier
    description
    name
    actionStatus
    target {
      identifier
      title
      __typename
    }
    object {
      ... on MetadataInterface {
        identifier
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

# def get_sub_dict(query):
#     payload = {"variables":{},
#     "extensions": {},
#     # "operationName":StringConstant("null").value,
#     "query": query}
#     message = {"id":"1",
#     "type":"start",
#     "payload": payload}
#     return json.dumps(message)

# async def main():
#     created_application = mutation_create_application("Verovio MusicXML Converter", "https://www.verovio.org", "Verovio",
#                                         "https://github.com/rism-ch/verovio","Music notation engraving library for MEI with MusicXML,Humdrum support, toolkits, JavaScript, Python",
#                                         "Verovio supports conversion from MusicXML to MEI. When converting from this web interface, the resulting MEI data will be displayed directly in the MEI-Viewer.\
#                                          The MEI file can be saved through the MEI  button that will be displayed on the top right.","en")
#     print(created_application)
#     resp = await submit_query(created_application)
#     print(resp)
#     created_app_id = resp['data']['CreateSoftwareApplication']['identifier']
#     created_entrypoint = mutation_create_entry_point("Verovio MusicXML Converter", "https://www.verovio.org", "Music notation engraving library for MEI with MusicXML,Humdrum support, toolkits, JavaScript, Python",
#                                         "Verovio supports conversion from MusicXML to MEI. When converting from this web interface, the resulting MEI data will be displayed directly in the MEI-Viewer. \
#                                         The MEI file can be saved through the MEI  button that will be displayed on the top right.","Verovio", "https://github.com/rism-ch/verovio","en", "TROMPA algorithm proof of concept.", ["json"],["text"], identifier="d7a3b614-4c40-413f-99d6-c0da2c844963")
#     print(created_entrypoint)
#     resp = await submit_query(created_entrypoint)
#     print(resp)
#     created_ep_id = resp['data']['CreateEntryPoint']['identifier']
#     created_add_entrypoint = mutation_add_entrypoint_application(created_app_id, created_ep_id)
#     print(created_add_entrypoint)
#     resp = await submit_query(created_add_entrypoint)
#     print(resp)
#     created_control_action = mutation_create_controlaction("MusicXML to MEI conversion", "Make Bubbles", "accepted")
#     print(created_control_action)
#     resp = await submit_query(created_control_action)
#     print(resp)
#     created_ca_id = resp['data']['CreateControlAction']['identifier']
#     created_match = mutation_add_entrypoint_controlaction(created_ep_id, created_ca_id)
#     print(created_match)
#     resp = await submit_query(created_match)
#     print(resp)
#     created_property = mutation_create_property("MusicXML file", "targetFile", "Select a MusicXML file to be converted.", ["DigitalDocument"])
#     print(created_property)
#     resp = await submit_query(created_property)
#     print(resp)
#     created_property_id = resp['data']['CreateProperty']['identifier']
#     created_match = mutation_add_controlaction_property(created_ca_id, created_property_id)
#     print(created_match)
#     resp = await submit_query(created_match)
#     print(resp)
#     created_propertyvaluespecification= mutation_create_propertyvaluespecification("Result name", "What Bubble would you like to give.", "", 100, 4, False, "resultName", "String", True)
    
#     print(created_propertyvaluespecification)
#     resp = await submit_query(created_propertyvaluespecification)
#     print(resp)
#     created_propertyvaluespec_id = resp['data']['CreatePropertyValueSpecification']['identifier']
#     created_match = mutation_add_controlaction_propertyvaluepsecification(created_ca_id, created_propertyvaluespec_id)
#     print(created_match)
#     resp = await submit_query(created_match)
#     print(resp)
#     subs = subscription_controlaction(created_ep_id)
#     await client(subs)


# async def consumer(message):
#     print("got a message")
#     print(message)

# async def handle_control_action(identifier):
#     print(identifier)


# async def client(subs):
#     uri = "ws://127.0.0.1:4000/graphql"
#     is_ok = False
#     async with websockets.connect(uri, subprotocols=['graphql-ws']) as websocket:
#         await websocket.send(INIT_STR)
#         async for message in websocket:
#             if message == """{"type":"connection_ack"}""":
#                 is_ok = True
#                 print("Ack recieved")
#                 # import pdb;pdb.set_trace()c
#                 await websocket.send(get_sub_dict(subs))
#             elif is_ok:
#                 # import pdb;pdb.set_trace()
#                 control_id = json.loads(message)["payload"]["data"]["ControlActionRequest"]["identifier"]
#                 await handle_control_action(control_id)
#                 break
#             if not is_ok:
#                 raise Exception("don't have an ack yet")
# # asyncio.get_event_loop().run_until_complete(client())


async def main():
    application_name = "UPF magic doer"
    subject = "This app can do magic"
    description = "Wow, we can do magic now"
    source = "www.upf.org/magic"
    formatin = "wav"
    actionStatus = "accepted"
    actionPlatform = "The magic platform"
    contentType = ["json"]
    encodingType = ["text"]
    property_name = "Magic input"
    property_title = "Targetfile"
    property_description = "This is a magical input"
    rangeIncludes = ["DigitalDocument"]
    value_name = "Name of the output file"
    value_description = "How would you like to name the output"
    defaultValue = ""
    valueMaxLength = 100
    valueMinLength = 0
    multipleValues = False
    valueName = "outputName"
    valuePattern = "String"
    valueRequired = True
    contributor = "UPF"
    creator = "www.upf.edu"
    language = "en"

    created_app_id, created_ep_id, created_ca_id, created_property_id, created_propertyvaluespec_id = await create_application(application_name, subject, description, source, formatin, actionStatus, actionPlatform, contentType,\
        encodingType,property_title, property_name, property_description, rangeIncludes,
        value_name, value_description, defaultValue, valueMaxLength, valueMinLength , multipleValues,
        valueName, valuePattern, valueRequired, language, contributor, creator)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # subs = subscription_controlaction(32)
    # query = get_sub_dict(subs)
    import pdb;pdb.set_trace()







