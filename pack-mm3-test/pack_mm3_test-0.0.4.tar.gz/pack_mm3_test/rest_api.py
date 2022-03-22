from requests_negotiate_sspi import HttpNegotiateAuth
from requests.models import Response
import requests
import json
import pandas as pd
from datetime import datetime
import math
import numpy as np

DEFAULT_INGESTION_END = "2199-12-31"

# arena config
def _get_mm_base_url(env='local'):
    if (env == 'local'):
        return 'http://localhost:8000/modelmanagement'
    elif (env == 'dev'):
        return 'http://arenadev:8000/modelmanagement'
    elif (env == 'uat'):
        return 'https://arena1:7999/modelmanagement'
    elif (env == 'prod'):
        return 'https://arena1:8000/modelmanagement'
    else:
        raise Exception("env should be 'local', 'dev', 'uat', 'prod'. Found {}".format(env))


# ----- Helper functions ------ #
def _get_all(url, env='local'):
    """
        Sends a GET request without any data. Returns the content received
        To be used by internal functions
    """
    base_url = _get_mm_base_url(env)
    # Time out is used to force ipv4 over ipv6
    resp = requests.get("{}/{}/".format(base_url, url), auth=HttpNegotiateAuth())
    try:
        content = json.loads(resp.content)
    except:
        print("Error in {}".format(url))
        print(resp.content)
        content = resp.content
    return content


def _post_data(url, data, env='local'):
    """
        Sends a POST request with data. Returns the content received. Uses response.text
        To be used by internal functions
    """
    base_url = _get_mm_base_url(env)
    r = requests.post("{}/{}/".format(base_url, url), data=data, auth=HttpNegotiateAuth())

    if 200 <= r.status_code < 300:
        return json.loads(r.text)
    else:
        print("Error in {}".format(url))
        print(r.status_code)
        print(r.text)
    return r


def _post_json(url, data, env='local'):
    """
        Sends a POST request with data as JSON. Returns the content received
        To be used by internal functions
    """
    base_url = _get_mm_base_url(env)
    r = requests.post("{}/{}/".format(base_url, url), json=data, auth=HttpNegotiateAuth())

    if 200 <= r.status_code < 300:
        return json.loads(r.text)
    else:
        print("Error in {}".format(url))
        print(r.status_code)
        print(r.text)
    return r


def _post_json_using_chunks(url, df, env='local'):

    num_rows = df.shape[0]
    chunk_size = 500000
    if(num_rows < 500000):
        chunk_size = 100000
    elif(num_rows < 1000000):
        chunk_size = 300000

    # Only one group
    if(num_rows<chunk_size):
        return _post_json(url, df.to_dict(orient='records'), env)

        
    df['signal_composite_name'] = df['signal_namespace']+'||'+df['signal_name']+'||'+df['signal_version'].astype(str)
    
    unique_signals = df['signal_composite_name'].unique().tolist()
    num_groups = math.ceil(num_rows / chunk_size) # number of groups
    num_signals_in_group = math.ceil(len(unique_signals) / num_groups) # number of signals in each group

    # Assign each signal to a group
    df['group_num'] = df['signal_composite_name'].map(unique_signals.index)
    df['group_num'] = np.ceil((df['group_num']+1) / num_signals_in_group)
    df.drop('signal_composite_name', axis=1, inplace=True)
    # Iterate through each group and upload to DB
    df_list = [y for _, y in df.groupby(['group_num'], as_index=False)]

    for index, group_df in enumerate(df_list):
        print(group_df['group_num'].unique())
        resp = _post_json(url, group_df.to_dict(orient='records'), env)
        if(isinstance(resp, Response)):
            return {
                'df': df,
                'group': index+1,
                'error': resp
            }
        
    return {'message': '{} rows inserted'.format(num_rows)}


def _convert_response_to_df(resp, convert_to_datetime=False):
    if(isinstance(resp, Response)):
        return resp

    df = pd.DataFrame(resp)
    if(df.empty):
        return df

    df.drop(columns='index', inplace=True, errors='ignore')

    if(convert_to_datetime):
        df['data_date'] = pd.to_datetime(df['data_date']).dt.strftime('%Y-%m-%d')

    return df


def _convert_response_to_df_split(resp, convert_to_datetime=False):
    """Use this if API is returning df in the format {'columns': [], 'index': [], 'data': []} created using to_json(orient='split')

    Args:
        resp (JSON): Respose from API
        convert_to_datetime (bool, optional): Convert to datetime or not. Defaults to False.

    Returns:
        DataFrame: DataFrame in the response
    """
    if(isinstance(resp, Response)):
        return resp

    df = pd.DataFrame(resp['data'], columns=resp['columns'])
    if(df.empty):
        return df

    df.drop(columns='index', inplace=True, errors='ignore')

    if(convert_to_datetime):
        df['data_date'] = pd.to_datetime(df['data_date']).dt.strftime('%Y-%m-%d')

    return df

# ----- Assets ------ #
def get_all_asset_types(env='local'):
    """
        Return all asset_type as DataFrame. No parameters required.
    """
    url = "asset_type"
    df = pd.DataFrame(_get_all(url, env))
    return df


def insert_asset_type(name, description, env='local'):
    """Create one Asset Type record. 
    Args:
        name (string): Name of the Asset Type (must be unique)
        description (string): Description of the asset type

    Returns:
        Response message from API 
    """
    df = pd.DataFrame.from_records([
        {
            "name": name,
            "description": description}
    ])
    return insert_asset_type_bulk(df, env)


def insert_asset_type_bulk(df, env='local'):
    """
        Create multiple Asset Type records
    Args:    
        df must be pandas dataframe containing the columns: name, description
    Returns:
        Response message from API 
    """
    url = "asset_type"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_return_type(name, display_name, description, asset_type_name, env='local'):
    """Create one Return Type record.
    Args:
        name (string): Name of the Return Type (must be unique)
        display name (string): Display name of the return type
        description (string): Description of the return type
        asset_type_name (str): Asset type associated with this return type

    Returns:
        Response message from API
    """
    df = pd.DataFrame.from_records([
        {
            "name": name,
            "description": description,
            "display_name": display_name,
            "asset_type_name": asset_type_name}
    ])
    return insert_return_type_bulk(df, env)


def insert_return_type_bulk(df, env='local'):
    """
        Create multiple Asset Type records
    Args:
        df must be pandas dataframe containing the columns: name, display_name, description, asset_type_name
    Returns:
        Response message from API
    """
    url = "return_type"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_return_types(env='local'):
    url = "return_type"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_assets(env='local'):
    """
        Return all assets as DataFrame. No parameters required.
    """
    url = "asset"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_assets_equity(asset_type_name="EQ_STK" , env='local'):
    """
        Return all EQ_STK assets as DataFrame. No parameters required.
    """
    asset_df = get_all_assets()
    if(asset_df.empty):
        return "No assets found"
    asset_df = asset_df[asset_df['asset_type_name'] == asset_type_name]
    return asset_df


def get_all_assets_fi_futures(asset_type_name="FI_FUT" , env='local'):
    """
        Return all FI_FUT assets as DataFrame. No parameters required.
    """
    asset_df = get_all_assets()
    if(asset_df.empty):
        return "No assets found"
    asset_df = asset_df[asset_df['asset_type_name'] == asset_type_name]
    return asset_df


def get_all_assets_fx_fwd(asset_type_name="FX_FWD" , env='local'):
    """
        Return all FX_FWD assets as DataFrame. No parameters required.
    """
    asset_df = get_all_assets()
    if(asset_df.empty):
        return "No assets found"
    asset_df = asset_df[asset_df['asset_type_name'] == asset_type_name]
    return asset_df


def _insert_asset_bulk(df, env='local'):
    """Called internally"""
    url = "asset/independent"
    asset_response = _post_json(url, df.to_dict(orient='records'))
    asset_return_synchronize()
    return asset_response


def _insert_asset_with_external_bulk(df, env='local'):
    """Called internally"""
    url = "asset/with_external"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_asset_eq_stk(name, display_name, external_id, description, asset_type_name="EQ_STK", env='local'):
    """
        Insert equity asset record.
        Input - name, display_name, external_id, description, asset_type_name (optional)
        Output - response from API
    """
    df = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "external_id": external_id,
        "asset_type_name": asset_type_name,
    }])
    return insert_asset_eq_stk_bulk(df, env)


def insert_asset_eq_stk_bulk(df, asset_type_name="EQ_STK", env='local'):
    """
        Insert multiple equity asset records
        Input Dataframe with the following columns:  asset_name, display_name, external_id, description
        Output - Response from API
    """
    if ("asset_type_name" not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_with_external_bulk(df, env)


def insert_asset_eq_fut(name, display_name, description, is_primary=0, asset_type_name="EQ_FUT", env='local'):
    """
        Insert EQ Futures asset record.
        Input params  - name, display_name, description, is_primary=0
        Output - response from API
    """
    data = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "is_primary": is_primary,
        "asset_type_name": asset_type_name
    }])
    return insert_asset_eq_fut_bulk(data, env)


