from unittest import TestCase
from ofanalysis.lixingren.lixingren_sw_data import LixingrenSWData


class TestLixingrenSWData(TestCase):
    def setUp(self) -> None:
        self.index_data_object = LixingrenSWData(
            code='370000'
        )
    def test_build_sw_ind_df(self):
        self.index_data_object.build_sw_ind_df(
            type='pe_ttm',
            granularity='fs',
            metrics_type='median'
        )
        print()
