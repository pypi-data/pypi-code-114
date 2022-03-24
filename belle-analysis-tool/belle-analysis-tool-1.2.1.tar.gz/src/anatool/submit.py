import pkgutil
from io import StringIO
import os
import csv
import urllib.parse


def run_list(dataType='on_resonance'):
    with StringIO(pkgutil.get_data(__package__, f'data/{dataType}.dat').decode()) as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield urllib.parse.urlencode(row)


def url_list(
        dataType='on_resonance',
        eventTypes=['evtgen-uds', 'evtgen-charm', 'evtgen-charged', 'evtgen-mixed'],
        stream_cardinal=0,
        exs=None,
        data=False,
    ):
    for runs in run_list():
        ex = int(urllib.parse.parse_qs(runs)['ex'][0])
        if exs and ex not in exs: continue
        if data:
            skim = 'HadronB'  if ex < 20 else 'HadronBJ'
            yield f'http://bweb3/mdst.php?{runs}&skm={skim}&dt={dataType}&bl=caseB'
        else:
            stream_base = 10 if ex < 30 else 0
            stream = stream_base + stream_cardinal
            for eventType in eventTypes:
                yield f'http://bweb3/montecarlo.php?{runs}&ty={eventType}&dt={dataType}&bl=caseB&st={stream}'


def convert_to_stem(url):
    return '_'.join(value[0] for value in urllib.parse.parse_qs(url).values())

