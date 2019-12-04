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

pq_3 = """query{
  DigitalDocument {
    identifier
    description
    format
    title
    name
  } 
}
"""

q1 = """mutation{{
RequestControlAction(
  controlAction: {{
  entryPointIdentifier: "{entrypoint_id}", 
    potentialActionIdentifier: "{controlaction_id}",
  propertyObject: [{{potentialActionPropertyIdentifier:"{property_id}",
    nodeIdentifier:"{doc_id}",
    nodeType:DigitalDocument}}],
  propertyValueObject: [{{potentialActionPropertyValueSpecificationIdentifier:"{propertyvalue_id}",
    value:"{output_name}",
    valuePattern:String}}]
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
	if isinstance(dicty,dict):
		for keys in dicty.keys():
			print("{}: ".format(keys), end ="\n ")
			print_dict(dicty[keys])
	else:
		print(dicty)



async def main():
	resp_p3 = await submit_query(pq_3)
	data_ids = { y : {"Title": x['title'], "Name": x['name'], "Id": x['identifier'], "Description": x['description']} for y, x in enumerate(resp_p3['data']['DigitalDocument'])}
	print("Found the following documents:")
	print_dict(data_ids)
	# for ids in data_ids:
	# 	print("{}".format(ids))
	# 	print("    Title: {}".format(data_ids[ids]["Title"]))
	# 	print("    Description: {}".format(data_ids[ids]["Description"]))
	data_id = int(input("Select an id between {} and {} ".format("0", len(data_ids)-1)))
	assert data_id>=0 and data_id<len(data_ids)
	resp_p1 = await submit_query(pq_1) 
	control_action_ids = [x['identifier'] for x in resp_p1['data']['ControlAction']]
	resp_p2 = await submit_query(pq_2) 

	entry_point_ids = {y: {"Id": x['identifier'], "Description": x['description'], x['potentialAction'][0]['__typename']+"_id": x['potentialAction'][0]['identifier']\
	, x['potentialAction'][0]['__typename']+"_name": x['potentialAction'][0]['name']\
		, x['potentialAction'][0]['__typename']+"_properties": {z['__typename']+'_id': z['identifier'] for z in x['potentialAction'][0]['object']}}\
		for y,x in enumerate(resp_p2['data']['EntryPoint'])}

	print("Found the following actions: ")

	print_dict(entry_point_ids)

	entry_id = int(input("Select an entry point id between {} and {} ".format("0", len(entry_point_ids)-1)))
	assert entry_id>=0 and entry_id<len(entry_point_ids)

	request_query = q1.format(entrypoint_id=entry_point_ids[entry_id]["Id"], controlaction_id=entry_point_ids[entry_id]['ControlAction_id'],\
	 property_id=entry_point_ids[entry_id]['ControlAction_properties']['Property_id'],\
	 propertyvalue_id=entry_point_ids[entry_id]['ControlAction_properties']['PropertyValueSpecification_id'], doc_id = data_ids[data_id]["Id"], output_name="File_Name.ogg")

	resp_1 = await submit_query(request_query)

	output_id = resp_1['data']['RequestControlAction']['identifier']

	status_query = q2.format(control_id=output_id)


	resp_2 = await submit_query(status_query)

	act_status = {y :{"ID": x['identifier'], "Description": x['description'], 'actionStatus': x['actionStatus'], "Errors": x['error']} for y,x in enumerate(resp_2['data']['ControlAction'])}

	print("Results:")

	print_dict(act_status)
	

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    # subs = subscription_controlaction(32)
    # query = get_sub_dict(subs)
    # import pdb;pdb.set_trace()

