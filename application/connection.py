import aiohttp
import asyncio
import requests
# from trompace.mutations.application import mutation_create_application, mutation_add_entrypoint_application


async def submit_query(querystr: str):
    q = {"query": querystr}
    server = 'http://localhost:4000'
    r = requests.post(server, json=q)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        print("error")
        print(r.json())
        print(querystr)
    return r.json()




