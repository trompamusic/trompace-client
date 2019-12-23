# A script to get all control actions, property values and property value specifications and write ini files for input.
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


async def main():
    resp_p2 = await submit_query(pq_2)

    i = 1

    for ep in resp_p2['data']['EntryPoint']:
        

        ap_dict = {}
        ap_dict['ce_id'] = ep['identifier']
        ap_dict['title'] = ep['title']
        ap_dict['description'] = ep['description']


        for ca in ep['potentialAction']:
            parser = configparser.ConfigParser()
            ca_dict = {}
            ca_dict['ce_id'] = ca['identifier']
            ca_dict['name'] = ca['name']
            props = []
            pvs = []
            for obj in ca['object']:
                if obj['__typename'] == 'PropertyValueSpecification':
                    pvs_dict = {}
                    pvs_dict['ce_id'] = obj['identifier']
                    pvs_dict['title'] = obj['title']
                    pvs_dict['description'] = obj['description']
                    pvs_dict['value'] = obj['defaultValue']
                    pvs_dict['valueName'] = obj['valueName']
                    pvs_dict['valueRequired'] = str(obj['valueRequired'])
                    pvs_dict['valuePattern'] = obj['valuePattern']
                    pvs.append(pvs_dict)
                elif obj['__typename'] == 'Property':
                    pro_dict = {}
                    pro_dict['ce_id'] = obj['identifier']
                    pro_dict['title'] = obj['title']
                    pro_dict['value'] = ''
                    pro_dict['description'] = obj['description']
                    pro_dict['rangeIncludes'] = str(obj['rangeIncludes']).replace('[','').replace(']','').replace('\'','')
                    props.append(pro_dict)
            ca_dict['numprops'] = str(len(props))
            ca_dict['numpvs'] = str(len(pvs))

            parser.add_section('EntryPoint')
            for key in ap_dict.keys():
                parser.set('EntryPoint', key, ap_dict[key])

            parser.add_section('ControlAction')
            for key in ca_dict.keys():
                parser.set('ControlAction', key, ca_dict[key])

            for j in range(len(props)):
                parser.add_section('Property{}'.format(j+1))
                for key in props[j].keys():
                    parser.set('Property{}'.format(j+1), key, props[j][key])

            for j in range(len(pvs)):
                parser.add_section('PropertyValueSpecification{}'.format(j+1))
                for key in pvs[j].keys():
                    parser.set('PropertyValueSpecification{}'.format(j+1), key, pvs[j][key])
                    
            with open('req_config{}.ini'.format(i), 'w') as f:
                parser.write(f)
            i+=1


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