def insert_asset_eq_fut_bulk(df, asset_type_name="EQ_FUT", env='local'):
    """
        Insert multiple EQ Futures asset records.
        Input params - DataFrame containing the following columns: name, display_name, description, is_primary=0
        Output - response from API
    """
    if ('asset_type_name' not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)


def insert_asset_cm_fut(name, display_name, description, asset_type_name="CM_FUT", env='local'):
    """
        Insert CM Futures asset record.
        Input params  - name, display_name, description
        Output - response from API
    """
    data = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "asset_type_name": asset_type_name
    }])
    return insert_asset_cm_fut_bulk(data, env)


def insert_asset_cm_fut_bulk(df, asset_type_name="CM_FUT", env='local'):
    """
        Insert multiple CM Futures asset records.
        Input params - DataFrame containing the following columns: name, display_name, description
        Output - response from API
    """
    if ('asset_type_name' not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)


def insert_asset_fi_fut(name, display_name, description, asset_type_name="FI_FUT", env='local'):
    """
        Insert FI Futures asset record.
        Input params  - name, display_name, description
        Output - response from API
    """
    data = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "asset_type_name": asset_type_name
    }])
    return insert_asset_fi_fut_bulk(data, env)


def insert_asset_fi_fut_bulk(df, asset_type_name="FI_FUT", env='local'):
    """
        Insert multiple FI Futures asset records.
        Input params - DataFrame containing the following columns: name, display_name, description, is_primary=0
        Output - response from API
    """
    if ('asset_type_name' not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)


def insert_asset_fx_fwd(name, display_name, description, asset_type_name="FX_FWD", env='local'):
    data = pd.DataFrame([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "asset_type_name": asset_type_name
    }])
    return _insert_asset_bulk(data, env)


def insert_asset_fx_fwd_bulk(df, asset_type_name="FX_FWD", env='local'):
    """
        Insert multiple FX Forward asset records.
        Input params - DataFrame containing the following columns: asset_name, display_name, is_primary_child=0, asset_type_name
        Output - response from API
    """
    if ("asset_type_name" not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)

def insert_asset_cr_cds(name, display_name, description, asset_type_name="CR_CDS", env='local'):
    data = pd.DataFrame([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "asset_type_name": asset_type_name
    }])
    return _insert_asset_bulk(data, env)


def insert_asset_cr_cds_bulk(df, asset_type_name="CR_CDS", env='local'):
    """
        Insert multiple FX Forward asset records.
        Input params - DataFrame containing the following columns: asset_name, display_name, is_primary_child=0, asset_type_name
        Output - response from API
    """
    if ("asset_type_name" not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)


def insert_asset_fi_irs(name, display_name, description, asset_type_name="FI_IRS", env='local'):
    data = pd.DataFrame([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "asset_type_name": asset_type_name
    }])
    return _insert_asset_bulk(data, env)


def insert_asset_fi_irs_bulk(df, asset_type_name="FI_IRS", env='local'):
    """
        Insert multiple FX Forward asset records.
        Input params - DataFrame containing the following columns: asset_name, display_name, is_primary_child=0, asset_type_name
        Output - response from API
    """
    if ("asset_type_name" not in df and df.shape[0] > 0):
        df.loc[:, 'asset_type_name'] = asset_type_name
    return _insert_asset_bulk(df, env)

def get_all_asset_return_types(env='local'):
    """
        Return all asset_return types as DataFrame. No parameters required.
    """
    url = "asset_return"
    df = pd.DataFrame(_get_all(url, env))
    return df


def insert_asset_return(asset_name, return_type, is_primary=0, env='local'):
    """Insert asset return recod in DB

    Args:
        asset_name (string): name of asset
        return_type (string): return type (example: TOTAL)
        is_primary (int, optional): is this the primary return for this asset. Defaults to 0.

    Returns:
        str: API message from response
    """
    data = pd.DataFrame([{
        "asset_name": asset_name,
        "return_type": return_type,
        "is_primary": is_primary
    }])
    return insert_asset_return_bulk(data, env)


def insert_asset_return_bulk(df, env='local'):
    """Insert multiple asset return records

    Args:
        df (DataFrame): DataFrame containing the following columns: asset_name, return_type, is_primary (default 0)

    Returns:
        str: Message from API
    """

    url = "asset_return"
    if ("is_primary" not in df):
        df["is_primary"] = 0
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_asset_return_ts_bulk(df, env='local'):
    """Insert asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, name, return_type_name, data

    Returns:
        str: Message from API
    """
    url = "asset_return_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_asset_universes(env='local'):
    """
        Return all asset_universe as DataFrame. No parameters required.
    """
    url = "asset_universe"
    df = pd.DataFrame(_get_all(url, env))
    return df


def insert_asset_universe(name, type, description, version=1, env='local'):
    """Insert asset universe

    Args:
        name (str): Name of asset universe
        type (str): Type of asset universe (static/dynamic)
        description (str): Description of asset universe
        version (int, optional): Defaults to 1.

    Returns:
        str: Response message from API
    """
    data = pd.DataFrame([{
        "name": name,
        "type": type,
        "description": description,
        "version": version
    }])
    return insert_asset_universe_bulk(data, env)


def insert_asset_universe_bulk(df, env='local'):
    """Insert multiple asset universe records

    Args:
        df(DataFrame): containing the following columns: name, type, description, version (optional)
    
    Returns:
        str: Response message from API
    """
    url = "asset_universe"
    return _post_json(url, df.to_dict(orient='records'), env)


def upgrade_asset_universe(name, env='local'):
    """Insert asset universe

    Args:
        name (str): Name of asset universe

    Returns:
        str: Response message from API
    """
    url = "upgrade_asset_universe"
    data = {
        "name": name,
    }
    return _post_data(url, data, env)



def get_all_asset_universe_constituents_static(env='local'):
    """
        Return all asset_universe_constituent_static as DataFrame. No parameters required.
    """
    url = "asset_universe_constituent_static"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_asset_universes_static(type="static" , env='local'):
    """
        Return all asset_universe_static as DataFrame. No parameters required.
    """
    asset_universe_df = get_all_asset_universes(env)
    if(asset_universe_df.empty):
        return "No universes found"
    asset_universe_df = asset_universe_df[asset_universe_df['type'] == type]

    return asset_universe_df


def insert_asset_universe_constituent_static(asset_universe_name, asset_name, asset_universe_version="latest", env='local'):
    """Insert constituent into a static asset universe 

    Args:
        asset_universe_name (str): Name of asset universe,
        asset_name (str): Name of asset
        asset_universe_version (str): Version of asset universe (default is latest)

    Returns:
        JSON: Response message from API
    """
    data = pd.DataFrame([{
        "asset_universe_name": asset_universe_name,
        "asset_universe_version": asset_universe_version,
        "asset_name": asset_name,
    }])
    return insert_asset_universe_constituent_static_bulk(data, env)


def insert_asset_universe_constituent_static_bulk(df, env='local'):
    """
        Insert multiple asset universe constituent static records specifying asset using asset name
        Input params - Dataframe containing the following columns: asset_universe_name, asset_name, asset_universe="latest"
    """
    url = "asset_universe_constituent_static"
    if ("asset_universe_version" not in df):
        df["asset_universe_version"] = "latest"

    return _post_json(url, df.to_dict(orient='records'), env)


def delete_asset_universe(asset_universe_name, asset_universe_version="latest", env='local'):
    """Remove the Asset Universe by the name

    Args:
        asset_universe_name (str): Name of asset universe
        asset_universe_version (str, optional): Version of asset universe. Defaults to "latest".
    """
    url = "delete_asset_universe"
    data = {
        "name": asset_universe_name,
        "version": asset_universe_version
    }
    return _post_data(url, data, env)


def delete_asset_universe_constituent_static(asset_universe_name, asset_universe_version="latest", env='local'):
    """Remove the constituents of the given asset universe

    Args:
        asset_universe_name (str): Name of asset universe
        asset_universe_version (str, optional): Version of asset universe. Defaults to "latest".
    """
    url = "delete_asset_universe_constituent_static"
    data = {
        "name": asset_universe_name,
        "version": asset_universe_version
    }
    return _post_data(url, data, env)

def get_all_asset_universe_constituents_dynamic(env='local'):
    """
        Return all asset_universe_constituent_dynamic as DataFrame. No parameters required.
    """
    url = "asset_universe_constituent_dynamic"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_asset_universes_dynamic(type="dynamic" , env='local'):
    """
        Return all asset_universe_dynamic as DataFrame. No parameters required.
    """
    asset_universe_df = get_all_asset_universes(env)
    if(asset_universe_df.empty):
        return "No universes found"
    asset_universe_df = asset_universe_df[asset_universe_df['type'] == type]
    return asset_universe_df


