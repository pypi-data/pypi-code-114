# # Module file: hmrc_rate.py
# enviroment
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

""" The XML is the hmrc XML"""
# http://www.hmrc.gov.uk/softwaredevelopers/rates/exrates-monthly-0222.XML

def hmrc_to_dataframe(month, year):
    url = f"http://www.hmrc.gov.uk/softwaredevelopers/rates/exrates-monthly-{month.zfill(2)}{year[2:]}.XML"
    document = requests.get(url)
    soup = BeautifulSoup(document.content, "xml")
    countryName = soup.find_all('countryName')
    countryCode = soup.find_all('countryCode')
    currencyName = soup.find_all('currencyName')
    currencyCode = soup.find_all('currencyCode')
    rateNew = soup.find_all('rateNew')

    currency_data = []
    for i in range(0, len(countryName)):
        rows = [countryName[i].get_text(),
                countryCode[i].get_text(),
                currencyName[i].get_text(),
                currencyCode[i].get_text(),
                rateNew[i].get_text()]
        currency_data.append(rows)

    exchange_rate_df = pd.DataFrame(currency_data, columns=[
                                    'countryName', 'countryCode', 'currencyName', 'currencyCode', 'rateNew'])
    exchange_rate_df['reported_month_year'] = url[-8:-4]
    exchange_rate_df['exchageRate_starDate'] = pd.to_datetime(
        exchange_rate_df['reported_month_year'], format="%m%y")
    return exchange_rate_df
