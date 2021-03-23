from trompace import connection
from trompace.config import config
config.load()


def send_query_and_get_id(query, return_type=None):
    response = connection.submit_query(query, auth_required=True)
    data = response.get("data")
    if data and return_type:
        item = data.get(return_type)
        if item:
            if isinstance(item, list):
                return [i["identifier"] for i in item]
            return item["identifier"]
    return None
