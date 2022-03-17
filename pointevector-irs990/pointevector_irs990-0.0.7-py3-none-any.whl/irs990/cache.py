import csv
import logging
from pathlib import Path
from typing import Any, List
import zipfile

from pointevector.irs990.config import CacheConfig, Config
from pointevector.xml_parser import ParserConfig, parse

def gen_records(config: Config, parser_config: ParserConfig):
    cache_path = config['cache']['cache_directory']

    with open(cache_path.joinpath('index.csv'), 'r') as f:
        # Open caches
        index = csv.DictReader(f)
        archives = {a: zipfile.ZipFile(cache_path.joinpath(a)) for a in set(r['archive'] for r in index)}

        # Reset DictReader and ignore header
        f.seek(0)
        next(index)

        # Get records
        for row in index:
            yield (
                cache_path.joinpath(row['archive']),
                row['filename'],
                parse(
                    config=parser_config,
                    data=archives[row['archive']].open(row['filename']),
                ),
            )

def _csv_column_values(filename: Path, column_name: str):
    with open(filename, 'r') as f:
        for row in csv.DictReader(f):
            yield row[column_name]

def _partitions(config: CacheConfig):
    for item in _csv_column_values(config['company_map'], config['partition_dimension']):
        for dim in item.split(';'):
            yield dim

def _filter_csv_column_by_values(filename: Path, column_name: str, by_values: List[Any]):
    with open(filename, 'r') as f:
        for record in csv.DictReader(f):
            if record[column_name] in by_values:
                yield record

def _load_map(filename: Path):
    return {
        row['ein']: {
            'organization_name': row['organization_name'],
            'dance_styles': row['dance_styles'],
        } for row in csv.DictReader(open(filename, 'r'))
    }

def _partitions_from_index_record(config: CacheConfig):
    def _internal(record):
        for dim in map.get(record['ein'])[config['partition_dimension']].split(';'):
            yield dim
    
    map = _load_map(config['company_map'])
    return _internal

def build(config: CacheConfig):
    archive_path = config['archive_directory']
    record_partitions = _partitions_from_index_record(config)

    reduced_index = list(_filter_csv_column_by_values(
        filename=archive_path.joinpath('index.csv'),
        column_name='ein',
        by_values=set(_csv_column_values(config['company_map'], 'ein')),
    ))
    
    caches = {
        cache: zipfile.ZipFile(
            file=f"{config['cache_directory'].joinpath(cache)}.zip",
            mode='w',
            compression=zipfile.ZIP_DEFLATED,
        ) for cache in _partitions(config)
    }
    unique_archives = set(_csv_column_values(archive_path.joinpath('index.csv'), 'archive'))
    for archive in unique_archives:
        with zipfile.ZipFile(archive_path.joinpath(archive)) as a:
            for record in filter(lambda r: r['archive'] == archive, reduced_index):
                data = a.read(record['filename'])
                for dim in record_partitions(record):
                    try:
                        caches[dim].writestr(record['filename'], data)
                    except zipfile.BadZipFile as e:
                        logging.warning(f"{e}: {record}")