def insert_asset_universe_constituent_dynamic(data_date, asset_universe_name, asset_name,asset_universe_version="latest", env='local'):
    """Insert constituent into asset universe dynamic

    Args:
        data_date (str): Data date
        asset_universe_name (str): Name of universe
        asset_name (str): Name of asset
        asset_universe_version (str, optional): Version of universe. Defaults to "latest".

    Returns:
        JSON: Response from API
    """
    data = pd.DataFrame([{
        "data_date": data_date,
        "asset_universe_name": asset_universe_name,
        "asset_universe_version": asset_universe_version,
        "asset_name": asset_name,
    }])
    return insert_asset_universe_constituent_dynamic_bulk(data, env)


def insert_asset_universe_constituent_dynamic_bulk(df, env='local'):
    """Insert multiple asset universe constituent dynamic records specifying asset using asset name

    Args:
        df (DataFrame):  Dataframe containing the following columns: data_date, asset_universe_name, asset_name, asset_universe_version (optional)

    Returns:
        JSON: Response from API
    """
    url = "asset_universe_constituent_dynamic"
    if ("asset_universe_version" not in df):
        df["asset_universe_version"] = "latest"
    return _post_json(url, df.to_dict(orient='records'), env)


# ------------ SIGNAL ------------- #

def get_all_signals(env='local'):
    """
        Return all signal as DataFrame. No parameters required.
    """
    url = "retrieve_all_signals"
    df = pd.DataFrame(_post_data(url, {}, env))
    return df


def get_all_signal_pointers(env='local'):
    """
        Return all signal pointers as DataFrame. No parameters required.
    """
    url = "signal_pointer"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_signal_meta_data_field_defs(env='local'):
    """
        Return all signal_meta_data_field_def as DataFrame. No parameters required.
    """
    url = "signal_meta_data_field_def"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_signal_meta_data(env='local'):
    """
        Return all signal_meta_data as DataFrame. No parameters required.
    """
    url = "signal_meta_data"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_signal_signal_rel_registry(env='local'):
    """
        Return all signal_signal_rel_registry as DataFrame. No parameters required.
    """
    url = "signal_signal_rel_registry"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_signal_scaler(namespace, name, start_date, version="latest", end_date=None, env='local'):
    """Get All signal scaler time series filtered by signal and date range

    Args:
        namespace (str, optional): Namespace of signal.
        name (str): Name of signal
        start_date (str): Start date (inclusive - %Y/%m/%d)
        version (str, optional): Version of signal. Defaults to latest
        end_date (str, optional): End date (inclusive - %Y/%m/%d). Defaults to None

    Returns:
        JSON: response from API
    """
    url = "retrieve_signal_scaler"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "start_date": start_date,
        "end_date": end_date,
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def get_signal_asset_scaler(namespace, name, start_date, version='latest', end_date=None, env='local'):
    """Get All signal asset scaler time series filtered by signal and date range

    Args:
        start_date (str): Start date (inclusive - %Y/%m/%d)
        end_date (str): End date (inclusive - %Y/%m/%d)
        namespace (str): Namespace of signal
        name (str): Name of signal
        version (str, optional): Version of signal. Defaults to latest

    Returns:
        df: DataFrame containing the signal asset scalers
    """
    url = "retrieve_signal_asset_scaler"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "start_date": start_date,
        "end_date": end_date,
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def insert_signal(namespace, name, display_name, description, process_type, asset_universe_name, launch_date, is_leaf, scaler_type, is_path_dependent=0, asset_universe_version="latest", version=None, env='local'):
    """Insert signal record

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        display_name (str): Display name of signal
        description (str): Description
        process_type (str): Process type (raw/signal_10_vol/etc)
        asset_universe_name (str): Asset universe name
        launch_date (str, format: "%Y-%m-%d"): Launch date of signal
        is_leaf (bool): whether it is a leaf signal (has no further no children) or not
        scaler_type (str): specifies what kind of scaler to expect: none, asset, signal
        is_path_dependent (int, optional): boolean to specify whether signal is path dependent or not. Defaults to 0.
        asset_universe_version (str, optional): asset universe version. Defaults to "latest".

    Returns:
        JSON: response from API
    """
    data = pd.DataFrame([{
        "name": name,
        "display_name": display_name,
        "namespace": namespace,
        "description": description,
        "process_type": process_type,
        "asset_universe_name": asset_universe_name,
        "asset_universe_version": asset_universe_version,
        "launch_date": launch_date,
        "is_leaf": is_leaf,
        "scaler_type": scaler_type,
        "is_path_dependent": is_path_dependent
    }])

    if(version):
        data.loc[:, 'version'] = version
    return insert_signal_bulk(data, env)


def insert_signal_bulk(df, env='local'):
    """Insert multiple signal records.
    Args:
        df (DataFrame): containing the following columns: namespace, name, display_name, description, process_type, asset_universe_name, launch_date, is_leaf, scaler_type, is_path_dependent, asset_universe_version, tc_aum_name

    Returns: 
        JSON: Response from API
    """
    url = "signal"
    if ("ingestion_end" not in df.columns):
        df['ingestion_end'] = DEFAULT_INGESTION_END
    return _post_json(url, df.to_dict(orient='records'), env)


def upgrade_signal(namespace, name, launch_date, asset_universe_name=None, asset_universe_version="latest", env='local'):
    """Upgrade an existing signal

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        launch_date (str, format: "%Y-%m-%d"): Launch date of signal
        asset_universe_name (str): Asset universe name
        asset_universe_version (str, optional): asset universe version. Defaults to "latest".

    Returns:
        JSON: response from API
    """
    data = {
        "name": name,
        "namespace": namespace,
        "asset_universe_name": asset_universe_name,
        "asset_universe_version": asset_universe_version,
        "launch_date": launch_date,
    }

    url = "upgrade_signal"
    
    return _post_data(url, data, env)


def upgrade_signal_bulk(df, env='local'):
    """Upgrade multiple signal records.
    Args:
        df (DataFrame): containing the following columns: namespace, name, launch_date, asset_universe_name, asset_universe_version

    Returns:
        JSON: Response from API
    """
    url = "upgrade_signal_bulk"
    return _post_json(url, df.to_dict(orient='records'), env)


def edit_signal(namespace, name, version, field_name, field_value, env='local'):
    """Edit an existing signal
    field_name must be one of the following :
     ['DISPLAY_NAME', 'DESCRIPTION', 'ASSET_UNIVERSE_ID', 'LAUNCH_DATE', 'TC_AUM_ID', 'SCALER_TYPE']

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        version (str): Version of signal
        field_name (str): Name of the field to edit
        field_value (str): Value of the field to replace

    Returns:
        JSON: response from API
    """
    data = {
        "name": name,
        "namespace": namespace,
        "version": version,
        "field_name": field_name,
        "field_value": field_value,
    }

    url = "edit_signal"
    
    return _post_data(url, data, env)

def insert_signal_meta_data_field_def(name, description, is_required, options, env='local'):
    """Insert signal meta data field definition record

    Args:
        name (str): Name
        description (str): Description
        is_required (bool): 1 for true and 0 for false
        options (str): List containing probable options for the field value

    Returns:
        str: [description]
    """
    data = pd.DataFrame([{
        "name": name,
        "description": description,
        "is_required": is_required,
        "options": options
    }])
    return insert_signal_meta_data_field_def_bulk(data, env)


def insert_signal_meta_data_field_def_bulk(df, env='local'):
    """
        Insert multiple records of signal_meta_data_field_def. 
        Input params - Dataframe containing the following columns: name, description, is_required, options
    """
    url = "signal_meta_data_field_def"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_signal_meta_data(signal_namespace, signal_name, signal_version, field_name, field_value, env='local'):
    """Insert signal meta data

    Args:
        signal_namespace (str): Namespace.
        signal_name (str): Signal score name
        signal_version (str): Signal score version (can be "latest")
        field_name (str): Meta data field name
        field_value (str): Field value

    Returns:
        str: [description]
    """
    data = pd.DataFrame([{
        "signal_name": signal_name,
        "signal_version": signal_version,
        "signal_namespace": signal_namespace,
        "field_name": field_name,
        "field_value": field_value
    }])
    return insert_signal_meta_data_bulk(data, env)


def insert_signal_meta_data_bulk(df, env='local'):
    """
        Insert multiple records of signal_meta_data_bu. 
        Input params - Dataframe containing the following columns: signal_namespace, signal_name, signal_version(optional), field_name, field_value
    """
    url = "signal_meta_data"
    if("signal_version" not in df.columns):
        df['signal_version'] = "latest"
    return _post_json(url, df.to_dict(orient='records'), env)



def insert_signal_pointer(namespace, name, version, signal_namespace, signal_name, signal_version, is_top_node=1, env='local'):
    """Insert signal meta data

    Args:
        namespace (str): Pointer Namespace.
        name (str): Pointer name
        version (str): Pointer version (can be "latest")
        signal_namespace (str): Signal Namespace.
        signal_name (str): Signal name
        signal_version (str): Signal version (can be "latest")
        is_top_node(bool): specifies whether the pointer is top node or not. Optional (defaults to 1)

    Returns:
        str: [description]
    """
    data = pd.DataFrame([{
        "namespace": namespace,
        "name": name,
        "version": version,
        "signal_namespace": signal_namespace,
        "signal_name": signal_name,
        "signal_version": signal_version,
        "is_top_node": is_top_node
    }])
    return insert_signal_pointer_bulk(data, env)


