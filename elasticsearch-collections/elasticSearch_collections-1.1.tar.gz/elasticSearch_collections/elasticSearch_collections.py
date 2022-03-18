#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
import csv
from typing import Dict, Any, List

from scroll_source import ScrollSource
from elasticsearch import Elasticsearch, helpers


class ElasticSearchCollections:

    def __init__(self, hosts: Any = ..., **kwargs: Any) -> None:
        self.scroll_id = None
        self.client = Elasticsearch(hosts, **kwargs)

    def bulk(self, actions: List[Dict[Any, Any]]):
        helpers.bulk(client=self.client, actions=actions)

    def upload_source_from_csv(self, csvfile):
        """
        update $.'_source' from csvfile.
        fn need to be re-written once the date parse logic changed.
        """
        with open(csvfile, "r") as f:
            csv_reader = csv.DictReader(f)
            actions = []
            for row in csv_reader:
                actions.append(row)
        if actions:
            self.bulk(actions)

    def download_source_to_csv(self, csvfile: str, field_names: List[str], search_info: Dict[str, any]):
        """
        Parse the search result ($.'_source': dict) to csv.
        Example: download_source_to_csv("test1.csv", ['_source']['xxxData'], es_search_info)
        fn need to be re-written once the date parse logic changed.
        """
        with open(csvfile, "w") as f:
            csv_writer = csv.DictWriter(f, fieldnames=field_names)
            csv_writer.writeheader()
            _source = ScrollSource(search_info, self.client)

            for _data_list in _source:
                for i in _data_list:
                    csv_writer.writerow(i['_source'])

            _source.delete_scroll_id()
