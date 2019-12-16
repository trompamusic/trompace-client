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
from trompace.application.application import create_application_CE

async def main():
    await create_application()


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

    ce_id = app['ce_id']
    if ce_id == '':
        print("App ce_id not found, creating new application")
        created_app_id = await create_application_CE(application_name, subject, description, source, formatin,\
        language, contributor, creator)
        config['app']['ce_id'] = created_app_id
        with open(app_config_file, 'w') as configfile: 
            config.write(configfile)
    else:
        # Todo, check if the id exists in the CE.
        print("App already exists, the id is {}".format(ce_id))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
