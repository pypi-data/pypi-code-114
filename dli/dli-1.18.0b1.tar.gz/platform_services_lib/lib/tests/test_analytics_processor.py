#
# Copyright (C) 2019 IHS Markit.
# All Rights Reserved
#

from mock import Mock

from ..services.analytics_service import AnalyticsService


class TestAnalyticsProcessor:

    _analytics_processor = AnalyticsService(Mock())

    def test_process_action_returns_none_for_none_input(self):
        assert self._analytics_processor.process(None) is None

    def test_process_action_calls_analytics_service_methods(self):
        input = {'what': 'ever'}
        expected_body = 'body'
        self._analytics_processor._analytics_service.create_message_body = \
            Mock(return_value=expected_body)
        self._analytics_processor.process(input)

        self._analytics_processor._analytics_service.create_message_body \
            .assert_called_once_with(input)
        self._analytics_processor._analytics_service.send_message\
            .assert_called_once_with(expected_body)
