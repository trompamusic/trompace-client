# Create the applications with the specifications in the config file

import asyncio
import websockets
import json
import configparser
import argparse

from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, \
    mutation_add_controlaction_propertyvaluespecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from trompace.connection import submit_query
from trompace.application.application import create_entrypointcontrolaction_CE, create_property_CE, \
    create_propertyvalue_CE, create_application_CE, subscribe_controlaction
from trompace.exceptions import IDNotFoundException, ConfigRequirementException
from trompace.mutations import StringConstant
from trompace.subscriptions.controlaction import subscription_controlaction
from trompace.connection import submit_query


async def main(app_config_file, ep_config_file):
    await create_entrypoint(app_config_file,
                            ep_config_file)  # Make sure the application and the entry point exist, if not, create
    await subscribe_entrypoint(app_config_file, ep_config_file)  # Subscribe to the entry point.


async def create_application(app_config_file='app_config.ini'):
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
    description = app['description']
    source = app['source']
    formatin = app['formatin']
    contributor = app['contributor']
    creator = app['creator']
    language = app['language']

    if 'ce_id' not in app.keys():
        ce_id = ''
    else:
        ce_id = app['ce_id']

    if ce_id == '':
        print("App ce_id not found, creating new application")
        created_app_id = await create_application_CE(application_name, subject, description, source, formatin, \
                                                     language, contributor, creator)
        config['app']['ce_id'] = created_app_id
        with open(app_config_file, 'w') as configfile:
            config.write(configfile)
    else:
        # Todo, check if the id exists in the CE.
        print("App already exists, the id is {}".format(ce_id))


