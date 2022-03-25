import asyncio
from aiohttp_requests import requests
from elasticsearch import Elasticsearch
from datetime import datetime
import re



def toDomain(url):
    return re.sub(r'^https?://', '', url)


async def get_sites(sem,url, esclient,index, forcecreate=False, timeout=10, convertDomain=True):
    if not url:
        return
    async with sem:    
        print(url)
        if convertDomain:
            domain = toDomain(url)
        else:
            domain = url
        if not domain:
            return
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
            domainid = domain.replace('/', '_')
            esclient.update(index="foxhouse", id=domainid, body={"doc":doc},doc_as_upsert=True)


async def scrapeurlses(urls, esclient, index, forcecreate=False,timeout=10, njobs=50,convertDomain=True):
    # esclient is an instance of Elasticsearch client
    tasks = []
    sem = asyncio.Semaphore(njobs)
    for url in urls:
        tasks.append(asyncio.create_task(get_sites(sem,url,esclient,index, forcecreate, timeout,convertDomain)))
    await asyncio.gather(*tasks)
