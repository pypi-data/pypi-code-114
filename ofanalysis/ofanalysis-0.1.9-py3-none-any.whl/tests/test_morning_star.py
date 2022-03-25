from unittest import TestCase

from ofanalysis.morningstar.morning_star import MorningStar


class TestMorningStar(TestCase):
    def setUp(self) -> None:
        self.morning_star = MorningStar(
            web_driver_path='./drivers/chromedriver',
            assets_path='./assets'
        )

    def test_get_fund_list(self):
        self.morning_star.get_fund_list()

    def test_write_to_db(self):
        # self.morning_star.write_to_db()
        pass
