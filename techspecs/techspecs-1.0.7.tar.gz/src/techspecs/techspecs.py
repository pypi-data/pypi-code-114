import json
import requests


def search(techspecs_base, query: dict, techspecs_key, mode='raw'):
    q = query["keyword"].strip()
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/api/product/search?query={q}'
    header = {
        "Accept": "application/json",
        "x-blobr-key": techspecs_key.strip(),
        "Content-Type": "application/json"
    }
    payload = {"category": query['category'].strip()}
    req = requests.post(url, json=payload, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['results']
            return json.dumps(mod_list, indent=4)
        except:
            return req

    else:
        return 'Invalid Mode'


def detail(techspecs_base, techspecs_id, techspecs_key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/api/product/get/{techspecs_id.strip()}'
    header = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "x-blobr-key": techspecs_key.strip()
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['product']
            modified_data = []
            for m in mod_list:
                mod_dict = {}
                for a, b in m.items():
                    try:
                        mod_dict[a] = b
                    except:
                        for x, y in b:
                            mod_dict[x] = y
                modified_data.append(mod_dict)
            return json.dumps(modified_data, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def brands(techspecs_base, techspecs_key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/api/product/brands'
    header = {
        "Accept": "application/json",
        "x-blobr-key": techspecs_key.strip()
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['brands']
            return json.dumps(mod_list, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def categories(techspecs_base, techspecs_key, mode='raw'):
    url = f'https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/api/category/getAll'
    header = {
        "Accept": "application/json",
        "x-blobr-key": techspecs_key.strip()
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['Category']
            return json.dumps(mod_list[1], indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def products(techspecs_base, brand: list, category: list, date: dict, page, techspecs_key, mode='raw'):
    url = f"https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/api/product/getAll?page=" + str(page)
    payload = {
        "brand": brand,
        "category": category,
        "from": date['from'],
        "to": date['to']
    }
    header = {
        "Accept": "application/json",
        "X-BLOBR-KEY": techspecs_key.strip(),
        "Content-Type": "application/json"
    }
    req = requests.post(url, json=payload, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        try:
            mod_list = req['data']['product']
            return json.dumps(mod_list, indent=4)
        except:
            return req
    else:
        return 'Invalid Mode'


def apple_machine_id(techspecs_base, machine_id, techspecs_key, mode='raw'):
    url = f"https://apis.dashboard.techspecs.io/{techspecs_base.strip()}/MachineIDLookup?q={machine_id.strip()}"
    header = {
        "Accept": "application/json",
        "X-BLOBR-KEY": techspecs_key.strip()
    }
    req = requests.get(url, headers=header).json()
    if mode == 'raw':
        return req
    elif mode == 'pretty':
        return json.dumps(req, indent=4)
    else:
        return 'Invalid Mode'
