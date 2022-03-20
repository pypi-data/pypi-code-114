from mock import patch
import logging

from tests.test_sixgill_base_client import TestSixgillBaseClient
from sixgill.sixgill_feed_client import SixgillFeedClient
from sixgill.sixgill_constants import FeedStream
from tests.test_sixgill_darkfeed_client import expected_output_data


class TestSixgillDarkFeedClient(TestSixgillBaseClient):

    def setUp(self):
        super(TestSixgillDarkFeedClient, self).setUp()
        self.sixgill_darkfeed_freemium_client = SixgillFeedClient('client_id', 'secret', 'random',
                                                                  FeedStream.DARKFEED_FREEMIUM,
                                                                  logging.getLogger("test"), bulk_size=7)

    def test_get_indicators(self):
        with patch('requests.sessions.Session.send', new=self.mocked_request):
            indicators = []
            for indicator in self.sixgill_darkfeed_freemium_client.get_indicator():
                indicators.append(indicator)

        expected_output = expected_output_data()

        self.assertEqual(indicators, expected_output)
