from pathlib import Path
import pandas as pd
import datetime

def build_index(target_folder):
    target_folder = Path(target_folder)
    dfs = [
            get_measurement_info(_get_json_file(_)) 
            for _ in target_folder.iterdir() 
            if _.is_dir()
        ]
    if len(dfs) == 0:
        raise "No data found"
    else:
        return pd.concat(dfs, ignore_index=True).drop_duplicates()

def _get_json_file(data_folder):
    for _ in data_folder.iterdir():
        if _.suffix == '.json':
            return _

def get_measurement_info(json_file):
    df = pd.read_json(json_file, convert_dates=['measurement_datetime'])
    return df[['measurement_datetime', 'measurement_name', 'uuid', "measurement_type"]]

def save_index(target_folder):
    target_folder = Path(target_folder)
    index = build_index(target_folder)
    _save_json(target_folder, index)

def _save_json(target_folder, df):
    df['measurement_datetime'] = df['measurement_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df.to_json(
        str((target_folder / 'index.json').absolute()), indent=4, orient='records'
    )

def load_index(target_folder):
    target_folder = Path(target_folder)
    return pd.read_json(target_folder/'index.json', convert_dates=['measurement_datetime'])

def append_index(target_folder, new_data):
    target_folder = Path(target_folder)
    if not (target_folder/'index.json').exists():
        return save_index(target_folder)
    else:
        df = load_index(target_folder)
        df = pd.concat([df, new_data[['measurement_datetime', 'measurement_name', 'uuid', "measurement_type"]]], ignore_index=True).drop_duplicates()
        _save_json(target_folder, df)
