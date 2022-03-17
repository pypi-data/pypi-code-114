#!/usr/bin/env python3

"""
    Delete JAWS AVRO schemas from the Schema Registry
"""

import os
import json
import pkgutil
import traceback

from confluent_kafka.schema_registry import SchemaRegistryClient, SchemaRegistryError

scriptpath = os.path.dirname(os.path.realpath(__file__))
projectpath = scriptpath + '/../../'

sr_conf = {'url':  os.environ.get('SCHEMA_REGISTRY', 'http://localhost:8081')}
client = SchemaRegistryClient(sr_conf)


def __process(record):
    try:
        versions = client.delete_subject(record['subject'], True)
        print('Successfully deleted {}; versions: {}'.format(record['subject'], versions))
    except SchemaRegistryError:
        print('Unable to delete: {}'.format(record['subject']))
        traceback.print_exc()


def delete_schemas() -> None:
    """
        Delete JAWS AVRO schemas from the Schema Registry
    """
    conf = os.environ.get('SCHEMA_CONFIG', projectpath + 'config/schema-registry.json')

    conf = pkgutil.get_data("jlab_jaws", "avro/schema-registry.json")

    records = json.loads(conf)

    records.reverse()

    for record in records:
        __process(record)


if __name__ == "__main__":
    delete_schemas()
