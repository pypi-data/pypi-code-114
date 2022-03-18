#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-

from typing import Generator, Dict, Any, List, Iterator

from loguru import logger


class ScrollSource:
    """

    Sample:
        _source = ScrollSource(es_search_info, es_client)
        # Delete scroll_id by using:
        _source.delete_scroll_id()

    """

    def __init__(self, search_info: Dict[str, any], es_client) -> None:
        self.scroll_id = None
        self.client = es_client
        self.search_info = search_info

    def __iter__(self) -> Generator[List[Dict[Any, Any]], None, None]:
        """Generator fn to get the scroll _source"""
        total_size = 0
        data = self.client.search(**self.search_info)
        scroll_size = len(data['hits']['hits'])
        self.scroll_id = data['_scroll_id']
        logger.info(f"Scrolling {str(self.client)} by index: {self.search_info['index']}\n scroll_id: {self.scroll_id}")
        if scroll_size == 0:
            self.client.clear_scroll(scroll_id=self.scroll_id)
        while scroll_size > 0:
            request_list = data['hits']['hits']
            total_size += scroll_size
            logger.info(f"scroll size: {total_size}")
            data = self.client.scroll(scroll_id=self.scroll_id, scroll=self.search_info["scroll"])
            scroll_size = len(data['hits']['hits'])
            yield request_list

    def delete_scroll_id(self):
        if self.scroll_id:
            self.client.clear_scroll(scroll_id=self.scroll_id)
