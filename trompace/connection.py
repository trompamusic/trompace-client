# Utility functions for sending queries and downloading files. 
import configparser
import aiohttp
import asyncio
import requests
import aiofiles

config = configparser.ConfigParser()
config.read('import.ini')


async def submit_query(querystr: str):
    """
    Sends a query to the server set in the import.ini config file
    Arguments:
    querystr: The query to be submitted in string format. 
    """
    q = {"query": querystr}
    server = config["import"]["server"]
    r = requests.post(server, json=q)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("error")
        print(r.json())
        print(querystr)
    resp = r.json()
    if "errors" in resp.keys():
        raise QueryException(resp['errors'])
    return resp



async def download_file(url, file_link):
    """
    Downloads a file linked by the URL as saves it in the link provided in file_link.
    Arguments:
    url: url for the file to be downloaded
    file_link: the path to save the file in
    """
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_link, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk:
                    f.write(chunk)