import configparser

import requests


config = configparser.ConfigParser()
config.read('import.ini')


def submit_query(querystr: str):
    q = {"query": querystr}
    server = config["import"]["server"]
    r = requests.post(server, json=q)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("error")
        print(r.json())
        print(querystr)
    return r.json()