def insert_signal_pointer_bulk(df, env='local'):
    """
        Insert multiple records of signal_pointer . 
        Input params - Dataframe containing the following columns: namespace, name, version, signal_namespace, signal_name, signal_version(optional), is_top_node(optional)
    """
    url = "signal_pointer"
    if("signal_version" not in df.columns):
        df['signal_version'] = "latest"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_signal_signal_rel_registry_bulk(df, env='local'):
    """
        Insert multiple records of signal signal relationship registry
        Input params - Dataframe containing the following columns: pri_signal_namespace, pri_signal_name, pri_signal_version(optional), sec_signal_namespace, sec_signal_name, sec_signal_version(optional), rel_type
    """
    url = "signal_signal_rel_registry"
    if("pri_signal_version" not in df.columns):
        df['pri_signal_version'] = 'latest'
    if("sec_signal_version" not in df.columns):
        df['sec_signal_version'] = 'latest'

    return _post_json(url, df.to_dict(orient='records'), env)


def insert_signal_signal_rel_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_signal_rel_ts. 
        Input params - Dataframe containing the following columns: pri_signal_namespace, pri_signal_name, pri_signal_version(optional), sec_signal_namespace, sec_signal_name, sec_signal_version(optional), start_date, end_date, weight
    """
    url = "signal_signal_rel_ts"
    if("pri_signal_version" not in df.columns):
        df['pri_signal_version'] = 'latest'
    if("sec_signal_version" not in df.columns):
        df['sec_signal_version'] = 'latest'

    return _post_json(url, df.to_dict(orient='records'), env)


def insert_signal_scaler_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_scaler_ts. 
        Input params - Dataframe containing the following columns: data_date, signal_namespace, signal_name, signal_version(optional), data
    """
    url = "signal_scaler_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    return _post_json_using_chunks(url, df, env)


def insert_signal_asset_scaler_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_asset_scaler_ts specifying asset by asset_name. 
        Input params - Dataframe containing the following columns: data_date, signal_namespace, signal_name, signal_version(optional), asset_name, data
    """
    url = "signal_asset_scaler_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'

    return _post_json_using_chunks(url, df, env)


def insert_signal_asset_weight_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_asset_weight_ts specifying asset by asset_name. 
        Input params - Dataframe containing the following columns: data_date, signal_namespace, signal_name, signal_version(optional), asset_name, weight
    """
    url = "signal_asset_weight_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    return _post_json_using_chunks(url, df, env)


def insert_signal_asset_weight_ts_theoretical_bulk(df, env='local'):
    """
        Insert multiple records of signal_asset_weight_ts THEORETICAL (only for path dependent signals) specifying asset by asset_name.
        Input params - Dataframe containing the following columns: data_date, signal_namespace, signal_name, signal_version(optional), asset_name, weight
    """
    url = "signal_asset_weight_ts/theoretical"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    return _post_json_using_chunks(url, df, env)


# ---------- TC MODEL ------- #
def get_all_tc_models(env='local'):
    """Get all TC models
    """

    url = "tc_model"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_tc_model_asset_rel_quad_coeff(env='local'):
    """Get all TC model linear coefficients
    """

    url = "tc_model_asset_rel_quad_ts"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_tc_aum(env='local'):
    """Get all TC AUM models
    """

    url = "tc_aum"
    df = pd.DataFrame(_get_all(url, env))
    return df


# --------- Strategy ---------- #

def get_all_strategies(env='local'):
    """
        Return all strategy as DataFrame. No parameters required.
    """
    url = "strategy"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_strategy_clusters(env='local'):
    """
        Return all strategy_cluster as DataFrame. No parameters required.
    """
    url = "strategy_cluster"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_strategy_cluster_strategy_rels(env='local'):
    """
        Return all strategy_cluster_strategy_rel as DataFrame. No parameters required.
    """
    url = "strategy_cluster_strategy_rel"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_all_strategy_ts(env='local'):
    """
        Return all strategy as DataFrame. No parameters required.
    """
    url = "strategy_ts"
    df = pd.DataFrame(_get_all(url, env))
    return df



def insert_strategy(namespace, name, display_name, description, env='local'):
    """Insert strategy record

    Args:
        namespace (str): namespace
        name (str): name of strategy (must be unique)
        display_name (str): display name
        description (str): description

    Returns:
        JSON: Response from API
    """
    data = pd.DataFrame([{
        "namespace": namespace,
        "name": name,
        "display_name": display_name,
        "description": description,
    }
    ])
    return insert_strategy_bulk(data, env)


def insert_strategy_bulk(df, env='local'):
    """
        Insert multiple strategy records.
        Input params - dataframe containing the following columns: namespace, name, display_name, description
    """
    url = "strategy"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_strategy_ts_bulk(df, env='local'):
    """
        Insert multiple strategy_ts records.
        Input params - dataframe containing the following columns: strategy_namespace, strategy_name, signal_namespace, signal_name, signal_version(optional), gic_portfolio_code, aum, start_date, end_date(optional)
    """

    url = "strategy_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_strategy_cluster(namespace, name, display_name, description, env='local'):
    """Insert strategy cluster record

    Args:
        namespace (str): Namespace of strategy cluster
        name (str): name of strategy cluster (combined with namespace must be unique)
        display_name (str): display name
        description (str): description

    Returns:
        JSON: response from API
    """
    data = pd.DataFrame([{
        "namespace": namespace,
        "name": name,
        "display_name": display_name,
        "description": description,
    }])
    return insert_strategy_cluster_bulk(data, env)


def insert_strategy_cluster_bulk(df, env='local'):
    """
        Insert multiple strategy_cluster records. 
        Input params - dataframe containing the following columns: namespace, name, display_name, description
    """

    url = "strategy_cluster"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_strategy_cluster_strategy_rel(strategy_cluster_namespace, strategy_cluster_name, strategy_name, strategy_namespace,
                                   start_date, end_date=None, env='local'):
    """Insert one strategy into one strategy cluster

    Args:
        strategy_cluster_namespace (str): Namespace of strategy cluster
        strategy_cluster_name (str): name of strategy cluster
        strategy_namespace (str): namespace of strategy
        strategy_name (str): name of strategy
        start_date (str): start_date of relationship
        end_date (str, optional): end_date of relationship. Defaults to None.

    Returns:
        JSON: Response from API
    """
    data = pd.DataFrame([{
        "strategy_cluster_namespace": strategy_cluster_namespace,
        "strategy_cluster_name": strategy_cluster_name,
        "strategy_namespace": strategy_namespace,
        "strategy_name": strategy_name,
        "start_date": start_date,
        "end_date": end_date
    }])
    return insert_strategy_cluster_strategy_rel_bulk(data, env)


def insert_strategy_cluster_strategy_rel_bulk(df, env='local'):
    """
        Insert multiple strategy_cluster_strategy_rel records. 
        Input params - dataframe containing the following columns: 
            strategy_cluster_namespace, strategy_cluster_name, strategy_namespace, strategy_name, start_date, end_date
    """

    url = "strategy_cluster_strategy_rel"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_strategy_cluster_strategy_cluster_rel_bulk(df, env='local'):
    """
        Insert multiple strategy_cluster_strategy_cluster_rel records.
        Use is_primary to specify the primary strategy within a cluster.

    Args:
        df (DataFrame): dataframe containing the following columns: 
            parent_strategy_cluster_namespace, parent_strategy_cluster_name, child_strategy_cluster_name, child_strategy_cluster_namespace, is_primary, start_date, end_date

    Returns:
        JSON: Response from API
    """

    url = "strategy_cluster_strategy_cluster_rel"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_tc_model(name, display_name, description, type='quadratic', env='local'):
    """Registry a new TC model. Type can be "linear" or "quadratic"

    Args:
        name (str): name of tc model
        display_name (str): display name
        description (str): description
        type (str, optional): type of tc model. Defaults to 'quadratic'.

    Returns:
        JSON: Response from API
    """
    df = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "type": type
    }])

    return insert_tc_model_bulk(df, env)


def insert_tc_model_bulk(df, env='local'):
    """
        Registry multiple TC Models.
        Input params - dataframe containing the following columns: name, display_name, description, type (can be "linear" or "quadratic")
    """
    if ('type' not in df):
        df['type'] = 'linear'
    url = "tc_model"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_tc_model_asset_rel_quad_ts_bulk(df, env='local'):
    """Insert TC model asset coefficients (slope and intercept).

    Args:
        df(DataFrame) - Dataframe containing the following columns: data_date, tc_model_name, asset_name, param_0(intercept), param_1(slope)

    Returns:
        JSON - Response from API
    """
    url = "tc_model_asset_rel_quad_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_tc_aum(name, display_name, description, type, aum_source=None, env='local'):
    """
    Register a new TC Aum object.
    type can be : custom, strategy_stitched, strategy_latest
    aum_source can contain the single/list of strategy IDs where aum is extracted from
    aum_source cannot be null if type is not custom
    """
    df = pd.DataFrame.from_records([{
        "name": name,
        "display_name": display_name,
        "description": description,
        "type": type,
        "aum_source": aum_source
    }])

    return insert_tc_aum_bulk(df, env)


