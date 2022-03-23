import os
from trell_ai_util.BigQueryAdapter import *
import unittest


class Test_BigQueryAdapter(unittest.TestCase):
    
        
    def test_get_bigquery_data_from_query(self):
        try:
            query = "select * from `trellatale.trellDbDump.userLanguages` limit 2"
            df = get_bigquery_data_from_query(query)
            status = True
        except exception as e:
            print(str(e))
            status = False
        
        
        self.assertEqual(status, True)
        
        
    def test_execute_bigquery_query(self):
        try:
            query = "INSERT rahul_temp.demo (id, userId) VALUES(1,1),(1,1)"
            execute_bigquery_query(query)
            status = True
        except:
            status = False
            
        
        self.assertEqual(status, True)