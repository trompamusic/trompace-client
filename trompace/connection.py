# Utility functions for sending queries and downloading files.
import requests

from trompace.config import config
from trompace.exceptions import QueryException


async def submit_query_async(querystr: str, auth_required=False):
    """Submit a query to the CE (async).
    Arguments:
        querystr: The query to be submitted
        auth_required: If true, send an authentication key with this request. Don't send a key
           if the global config.server_auth_required is false
    """
    q = {"query": querystr}
    headers = {}
    if auth_required and config.server_auth_required:
        token = config.jwt_token
        headers["Authorization"] = f"Bearer {token}"
    r = requests.post(config.host, json=q, headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("error")
        print(r.content)
    try:
        resp = r.json()
        if "errors" in resp.keys():
            raise QueryException(resp['errors'])
    except ValueError:
        raise QueryException(r.content)
    return resp


def submit_query(querystr: str, auth_required=False):
    """Submit a query to the CE.
    Arguments:
        querystr: The query to be submitted
        auth_required: If true, send an authentication key with this request. Don't send a key
           if the global config.server_auth_required is false
    """
    q = {"query": querystr}
    headers = {}
    if auth_required and config.server_auth_required:
        token = config.jwt_token
        headers["Authorization"] = f"Bearer {token}"
    r = requests.post(config.host, json=q, headers=headers)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("error")
        print(r.content)
    try:
        resp = r.json()
        if "errors" in resp.keys():
            raise QueryException(resp['errors'])
    except ValueError:
        raise QueryException(r.content)
    return resp


async def download_file_async(url, file_link):
    """
    Downloads a file linked by the URL as saves it in the link provided in file_link.
    Arguments:
    url: url for the file to be downloaded
    file_link: the path to save the file in
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_link, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

def download_file(url, file_link):
    """
    Downloads a file linked by the URL as saves it in the link provided in file_link.
    Arguments:
    url: url for the file to be downloaded
    file_link: the path to save the file in
    """
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_link, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)