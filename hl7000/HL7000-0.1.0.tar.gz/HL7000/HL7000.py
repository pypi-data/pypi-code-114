import configparser
import pandas as pd
import datetime
from pathlib import Path
from uuid import uuid4

import shutil

from HL7000.helper_functions import save_index, append_index, load_index

class Measurement:
    def __init__(self, measurement_folder):
        self.measurement_folder = Path(measurement_folder)
        self.config_file = self.measurement_folder/'info.ini'
        self.config_data = self.read_config(self.config_file)
        self.measurement_type = self.get_measurement_type(self.config_data)
        self.measurement_uuid = str(uuid4()).replace("-", "_")
        self.data = self.parse_measurement()

    def parse_measurement(self):
        # self.measurement_folder = Path(measurement_folder)
        # self.config_file = self.measurement_folder/'info.ini'
        # self.config_data = self.read_config(self.config_file)
        # self.measurement_type = self.get_measurement_type(self.config_data)

        self.data = None
        if self.measurement_type == "Histogram":
            self.data = self.parse_histogram_measurement(self.config_data, self.measurement_folder)
        elif self.measurement_type == "Level":
            self.data =  self.parse_level_measurement(self.config_data, self.measurement_folder)
        else:
            raise Exception("Unknown measurement type")

        return self.data

    def read_config(self, _config_file):
        config = configparser.ConfigParser()
        config.read(_config_file)
        return config

    def get_measurement_type(self, _config):
        return {
            'Histogram': "Histogram",
            'Levelmeasurement': "Level"    
        }.get(_config['Measurementinfo']['Measurementtype'])

    def parse_measurement_info(self, _config):
        _data = _config['Measurementinfo']
        _date = datetime.datetime.strptime(_data['Measurementdate'], "%d.%m.%Y").date()
        _time = datetime.time(*[int(_) for _ in _data['Measurementtime'].split(":")]) 

        return {
            "measurement_datetime": datetime.datetime.combine(_date, _time),
            "measurement_name": _data['Measurementname'],
            "measurement_type": _data['Measurementtype'],
            "firmware_version": _data['Firmwareversion'],
        }

    def parse_filter(self, _config):
        _config = _config["Filter"]
        return {
        "filter_type": _config["filtertype"],
        "high_cutoff": int(_config["highcutoff-frequency"]),
        "low_cutoff": int(_config["lowcutoff-frequency"])
        }

    def parse_gain(self, _config):
        _config = _config["Gains"]
        return {
            "headphone_gain": _config["headphone-gain"],
            "microphone_gain": _config["microphone-gain"],
        }

    def build_level_data(self, _config):
        fft = _config["FFT"]
        fft_size = fft["fft-size"]
        fft_values = fft['fft-values'].replace('"', "")
        fft_samplerate = fft['samplerate']
        gps = _config["GPS-Positions"]["GPS-Position"].replace('"', "")

        gps_lat = float(gps.split(', ')[0])
        gps_long = float(gps.split(', ')[1])

        return {
            "fft_size": fft_size,
            "fft_values": fft_values,
            "fft_samplerate": fft_samplerate,
            "gps_latitude": gps_lat,
            "gps_longitude": gps_long
        }

    def parse_level_measurement(self, config, folder_path):
        _d = pd.DataFrame(self.build_level_data(config), index=[0])
        _m = pd.DataFrame(self.parse_measurement_info(config), index=[0])
        _f = pd.DataFrame(self.parse_filter(config), index=[0])
        _g = pd.DataFrame(self.parse_gain(config), index=[0])

        _df = _d.merge(_m, how='cross').merge(_f, how='cross').merge(_g, how='cross')

        _df["sample_path"] = str((folder_path/f"LE_Sound.wav").absolute())
        _df = _df.loc[_df['sample_path'].apply(lambda x: Path(x).is_file())]

        _df['uuid'] = self.measurement_uuid

        return _df

    def build_histogram_data(self, _config):
        gps_sorted = sorted(_config['GPS-Positions'], key=lambda x: int(x.split('_')[1]))
        gps_data = [_config['GPS-Positions'][_].replace('"', "") for _ in gps_sorted]

        gps_lat = [float(_.split(', ')[0]) for _ in gps_data]
        gps_long = [float(_.split(', ')[1]) for _ in gps_data]

        levels_level = [_ for _ in _config['Levels'] if 'Level'.upper() in _.upper()]
        levels_sorted = sorted(levels_level, key=lambda x: int(x.split('_')[1]))
        levels_data = [float(_config['Levels'][_]) for _ in levels_sorted]

        frequency_level = [_ for _ in _config['Levels'] if 'Frequency'.upper() in _.upper()]
        frequency_sorted = sorted(frequency_level, key=lambda x: int(x.split('_')[1]))
        frequency_data = [int(_config['Levels'][_]) for _ in frequency_sorted]

        sample_number = [int(_.split("_")[1]) for _ in gps_sorted]

        return {
            # 'gps_data': gps_data,
            'sample_number': sample_number,
            'gps_latitude': gps_lat,
            'gps_longitude': gps_long,
            'levels_data': levels_data,
            'frequency_data': frequency_data
        }

    def parse_histogram_measurement(self, config, folder_path):
        _d = pd.DataFrame(self.build_histogram_data(config))
        _m = pd.DataFrame(self.parse_measurement_info(config), index=[0])
        _f = pd.DataFrame(self.parse_filter(config), index=[0])
        _g = pd.DataFrame(self.parse_gain(config), index=[0])

        _df = _d.merge(_m, how='cross').merge(_f, how='cross').merge(_g, how='cross')

        _df["sample_path"] = _df['sample_number'].apply(lambda x: str((folder_path/f"PP_Sound_{x}.wav").absolute())) 
        _df = _df.loc[_df['sample_path'].apply(lambda x: Path(x).is_file())]

        _df['uuid'] = self.measurement_uuid

        return _df

    def save_measurement(self, root_folder):
        source_data = self.data
        data = source_data.copy()

        if data.shape[0] == 0:
            return
        
        new_measurement = self.validate_is_new(root_folder, data)
        if not new_measurement:
            print("Measurement already exists")
            return

        target_folder = Path(root_folder)/self.measurement_uuid
        if not target_folder.exists():
            target_folder.mkdir(parents=True)

        source_path = data['sample_path']
        target_path = data['sample_path'].str.replace(
            str(self.measurement_folder.absolute()), 
            str(target_folder.absolute()), 
            regex=False
        ).tolist()
        move_list = list(zip(source_path, target_path))
        data['measurement_datetime'] = data['measurement_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
        data.to_json(target_folder/f"data_{self.measurement_uuid}.json", orient='records', indent=4)
        for source, target in move_list:
            shutil.copy(source, target)
        
        append_index(root_folder, source_data)

    def validate_is_new(self, target_folder, data):
        target_folder = Path(target_folder)
        index_file = target_folder/'index.json'
        if not (target_folder/'index.json').exists():
            return True

        index = load_index(target_folder).set_index(['measurement_datetime', 'measurement_name'])

        data = data[['measurement_datetime', 'measurement_name']].drop_duplicates().set_index(['measurement_datetime', 'measurement_name'])

        if index.join(data, how='inner', lsuffix='_ix', rsuffix='_a').shape[0] == 0:
            return True
        else:
            return False
        

def load_folder(source_folder, target_folder):
    source_folder = Path(source_folder)
    target_folder = Path(target_folder)
    
    for _ in source_folder.iterdir():
        if not _.is_dir():
            continue

        Measurement(_).save_measurement(target_folder)