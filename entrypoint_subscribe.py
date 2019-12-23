import asyncio
import websockets
import json
import sys
import configparser

from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from trompace.connection import submit_query
from trompace.application.application import subscribe_controlaction




async def main(app_config_file='app_config.ini', ep_config_file='ep_config.ini'):

    config_ep = configparser.ConfigParser()
    config_ep.read(ep_config_file)

    ep = config_ep['EntryPoint'] 
    ca = config_ep['ControlAction']

    entrypoint_name = ep['name']
    description_ep = ep['description']
    actionPlatform = ep['actionplatform']
    contentType = ep['contenttype'].split(',')
    encodingType = ep['encodingtype'].split(',')
    formatin =ep['formatin']
    ep_id = ep['ce_id']

    control_name = ca['name']
    description_ca = ca['description']
    actionStatus = ca['actionstatus']
    ca_id = ca['ce_id']
    command_line = ca['command_line']
    num_properties = int(ca['numproperties'])
    num_propertyvalues = int(ca['numpropertyvaluespecifications'])

    properties = []
    property_values = []

    for i in range(num_properties):
        pro = config_ep['Property{}'.format(i+1)]
        property_title = pro['title']
        properties.append(property_title)
        #TODO: Add type of expected document, based on RangeIncludes

    for i in range(num_propertyvalues):
        pro = config_ep['PropertyValueSpecification{}'.format(i+1)]
        value_name = pro['valuename']
        property_values.append(value_name)
        #TODO: Add optional value based on valueRequired.


    await subscribe_controlaction(ep_id, command_line, properties, property_values)

if __name__ == '__main__':
    # if len(sys.argv)<2 or sys.argv[1] == '-help' or sys.argv[1] == '--help' or sys.argv[1] == '--h' or sys.argv[1] == '-h':
    #     print("%s --help or -h or --h or -help to see this menu" % sys.argv[0])
    # elif sys.argv[1] == '-e' or sys.argv[1] == '--e' or sys.argv[1] == '--eval' or sys.argv[1] == '-eval':
    #     if len(sys.argv)<3:
    #         print("Please give a hdf5 file to evaluate")
    #     else:
            # file_name = sys.argv[2]
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())







