from mock import patch
import logging
import json

from tests.test_sixgill_base_client import TestSixgillBaseClient, util_load_json
from sixgill.sixgill_intel_items_client import SixgillIntelItemsClient


class TestSixgillIntelItemsClient(TestSixgillBaseClient):

    def setUp(self):
        super(TestSixgillIntelItemsClient, self).setUp()
        self.sixgill_intel_items_client = SixgillIntelItemsClient('client_id', 'secret', 'random',
                                                                  logging.getLogger("test"))

    def test_get_intel_items(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            intel_items = self.sixgill_intel_items_client.get_intel_items(query='sample')

        expected_output = json.loads(util_load_json("mock_data/IntelItems/get_intel_items.json")).get("intel_items")

        self.assertEqual(intel_items, expected_output)

    def test_intel_items(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            intel_items = self.sixgill_intel_items_client.advanced_intel_items(query="emotat", scroll=True, results_size=2)

        expected_output = util_load_json("mock_data/IntelItems/post_intel_items.json")

        self.assertEqual(intel_items, expected_output)
