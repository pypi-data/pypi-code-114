import pandas as pd
import geopandas as gpd
from bs4 import BeautifulSoup, SoupStrainer
import zipfile
import wget
import os
import requests
from datetime import datetime
import json
from zipfile import ZipFile
from urllib.request import urlopen 

place_ref = r'https://github.com/Fair-Lines-America/FLA_basic_tools/blob/main/data/place_ref.zip?raw=true'
vtd_ref = r'https://github.com/Fair-Lines-America/FLA_basic_tools/blob/main/data/vtd_ref.zip?raw=true'
mil_ref = r'https://raw.githubusercontent.com/Fair-Lines-America/FLA_basic_tools/main/data/mil_ref.csv'
########
#Helper Functions
########
def get_links(url):
    url_base = 'https://www2.census.gov/geo/tiger/TIGER2020/COUNTY/'
    res = requests.get(url)
    res = res.content
    array = []
    f= None 
    for link in BeautifulSoup(res, parse_only=SoupStrainer('a')):
        if link.has_attr('href') and '.zip'  in link['href']:
            array.append(link['href'])
    return array

########
#Split Functions
########


def community_split(distr, geoid, disid):
    if not isinstance(distr, pd.DataFrame):
        raise Exception('distr is not a Dataframe')
    url_base = 'https://www2.census.gov/geo/tiger/TIGER2020/'
    f = None 
    distr = distr[[disid,geoid]]
    distr = distr.astype(str)
    if len(distr[geoid].iloc[0]) < 15:
        raise Exception('GEOID column not in 15 digital Geocode for Census Blocks')
    state = distr[geoid].iloc[0][:2]
    links = get_links(f'{url_base}TABBLOCK20') 
    for l in links:
        if state in l.split('_')[2]:
            f = l
            break
    wget.download(f'{url_base}/TABBLOCK20/{f}')
    tabblock = gpd.read_file(f, dtype={'GEOID20': str})
    distr = distr.rename(columns={geoid:'GEOID20'})
    df_dist = tabblock.merge(distr, on='GEOID20')
    os.remove(f)
    if len(df_dist.index) == 0:
        raise Exception('Pandas Merge Fail')
    #County Split
    keep=[disid,'COUNTYFP20']
    remove=[]
    for i in df_dist.columns:
        if i not in keep:
            remove.append(i)
    df_dist = df_dist.drop(columns=remove)
    district_list = list(set(df_dist['COUNTYFP20'].values.tolist()))
    pivot_tbd = {}
    for i in district_list:
        pivot_tbd[i] = []
    for idx, row in df_dist.iterrows():
        pivot_tbd[row['COUNTYFP20']].append(row[disid])
        pivot_tbd[row['COUNTYFP20']] = list(set(pivot_tbd[row['COUNTYFP20']]))
    r = []
    for key, value in pivot_tbd.items():
        if len(value) < 2:
            r.append(pivot_tbd[key])
    Segement_Count =  0
    Split_Count = 0
    for key,value in pivot_tbd.items():
        if len(value) > 1:
            Segement_Count += len(value)
            Split_Count += 1
    out_county = {'Segement_Count':Segement_Count, 'Split_Count':Split_Count, 'County_List': pivot_tbd}
    r =[]
    for key, value in out_county['County_List'].items():
        if len(value) < 2:
            r.append(key)
    for i in r:
        del out_county['County_List'][i]
