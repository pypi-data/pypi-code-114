#!/usr/bin/env python3
import sys, os, socket, re, time, json, logging
from urllib.parse import urlparse

#class OVSDBConnection(threading.Thread):
class OVSDBConnection(object):
    """ This is a connects to an ovsdb server that has manager set using
        ovs-vsctl set-manager ptcp:5000
    """
    def __init__(self, server_path, db = None, verbose = False):
        log_file = "libovsdb_%s.log" %(time.strftime("%Y%m%d%H%M%S", time.localtime()))
        #print(verbose)
        logging.basicConfig(
                #filename = log_file,
                level= verbose and logging.DEBUG or logging.INFO,
                format='%(asctime)s%(message)s',
                datefmt='[%Y%m%d %I:%M:%S]',
                filemode = 'w')

        #threading.Thread.__init__(self)
        o = urlparse(server_path)
        #print(o)

        if o.scheme == "tcp":
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            addr = o.path.split(":")
            self.socket.connect((addr[0], int(addr[1])))
        elif o.scheme == "unix":
            self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.socket.connect(o.path)

        self.id = 0
        self.db_name = db
        self.server_path = server_path
        if not self.db_name:
            ret = self.list_dbs()
            self.db_name = ret["result"][0]
        logging.debug("succeed to connected db: %s/%s" %(server_path, self.db_name))
        #self.start()

    def send (self, message, callback=None):
        '''
        send request to the ovsdb server
        '''
        if callback:
            self.callbacks[message['id']] = callback
        request = json.dumps(message)
        logging.debug("%s" %(request))
        self.socket.send(request.encode("UTF-8"))

    def recv (self, buffer_len = 4096):
        '''
        recieve response from the ovsdb server. It's in block mode and user
        should give a big enouth buffer len.
        '''
        response = self.socket.recv(buffer_len).decode("UTF-8")
        logging.debug("%s" %(response))
        return json.loads(response)

    def list_dbs (self, buffer_len = 4096):
        '''
        list_dbs
        '''
        list_dbs_query = {"method":"list_dbs", "params":[], "id": self.id}
        self.send(list_dbs_query)
        self.id += 1
        return self.recv()

    def transact (self, *args, **kwargs):
        '''
        Generate a transaction for send "TRANSACT" request to the ovsdb
        server. Caller should call commit() to real commit the request
        '''
        return OVSDBTransact(self)
        #list_dbs_query = {"method":"transact",
        #        "params": [self.db_name, *operations],
        #        "id": self.id}
        #self.id += 1
        #self.send(list_dbs_query)
        #return db.recv()

