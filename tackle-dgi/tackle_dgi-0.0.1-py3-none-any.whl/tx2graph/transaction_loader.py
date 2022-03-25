################################################################################
# Copyright IBM Corporation 2021, 2022
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

import os
import re
import sys
import yaml
import json
import logging
import argparse
from tqdm import tqdm
from pathlib import Path
from neomodel import config
from collections import OrderedDict
from neomodel import DoesNotExist
from neomodel.exceptions import DoesNotExist, MultipleNodesReturned
# Import our modules
from .sqlparse import sqlexp
from dgi.models import ClassNode, SQLTable, MethodNode


def clear_all_nodes():
    """ Delete all nodes """
    for node in SQLTable.nodes.all():
        node.delete()


def crud0(ast, write=False):
    if isinstance(ast, list):
        res = [set(), set()]
        for child in ast[1:]:
            rs, ws = crud0(child, ast[0] != 'select')
            res[0] |= rs
            res[1] |= ws
        return res
    elif isinstance(ast, dict) and ':from' in ast:
        ts = [list(t.values())[0] if isinstance(t, dict)
              else t for t in ast[':from'] if not isinstance(t, tuple)]
        res = set()
        for t in ts:
            if isinstance(t, list):
                res |= crud0(t, False)[0]
            else:
                res.add(t)
        return [set(), res] if write else [res, set()]
    else:
        return [set(), set()]


def crud(sql):
    r = sqlexp(sql.lower())
    if r:
        return crud0(r[1])
    else:
        return [set(), set()]


def analyze(txs):
    # annotate subtransaction, e.g., BEGIN? by
    # dependency relation
    #
    # TODO: what about already parallel txs?
    for tx in txs:
        stack = []
        if tx['transaction'] and tx['transaction'][0]['sql'] != 'BEGIN':
            tx['transaction'] = [{'sql': 'BEGIN'}] + tx['transaction']
        for op in tx['transaction']:
            if op['sql'] == 'BEGIN':
                stack.append([set(), set()])
                op['rwset'] = stack[-1]
            elif op['sql'] in ('COMMIT', 'ROLLBACK'):
                if len(stack) > 1:
                    stack[-2][0] |= stack[-1][0]
                    stack[-2][1] |= stack[-1][1]
                stack[-1][0] = set(stack[-1][0])
                stack[-1][1] = set(stack[-1][1])
                stack.pop()
            else:
                rs, ws = crud(op['sql'])
                stack[-1][0] |= rs
                stack[-1][1] |= ws
    return txs


def find_or_create_class_node(method_signature):
    method_name = method_signature.split('.')[-1]
    class_short_name = method_signature.split('.')[-2]
    class_name = ".".join(method_signature.split('.')[:-1])
    try:
        node = ClassNode.nodes.get(node_short_name=class_short_name)
    except DoesNotExist:
        node = ClassNode(node_class=class_name,
                         node_short_name=class_short_name).save()

    return node


def find_or_create_method_node(method_signature):
    method_name = method_signature.split('.')[-1]
    class_short_name = method_signature.split('.')[-2]
    class_name = ".".join(method_signature.split('.')[:-1])
    try:
        node = MethodNode.nodes.get(node_name=method_name)
    except DoesNotExist:
        node = MethodNode(node_name=method_signature, node_class=class_name,
                          node_method=method_name, node_short_name=class_short_name).save()

    return node


def find_or_create_table_node(table_name):
    try:
        node = SQLTable.nodes.get(name=table_name)
    except DoesNotExist:
        node = SQLTable(name=table_name).save()

    return node


def populate_transaction_read(label, txid, table):
    entry_method_signature = label['entry']['methods'][0]
    class_node = find_or_create_class_node(entry_method_signature)
    table_node = find_or_create_table_node(table)
    rel = class_node.transaction_read.relationship(table_node)
    if not rel:
        action = "null" if label.get(
            'http-param') is None else label.get('http-param').get('action')[0]
        table_node.transaction_read.connect(class_node,
                                            {
                                                "txid": txid,
                                                "tx_meth": entry_method_signature.split(".")[-1],
                                                "action": action
                                            }
                                            )


def populate_transaction_write(label, txid, table):
    entry_method_signature = label['entry']['methods'][0]
    class_node = find_or_create_class_node(entry_method_signature)
    table_node = find_or_create_table_node(table)
    rel = class_node.transaction_write.relationship(table_node)
    if not rel:
        action = "null" if label.get(
            'http-param') is None else label.get('http-param').get('action')[0]
        class_node.transaction_write.connect(table_node,
                                             {
                                                 "txid": txid,
                                                 "tx_meth": entry_method_signature.split(".")[-1],
                                                 "action": action
                                             }
                                             )


def tx2neo4j(transactions, label):
    # If there are no transactions to process, nothing to do here.
    if not transactions:
        return

    # -> Format lable into a proper JSON string <-
    label = re.sub("\n", '', label)  # -- Strip newline
    label = re.sub("entry", '"entry"', label)  # -- format 'entry' key
    label = re.sub("action", '"action"', label)  # -- format 'action' key
    label = re.sub("methods", '"methods"', label)  # -- format 'methods' key
    # -- format 'http-param' key
    label = re.sub("http-param", '"http-param"', label)
    label = re.sub("\[", '["', label)  # -- format 'http-param' key
    label = re.sub("\]", '"]', label)  # -- format 'http-param' key

    label = json.loads(label)

    for transaction_dict in transactions:
        txid = transaction_dict['txid']
        read, write = transaction_dict['transaction'][0]['rwset']
        for t in read:
            # FIXME: Not sure if just converting to upper is always correct.
            # Maybe it's a better idea to get the name from DDL files.
            # In general, looks like table names are case-insensitve depending
            # on the OS (insensitive in Windows, sensitive in Unix). Ref:
            # https://dev.mysql.com/doc/refman/8.0/en/identifier-case-sensitivity.html
            populate_transaction_read(label, txid, t)
        for t in write:
            # FIXME: Not sure if just converting to upper is always correct.
            # Maybe it's a better idea to get the name from DDL files
            populate_transaction_write(label, txid, t)
