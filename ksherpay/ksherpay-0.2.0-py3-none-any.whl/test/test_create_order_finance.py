import unittest
from ksherpay import Payment
from ksherpay import API_TYPE
import os
import json
import logging
from dotenv import load_dotenv
import webbrowser
logging.root.setLevel('INFO')
import time
import base64
import os


class FinanceOrderCreateTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        load_dotenv()
        self.BASE_URL = 'https://sandboxbkk.vip.ksher.net'
        self.token = os.environ.get("API_TOKEN") 
        logging.info("token:{}".format(self.token))
        # self.database_name = "trivia_test"
        # self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        # setup_db(self.app, self.database_path)

    def tearDown(self):
        """Executed after reach test"""
        print('-=- teart donw-=-')
        pass

    def test_success_channels(self):
        logging.info("============ START test case: test_success_channels ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE ,token=self.token)
        data = {
            "mid": "35618",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.channels(params=data)
        data = resp.json()
        if resp.status_code == 200:
            logging.info("successfully query channels available with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('promptpay2',data['data']['channels'])

        logging.info("============ END test case: test_success_channels ============")
    
    def test_fail_channels(self):
        logging.info("============ START test case: test_fail_channels ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        # use not allow mid
        data = {
            "mid": "1111",
            "signature": "string",
            "timestamp": "string"
        }
        time.sleep(1)
        resp = payment_handle.settlements.channels(params=data)
        if resp.status_code == 200:
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'UNKNOWN')
            self.assertIn('NOT allowed mid',data['error_message'])
        logging.info("============ END test case: test_fail_channels ============")

    def test_success_order(self):
        logging.info("============ START test case: test_success_order ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        data = {
            "mid": "35618",
            "offset":0,
            "limit":50,
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.order(yyyymmdd="20220228",params=data)
        self.assertEqual(resp.status_code, 200)
        if resp.status_code == 200:
            logging.info("successfully create Transaction report with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('total',data['data'])
        logging.info("============ END test case: test_create_query_pending ============")

    def test_fail_order(self):
        logging.info("============ START test case: test_fail_order ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        # missing need param
        data = {
            "signature": "string",
            "timestamp": "string"
        }
        time.sleep(1)
        resp = payment_handle.settlements.order(yyyymmdd="20220228",params=data )
        self.assertEqual(resp.status_code, 400)
        logging.info("============ END test case: test_fail_order ============")

    def test_success_settlements(self):
        logging.info("============ START test case: test_success_settlements ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        data = {
            "channel": "truemoney",
            "mid":"mch35618",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.settlements(yyyymmdd="20220317",params=data)
        
        self.assertEqual(resp.status_code, 200)
        if resp.status_code == 200:
            logging.info("successfully create settlements report with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
        logging.info("============ END test case: test_success_settlements ============")
    
    def test_fail_settlements(self):
        logging.info("============ START test case: test_fail_settlements ============")
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        # missing need param
        data = {
            "mid":"mch35618",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.settlements(yyyymmdd="20220317",params=data)
        self.assertEqual(resp.status_code, 400)
        logging.info("============ END test case: test_success_settlements ============")

    def test_success_settlement_order(self):
        logging.info("============ START test case: test_success_settlement_order ============")
        # ceate an order and not pay result in pending order
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        data = {
            "limit":50,
            "offset":0,
            "reference_id":"20220317_35618_GDHTQL",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.settlement_order(params=data)
        self.assertEqual(resp.status_code, 200)
        if resp.status_code == 200:
            logging.info("successfully create read inside settlement report with following response data:")
            data = resp.json()
            logging.info(f"data:{data}")
            self.assertEqual(data['error_code'], 'SUCCESS')
            self.assertIn('total',data['data'])
        logging.info("============ END test case: test_success_settlement_order ============")

    def test_fail_settlement_order(self):
        logging.info("============ START test case: test_fail_settlement_order ============")
        # ceate an order and not pay result in pending order
        payment_handle = Payment(base_url=self.BASE_URL, apiType=API_TYPE.FINANCE, token=self.token)
        data = {
            "reference_id":"20220317_35618_GDHTQL",
            "signature": "string",
            "timestamp": "string"
        }
        # make sure time will be different for altest 1 second
        time.sleep(1)
        resp = payment_handle.settlements.settlement_order(params=data)
        self.assertEqual(resp.status_code, 400)
        logging.info("============ END test case: test_fail_settlement_order ============")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()