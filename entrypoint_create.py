# Create the applications with the specifications in the config file

import asyncio
import websockets
import json
import configparser

from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification,\
 mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from trompace.connection import submit_query
from trompace.application.application import create_entrypointcontrolaction_CE, create_property_CE, create_propertyvalue_CE
from trompace.exceptions import IDNotFoundException
from trompace.mutations import StringConstant

async def main():
    await create_entrypoint()


async def create_entrypoint(app_config_file='app_config.ini', ep_config_file='ep_config.ini'):
    """
    Creates an application in the contributor environment based on the settings in the app_config_file. 
    Checks if the 
    Arguments:
    app_config_file: The path to the config file for the application. 
    ToDo:
    Query CE to check if the app id already exists.
    """

    config = configparser.ConfigParser()
    config.read(app_config_file)
    app = config['app']


    application_name = app['application_name']
    subject = app['subject']
    source = app['source']
    formatin = app['formatin']
    contributor = app['contributor']
    creator = app['creator']
    language = app['language']
    app_id = app['ce_id']

    if app_id == '':
        raise IDNotFoundException("Application")

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
    num_properties = int(ca['numproperties'])
    num_propertyvalues = int(ca['numpropertyvaluespecifications'])

    if ep_id == '' and ca_id!='':
        raise IDNotFoundException("EntryPoint")
    elif ep_id != '' and ca_id=='':
        raise IDNotFoundException("ControlAction")
    elif ep_id == '' and ca_id=='':
        print("Creating and linking Control Action and Entry Point")
        created_ep_id, created_ca_id = await create_entrypointcontrolaction_CE(app_id, entrypoint_name, contributor, subject, description_ep, creator,\
         source, language, actionPlatform, contentType, encodingType, formatin, control_name, description_ca, actionStatus)
        config_ep['EntryPoint']['ce_id'] = created_ep_id
        config_ep['ControlAction']['ce_id'] = created_ca_id
        with open(ep_config_file, 'w') as configfile: 
            config_ep.write(configfile)
        ep_id = created_ep_id
        ca_id = created_ca_id

    for i in range(num_properties):
        pro = config_ep['Property{}'.format(i+1)]
        property_name = pro['name']
        property_title = pro['title']
        property_description = pro['description']
        rangeIncludes = [StringConstant(x) for x in pro['rangeincludes'].split(',')]
        pro_id = pro['ce_id']
        if pro_id == '':
            print("Creating property {} and linking to CA".format(i+1))
            created_property_id = await create_property_CE(property_title, property_name, property_description, rangeIncludes, ca_id)
            config_ep['Property{}'.format(i+1)]['ce_id'] = created_property_id
            with open(ep_config_file, 'w') as configfile: 
                config_ep.write(configfile)         

    for i in range(num_propertyvalues):
        pro = config_ep['PropertyValueSpecification{}'.format(i+1)]
        value_name = pro['name']
        value_description = pro['description']
        defaultValue = pro['defaultValue']
        valueMaxLength = int(pro['valuemaxlength'])
        valueMinLength = int(pro['valueminlength'])
        multipleValues = pro.getboolean('multiplevalues')
        valueName = pro['valuename']
        valuePattern = pro['valuepattern']
        valueRequired = pro.getboolean('valuerequired')
        pro_id = pro['ce_id']
        if pro_id == '':
            print("Creating property value specification {} and linking to CA".format(i+1))
            created_id = await create_propertyvalue_CE(ca_id,value_name, value_description, defaultValue, valueMaxLength, valueMinLength\
                , multipleValues, valueName, valuePattern, valueRequired )
            config_ep['PropertyValueSpecification{}'.format(i+1)]['ce_id'] = created_id
            with open(ep_config_file, 'w') as configfile: 
                config_ep.write(configfile)  





    



    #     config['app']['ce_id'] = created_app_id
    #     with open(app_config_file, 'w') as configfile: 
    #         config.write(configfile)
    # else:
    #     # Todo, check if the id exists in the CE.
    #     print("App already exists, the id is {}".format(ce_id))

# [StringConstant(x) for x in ep['contenttype'].split(',')]
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
