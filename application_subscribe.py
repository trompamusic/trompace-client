import asyncio
import websockets
import json
import sys

from trompace.mutations import StringConstant
from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application
from trompace.mutations.entrypoint import mutation_create_entry_point
from trompace.mutations.controlaction import mutation_create_controlaction, mutation_add_entrypoint_controlaction
from trompace.mutations.property import mutation_create_property, mutation_create_propertyvaluespecification, mutation_add_controlaction_propertyvaluepsecification, mutation_add_controlaction_property
from trompace.subscriptions.controlaction import subscription_controlaction
from application.connection import submit_query
from application.application import subscribe_controlaction


async def main(created_ep_id):
    await subscribe_controlaction(created_ep_id)
    

    # await get_control_all_actions()
    # await get_control_action_id("8e5f0994-a962-4e57-854d-b5621c6fee3c")

if __name__ == '__main__':
    if len(sys.argv)<2 or sys.argv[1] == '-help' or sys.argv[1] == '--help' or sys.argv[1] == '--h' or sys.argv[1] == '-h':
        print("%s --help or -h or --h or -help to see this menu" % sys.argv[0])
    elif sys.argv[1] == '-e' or sys.argv[1] == '--e' or sys.argv[1] == '--eval' or sys.argv[1] == '-eval':
        if len(sys.argv)<3:
            print("Please give a hdf5 file to evaluate")
        else:
            file_name = sys.argv[2]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(main(file_name))







