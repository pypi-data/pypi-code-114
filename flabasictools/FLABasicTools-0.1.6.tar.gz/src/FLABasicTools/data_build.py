import pandas as pd
import geopandas as gpd
from bs4 import BeautifulSoup, SoupStrainer
import zipfile
import wget
import os
import requests
from datetime import datetime
from zipfile import ZipFile
from urllib.request import urlopen 
from shapely.ops import unary_union 
########   
#Data retrive / Data build Functions
########
states_df = r'https://raw.githubusercontent.com/Fair-Lines-America/FLA_basic_tools/main/data/us-state-ansi-fips.csv'
def get_census_shp(fips=False, Geography=None, year=datetime.now().year-1):
    if year < 2008:
        raise Exception('Pre 2008 Tiger Files either do not existis or are not in common formate')
    stateList = pd.read_csv(states_df, dtype=str, skipinitialspace=True)
    base = f'https://www2.census.gov/geo/tiger/TIGER{year}/'
    if Geography is None:
        res = requests.get(base)
        res = res.content
        dir_list = []
        for link in BeautifulSoup(res, parse_only=SoupStrainer('a'), features="html.parser"):
            if not link.has_attr("class"):
                if 'https:' not in link.get("href") and '?' not in link.get("href") and (len(link.get("href").split('/')) == 2):
                    dir_list.append(link.get("href").replace('/',''))
        return print(f'Please Choice a Geography/Subdirectory you would like the shapefile for/from', *dir_list, sep='\n')
                
    elif not fips:
        raise Exception('Please Include State')
    sub = f'{Geography}/'
    url = base+sub
    res = requests.get(url)
    res = res.content
    zip_list = []
    for link in BeautifulSoup(res, parse_only=SoupStrainer('a'), features="html.parser"):
        if not link.has_attr("class"):
            zip_list.append(link.get("href"))
    try:
        int(fips)
    except:
        if len(fips) == 2:
            fips = stateList[stateList['stusps'] == fips.upper()]
            fips = fips['st'].values[0]
        elif len(fips) > 2:
            fips = stateList[stateList['stname'] == fips.capitalize()]
            fips = fips['st'].values[0]
    for i in zip_list:
        if fips in i.split('_') or 'us' in i.split('_'):
            gdf = gpd.read_file(f'{url}{i}', dtype={'GEOID20':str})
            return gdf




def assign_baf(baf, state, disid, geoid=None):
    if isinstance(baf, pd.DataFrame) and not isinstance(baf, gpd.GeoDataFrame) and (geoid is None and len(baf[geoid].iloc[0]) != 15):
        raise Exception('Need to include 15 digit GEOID for joiner')
    if isinstance(baf, gpd.GeoDataFrame) and 'geometry' not in baf.columns:
        raise Exception('Geopandas DataFrame need Geometry Column')
    if isinstance(baf, gpd.GeoDataFrame):
        blk_df = get_census_shp(fips=state, Geography='TABBLOCK20')
        geoid = 'GEOID20'
        blk_df['geometry'] = blk_df['geometry'].centroid
        out_df = gpd.sjoin(baf,blk_df)
        r = [i for i in out_df if i not in [disid,geoid]]
        out_txt = out_df.drop(columns=r)
        out_txt.to_csv(f'simple_{state}_baf.csv', index=False)
    elif isinstance(baf, pd.DataFrame):
        baf[geoid] = baf[geoid].astype('str')
        blk_df = get_census_shp(fips=state, Geography='TABBLOCK20')
        blk_df = blk_df.rename(columns={'GEOID20':geoid})
        out_df = blk_df.merge(baf, on=geoid)
        out_shp = out_df[[disid,'geometry']]
        dest = gpd.GeoDataFrame(columns=[disid, 'geometry'], geometry='geometry')
        dist_list = list(set(out_shp[disid].tolist()))
        for dist in dist_list:
            df_temp = out_shp[out_shp[disid] == dist]
            df_temp = df_temp.reset_index()
            polygons = df_temp['geometry'].tolist()
            df_temp['geometry'] = unary_union(polygons)
            dest = dest.append(df_temp[[disid,'geometry']].iloc[0,:])
        dest.to_file(f'geo_{state}_baf.shp')
        
