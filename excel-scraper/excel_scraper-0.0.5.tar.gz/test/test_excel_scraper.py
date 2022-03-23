import pandas as pd
import os
from excel_scraper import excel_scraper

dirname, filename = os.path.split(os.path.abspath(__file__))
test_file = os.path.join(dirname, 'test_excel.xlsx')


def test_horizontal_scrape():
    df = excel_scraper.read_table(
        test_file,
        sheet_name='h1',
        skiprows=1,
        index_col=[0, 1],
        table_end= {'index_col' : 1, 'lookup_str' : 'Source' },
        horizontal_table=True,
    )

    assert isinstance(df, pd.DataFrame)
    assert isinstance(df.index, pd.DatetimeIndex)


def test_vertical_scrape():
    df = excel_scraper.read_table(
        test_file,
        sheet_name='v1',
        skiprows=1,
        index_col=0,
        header = [0, 1],
        select_dates_for_index_col = True,

    )

    assert isinstance(df, pd.DataFrame)
    assert isinstance(df.index, pd.DatetimeIndex)


def test_long_format_scrape():
    df = excel_scraper.read_long_format_table(
        test_file,
        sheet_name='lf1',
        index_col=0,
        dimension_cols=('product', 'category', 'geo', 'unit'),
        value_col='value'
    )

    assert isinstance(df, pd.DataFrame)
    assert isinstance(df.index, pd.DatetimeIndex)