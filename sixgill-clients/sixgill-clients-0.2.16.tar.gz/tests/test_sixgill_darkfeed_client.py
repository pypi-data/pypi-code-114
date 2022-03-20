from mock import patch
import logging
import json

from tests.test_sixgill_base_client import TestSixgillBaseClient, util_load_json
from sixgill.sixgill_feed_client import SixgillFeedClient
from sixgill.sixgill_constants import FeedStream
from sixgill.sixgill_utils import is_indicator


def expected_output_data():
    raw_data = json.loads(util_load_json("mock_data/Darkfeed/darkfeed_data.json"))

    indicators = []
    for record in raw_data:
        data = record.get("objects", [])
        indicators.extend(list(filter(is_indicator, data)))

    return indicators


class TestSixgillDarkFeedClient(TestSixgillBaseClient):

    def setUp(self):
        super(TestSixgillDarkFeedClient, self).setUp()
        self.sixgill_darkfeed_client = SixgillFeedClient('client_id', 'secret', 'random', FeedStream.DARKFEED,
                                                         logging.getLogger("test"), bulk_size=7)

    def test_get_indicators(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            indicators = []
            for indicator in self.sixgill_darkfeed_client.get_indicator():
                indicators.append(indicator)

        expected_output = expected_output_data()

        self.assertEqual(indicators, expected_output)
