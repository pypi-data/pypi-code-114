import asyncio
from aiohttp_requests import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import re



def toDomain(url):
    return re.sub(r'^https?://', '', url)


async def get_sites(sem,url, esclient,index, forcecreate=False, timeout=10):
    async with sem:    
        print(url)
        domain = toDomain(url)
        exists = False
        if not forcecreate:
            try:
                esclient.get(index=index, id=domain)
                exists = True
            except Exception as e:
                exists = False
        if not exists:
            try:
                res = await requests.get('http://'+domain, timeout=timeout)
                page = await res.text()
                doc= {
                    'domain': domain,
                    'url': url,
                    'status_code': res.status,
                    'htmlraw': page,
                    'last_scan':datetime.now()
                }
                
            except Exception as e:
                doc= {
                    'domain': domain,
                    'url': url,
                    'status_code': -1,
                    'htmlraw': 'timeout',
                    'last_scan':datetime.now()
                }
            esclient.update(index="foxhouse", id=url, body={"doc":doc},doc_as_upsert=True)


async def scrapeurlses(urls, esclient, index, forcecreate=False,timeout=10, njobs=50):
    # esclient is an instance of Elasticsearch client
    tasks = []
    sem = asyncio.Semaphore(njobs)
    for url in urls:
        tasks.append(asyncio.create_task(get_sites(sem,url,esclient,index, forcecreate, timeout)))
    await asyncio.gather(*tasks)
