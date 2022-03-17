"""
Copyright 2020 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
import datetime

import pandas as pd
import pytest
from testfixtures import Replacer
from testfixtures.mock import Mock

import gs_quant.timeseries.measures_reports as mr
from gs_quant.api.gs.assets import GsTemporalXRef
from gs_quant.api.gs.data import MarketDataResponseFrame
from gs_quant.data.core import DataContext
from gs_quant.errors import MqValueError
from gs_quant.markets.report import PerformanceReport, ThematicReport
from gs_quant.markets.securities import Stock
from gs_quant.models.risk_model import FactorRiskModel as Factor_Risk_Model
from gs_quant.target.common import ReportParameters, XRef
from gs_quant.target.reports import Report, PositionSourceType, ReportType
from gs_quant.target.risk_models import RiskModel, RiskModelCoverage, RiskModelTerm, RiskModelUniverseIdentifier

risk_model = RiskModel(coverage=RiskModelCoverage.Country, id_='model_id', name='Fake Risk Model',
                       term=RiskModelTerm.Long, universe_identifier=RiskModelUniverseIdentifier.gsid, vendor='GS',
                       version=1.0)

factor_risk_report = Report(position_source_id='position source id',
                            position_source_type=PositionSourceType.Portfolio,
                            type_=ReportType.Portfolio_Factor_Risk,
                            id_='report_id',
                            parameters=ReportParameters(risk_model='risk_model_id'),
                            status='new')

ppa_report = Report(position_source_id='position source id',
                    position_source_type=PositionSourceType.Portfolio,
                    type_=ReportType.Portfolio_Performance_Analytics,
                    id_='report_id',
                    parameters=ReportParameters(risk_model='risk_model_id'),
                    status='new')

factor_data = [
    {
        'date': '2020-11-23',
        'reportId': 'report_id',
        'factor': 'factor_id',
        'factorCategory': 'CNT',
        'pnl': 11.23,
        'exposure': -11.23,
        'proportionOfRisk': 1
    },
    {
        'date': '2020-11-24',
        'reportId': 'report_id',
        'factor': 'factor_id',
        'factorCategory': 'CNT',
        'pnl': 11.24,
        'exposure': -11.24,
        'proportionOfRisk': 2
    },
    {
        'date': '2020-11-25',
        'reportId': 'report_id',
        'factor': 'factor_id',
        'factorCategory': 'CNT',
        'pnl': 11.25,
        'exposure': -11.25,
        'proportionOfRisk': 3
    }
]

aggregate_factor_data = [
    {
        'date': '2020-11-23',
        'reportId': 'report_id',
        'factor': 'Factor',
        'factorCategory': 'CNT',
        'pnl': 11.23,
        'exposure': -11.23,
        'proportionOfRisk': 1,
        'dailyRisk': 1,
        'annualRisk': 1
    },
    {
        'date': '2020-11-24',
        'reportId': 'report_id',
        'factor': 'Factor',
        'factorCategory': 'CNT',
        'pnl': 11.24,
        'exposure': -11.24,
        'proportionOfRisk': 2,
        'dailyRisk': 2,
        'annualRisk': 2
    },
    {
        'date': '2020-11-25',
        'reportId': 'report_id',
        'factor': 'Factor',
        'factorCategory': 'CNT',
        'pnl': 11.25,
        'exposure': -11.25,
        'proportionOfRisk': 3,
        'dailyRisk': 3,
        'annualRisk': 3
    }
]

constituents_data_l_s = {
    'assetId': [
        "MA1",
        "MA1",
        "MA1",
        "MA2",
        "MA2",
        "MA2"
    ],
    'quantity': [
        -1.,
        -2.,
        -3.,
        1.,
        2.,
        3.
    ],
    'netExposure': [
        -1.,
        -2.,
        -3.,
        1.,
        2.,
        3.
    ],
    'pnl': [
        0.,
        -1.,
        -1.,
        0.,
        1.,
        1.
    ],
    'date': [
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04'
    ]
}

pnl_data_l_s = {
    'quantity': [
        -1.,
        -2.,
        -3.,
        -1.,
        -2.,
        -3.,
        1.,
        2.,
        3.,
        1.,
        2.,
        3.
    ],
    'pnl': [
        0.,
        -1.,
        -1.,
        0.,
        -1.,
        -1.,
        0.,
        1.,
        1.,
        0.,
        1.,
        1.
    ],
    'date': [
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04',
        '2020-01-02',
        '2020-01-03',
        '2020-01-04'
    ]
}

constituents_data = {
    'netExposure': [
        1.,
        2.,
        3.
    ],
    'assetId': [
        "MA",
        "MA",
        "MA"
    ],
    'quantity': [
        1.,
        1.,
        1.
    ],
    'pnl': [
        0.,
        1.,
        1.
    ],
    'date': [
        '2020-01-02',
        '2020-01-03',
        '2020-01-04'
    ]
}

constituents_data_s = {
    'netExposure': [
        -1.,
        -2.,
        -3.
    ],
    'assetId': [
        "MA",
        "MA",
        "MA"
    ],
    'quantity': [
        -1.,
        -1.,
        -1.
    ],
    'pnl': [
        0.,
        1.,
        1.
    ],
    'date': [
        '2020-01-02',
        '2020-01-03',
        '2020-01-04'
    ]
}

thematic_data = [
    {
        "date": "2021-07-12",
        "reportId": "PTAID",
        "basketId": "MA01GPR89HZF1FZ5",
        "region": "Asia",
        "grossExposure": 3.448370345015856E8,
        "thematicExposure": 2,
        "thematicBeta": 1,
        "updateTime": "2021-07-20T23:43:38Z"
    },
    {
        "date": "2021-07-13",
        "reportId": "PTAID",
        "basketId": "MA01GPR89HZF1FZ5",
        "region": "Asia",
        "grossExposure": 3.375772519907556E8,
        "thematicExposure": 2,
        "thematicBeta": 1,
        "updateTime": "2021-07-20T23:43:38Z"
    },
    {
        "date": "2021-07-14",
        "reportId": "PTAID",
        "basketId": "MA01GPR89HZF1FZ5",
        "region": "Asia",
        "grossExposure": 3.321189950666118E8,
        "thematicExposure": 2,
        "thematicBeta": 1,
        "updateTime": "2021-07-20T23:43:38Z"
    },
    {
        "date": "2021-07-15",
        "reportId": "PTAID",
        "basketId": "MA01GPR89HZF1FZ5",
        "region": "Asia",
        "grossExposure": 3.274071805135091E8,
        "thematicExposure": 2,
        "thematicBeta": 1,
        "updateTime": "2021-07-20T23:43:38Z"
    }
]


def mock_risk_model():
    risk_model = RiskModel(coverage=RiskModelCoverage.Country, id_='model_id', name='Fake Risk Model',
                           term=RiskModelTerm.Long, universe_identifier=RiskModelUniverseIdentifier.gsid, vendor='GS',
                           version=1.0)

    replace = Replacer()

    # mock getting risk model entity()
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model', Mock())
    mock.return_value = risk_model

    actual = Factor_Risk_Model.get(model_id='model_id')
    replace.restore()
    return actual


def test_factor_exposure():
    replace = Replacer()

    # mock getting risk model entity()
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model', Mock())
    mock.return_value = risk_model

    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_report', Mock())
    mock.return_value = factor_risk_report

    # mock getting report factor data
    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_factor_risk_report_results', Mock())
    mock.return_value = factor_data

    # mock getting risk model dates
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model_dates', Mock())
    mock.return_value = ['2010-01-01']

    # mock getting risk model factor category
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_data', Mock())
    mock.return_value = {
        'results': [{
            'factorData': [{
                'factorId': 'factor_id',
                'factorCategory': 'Factor Name'
            }]}
        ]}

    # mock getting risk model factor entity
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_factor_data', Mock())
    mock.return_value = [{
        'identifier': 'factor_id',
        'type': 'Factor',
        'name': 'Factor Name',
        'factorCategory': 'Factor Name'
    }]

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.factor_exposure('report_id', 'Factor Name')
        assert all(actual.values == [-11.23, -11.24, -11.25])

    with pytest.raises(MqValueError):
        mr.factor_exposure('report_id', 'Wrong Factor Name')
    replace.restore()


def test_factor_pnl():
    replace = Replacer()

    # mock getting risk model entity()
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model', Mock())
    mock.return_value = risk_model

    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_report', Mock())
    mock.return_value = factor_risk_report

    # mock getting report factor data
    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_factor_risk_report_results', Mock())
    mock.return_value = factor_data

    # mock getting risk model dates
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model_dates', Mock())
    mock.return_value = ['2010-01-01']

    # mock getting risk model factor category
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_data', Mock())
    mock.return_value = {
        'results': [{
            'factorData': [{
                'factorId': 'factor_id',
                'factorCategory': 'Factor Name'
            }]}
        ]}

    # mock getting risk model factor entity
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_factor_data', Mock())
    mock.return_value = [{
        'identifier': 'factor_id',
        'type': 'Factor',
        'name': 'Factor Name',
        'factorCategory': 'Factor Name'
    }]

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.factor_pnl('report_id', 'Factor Name')
        assert all(actual.values == [11.23, 11.24, 11.25])

    with pytest.raises(MqValueError):
        mr.factor_pnl('report_id', 'Wrong Factor Name')
    replace.restore()


def test_factor_proportion_of_risk():
    replace = Replacer()

    # mock getting risk model entity()
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model', Mock())
    mock.return_value = risk_model

    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_report', Mock())
    mock.return_value = factor_risk_report

    # mock getting report factor data
    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_factor_risk_report_results', Mock())
    mock.return_value = factor_data

    # mock getting risk model dates
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model_dates', Mock())
    mock.return_value = ['2010-01-01']

    # mock getting risk model factor category
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_data', Mock())
    mock.return_value = {
        'results': [{
            'factorData': [{
                'factorId': 'factor_id',
                'factorCategory': 'Factor Name'
            }]}
        ]}

    # mock getting risk model factor entity
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_factor_data', Mock())
    mock.return_value = [{
        'identifier': 'factor_id',
        'type': 'Factor',
        'name': 'Factor Name',
        'factorCategory': 'Factor Name'
    }]

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.factor_proportion_of_risk('report_id', 'Factor Name')
        assert all(actual.values == [1, 2, 3])

    with pytest.raises(MqValueError):
        mr.factor_proportion_of_risk('report_id', 'Wrong Factor Name')
    replace.restore()


def test_get_factor_data():
    replace = Replacer()

    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_report', Mock())
    mock.return_value = ppa_report

    with pytest.raises(MqValueError):
        mr.factor_proportion_of_risk('report_id', 'Factor Name')
    replace.restore()


def test_aggregate_factor_support():
    replace = Replacer()

    # mock getting risk model entity()
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model', Mock())
    mock.return_value = risk_model

    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_report', Mock())
    mock.return_value = factor_risk_report

    # mock getting report factor data
    mock = replace('gs_quant.api.gs.reports.GsReportApi.get_factor_risk_report_results', Mock())
    mock.return_value = aggregate_factor_data

    # mock getting risk model dates
    mock = replace('gs_quant.api.gs.risk_models.GsRiskModelApi.get_risk_model_dates', Mock())
    mock.return_value = ['2010-01-01']

    # mock getting risk model factor category
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_data', Mock())
    mock.return_value = {
        'results': [{
            'factorData': [{
                'factorId': 'factor_id',
                'factorCategory': 'Factor Name'
            }]}
        ]}

    # mock getting risk model factor entity
    mock = replace('gs_quant.api.gs.risk_models.GsFactorRiskModelApi.get_risk_model_factor_data', Mock())
    mock.return_value = [{
        'identifier': 'factor_id',
        'type': 'Factor',
        'name': 'Factor Name',
        'factorCategory': 'Factor Name'
    }]

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.factor_proportion_of_risk('report_id', 'Factor')
        assert all(actual.values == [1, 2, 3])

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.daily_risk('report_id', 'Factor')
        assert all(actual.values == [1, 2, 3])

    with DataContext(datetime.date(2020, 11, 23), datetime.date(2020, 11, 25)):
        actual = mr.annual_risk('report_id', 'Factor')
        assert all(actual.values == [1, 2, 3])

    with pytest.raises(MqValueError):
        mr.daily_risk('report_id', 'Factor Name')

    with pytest.raises(MqValueError):
        mr.annual_risk('report_id', 'Factor Name')
    replace.restore()


def test_normalized_performance():
    idx = pd.date_range('2020-01-02', freq='D', periods=3)
    replace = Replacer()
    expected = {None: pd.Series(data=[1, 2, 3], index=idx,
                                name='normalizedPerformance', dtype='float64'),
                "Long": pd.Series(data=[1, 2, 3], index=idx,
                                  name='normalizedPerformance', dtype='float64')}

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=constituents_data)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    for k, v in expected.items():
        with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
            actual = mr.normalized_performance('MP1', k)
            assert all(actual.values == v.values)
    replace.restore()


def test_normalized_performance_short():
    idx = pd.date_range('2020-01-02', freq='D', periods=3)
    replace = Replacer()
    expected = {"Short": pd.Series(data=[1, 1 / 2, 1 / 3], index=idx,
                                   name='normalizedPerformance', dtype='float64'),
                "Long": pd.Series(data=[1, 2, 3], index=idx,
                                  name='normalizedPerformance', dtype='float64'),
                None: pd.Series(data=[1, (2 + 1 / 2) / 2, (3 + 1 / 3) / 2], index=idx,
                                name='normalizedPerformance', dtype='float64')}

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=constituents_data_l_s)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    for k, v in expected.items():
        with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
            actual = mr.normalized_performance('MP1', k)
            assert all((actual.values - v.values) < 0.01)
    replace.restore()


def test_get_long_pnl():
    idx = pd.date_range('2020-01-02', freq='D', periods=3)
    replace = Replacer()
    expected = pd.Series(data=[0, 2, 2], index=idx, name='longPnl', dtype='float64')

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=pnl_data_l_s)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
        actual = mr.long_pnl('MP1')
        assert all(actual.values == expected.values)
    replace.restore()


def test_get_short_pnl():
    idx = pd.date_range('2020-01-02', freq='D', periods=3)
    replace = Replacer()
    expected = pd.Series(data=[0, -2, -2], index=idx, name='shortPnl', dtype='float64')

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=pnl_data_l_s)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
        actual = mr.short_pnl('MP1')
        assert all(actual.values == expected.values)
    replace.restore()


def test_get_short_pnl_empty():
    replace = Replacer()
    expected = pd.Series(dtype=float)

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=constituents_data)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
        actual = mr.short_pnl('MP1')
        assert all(actual.values == expected.values)
    replace.restore()


def test_get_long_pnl_empty():
    replace = Replacer()
    expected = pd.Series(dtype=float)

    mock = replace('gs_quant.api.gs.portfolios.GsPortfolioApi.get_reports', Mock())
    mock.return_value = [
        Report.from_dict({'id': 'RP1', 'positionSourceType': 'Portfolio', 'positionSourceId': 'MP1',
                          'type': 'Portfolio Performance Analytics',
                          'parameters': {'transactionCostModel': 'FIXED'}})]
    # mock PerformanceReport.get_portfolio_constituents()
    mock = replace('gs_quant.markets.report.PerformanceReport.get_portfolio_constituents', Mock())
    mock.return_value = MarketDataResponseFrame(data=constituents_data_s)

    # mock PerformanceReport.get()
    mock = replace('gs_quant.markets.report.PerformanceReport.get', Mock())
    mock.return_value = PerformanceReport(report_id='RP1',
                                          position_source_type='Portfolio',
                                          position_source_id='MP1',
                                          report_type='Portfolio Performance Analytics',
                                          parameters=ReportParameters(transaction_cost_model='FIXED'))

    with DataContext(datetime.date(2020, 1, 1), datetime.date(2019, 1, 3)):
        actual = mr.long_pnl('MP1')
        assert all(actual.values == expected.values)
    replace.restore()


def test_thematic_exposure():
    replace = Replacer()

    # mock getting PTA report
    mock = replace('gs_quant.markets.report.ThematicReport.get', Mock())
    mock.return_value = ThematicReport(id='report_id')

    # mock getting thematic exposure
    mock = replace('gs_quant.markets.report.ThematicReport.get_thematic_exposure', Mock())
    mock.return_value = pd.DataFrame(thematic_data)

    # mock getting asset
    mock = Stock('MAA0NE9QX2ABETG6', 'Test Asset')
    xrefs = replace('gs_quant.timeseries.measures.GsAssetApi.get_asset_xrefs', Mock())
    xrefs.return_value = [
        GsTemporalXRef(datetime.date(2019, 1, 1),
                       datetime.date(2952, 12, 31),
                       XRef(ticker='basket_ticker', ))
    ]
    replace('gs_quant.markets.securities.SecurityMaster.get_asset', Mock()).return_value = mock

    with DataContext(datetime.date(2020, 7, 12), datetime.date(2020, 7, 15)):
        actual = mr.thematic_exposure('report_id', 'basket_ticker')
        assert all(actual.values == [2, 2, 2, 2])

    replace.restore()


def test_thematic_beta():
    replace = Replacer()

    # mock getting PTA report
    mock = replace('gs_quant.markets.report.ThematicReport.get', Mock())
    mock.return_value = ThematicReport(id='report_id')

    # mock getting thematic exposure
    mock = replace('gs_quant.markets.report.ThematicReport.get_thematic_betas', Mock())
    mock.return_value = pd.DataFrame(thematic_data)

    # mock getting asset
    mock = Stock('MAA0NE9QX2ABETG6', 'Test Asset')
    xrefs = replace('gs_quant.timeseries.measures.GsAssetApi.get_asset_xrefs', Mock())
    xrefs.return_value = [
        GsTemporalXRef(datetime.date(2019, 1, 1),
                       datetime.date(2952, 12, 31),
                       XRef(ticker='basket_ticker', ))
    ]
    replace('gs_quant.markets.securities.SecurityMaster.get_asset', Mock()).return_value = mock

    with DataContext(datetime.date(2020, 7, 12), datetime.date(2020, 7, 15)):
        actual = mr.thematic_beta('report_id', 'basket_ticker')
        assert all(actual.values == [1, 1, 1, 1])

    replace.restore()


if __name__ == '__main__':
    pytest.main(args=[__file__])
