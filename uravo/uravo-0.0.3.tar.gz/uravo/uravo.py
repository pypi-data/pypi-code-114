#!/usr/bin/env python3

#import MySQLdb
import pymysql.cursors
import os
import re
import socket
import sys
import time
import uravo.config

class Uravo():
    def __init__(self):
        self.config = uravo.config.config
        self.db = None
        self.connect()
    
    def alert(self, server_id = None, AlertGroup = None, Severity = None, Summary = None, AlertKey = None, AdditionalInfo = '', Recurring = 0, Timeout = None, Agent = None):
        self.event(server_id = server_id, AlertGroup = AlertGroup, Severity = Severity, Summary = Summary, AlertKey = AlertKey, AdditionalInfo = AdditionalInfo, Recurring = Recurring, Timeout = Timeout, Agent = Agent)

    def alerts(self, server_id = None):
        self.events(server_id = server_id)

    def connect(self):
        if self.db is None:
            try:
                self.db = pymysql.connect(host=self.config["agent"]["outpost_server"],user=self.config["agent"]["db_user"],password=self.config["agent"]["db_password"],database="uravo", port=int(self.config["agent"]["outpost_db_port"]), autocommit=True)
            except Exception as e:
                self.db = None
                return False
        return True

    def event(self, server_id = None, AlertGroup = None, Severity = None, Summary = None, AlertKey = None, AdditionalInfo = '', Recurring = 0, Timeout = None, Agent = None):
        if (self.connect() is False): return

        if (server_id is None):
            server_id = re.sub(r"^([^.]+).*$", r"\1", socket.gethostname())
        if (server_id is None or AlertGroup is None or Severity is None or Summary is None): return


        if AlertKey is None and AlertGroup is not None:
            AlertKey = AlertGroup
        if (Timeout is None):
            Timeout = 0
        elif Timeout < 1400:
            Timeout = int(time.time()) + (Timeout * 60)

        if (Severity == 'red'): Severity = 4
        elif (Severity == 'orange'): Severity = 4
        elif (Severity == 'yellow'): Severity = 3 
        elif (Severity == 'blue'): Severity = 2
        elif (Severity == 'gray'): Severity = 1 
        elif (Severity == 'green'): Severity = 0 

        if (Agent is None):
            Agent = server_id + ':' + os.path.basename(__file__)
        
        Identifier = server_id + ' ' + AlertGroup + ' ' + AlertKey + ' SOCKET';

        c = self.db.cursor()
        # Add a record to the summary table.
        sql = "INSERT INTO alert_summary (server_id, AlertGroup, Agent, recurring, mod_date) VALUES (%s,%s,%s,%s, NOW()) ON DUPLICATE KEY UPDATE mod_date=NOW(), reported=0, recurring=%s"
        c.execute(sql, (server_id, AlertGroup, Agent, Recurring, Recurring))
        if (Recurring > 0):
            sql = "UPDATE alert SET Severity=0 WHERE AlertGroup='timeout' AND AlertKey=%s AND server_id=%s"
            c.execute(sql, (AlertGroup, server_id))

        if Severity == 0 and Identifier is None:
            return

        sql = "INSERT INTO new_alert (server_id, AlertGroup, Severity, Summary, AlertKey, Identifier, AdditionalInfo, Agent, Timeout, Recurring) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (server_id, AlertGroup, Severity, Summary, AlertKey, Identifier, AdditionalInfo, Agent, Timeout, Recurring)
        return c.execute(sql, val)

    def events(self, server_id = None):
        c = self.db.cursor()
        sql = "SELECT * FROM alert"
        params = []
        if (server_id is not None):
            sql = sql + " WHERE server_id=%s"
            params.append(server_id)
        c.execute(sql, params)
        return c.fetchall()

    def getServer(self, server_id = None):
        return None

    def main(self):
        print(self.events())

def main():
    u = Uravo()
    u.main()
    sys.exit()

if __name__ == "__main__":
    main()