def insert_tc_aum_bulk(df, env='local'):
    """
        Insert multiple TC AUM records.
        Input params - dataframe containing the following columns: name, display_name, description
        type can be : custom, strategy_stitched, strategy_latest
        aum_source can contain the single/list of strategy IDs where aum is extracted from.
        aum_source cannot be null if type is not custom

    """
    url = "tc_aum"
    return _post_json(url, df.to_dict(orient='records'), env)


def insert_tc_aum_ts_bulk(df, env='local'):
    """
        Insert multiple TC AUM TS records.
        Input params - dataframe containing the following columns: data_date, tc_aum_name
    """
    url = "tc_aum_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_sigma_notional_ts(env='local'):
    """
        Return all sigma_notional_ts as DataFrame. No parameters required.
    """
    url = "sigma_notional_ts"
    df = pd.DataFrame(_get_all(url, env))
    return df


def insert_signal_notional_ts_bulk(df, env='local'):
    """
        Insert multiple Sigma notional time series records.
        Input params - dataframe containing the following columns: start_date, end_date, notional, scaler
    """
    url = "sigma_notional_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_signal_asset_weight(namespace, name, start_date, end_date=None, version='latest', env='local'):
    """Return all signal_asset_weight_ts filtered by signal, start date and end date as DataFrame.

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        start_date (str): start_date from when you want the weights (YYYY-MM-DD)
        end_date (str, optional): end_date till when you want the weights. Defaults to None.
        version (str, optional): version of signal. Defaults to 'latest'.

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_asset_weight"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "version": version,
        "namespace": namespace
    }

    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_asset_weight_stitched(namespace, name, start_date, end_date=None, version='latest', env='local'):
    """Return all signal_asset_weight_ts filtered by signal stitched over time according to different versions with same namespace/name by launch date.

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        start_date (str): start_date from when you want the weights (YYYY-MM-DD)
        end_date (str, optional): end_date till when you want the weights. Defaults to None.
        version (str, optional): version of signal. Defaults to 'latest'.

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_asset_weight_stitched"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "version": version,
        "namespace": namespace
    }

    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_pointer_asset_weight(namespace, name, start_date, end_date=None, version='latest', env='local'):
    """Return all signal_asset_weight_ts filtered by signal pointer, start date and end date as DataFrame.

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        start_date (str): start_date from when you want the weights (YYYY-MM-DD)
        end_date (str, optional): end_date till when you want the weights. Defaults to None.
        version (str, optional): version of signal. Defaults to 'latest'.

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_pointer_asset_weight"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "version": version,
        "namespace": namespace
    }

    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_asset_return(namespace, name, start_date, asset_return_type, end_date=None, version='latest', tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """Compute asset returns for the given signal. 

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        start_date (str): start_date
        asset_return_type (str): asset return type to compute.
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal version. Defaults to 'latest'.
        tc_model_name (str, optional): Name of TC model to use to get post-tc results
        weight_lag (int, optional): Lag weights by n. Default 1
        imp_lag (int, optional): Lag weights by weight_lag+imp_lag. Default 0
        fillna (boolean, optional): If True then fill na with 0 else return NaN

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_asset_return"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_asset_return_stitched(namespace, name, start_date, asset_return_type, end_date=None, version='latest', tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """Compute asset returns for the given signal stitched across versions using launch date.

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        start_date (str): start_date
        asset_return_type (str): asset return type to compute.
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal version. Defaults to 'latest'.
        tc_model_name (str, optional): Name of TC model to use to get post-tc results
        weight_lag (int, optional): Lag weights by n. Default 1
        imp_lag (int, optional): Lag weights by weight_lag+imp_lag. Default 0
        fillna (boolean, optional): If True then fill na with 0 else return NaN

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_asset_return_stitched"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_return(namespace, name, asset_return_type, start_date, end_date=None, version='latest', tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """Compute returns aggregated to signal level as dataframe. 

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        asset_return_type (str): asset return type to compute.
        start_date (str): start_date
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal version. Defaults to 'latest'.
        tc_model_name (str, optional): Name of TC model to use to get post-tc results
        weight_lag (int, optional): Lag weights by n. Default 1
        imp_lag (int, optional): Lag weights by weight_lag+imp_lag. Default 0
        fillna (boolean, optional): If True then fill na with 0 else return NaN

    Returns:
        df: DataFrame containing the signal returns
    """
    url = "retrieve_signal_return"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "version": version,
        "namespace": namespace,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, True)


def get_signal_pointer_return(namespace, name, asset_return_type, start_date, end_date=None, version='latest', tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """Compute returns aggregated to signal_pointer level as dataframe.

    Args:
        namespace (str): Namespace of signal_pointer
        name (str): Name of signal_pointer
        asset_return_type (str): asset return type to compute.
        start_date (str): start_date
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal_pointer version. Defaults to 'latest'.
        tc_model_name (str, optional): Name of TC model to use to get post-tc results
        weight_lag (int, optional): Lag weights by n. Default 1
        imp_lag (int, optional): Lag weights by weight_lag+imp_lag. Default 0
        fillna (boolean, optional): If True then fill na with 0 else return NaN

    Returns:
        df: DataFrame containing the signal_pointer returns
    """
    url = "retrieve_signal_pointer_return"
    data = {
        "start_date": start_date,
        "end_date": end_date,
        "name": name,
        "version": version,
        "namespace": namespace,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, True)


def get_signal_return_bulk(df, asset_return_type, start_date, end_date=None, tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """Compute returns aggregated to signal level as dataframe for multiple signals. 

    Args:
        df (DataFrame): DataFrame containing 3 columns: namespace, name, version
        asset_return_type (str): asset return type to compute.
        start_date (str): start_date
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal version. Defaults to 'latest'.
        tc_model_name (str, optional): Name of TC model to use to get post-tc results
        weight_lag (int, optional): Lag weights by n. Default 1
        imp_lag (int, optional): Lag weights by weight_lag+imp_lag. Default 0
        fillna (boolean, optional): If True then fill na with 0 else return NaN

    Returns:
        df: DataFrame containing the signal returns
    """
    url = "retrieve_signal_return_bulk"

    if("version" not in df.columns):
        df["version"] = "latest"

    df.loc[:, 'asset_return_type'] = asset_return_type
    df.loc[:, 'start_date'] = start_date
    df.loc[:, 'end_date'] = end_date
    df.loc[:, 'tc_model_name'] = tc_model_name
    df.loc[:, 'weight_lag'] = weight_lag
    df.loc[:, 'imp_lag'] = imp_lag
    df.loc[:, 'fillna'] = fillna

    resp = _post_json(url, df.to_dict(orient='records'), env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_asset_return_types(asset_name, env='local'):
    """Get all the return types for an asset 

    Args:
        asset_name (str): name of asset

    Returns:
        df: DataFrame containing the different return types of asset
    """
    url = "retrieve_asset_return"
    data = {
        "name": asset_name,
    }
    return pd.DataFrame(_post_data(url, data, env))


def get_asset_return_ts_by_return_type(asset_return_type, start_date, end_date=None, env='local'):
    """Get the return time series for the specified asset and return type

    Args:
        asset_return_type (str): name of return type
        start_date (str, optional): start date for returns. Defaults to "latest".
        end_date (str, optional): end date for returns. Defaults to None.

    Returns:
        df: DataFrame containing asset returns time series
    """
    url = "retrieve_asset_return_ts_by_return_type"
    data = {
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "start_date": start_date,
        "end_date": end_date,
    }
    return pd.DataFrame(_post_data(url, data, env))


def get_asset_return_ts(asset_name, start_date, asset_return_type="primary", end_date=None, env='local'):
    """Get the return time series for the specified asset and return type

    Args:
        asset_name (str): name of asset
        start_date (str, optional): start date for returns. Defaults to "latest".
        end_date (str, optional): end date for returns. Defaults to None.
        asset_return_type (str, optional): return type to query

    Returns:
        df: DataFrame containing asset returns time series
    """
    url = "retrieve_asset_return_ts"
    data = {
        "name": asset_name,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str)
    }
    return pd.DataFrame(_post_data(url, data, env))


def get_strategy_return_latest(namespace, name, asset_return_type, start_date, end_date=None, tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """
        Latest strategy return means use the latest signal throughout history
    """
    url = "retrieve_strategy_return_latest"
    data = {
       "namespace": namespace,
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_strategy_return_stitched(namespace, name, asset_return_type, start_date, end_date=None, tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """
        Stitched strategy return means keep changing signal return based on which was linked to strategy at the time
    """
    url = "retrieve_strategy_return_stitched"
    data = {
        "namespace": namespace,
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna

    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_strategy_weight_stitched(namespace, name, start_date, end_date=None, env='local'):
    """
        Stitched strategy weight means keep changing signal weight based on which was linked to strategy at the time
    """
    url = "retrieve_strategy_weight_stitched"
    data = {
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "namespace": namespace
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_strategy_ts(namespace, name, env='local'):
    """
        Stitched strategy return means keep changing signal return based on which was linked to strategy at the time
    """
    url = "retrieve_strategy_ts"
    data = {
        "name": name,
        "namespace": namespace
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=False)


def get_asset(asset_name, env='local'):
    """
        Get Asset object specified by the name
    """
    url = "retrieve_asset"
    data = {
        "name": asset_name,
    }
    return _post_data(url, data, env)


def get_asset_by_id(id, env='local'):
    """Get model object specified by ID
    """
    url = "asset/{}".format(id)
    return _get_all(url, env)


def get_asset_by_id_list(id_list, env='local'):
    """Get model object specified by list of IDs
    """
    url = "retrieve_asset_by_id_list"
    data = {
        "id": id_list
    }

    resp = _post_data(url, data, env)
    return pd.DataFrame(resp)


def get_signal(namespace, name, version="latest", env='local'):
    """
        Get signal object specified by the name
    """
    url = "retrieve_signal"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
    }
    return _post_data(url, data, env)


def get_signal_pointer(namespace, name, version="latest", env='local'):
    """
        Get signal pointer object specified by the namespace/name
    """
    url = "retrieve_signal_pointer"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
    }
    return _post_data(url, data, env)


def get_signal_by_id(id, env='local'):
    """Get signal  specified by ID
    """
    url = "signal/{}".format(id)
    return _get_all(url, env)


def get_signal_by_id_bulk(id_list, env='local'):
    """Get signals specified the list of Ids
    """
    url  = 'retrieve_signal_by_id_bulk'
    data = {
        'id_list': ','.join([str(x) for x in id_list])
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def get_signal_asset_universe(namespace, name, version="latest", env='local'):
    """
        Get signal group meta data for the specified signal group
    """
    url = "retrieve_signal_asset_universe"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
    }
    return pd.DataFrame(_post_data(url, data, env))


def get_signal_meta_data(namespace, name, version="latest", env='local'):
    """Get signal meta data for the list of signals specified

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        version (str, optional): version of signal. Defaults to "latest".

    Returns:
        df: DataFrame containing meta data of signal
    """
    url = "retrieve_signal_meta_data"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
    }
    return pd.DataFrame(_post_data(url, data, env))

    
def get_signal_meta_data_bulk(df, env='local'):
    """Get signal meta data for the list of signals specified

    Args:
        df(DataFrame) : df containing the following columns:  name, version, namespace
    """
    url = "retrieve_signal_meta_data_bulk"
    return pd.DataFrame(_post_json(url, df.to_dict(orient='records'), env))


def get_asset_universe(name, version="latest" , env='local'):
    """Get asset universe object specified by the name and version
    """
    url = "retrieve_asset_universe"
    data = {
        "name": name,
        "version": version
    }
    return _post_data(url, data, env)


def get_asset_universe_by_id(id, env='local'):
    """Get model object specified by ID
    """
    url = "asset_universe/{}".format(id)
    return _get_all(url, env)


def get_asset_type(name, env='local'):
    """Get asset type object specified by the name
    """
    url = "retrieve_asset_type"
    data = {
        "name": name,
    }
    return _post_data(url, data, env)


def get_asset_universe_constituents(name, version="latest" , env='local'):
    """Get constituents of specified asset universe (can be static or dynamic)

    Args:
        name (str): Name of asset universe
        version (version, optional): Version of asset universe. Defaults to "latest".

    Returns:
        DataFrame: DF containing constituents of the asset universe
    """
    url = "retrieve_asset_universe_constituents"
    data = {
        "name": name,
        "version": version
    }
    return pd.DataFrame(_post_data(url, data, env))


def get_strategy(namespace, name, env='local'):
    """Get strategy dictionary specified by name/namespace
    """
    url = "retrieve_strategy"
    data = {
        "name": name,
        "namespace": namespace
    }
    return _post_data(url, data, env)


def get_strategy_cluster(namespace, name, env='local'):
    """Get strategy cluster details specified by name/namespace

    Args:
        namespace (str): Namespace
        name (str): Name

    Returns:
        JSON: Response from API
    """
    url = "retrieve_strategy_cluster"
    data = {
        "name": name,
        "namespace": namespace
    }
    return _post_data(url, data, env)


def get_tc_coefficients(tc_model_name, env='local'):
    """Get all coefficients for the given TC Model
    """

    url = "retrieve_tc_coefficients"
    data = {
        "name": tc_model_name,
    }

    return pd.DataFrame(_post_data(url, data, env))


def get_all_top_node_strategy_clusters(env='local'):
    """
        Return all top node strategy clusters as DataFrame
    """
    strategy_cluster_df = get_all_strategy_clusters(env)
    if (strategy_cluster_df.shape[0] == 0):
        return "No Strategy Clusters found!"
    strategy_cluster_df = strategy_cluster_df[strategy_cluster_df['name'] == strategy_cluster_df['namespace']]
    strategy_cluster_df.drop('namespace', axis=1, inplace=True)
    return strategy_cluster_df


def get_all_namespaces(env='local'):
    """
        Return all valid namespaces as list. No parameters required.
    """
    top_node_clusters = get_all_top_node_strategy_clusters(env)
    if (isinstance(top_node_clusters, str)):
        return top_node_clusters

    valid_namespace_list = top_node_clusters['name'].tolist()
    return valid_namespace_list


def get_strategy_cluster_return_stitched(namespace, name, asset_return_type, start_date, end_date=None, tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """
        Stitched strategy_cluster return means stitch the  stitched strategy returns 
    """
    url = "retrieve_strategy_cluster_return_stitched"
    data = {
        "namespace": namespace,
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna

    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df_split(resp, convert_to_datetime=True)


def get_strategy_cluster_return_latest(namespace, name, asset_return_type, start_date, end_date=None, tc_model_name=None, weight_lag=1, imp_lag=0, fillna=False, env='local'):
    """
        Latest strategy_cluster return means stitch the latest strategy returns 
    """
    url = "retrieve_strategy_cluster_return_latest"
    data = {
        "namespace": namespace,
        "name": name,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str),
        "tc_model_name": tc_model_name,
        "weight_lag": weight_lag,
        "imp_lag": imp_lag,
        "fillna": fillna

    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df_split(resp, convert_to_datetime=True)





def asset_return_synchronize(env='local'):
    """
        Combine assets with return types according to the asset type to create an Asset Return registry.
    """
    url = "asset_return_synchronize"
    return _post_data(url, None, env)


# Versioning
def get_signal_latest_version_bulk(df, env='local'):
    """Get latest versions of the signal provided

    Args:
        df (DataFrame): df should contain the following columns: namespace, name

    Returns:
        DataFrame: DF containing the latest signal versions
    """
    url = "retrieve_signal_latest_version_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)

    if (isinstance(resp, Response)):
        return resp
    return pd.DataFrame(resp)


def update_signal_asset_universe_bulk(df, env='local'):
    """Update asset universe of multiple signals

    Args:
        df (DataFrame): columns include namespace, name, version, asset_universe_name, asset_universe_version

    """
    url = "update_signal_asset_universe_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    return resp


def get_signal_signal_heuristic_weights_as_of_date(as_of_date=datetime.now().strftime("%Y-%m-%d"), env='local'):
    """Get all signal-signal heuristic weights active as at the given date

    Args:
        as_of_date (str, optional): Date in string. Defaults to datetime.now().strftime("%Y-%m-%d")

    Returns:
        df: DataFrame containing all signal-signal heuristic weights relationships
    """
    url = "retrieve_signal_signal_heuristic_weights_as_of_date"
    data = {
        "as_of_date": as_of_date
    }
    resp = _post_data(url, data, env)
    if isinstance(resp, Response):
        return resp
    return pd.read_json(resp)


def get_all_signal_signal_rel_registry(env='local'):
    """Get all signal signal relationship registry

    Returns:
        dataFrame: DF containing the relationship registries
    """
    url = "signal_signal_rel_registry"
    resp = pd.DataFrame(_get_all(url, env))
    return resp


# MM Staging

def insert_staging_job(context, launch_date, remarks, env='local'):
    """Creating a staging job record. To be called by the upgrade tool

    Args:
        context (str): string containing the list of top nodes used as context
        launch_date (str): launch date of this versioning upgrade
        remarks (str): Any remarks related to this upgrade

    Returns:
        JSON: Response from API
    """
    url = "staging_job"
    data = {
        "context": context,
        "launch_date": launch_date,
        "remarks": remarks,
    }

    return _post_data(url, data, env)


def insert_staging_signal_scaler_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_scaler_ts.
        Input params - Dataframe containing the following columns: job_id, data_date, signal_namespace, signal_name, signal_version, data
    """
    url = "staging_signal_scaler_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    df = df[df['data_date']>'2017-01-01']
    return _post_json_using_chunks(url, df, env)


