# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 10:56:20 2022

@author: chris.kerklaan

Rewriting the scenario downloader into a class for a single scenario
"""

# Third-party imports
import datetime as dt
from functools import cached_property  # usable from 3.8
import threedi_scenario_downloader.downloader as dl

# local imports
import threedi_raster_edits as tre

# globals
SRS = "EPSG:28992"
RES = 0.5
TIMESTAMP = "1970-01-01T00:00:00Z"
GC = tre.GlobalCache()


class Scenario:
    def __init__(self, uuid, api_key):
        self.uuid = uuid
        dl.set_api_key(api_key)
        self._set_rasters()

        GC["api_key"] = api_key

    @cached_property
    def data(self):
        return dl.find_scenarios(limit=1, uuid=self.uuid)[0]

    @cached_property
    def rasters(self):
        names = []
        for raster in self.raster_jsons["static"]:
            names.append(self._raster_name(raster))

        for raster in self.raster_jsons["temporal"]:
            names.append(self._raster_name(raster))
        return names

    @cached_property
    def raster_jsons(self):
        static, temporal = dl.rasters_in_scenario(self.data)
        return {"static": static, "temporal": temporal}

    def _set_rasters(self):
        for raster_json in self.raster_jsons["static"]:
            raster = ScenarioRaster(self.uuid, raster_json)
            setattr(self, self._raster_name(raster_json), raster)

        for raster_json in self.raster_jsons["temporal"]:
            raster = ScenarioRaster(self.uuid, raster_json)
            setattr(self, self._raster_name(raster_json), raster)

    def _raster_name(self, raster_json):
        return (
            raster_json["name_3di"]
            .lower()
            .replace(" ", "_")
            .replace("(", "")
            .replace(")", "")
        )

    def download_grid(self, path):
        dl.download_grid_administration(self.uuid, path)

    def download_results(self, path):
        dl.download_raw_results(self.uuid, path)

    def download_agg_results(self, path):
        dl.download_aggregated_results(self.uuid, path)

    def download_precipitation(
        self, path, target_srs=SRS, resolution=0.5, time=TIMESTAMP
    ):
        dl.download_precipitation_raster(
            self.uuid,
            target_srs,
            resolution,
            time,
            bounds=None,
            bounds_srs=None,
            pathname=None,
        )

    def download_waterlevel(self, path, target_srs=SRS, resolution=0.5, time=TIMESTAMP):
        dl.download_waterlevel_raster(
            self.uuid,
            target_srs,
            resolution,
            time,
            bounds=None,
            bounds_srs=None,
            pathname=None,
        )


class ScenarioRaster:
    def __init__(self, scenario_uuid, raster_json):
        self.uuid = raster_json["uuid"]
        self.scenario_uuid = scenario_uuid
        self.threedi_code = raster_json["code_3di"]
        self.data = raster_json

        steps = self.timesteps_interval(None)
        if steps[0] != None:

            self.start = dt.datetime.fromisoformat(steps[0])
            self.middle = dt.datetime.fromisoformat(steps[1])
            self.end = dt.datetime.fromisoformat(steps[2])
            self.temporal = True
        else:
            self.temporal = False

    def download(self, path, target_srs=SRS, resolution=0.5, time=TIMESTAMP):
        dl.download_raster(
            self.uuid,
            self.threedi_code,
            target_srs,
            resolution,
            bounds=None,
            bounds_srs=None,
            time=time,
            pathname=path,
        )

    def rextract(self, path, geometry, time, threads=4, cellsize=0.5):
        """Rextract is faster but needs a geometry"""
        rextract = tre.RasterExtraction(GC.api_key)
        rextract.run(
            path, self.uuid, geometry, time=time, threads=threads, cellsize=cellsize
        )

    def __repr__(self):
        return str(self.data)

    def timesteps_interval(self, interval_hours=3):
        return dl.get_raster_timesteps(self.data, interval_hours)

    def timesteps(self, hour_indices=[]):
        timestamps = []
        for i in hour_indices:
            timestamps.append((self.start + dt.timedelta(hours=i)).isoformat())
        return timestamps


if __name__ == "__main__":

    api_key = "KmBOtiLM.heFnG6o7rd9wvFEi0zXRVS2vjStdGIHD"
    scenario = Scenario("7efc6f2a-bc51-499c-9d75-311e98814807", api_key)