class OVSDBTransact(object):
    """transact
    """
    def __init__(self, ovsdb_connection):
        self.start_time = time.time()
        self.ovsdb_connection = ovsdb_connection
        self.counter = 0
        self.operations = []

    def __del__(self):
        '''
        Recycle resource when the object is destroied.
        '''
        print("transact %d, finish in %.2f seconds\n"
                %(self.ovsdb_connection.id, time.time() - self.start_time))

    def insert (self, table, row, op = "insert", **kwargs):
        '''
        Insert a row into the given table, you should compute the op
        parameters as the RFC7047:

            "op": "insert"          required
            "table": <table>        required
            "row": <row>            required
            "uuid-name": <id>       optional

        If there is reTable, you should open an mutate op, you should call
        commit() to send the transaction to the server, for example:

            name = tx.insert(table = "Logical_Switch_Port",
                            row = {"name":"ls1-lsp0"})
            tx.mutate(table = "Logical_Switch",
                      where = [["name", "==", "ls1"]],
                      mutations = [tx.make_mutations("ports", "insert", {"named-uuid": name})])
        '''
        self.counter += 1
        uuid_name = "row%d"%(self.counter)
        #operation = kwargs
        #operation["op"] = "insert"
        #operation["uuid-name"] = operation.get("uuid-name", uuid_name)
        operation = {"op": op,
                "row": row,
                "table": table}
        operation["uuid-name"] = operation.get("uuid-name", uuid_name)
        self.operations.append(operation)
        return uuid_name

    def mutate (self, table, where, mutations, op = "mutate", **kwargs):
        '''
        Mutate a column in the given table, you should compute the op
        parameters as the RFC7047:

            "op":  "mutate"               required
            "table": <table>              required
            "where": [<condition>*]       required
            "mutations": [<mutation>*]    required

        Normally mutate is used along with insert/delete, you should call
        commit() to send the transaction to the server, for example:

            name = tx.insert(table = "Logical_Switch_Port",
                            row = {"name":"ls1-lsp0"})
            tx.mutate(table = "Logical_Switch",
                      where = [["name", "==", "ls1"]],
                      mutations = [tx.make_mutations("ports", "insert", {"named-uuid": name})])
        '''
        #operation = kwargs
        #operation["op"] = "mutate"
        #self.operations.append(operation)
        #if args:
        #    operation["mutations"] = operation.get("mutations", []) 
        #    operation["mutations"].extend(args)
        #print("mutations: %s" %(mutations))
        operation = {"op": op,
                "where": where,
                "table": table,
                "mutations": mutations}
        self.operations.append(operation)

    def update (self, table, where, row, op = "update", **kwargs):
        '''
        Update a row in the given table, you should compute the op
        parameters as the RFC7047:

            "op": "update"                required
            "table": <table>              required
            "where": [<condition>*]       required
            "row": <row>                  required

        you should call commit() to send the transaction to the server, for
        example:

            tx.update(table = "Logical_Switch_Port",
                    row = {"addresses": "00:00:00:00:00:05"},
                    where = [["name", "==", "ls1-lsp0"]])
            tx.commit()
        '''
        #operation = kwargs
        #operation["op"] = "update"
        #operation["where"] = operation.get("where", [[]])
        operation = {"op": op,
                "where": where,
                "table": table,
                "row": row}
        self.operations.append(operation)

    def delete (self, table, where, op = "delete", **kwargs):
        '''
        Delete a row from the given table, you should compute the op
        parameters as the RFC7047:

            "op":  "delete"               required
            "table": <table>              required
            "where": [<condition>*]       required

        you should call commit() to send the transaction to the server, for
        example:

            # Get the uuid in other way, since it's needed in mutate op.
            uuid = 03934fdf-6087-48e7-b5ce-54d4d76e4368
            tx.delete(table = "Logical_Switch_Port",
                    where = [["uuid", "==", uuid]])
            tx.commit()
        '''
        #operation = kwargs
        #operation["op"] = "delete"
        #operation["where"] = operation.get("where", [[]])
        #self.operations.append(operation)
        operation = {"op": op,
                "where": where,
                "table": table}
        self.operations.append(operation)

    def select (self, table, where, op = "select", columns = None, **kwargs):
        '''
        select rows from the given table, you should compute the op
        parameters as the RFC7047:

            "op": "select"                required
            "table": <table>              required
            "where": [<condition>*]       required
            "columns": [<column>*]        optional

        you should call commit() to send the transaction to the server, for
        example:

            # Get the uuid in other way, since it's needed in mutate op.
            uuid = 03934fdf-6087-48e7-b5ce-54d4d76e4368
            tx.delete(table = "Logical_Switch_Port",
                    where = [["uuid", "==", uuid]])
            tx.commit()
        '''
        #operation = kwargs
        #operation["op"] = "select"
        #operation["where"] = operation.get("where", [])
        #operation["columns"] = operation.get("columns", [])
        #self.operations.append(operation)
        operation = {"op": op,
                "where": where,
                "table": table}
        if columns:
            operation["columns"] = columns
        self.operations.append(operation)

    def make_mutations (self, item, mutator, *args):
        '''
        自动生成operations 返回给调用者，以便作为参数传给transact. uuid_name
        为uuid-name, 如果该insert操作需要mutate 操作则必须传入mutate 里相同的
        参数，否则不需要传。
        {"mutations":[["ports","insert",["set",[["named-uuid","row3"]]]]],
        "op":"mutate","table":"Logical_Switch","where":[["name","==","ls1"]]}
        '''
        mutatesets = []
        # It seems that json don't support dump python set, so conver it to
        # list
        for a in args:
            mutateset = []
            if isinstance(a, dict):
                #{"named-uuid": name}
                for k,v in a.items():
                    mutateset.append(k)
                    mutateset.append(v)
            elif isinstance(a, list):
                #['uuid', '433fb2e1-fd87-4a40-b3ef-991dcd7b8014']
                mutateset = a
            #print("mutatesets: %s, a: %s, list(a): %s" %(mutatesets, a, list(a)))
            mutatesets.append(mutateset)
        mutations = [item, mutator, ["set", mutatesets]]
        return mutations

    def commit (self):
        '''
        接收来自ovsdb server的字典，并转成字符发给ovsdb server, 接收到回答后
        转成字典返回给调用者。
        注意：本函数可能阻塞
        '''
        list_dbs_query = {"method":"transact",
                "params": [self.ovsdb_connection.db_name, *self.operations],
                "id": self.ovsdb_connection.id}
        self.ovsdb_connection.send(list_dbs_query)
        self.ovsdb_connection.id += 1
        self.operations = [] # Clear the operations list for next commit.
        response = self.ovsdb_connection.recv()
        #print("transact %d, finish in %.2f seconds\n"
        #        %(self.ovsdb_connection.id, time.time() - self.start_time))
        #self.start_time = time.time() # reset the timer
        return response

    def row_insert (self, table, row, referby = None):
        '''
        Insert a row, if there is refTable by others, mutate it. It's a
        wrapper for self.insert() to let caller insert a row in one line. an
        example:
            tx.row_insert(table = "Logical_Switch_Port", row = {"name":"ls1-lsp0"},
                    referby = ["Logical_Switch", "ls1", "ports"])
        '''
        name = self.insert(table = table, row = row)
        if referby: #It's a refTable
            self.mutate(table = referby[0],
                    where = [["name", "==", referby[1]]],
                    mutations = [self.make_mutations(referby[2], "insert", {"named-uuid": name})])

    def row_delete (self, table, where = None, referby = None):
        '''
        Delete a row, if there is refTable by others, mutate it. It's a
        wrapper for self.delete() to let caller delete a row in one line. for
        example:
            tx.row_delete(table = "Logical_Switch_Port",
                    where = [["name", "==", "ls1-lsp0"]],
                    referby = ["Logical_Switch", "ls1", "ports"])
        '''
        # Get the uuid at frist it's needed in mutations.
        select_op = {"op": "select",
                "table": table,
                "columns": ["_uuid", "name"]}
        select_op["where"] = where and where or []
        list_dbs_query = {"method":"transact",
                "params": [self.ovsdb_connection.db_name, select_op],
                "id": self.ovsdb_connection.id}
        self.ovsdb_connection.send(list_dbs_query)
        self.ovsdb_connection.id += 1
        response = self.ovsdb_connection.recv()
        uuid = []
        for row in response["result"][0]["rows"]:
            uuid.append(row["_uuid"])
            #print(uuid)

        #self.delete(table = table, where = where) #delete op is not needed???
        if referby: #It's a refTable
            self.mutate(table = referby[0], where = [["name", "==", referby[1]]],
                    mutations = [self.make_mutations(referby[2], "delete", *uuid)])

    def row_update (self, table, row, where = None):
        '''
        Update a row, it's wrapper for self.update() an example:
            tx.row_update(table = "Logical_Switch_Port",
                    row = {"addresses": "00:00:00:00:00:05"},
                    where = [["name", "==", "ls1-lsp0"]])
        '''
        self.update(table = table, row = row, where = where)
    def row_select (self, **kwargs):
        '''
        select a row, it's wrapper for self.update() an example:
            response = tx.row_select(table = "Logical_Switch",
                    columns = ["_uuid", "name"],
                    where = [["name", "==", "ls1"]])
        '''
        self.select(**kwargs)

if __name__ == '__main__':
    ovsdb_server = 'unix:/usr/local/var/run/ovn/ovnnb_db.sock'
    db = OVSDBConnection(ovsdb_server, "OVN_Northbound", False)
    tx = db.transact()

    if options.insert:
        #tx.row_insert(table = "Logical_Switch", row = {"name":"ls1"})
        tx.row_insert(table = "Logical_Switch_Port",
                row = {"name":"ls1-lsp0"},
                referby = ["Logical_Switch", "ls1", "ports"])

    if options.update:
        tx.row_update(table = "Logical_Switch_Port",
                row = {"addresses": "00:00:00:00:00:05"},
                where = [["name", "==", "ls1-lsp0"]])

    if options.select:
        tx.row_select(table = "Logical_Switch",
                columns = ["_uuid", "name"],
                where = [["name", "==", "ls1"]])

    if options.delete:
        tx.row_delete(table = "Logical_Switch_Port",
                where = [["name", "==", "ls1-lsp0"]],
                referby = ["Logical_Switch", "ls1", "ports"])

    response = tx.commit()
    print("%s" %(response["result"]))
