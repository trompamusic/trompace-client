import aiohttp
import asyncio
import requests
import aiofiles
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




async def download_file(url, file_link):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(file_link, mode='wb')
                await f.write(await resp.read())
                await f.close()