async def create_entrypoint(app_config_file='./docs/app_config.ini', ep_config_file='./docs/ep_config.ini'):
    """
    Creates an entry point in the contributor environment based on the settings in the app_config_file. 
    Checks if the application exists already and creates one if not.
    Arguments:
    app_config_file: The path to the config file for the application. 
    ep_config_file: The path to the config file for the entry point. 
    ToDo:
    Query CE to check if the app id already exists.
    """

    config = configparser.ConfigParser()
    config.read(app_config_file)

    app = config['app']
    check_app = ['application_name', 'subject', 'source', 'formatin', 'contributor', 'creator', 'language']
    assert all(x in app.keys() for x in check_app), "{} not present in application config file".format(
        [x for x in check_app if x not in app.keys()]).replace('[', '').replace(']', '')

    application_name = app['application_name']
    subject = app['subject']
    source = app['source']
    formatin = app['formatin']
    contributor = app['contributor']
    creator = app['creator']
    language = app['language']

    if 'ce_id' not in app.keys():
        app_id = ''
    else:
        app_id = app['ce_id']

    if app_id == '':
        await create_application(app_config_file)

    config_ep = configparser.ConfigParser()
    config_ep.read(ep_config_file)

    check_eps = ['EntryPoint', 'ControlAction']

    if not all(x in config_ep.keys() for x in check_eps):
        missing_fields = [x for x in check_eps if x not in config_ep.keys()]
        raise ConfigRequirementException(missing_fields)

    ep = config_ep['EntryPoint']
    ca = config_ep['ControlAction']

    check_ep = ['name', 'description', 'actionplatform', 'contenttype', 'encodingtype', 'formatin']

    if not all(x in ep.keys() for x in check_ep):
        missing_fields = [x for x in check_ep if x not in ep.keys()]
        raise ConfigRequirementException(missing_fields)

    entrypoint_name = ep['name']
    description_ep = ep['description']
    actionPlatform = ep['actionplatform']
    contentType = ep['contenttype'].split(',')
    encodingType = ep['encodingtype'].split(',')
    formatin = ep['formatin']

    if 'ce_id' not in ep.keys():
        ep_id = ''
    else:
        ep_id = ep['ce_id']

    check_ca = ['name', 'description', 'actionstatus', 'numproperties', 'numpropertyvaluespecifications']

    if not all(x in ca.keys() for x in check_ca):
        missing_fields = [x for x in check_ca if x not in ca.keys()]
        raise ConfigRequirementException(missing_fields)

    control_name = ca['name']
    description_ca = ca['description']
    actionStatus = ca['actionstatus']
    num_properties = int(ca['numproperties'])
    num_propertyvalues = int(ca['numpropertyvaluespecifications'])

    if 'ce_id' not in ca.keys():
        ca_id = ''
    else:
        ca_id = ca['ce_id']

    if ep_id == '' and ca_id != '':
        raise IDNotFoundException("EntryPoint")
    elif ep_id != '' and ca_id == '':
        raise IDNotFoundException("ControlAction")
    elif ep_id == '' and ca_id == '':
        print("Creating and linking Control Action and Entry Point")
        created_ep_id, created_ca_id = await create_entrypointcontrolaction_CE(app_id, entrypoint_name, contributor,
                                                                               subject, description_ep, creator, \
                                                                               source, language, actionPlatform,
                                                                               contentType, encodingType, formatin,
                                                                               control_name, description_ca,
                                                                               actionStatus)
        config_ep['EntryPoint']['ce_id'] = created_ep_id
        config_ep['ControlAction']['ce_id'] = created_ca_id
        with open(ep_config_file, 'w') as configfile:
            config_ep.write(configfile)
        ep_id = created_ep_id
        ca_id = created_ca_id

    for i in range(num_properties):
        pro = config_ep['Property{}'.format(i + 1)]
        check_pro = ['name', 'title', 'description', 'rangeincludes']
        if not all(x in pro.keys() for x in check_pro):
            missing_fields = [x for x in check_pro if x not in pro.keys()]
            raise ConfigRequirementException(missing_fields)

        property_name = pro['name']
        property_title = pro['title']
        property_description = pro['description']
        rangeIncludes = [StringConstant(x) for x in pro['rangeincludes'].split(',')]
        if 'ce_id' not in pro.keys():
            pro_id = ''
        else:
            pro_id = pro['ce_id']
        if pro_id == '':
            print("Creating property {} and linking to CA".format(i + 1))
            created_property_id = await create_property_CE(property_title, property_name, property_description,
                                                           rangeIncludes, ca_id)
            config_ep['Property{}'.format(i + 1)]['ce_id'] = created_property_id
            with open(ep_config_file, 'w') as configfile:
                config_ep.write(configfile)

    for i in range(num_propertyvalues):
        pro = config_ep['PropertyValueSpecification{}'.format(i + 1)]
        check_pro = ['name', 'description', 'defaultValue', 'valuemaxlength', 'valueminlength', 'multiplevalues',
                     'valuename', 'valuepattern', 'valuerequired']
        if not all(x in pro.keys() for x in check_pro):
            missing_fields = [x for x in check_pro if x not in pro.keys()]
            raise ConfigRequirementException(missing_fields)
        value_name = pro['name']
        value_description = pro['description']
        defaultValue = pro['defaultValue']
        valueMaxLength = int(pro['valuemaxlength'])
        valueMinLength = int(pro['valueminlength'])
        multipleValues = pro.getboolean('multiplevalues')
        valueName = pro['valuename']
        valuePattern = pro['valuepattern']
        valueRequired = pro.getboolean('valuerequired')

        if 'ce_id' not in pro.keys():
            pro_id = ''
        else:
            pro_id = pro['ce_id']

        if pro_id == '':
            print("Creating property value specification {} and linking to CA".format(i + 1))
            created_id = await create_propertyvalue_CE(ca_id, value_name, value_description, defaultValue,
                                                       valueMaxLength, valueMinLength \
                                                       , multipleValues, valueName, valuePattern, valueRequired)
            config_ep['PropertyValueSpecification{}'.format(i + 1)]['ce_id'] = created_id
            with open(ep_config_file, 'w') as configfile:
                config_ep.write(configfile)


async def subscribe_entrypoint(app_config_file='app_config.ini', ep_config_file='ep_config.ini'):
    config_ep = configparser.ConfigParser()
    config_ep.read(ep_config_file)

    ep = config_ep['EntryPoint']
    ca = config_ep['ControlAction']

    entrypoint_name = ep['name']
    description_ep = ep['description']
    actionPlatform = ep['actionplatform']
    contentType = ep['contenttype'].split(',')
    encodingType = ep['encodingtype'].split(',')
    formatin = ep['formatin']
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
        pro = config_ep['Property{}'.format(i + 1)]
        property_title = pro['title']
        properties.append(property_title)
        # TODO: Add type of expected document, based on RangeIncludes

    for i in range(num_propertyvalues):
        pro = config_ep['PropertyValueSpecification{}'.format(i + 1)]
        value_name = pro['valuename']
        property_values.append(value_name)
        # TODO: Add optional value based on valueRequired.

    await subscribe_controlaction(ep_id, command_line, properties, property_values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='create software application bassed on config files')
    parser.add_argument('app_config_file', type=str, help='config file for application')
    parser.add_argument('ep_config_file', type=str, help='config file for entry point')
    args = parser.parse_args()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args.app_config_file, args.ep_config_file))
