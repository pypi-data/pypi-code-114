from unittest import TestCase
from ofanalysis.ts.ts_data_update import TSDataUpdate


class TestTSDataUpdate(TestCase):
    def setUp(self) -> None:
        self.ts_data_update_object = TSDataUpdate()

    def test_retrieve_all(self):
        self.ts_data_update_object.retrieve_all()
        print()
