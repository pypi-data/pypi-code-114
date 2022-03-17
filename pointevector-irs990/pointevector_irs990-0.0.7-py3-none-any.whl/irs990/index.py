import csv
import io
from pathlib import Path
import zipfile

from pointevector.irs990.config import CacheConfig
from pointevector.xml_parser import ParserConfig, parse

def _gen_filings(directory: Path):
    for archive in directory.glob('*.zip'):
        with zipfile.ZipFile(archive) as z:
            for filename in z.filelist:
                yield (archive.name, filename, z.open(filename).read())

def _worker(item, indexer: ParserConfig):
    archive, file_info, content = item
    results = parse(config=indexer, data=io.BytesIO(content))
    results['archive'] = archive
    results['filename'] = file_info.filename
    return results

def _get_fields(parser: ParserConfig):
    for t in ParserConfig.__annotations__:
        for k in parser.get(t, {}):
            yield k
    yield 'archive'
    yield 'filename'

def build(config: CacheConfig, cache: bool=True):
    directory = config['cache_directory'] if cache else config['archive_directory']
    print([i for i in _get_fields(config['parser'])])
    print(next(_worker(item, config['parser']).keys() for item in _gen_filings(directory)))
    with open(directory.joinpath('index.csv'), 'w') as f:
        index = csv.DictWriter(f, fieldnames=[f for f in _get_fields(config['parser'])], extrasaction='ignore')
        index.writeheader()
        index.writerows(_worker(item, config['parser']) for item in _gen_filings(directory))