#### EXTERNAL FILES FOR REFERNCE NEEDED ####
    url = urlopen(place_ref)
    output = open('place_ref.zip', 'wb')    # note the flag:  "wb"        
    output.write(url.read())
    output.close()
    df_place = pd.read_csv('place_ref.zip', dtype=str)
    df_place = distr.merge(df_place, left_on='GEOID20', right_on='GEOID20_0KM', suffixes=('_d', '') )
    df_place = df_place.drop(columns=['GEOID20_d','GEOID20_0KM'])
    district_list = list(set(df_place['GEOID20'].values.tolist()))
    pivot_tbd = {}
    for i in district_list:
        pivot_tbd[i] = []
    for idx, row in df_place.iterrows():
        pivot_tbd[row['GEOID20']].append(row[disid])
        pivot_tbd[row['GEOID20']] = list(set(pivot_tbd[row['GEOID20']]))
    r = []
    for key, value in pivot_tbd.items():
        if len(value) < 2:
            r.append(pivot_tbd[key])
    Segement_Count =  0
    Split_Count = 0
    for key,value in pivot_tbd.items():
        if len(value) > 1:
            Segement_Count += len(value)
            Split_Count += 1
    out_place = {'Segement_Count':Segement_Count, 'Split_Count':Split_Count, 'Place_List': pivot_tbd}
    r =[]
    for key, value in out_place['Place_List'].items():
        if len(value) < 2:
            r.append(key)
    for i in r:
        del out_place['Place_List'][i]
    df_mil = pd.read_csv(mil_ref, dtype=str)
    df_mil = distr.merge(df_mil, left_on='GEOID20', right_on='GEOID20_0KM', suffixes=('', '') )
    df_mil = df_mil.drop(columns=['GEOID20','GEOID20_0KM'])
    district_list = list(set(df_mil['AREAID'].values.tolist()))
    pivot_tbd = {}
    for i in district_list:
        pivot_tbd[i] = []
    for idx, row in df_mil.iterrows():
        pivot_tbd[row['AREAID']].append(row[disid])
        pivot_tbd[row['AREAID']] = list(set(pivot_tbd[row['AREAID']]))
    r = []
    for key, value in pivot_tbd.items():
        if len(value) < 2:
            r.append(pivot_tbd[key])
    Segement_Count =  0
    Split_Count = 0
    for key,value in pivot_tbd.items():
        if len(value) > 1:
            Segement_Count += len(value)
            Split_Count += 1
    out_mil = {'Segement_Count':Segement_Count, 'Split_Count':Split_Count, 'Mil_List': pivot_tbd}
    r = []
    for key, value in out_mil['Mil_List'].items():
        if len(value) < 2:
            r.append(key)
    for i in r:
        del out_mil['Mil_List'][i]
    url = urlopen(vtd_ref)
    output = open('vtd_ref.zip', 'wb')    # note the flag:  "wb"        
    output.write(url.read())
    output.close()
    df_vtd = pd.read_csv('vtd_ref.zip', dtype=str)
    df_vtd = distr.merge(df_vtd, left_on='GEOID20', right_on='GEOID20', suffixes=('_d', '') )
    df_vtd = df_vtd.drop(columns=['GEOID20'])
    district_list = list(set(df_vtd['VTD_GEOID20'].values.tolist()))
    pivot_tbd = {}
    for i in district_list:
        pivot_tbd[i] = []
    for idx, row in df_vtd.iterrows():
        pivot_tbd[row['VTD_GEOID20']].append(row[disid])
        pivot_tbd[row['VTD_GEOID20']] = list(set(pivot_tbd[row['VTD_GEOID20']]))
    r = []
    for key, value in pivot_tbd.items():
        if len(value) < 2:
            r.append(pivot_tbd[key])
    Segement_Count =  0
    Split_Count = 0
    for key,value in pivot_tbd.items():
        if len(value) > 1:
            Segement_Count += len(value)
            Split_Count += 1
    out_vtd = {'Segement_Count':Segement_Count, 'Split_Count':Split_Count, 'Vtd_List': pivot_tbd}
    r = []
    for key, value in out_vtd['Vtd_List'].items():
        if len(value) < 2:
            r.append(key)
    for i in r:
        del out_vtd['Vtd_List'][i]
    out = {'vtd' : out_vtd,
        'county' : out_county,
        'place' : out_place,
        'mil' : out_mil}
    ## OUTPUT
    with open('geo_splits.json', 'w') as f:
        json.dump(out, f)
    return out