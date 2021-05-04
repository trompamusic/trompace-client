# Get a list of all IDs in the CE and download each node as json-ld
import datetime
import json
import os

import requests

from trompace.config import config
from trompace import connection


def download_ids(ids):
    outdir = f"cearchive-{datetime.date.today().isoformat()}"
    host = config.host
    os.makedirs(outdir, exist_ok=True)
    total = len(ids)
    for i, id_ in enumerate(ids, 1):
        outname = os.path.join(outdir, f"{id_}.json")
        if os.path.exists(outname):
            continue
        print(f"{i}/{total}")
        print(id_)
        r = requests.get(host + "/" + id_, headers={"Accept": "application/ld+json"})
        try:
            resp = r.json()
            with open(outname, "w") as fp:
                json.dump(resp, fp, indent=2)
        except ValueError:
            print(r.content)


def get_ids():
    query = """
    query {
  ThingInterface {
    identifier
  }
}
    """
    response = connection.submit_query(query)
    data = response["data"]["ThingInterface"]
    ids = [i["identifier"] for i in data]
    return ids


if __name__ == '__main__':
    config.load()
    ids = get_ids()
    download_ids(ids)