def insert_staging_signal_asset_scaler_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_asset_scaler_ts.
        Input params - Dataframe containing the following columns: job_id, data_date, signal_namespace, signal_name, signal_version, asset_name, data
    """
    url = "staging_signal_asset_scaler_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    #TODO: REMOVE THIS
    df = df[df['data_date']>'2017-01-01']
    return _post_json_using_chunks(url, df, env)


def insert_staging_signal_asset_weight_ts_bulk(df, env='local'):
    """
        Insert multiple records of signal_asset_weight_ts.
        Input params - Dataframe containing the following columns: job_id, data_date, signal_namespace, signal_name, signal_version, asset_name, weight
    """
    url = "staging_signal_asset_weight_ts"
    if("signal_version" not in df.columns):
        df['signal_version'] = 'latest'
    df = df[df['data_date']>'2017-01-01']
    return _post_json_using_chunks(url, df, env)


def commit_version_upgrade(upgrade_dict, env='local'):
    """Commit all the versioning changes to the DB (to be called through the upgrade tool)

    Args:
        upgrade_dict (dict): Dict containing various dataframes to commit to db

    Returns:
        JSON: Response from API
    """
    url = "commit_version_upgrade"
    resp = _post_json(url, upgrade_dict, env)
    if isinstance(resp, Response):
        return resp.json()
    return resp


def get_signal_scaler_bulk(df, env='local'):
    """Return signal scalers of the signals specified

    Args:
        df (DataFrame): DataFrame containing the following columns: namespace, name, version

    Returns:
        df (DataFrame): DataFrame containing the scalers of the signals
    """
    url = "retrieve_signal_scaler_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)


def get_signal_asset_scaler_bulk(df, env='local'):
    """Return signal asset scalers of the signals specified

    Args:
        df (DataFrame): DataFrame containing the following columns: namespace, name, version

    Returns:
        df (DataFrame): DataFrame containing the asset scalers of the signals
    """
    url = "retrieve_signal_asset_scaler_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)


def get_signal_asset_weight_bulk(df, start_date, end_date="2199-12-31", env='local'):
    """Return signal asset weights of the signals specified

    Args:
        df (DataFrame): DataFrame containing the following columns: namespace, name, version
        start_date(str): Date from where you want the asset weights to start. (in YYYY-MM-DD)

    Returns:
        df (DataFrame): DataFrame containing the asset weights of the signals
    """
    url = "retrieve_signal_asset_weight_bulk"
    df.loc[:, 'start_date'] = start_date
    df.loc[:, 'end_date'] = end_date
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)


def get_signal_bulk(df, env='local'):
    """Return a list of signals as specified by the input parameters

    Args:
        df (DataFrame): DataFrame containing the following columns: namespace, name, version

    Returns:
        df (DataFrame): DataFrame containing the list of signals with those attributes
    """
    url = "retrieve_signal_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)


def get_signal_pointer_bulk(df, env='local'):
    """Return a list of signal pointers as specified by the input parameters

    Args:
        df (DataFrame): DataFrame containing the following columns: namespace, name, version

    Returns:
        df (DataFrame): DataFrame containing the list of signal pointerss with those attributes
    """
    url = "retrieve_signal_pointer_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)



def get_signal_pointer_using_signal_bulk(df, env='local'):
    """Return a list of signal pointers based on the given signal attributes

    Args:
        df (DataFrame): DataFrame containing the following columns: signal_namespace, signal_name, signal_version

    Returns:
        df (DataFrame): DataFrame containing the list of signal pointers associated with the given signals
    """
    url = "retrieve_signal_pointer_using_signal_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if isinstance(resp, Response):
        return resp
    return pd.DataFrame(resp)


def delete_signal_details(namespace, name, version='latest', env='local'):
    """Delete everything related to a signal to start over. Deletes the following:
    1. Signal Asset Scaler / Signal Scaler / Signal Asset Weight
    2. Signal Signal relationships
    3. Signal meta data
    4. Signal pointer
    5. Strategy Time series
    6. Signal Registry
    7. Asset universe constituents
    8. Asset universe registry

    Args:
        namespace (str): namespace of signal
        name (str): name of signal
        version (str, optional): Signal version. Defaults to 'latest'.
    """
    url = "delete_signal_details"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version
    }
    resp = _post_json(url, data, env)
    return resp


def get_signal_children(namespace, name, version='latest', as_of_date=datetime.now().strftime("%Y-%m-%d"), env='local'):
    """Return all child signals of the specified signal

    Args:
        namespace (str): Namespace of signal
        name (str): Name of signal
        version (str, optional): Version of signal. Defaults to 'latest'.
        as_of_date (str, optional): Date to fetch relationships as of. Defaults to now
    """

    url = "retrieve_signal_children"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "as_of_date": as_of_date
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)


def get_signal_pointer_descendents(pointer_namespace, pointer_name, pointer_version='latest', env='local'):
    """Return all child signals of the specified signal using signal pointer

    Args:
        pointer_namespace (str): namespace of signal pointer
        pointer_name (str): name of signal pointer
        version (str, optional): Version of signal pointer. Defaults to 'latest'.
        as_of_date (str, optional): Date to fetch relationships as of. Defaults to now
    """

    url = "retrieve_signal_pointer_descendents"
    data = {
        "namespace": pointer_namespace,
        "name": pointer_name,
        "version": pointer_version,
    }
    resp = _post_data(url, data, env)
    if(isinstance(resp, Response)):
        return resp

    return resp


def delete_staging_signal_asset_scaler_by_job_id(job_id, env='local'):
    """Delete Staging signal asset scaler by job id

    Args:
        job_id (int): Job ID to delete asset scalers of

    Returns:
        JSON: Response from API
    """
    url = "delete_staging_signal_asset_scaler_by_job_id"
    data = {
        "job_id": job_id,
    }
    resp = _post_json(url, data, env)
    return resp


def delete_staging_signal_asset_weight_by_job_id(job_id, env='local'):
    """Delete Staging signal asset weight by job id

    Args:
        job_id (int): Job ID to delete asset weights of

    Returns:
        JSON: Response from API
    """
    url = "delete_staging_signal_asset_weight_by_job_id"
    data = {
        "job_id": job_id,
    }
    resp = _post_json(url, data, env)
    return resp


def delete_staging_signal_scaler_by_job_id(job_id, env='local'):
    """Delete Staging signal scaler by job id

    Args:
        job_id (int): Job ID to delete scalers of

    Returns:
        JSON: Response from API
    """
    url = "delete_staging_signal_scaler_by_job_id"
    data = {
        "job_id": job_id,
    }
    resp = _post_json(url, data, env)
    return resp


def update_strategy_ts(strategy_namespace, strategy_name, start_date, aum=None, signal_id=None, gic_portfolio_code=None, env='local'):
    """Update AUM of a strategy. Only submit the signal_id and gic_portfolio code if replacing the current ones.

    Args:
        strategy_namespace (str): Namespace of strategy
        strategy_name (str): Name of strategy
        start_date (str): start_date from when new AUM is implemented
        aum (float): AUM value to override current aum. Optional
        signal_id (int, optional): ID of signal to override the current signal. Do not need to submit if using the same signal. Defaults to None.
        gic_portfolio_code (str, optional): GIC Portfolio code to override the current code. Do not need to submit if using the same code. Defaults to None.
    """
    url = "update_strategy_ts"
    if((not aum) and (not signal_id) and (not gic_portfolio_code)):
        return "Please insert one of aum/signal_id/gic_portfolio_code to update"
    data = {
        "strategy_namespace": strategy_namespace,
        "strategy_name": strategy_name,
        "start_date": start_date,
        "aum": aum,
        "signal_id": signal_id,
        "gic_portfolio_code": gic_portfolio_code
    }

    resp = _post_json(url, data, env)
    return resp


def get_signal_heuristic_weights(signal_namespace, signal_name, signal_version='latest', env='local'):
    """Get current heuristic weights of a signal

    Args:
        signal_namespace (str): Namespace
        signal_name (str): Name of signal
        signal_version (str, optional): version of signal. Defaults to 'latest'.
    """

    url = "retrieve_signal_heuristic_weights"
    data = {
        "namespace": signal_namespace,
        "name": signal_name,
        "version": signal_version
    }

    resp = _post_json(url, data, env)
    return _convert_response_to_df(resp)


def get_all_signals_with_asset_weight(env='local'):
    """
        Return all signal as DataFrame. No parameters required.
    """
    url = "retrieve_all_signals_with_asset_weight"
    df = pd.DataFrame(_get_all(env, url))
    return df

def get_all_signals_with_asset_scaler(env='local'):
    """
        Return all signal as DataFrame. No parameters required.
    """
    url = "retrieve_all_signals_with_asset_scaler"
    df = pd.DataFrame(_get_all(url, env))
    return df

def get_all_signals_with_signal_scaler(env='local'):
    """
        Return all signal as DataFrame. No parameters required.
    """
    url = "retrieve_all_signals_with_signal_scaler"
    df = pd.DataFrame(_get_all(url, env))
    return df


def get_signal_pointer_asset_return(namespace, name, start_date, asset_return_type, end_date=None, version='latest', env='local'):
    """Compute asset returns for the given signal pointer.

    Args:
        namespace (str): Namespace of signal pointer
        name (str): Name of signal pointer
        start_date (str): start_date
        asset_return_type (str): asset return type to compute.
        end_date (str, optional): end_date. Defaults to None.
        version (str, optional): signal pointer version. Defaults to 'latest'.

    Returns:
        JSON: Response from API
    """
    url = "retrieve_signal_pointer_asset_return"
    data = {
        "namespace": namespace,
        "name": name,
        "version": version,
        "start_date": start_date,
        "end_date": end_date,
        "asset_return_type": json.dumps(asset_return_type, indent=4, sort_keys=True, default=str)
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp, convert_to_datetime=True)

def get_signal_pointer_return_bulk(df, env='local'):
    """Get returns of a list of signal pointers.
    df should contain the following columns: namespace, name, version, asset_return_type, start_date, end_date(optional), tc_model_name(optional)

    Args:
        df (DataFrame): DataFrame containing signal pointer details
    """
    url = "retrieve_signal_pointer_return_bulk"
    resp = _post_json(url, df.to_dict(orient='records'), env)
    if (isinstance(resp, Response)):
        return resp
    return pd.DataFrame(resp)


# Auth

def insert_group(group_name, env='local'):
    """Create a User group

    Args:
        group_name (str): name of user group
    """
    return insert_group_bulk([group_name], env)

def insert_group_bulk(group_name_list, env='local'):
    """Create multiple user groups

    Args:
        group_name_list (list(str)): List of strings containing the group names to create
    """
    url = "group"
    df = pd.DataFrame({
        'name': group_name_list
    })
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_groups(env='local'):
    """Get all user groups

    Returns:
        DF: DataFrame containing all user groups
    """
    url = "group"
    return pd.DataFrame(_get_all(url, env))


def insert_user_group_rel(group_name, ntid, env='local'):
    """Insert relationship between user and group

    Args:
        group_name (str): name of group
        ntid (str): ntid of user
    """
    df = pd.DataFrame({
        "group_name": group_name,
        "ntid": ntid,
    }, index=[0])

    return insert_user_group_rel_bulk(df, env)

def insert_user_group_rel_bulk(df, env='local'):
    """Insert multiple relationship between users and groups
    DF should be containing 2 columns: group_name, ntid
    """
    url = "user_group_rel"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_user_group_rel(env='local'):
    """Get all relationships between user and groups

    Returns:
        DataFrame: DF containing r'ship between ntids and group names
    """
    url = "user_group_rel"
    return pd.DataFrame(_get_all(url, env))


def insert_strategy_group_rel(strategy_namespace, strategy_name, group_name, env='local'):
    """Link strategy to group

    Args:
        strategy_namespace (str): namespace of strategy
        strategy_name (str): name of strategy
        group_name (str): name of group
    """
    df = pd.DataFrame({
        "strategy_namespace": strategy_namespace,
        "strategy_name": strategy_name,
        "group_name": group_name,
    }, index=[0])

    return insert_strategy_group_rel_bulk(df, env)

def insert_strategy_group_rel_bulk(df, env='local'):
    """Link multiple strategies to groups
    Df should be containing the following columns: strategy_namespace,strategy_name,group_name

    Args:
        df (DataFrame): DF containing the strategies and groups
    """
    url = "strategy_group_rel"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_strategy_group_rel(env='local'):
    """Get all relationships between strategies and groups

    Returns:
        df: DataFrame containing relationships between strategies and groups
    """
    url = "strategy_group_rel"
    return pd.DataFrame(_get_all(url, env))


def insert_signal_strategy_rel(strategy_namespace, strategy_name, signal_namespace, signal_name, signal_version="latest", env='local'):
    """Create relationship between strategy and signal

    Args:
        strategy_namespace (str): namespace of strategy
        strategy_name (str): name of strategy
        signal_namespace (str): namespace of signal
        signal_name (str): name of signal
        signal_version (str, optional): version of signal. Defaults to "latest".
    """
    df = pd.DataFrame({
        "strategy_namespace": strategy_namespace,
        "strategy_name": strategy_name,
        "signal_namespace": signal_namespace,
        "signal_name": signal_name,
        "signal_version": signal_version,
    }, index=[0])

    return insert_signal_strategy_rel_bulk(df, env)

def insert_signal_strategy_rel_bulk(df, env='local'):
    """Create multiple relationships between strategies and signals.
    DF should be containing the following columns: strategy_namespace, strategy_name, signal_namespace, signal_name, signal_version(optional)

    Args:
        df (DataFrame): DF containing the aforementioned columns
    """
    url = "signal_strategy_rel"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_signal_strategy_rel(env='local'):
    """Get all relationships between strategies and signals

    Returns:
        df: DataFrame containing relationships between strategies and groups
    """
    url = "signal_strategy_rel"
    return pd.DataFrame(_get_all(url, env))
    

def signal_strategy_rel_synchronize(env='local'):
    """Automatically create relationships between signals and strategies for the purpose of authentication
    """ 
    url = "signal_strategy_rel_synchronize"
    return _post_data(url, None, env)


def get_strategy_cluster_strategy_rels(namespace, name, env='local'):
    """Get members of a strategy cluster

    Args:
        namespace (str): Namespace of strategy cluster
        name (str): name of strategy cluster
    """
    url = "retrieve_strategy_cluster_strategy_rels"
    data = {
        "namespace": namespace,
        "name": name
    }

    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def insert_strategy_param_ts(data_date, strategy_namespace, strategy_name, param, env='local'):
    """Create time series data beadding a JSON param field to strategy

    Args:
        data_date (str): data_date in YYYY-MM-DD
        strategy_namespace (str): namespace of strategy
        strategy_name (str): name of strategy
        param (str): string representation of JSON containing data to upload

    Returns:
        _type_: _description_
    """
    df = pd.DataFrame({
        "data_date": data_date,
        "strategy_namespace": strategy_namespace,
        "strategy_name": strategy_name,
        "param": param,
    }, index=[0])

    return insert_strategy_param_ts_bulk(df, env)


def insert_strategy_param_ts_bulk(df, env='local'):
    """Create time series data adding a aram field to strategy
    DF should be containing the following columns: data_date, strategy_namespace, strategy_name, param(JSON)

    Args:
        df (DataFrame): DF containing the aforementioned columns
    """
    url = "strategy_param_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_all_strategy_param_ts(env='local'):
    """Get all relationships between strategies and signals

    Returns:
        df: DataFrame containing relationships between strategies and groups
    """
    url = "strategy_param_ts"
    return pd.DataFrame(_get_all(url, env))


def get_strategy_param_ts(namespace, name, env='local'):
    """Get all relationships between strategies and signals

        Args:
        namespace (str): Namespace of strategy 
        name (str): name of strategy 
    """
    url = "retrieve_strategy_param_ts"
    data = {
        "namespace": namespace,
        "name": name
    }

    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def delete_signal_asset_weight_ts_bulk(signal_id_list, env='local'):
    url = "delete_signal_asset_weight_ts_bulk"
    data = {
        "id": signal_id_list
    }

    resp = _post_data(url, data, env)
    return pd.DataFrame(resp)


def get_all_asset_return_config(env='local'):
    """Get all asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, name, return_type_name, data

    Returns:
        str: Message from API
    """
    url = "asset_return_config"
    df = pd.DataFrame(_get_all(url, env))
    return df


def insert_asset_return_config_bulk(df, env='local'):
    """Insert asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, name, return_type_name, data

    Returns:
        str: Message from API
    """
    url = "asset_return_config"
    return _post_json(url, df.to_dict(orient='records'), env)


def get_asset_return_status_ts(start_date, end_date=datetime.now().strftime("%Y-%m-%d"), env='local'):
    """Get Asset return status 

    Args:
        start_date (str): start date
        end_date (str, optional): end date. Defaults to today
        env (str, optional): environment. Defaults to 'local'.

    Returns:
        df: DataFrame containing the return ingestion statuses
    """
    url = "retrieve_asset_return_status_ts"
    data = {
        "start_date": start_date,
        "end_date": end_date
    }
    resp = _post_data(url, data, env)
    return _convert_response_to_df(resp)


def insert_asset_return_status_ts_bulk(df, env='local'):
    """Insert asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, asset_name, return_type_name, data

    Returns:
        str: Message from API
    """
    url = "asset_return_status_ts"
    return _post_json(url, df.to_dict(orient='records'), env)


def update_asset_return_status_ts_bulk(df, env='local'):
    """Insert asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, asset_name, return_type_name, status

    Returns:
        str: Message from API
    """
    url = "asset_return_status_ts/update_status"
    return _post_json(url, df.to_dict(orient='records'), env)


def delete_asset_return_ts_bulk(df, env='local'):
    """Insert asset return time series specifying asset using asset_name
    Args:
        df (DataFrame): DataFrame containing the following columns: data_date, asset_name, return_type_name

    Returns:
        str: Message from API
    """
    url = "delete_asset_return_ts_bulk"
    return _post_json(url, df.to_dict(orient='records'), env)
