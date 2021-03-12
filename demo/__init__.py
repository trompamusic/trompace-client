from trompace import connection
from trompace.config import config
config.load()


def send_query_and_get_id(query, return_type=None):
    response = connection.submit_query(query, auth_required=True)
    data = response.get("data")
    print(f"Getting type {return_type} with this data:")
    print(data)
    if data and return_type:
        item = data.get(return_type)
        if item:
            return item["identifier"]
    return None
