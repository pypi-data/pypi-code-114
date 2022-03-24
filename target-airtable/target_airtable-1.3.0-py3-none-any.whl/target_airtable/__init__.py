#!/usr/bin/env python3

import argparse
import collections
import io
import json
import os.path
import sys

import singer
from jsonschema.validators import Draft4Validator
from pyairtable import Table

logger = singer.get_logger()


def emit_state(state):
    if state is not None:
        line = json.dumps(state)
        logger.debug('Emitting state {}'.format(line))
        sys.stdout.write("{}\n".format(line))
        sys.stdout.flush()


def flatten(d, parent_key='', sep='__'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, str(v) if type(v) is list else v))
    return dict(items)


def process_records(config, table_name, records):
    table_obj = Table(config.get('api_token'), config.get('base'), table_name)

    # Perform record creation
    table_obj.batch_create(records, typecast=config.get("typecast", True))

    logger.info(f"Table {table_name}: {len(records)} total records processed")


def create_mapping(all_records, unique_field_name, table_records=True):
    # Create an object mapping of the primary field to the record ID
    # Scan for duplicate records in the data and raise an exception if found
    field_value_to_existing_record_id = dict()
    duplicates = set()
    for existingRecord in all_records:
        if table_records:
            unique_field_value = existingRecord['fields'].get(unique_field_name)
        else:
            unique_field_value = existingRecord.get(unique_field_name)

        if unique_field_value not in field_value_to_existing_record_id:
            field_value_to_existing_record_id[unique_field_value] = existingRecord['id']
        else:
            duplicates.add(unique_field_value)

    return field_value_to_existing_record_id, duplicates


def process_records_upsert(config, table_name, records):
    unique_field_name = config.get("unique_field_name", "id")
    table_obj = Table(config.get('api_token'), config.get('base'), table_name)

    # Retrieve all existing records from the base through the Airtable REST API
    all_existing_records = table_obj.all()
    logger.info(f"Table {table_name}: {len(all_existing_records)} existing records found")

    # map the table records and check for duplicates
    upsert_field_value_to_existing_record_id, table_duplicates = \
        create_mapping(all_existing_records, unique_field_name)
    if len(table_duplicates) > 0:
        raise ValueError(f"{len(table_duplicates)} duplicates found in table {table_name}: {table_duplicates}")

    # check the records to be upserted for duplicates
    record_duplicates = create_mapping(records, unique_field_name, False)[1]
    if len(record_duplicates) > 0:
        raise ValueError(f"{len(record_duplicates)} duplicates found in new records to be upserted into table "
                         f"{table_name}: {record_duplicates}")

    # Create two arrays: one for records to be created, one for records to be updated
    records_to_create = []
    records_to_update = []

    # For each input record, check if it exists in the existing records.
    # If it does, update it. If it does not, create it.
    logger.info(f"Table {table_name}: {len(records)} input records")
    for inputRecord in records:
        record_unique_value = inputRecord.get(unique_field_name)
        logger.debug(f"Processing record {unique_field_name} === {record_unique_value}")

        existing_record_id_based_on_upsert_field = upsert_field_value_to_existing_record_id.get(
            record_unique_value)

        # and if the upsert field value matches an existing one...
        if existing_record_id_based_on_upsert_field:
            # Add record to list of records to update
            logger.debug(f"Existing record ID {existing_record_id_based_on_upsert_field} found; "
                         f"adding to records_to_update")
            records_to_update.append(
                dict(id=existing_record_id_based_on_upsert_field, fields=inputRecord))
        else:
            # Otherwise, add record to list of records to create
            logger.debug("No existing records match; adding to records_to_create")
            records_to_create.append(inputRecord)

    # Read out array sizes
    logger.info(f"Table {table_name}: {len(records_to_create)} records to create")
    logger.info(f"Table {table_name}: {len(records_to_update)} records to update")

    typecast = config.get("typecast", True)

    # Perform record creation
    table_obj.batch_create(records_to_create, typecast=typecast)

    # Perform record updates on existing records
    table_obj.batch_update(records_to_update, typecast=typecast)


def persist_lines(config, lines):
    state = None
    schemas = {}
    key_properties = {}
    validators = {}

    # collect records for batch upload
    records_bulk = dict()
    records_schema = set()

    # Loop over lines from stdin
    for line in lines:
        try:
            o = json.loads(line)
        except json.decoder.JSONDecodeError:
            logger.error("Unable to parse:\n{}".format(line))
            raise

        if 'type' not in o:
            raise Exception("Line is missing required key 'type': {}".format(line))
        t = o['type']

        if t == 'RECORD':
            if 'stream' not in o:
                raise Exception("Line is missing required key 'stream': {}".format(line))
            if o['stream'] not in schemas:
                raise Exception(
                    "A record for stream {} was encountered before a corresponding schema".format(o['stream']))
            if o['stream'] not in records_bulk:
                records_bulk[o['stream']] = []

            # Validate record
            validators[o['stream']].validate(o['record'])

            # If the record needs to be flattened, uncomment this line
            flattened_record = flatten(o['record'])

            if config.get("output_schema", False):
                # store flattened schema
                for k in flattened_record.keys():
                    records_schema.add(k)
            else:
                # capture record
                records_bulk[o['stream']].append(flattened_record)

            state = None
        elif t == 'STATE':
            logger.debug('Setting state to {}'.format(o['value']))
            state = o['value']
        elif t == 'SCHEMA':
            if 'stream' not in o:
                raise Exception("Line is missing required key 'stream': {}".format(line))
            stream = o['stream']
            schemas[stream] = o['schema']
            validators[stream] = Draft4Validator(o['schema'])
            if 'key_properties' not in o:
                raise Exception("key_properties field is required")
            key_properties[stream] = o['key_properties']
        else:
            raise Exception("Unknown message type {} in message {}"
                            .format(o['type'], o))

    if config.get("output_schema", False):
        # write produced schema to file
        with open(os.path.join(config.get("output_schema_path", ""), "output_schema.txt"), "w") as f:
            f.write(str(records_schema))
    else:
        # process all collected entries
        for table, records in records_bulk.items():

            # determine upload method
            if config.get("upsert", False):
                # upsert records
                try:
                    process_records_upsert(config, table, records)
                except Exception as exc:
                    msg = '[Error] Failed to upsert stream {}'.format(table)
                    logger.error(msg)
                    logger.exception(str(exc))
            else:
                # batch process and insert records
                process_records(config, table, records)

    return state


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='Config file')
    args = parser.parse_args()

    if args.config:
        with open(args.config) as input_conf:
            config = json.load(input_conf)
    else:
        config = {}

    input_conf = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
    state = persist_lines(config, input_conf)

    emit_state(state)
    logger.debug("Exiting normally")


if __name__ == '__main__':
    main()
