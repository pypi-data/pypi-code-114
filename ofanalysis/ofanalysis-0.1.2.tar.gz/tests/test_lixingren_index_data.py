from unittest import TestCase
from ofanalysis.lixingren.lixingren_index_data import LixingrenIndexData


class TestLixingrenIndexData(TestCase):
    def setUp(self) -> None:
        self.index_data_object = LixingrenIndexData(
            code='000300'
        )

    def test_build_index_df(self):
        self.index_data_object.build_index_df(
            type='pe_ttm',
            granularity='fs',
            metrics_type='median'
        )
        print()
