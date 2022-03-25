import asyncio
from aiohttp_requests import requests
import os, re

def toDomain(url):
    return re.sub(r'^https?://', '', url)


async def get_sites(sem,url,foxhousePath, forcecreate=False, timeout=10):
    async with sem:    
        print(url)
        domain = toDomain(url)
        filepath = os.path.join(foxhousePath,domain + '.html')
        if foxhousePath and forcecreate==False:
            if os.path.exists(filepath):
                return            
        try:
            res = await requests.get('http://'+domain, timeout=timeout)
            page = await res.text()
            with open(filepath,'w') as f:
                f.write(page)
        except Exception as e:
            with open(filepath,'w') as f:
                f.write('timeout')
            print(e)
        os.chmod(filepath,0o666)

async def scrapeurls(urls, foxhousePath='websites_foxhouse', forcecreate=False, timeout=10, njobs=50):
    if not os.path.exists(foxhousePath):
        os.mkdir(foxhousePath)
    tasks = []
    sem = asyncio.Semaphore(njobs)
    for url in urls:
        tasks.append(asyncio.create_task(get_sites(sem,url,foxhousePath,forcecreate, timeout)))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = ['ibm.com','idc.com']
    asyncio.run(scrapeurls(urls))