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
from application.application import create_application, get_control_all_actions, get_control_action_id

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

    print(created_ep_id)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())