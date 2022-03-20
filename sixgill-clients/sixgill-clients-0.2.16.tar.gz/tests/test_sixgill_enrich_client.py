import json

from mock import patch

from tests.test_sixgill_base_client import TestSixgillBaseClient, util_load_json
from sixgill.sixgill_enrich_client import SixgillEnrichClient

expected_output = json.loads(util_load_json("mock_data/Darkfeed/darkfeed_enrich_data.json")).get("items")


class TestSixgillEnrichClient(TestSixgillBaseClient):

    def setUp(self):
        super(TestSixgillEnrichClient, self).setUp()
        self.sixgill_enrich_client = SixgillEnrichClient('client_id', 'secret', 'random')

    def test_enrich_postid(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            enrich_data = self.sixgill_enrich_client.enrich_postid("1234567890asdfghjkl", 0)
        self.assertEqual(enrich_data[0], expected_output[0])

    def test_enrich_actor(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            enrich_data = self.sixgill_enrich_client.enrich_actor("IronMan")
        self.assertEqual(enrich_data[0], expected_output[0])

    def test_enrich_ioc(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            enrich_data = self.sixgill_enrich_client.enrich_ioc("ip", "1.1.1.1")
        self.assertEqual(enrich_data[0], expected_output[0])
