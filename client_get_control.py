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

pq_2 = """query{
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
def print_dict(dicty):
  if isinstance(dicty,dict):
    for keys in dicty.keys():
      print("{}: ".format(keys), end ="\n ")
      print_dict(dicty[keys])
  else:
    print(dicty)

async def main():
	resp_p2 = await submit_query(pq_2) 

	entry_point_ids = {y: {"Id": x['identifier'], "Description": x['description'], x['potentialAction'][0]['__typename']+"_id": x['potentialAction'][0]['identifier']\
	, x['potentialAction'][0]['__typename']+"_name": x['potentialAction'][0]['name']\
		, x['potentialAction'][0]['__typename']+"_properties": {z['__typename']+'_id': z['identifier'] for z in x['potentialAction'][0]['object']}}\
		for y,x in enumerate(resp_p2['data']['EntryPoint'])}

	print("Found the following actions: ")

	print_dict(entry_point_ids)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())