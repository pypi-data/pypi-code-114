import json
import time
from typing import List

from wxcloud.mappings import Model

def read_from_file(c, data, after, tag):
    with open(data, 'r') as f:
        data = json.load(f)
        for item in data:
            m = Model()
            m.tag = tag
            m.decode_from_webscraper(item)

            if m.when != None and m.when != '' and time.strptime(m.when, '%Y/%m/%d') >= time.strptime(after, '%Y/%m/%d'):
                c.data.append(m)

def filter_existed_data(results, data):
    result: List = []
    for i in data:
        exists: bool = False
        for j in results:
            d = json.loads(j)
            if i.digest == d['digest']:
                exists = True
                break
        if not exists:
            result.append(i)
    return result
