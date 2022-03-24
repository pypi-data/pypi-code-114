# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:18:09 2021

@author: ormondt
"""

import os
import datetime
import numpy as np

from cht import fileops as fo

class CoSMoS:
    
    def __init__(self):
        
        self.delay = 6.0 # delay in hours
        
        # Read configuration file

        # Set paths etc.
        
        # makedir([hm.scenarioDir 'joblist']);
        # makedir([hm.scenarioDir 'cyclelist']);
        
        # % Read all data
        # wb = waitbox('Loading tide database ...');
        # hm=getTideStations(hm);
        # close(wb);
        
        # wb = waitbox('Loading observations database ...');
        # hm=getObservationStations(hm);
        # close(wb);
        
        # hm.mainWindow=MakeNewWindow('CoSMoS',[750 500]);
        
        # set(hm.mainWindow,'CloseRequestFcn',@closeOMS);
        # set(hm.mainWindow,'Tag','OMSMain');
        
        # hm.runSimulation=1;
        # hm.extractData=1;
        # hm.DetermineHazards=1;
        # hm.runPost=1;
        # hm.makeWebsite=1;
        # hm.uploadFTP=1;
        # hm.archiveInput=0;
        # hm.catchUp=0;

    def initialize(self, main_path, scenario_name):        

#        self.read_configuration_file(config_file)
        self.config = CoSMoSConfiguration(main_path)

        # Stations
        from cosmos.cosmos_stations import CoSMoSStations
        self.stations = CoSMoSStations()
        self.stations.read()
        
        # Loop through regions to make model_list
        cosmos.model_list = []
        region_list = fo.list_folders(os.path.join(self.config.main_path,
                                                   "models", "*"))
        for region_path in region_list:
            region_name = os.path.basename(region_path)
            type_list = fo.list_folders(os.path.join(region_path,"*"))
            for type_path in type_list:
                type_name = os.path.basename(type_path)
                name_list = fo.list_folders(os.path.join(type_path,"*"))
                for name_path in name_list:
                    name = os.path.basename(name_path)
                    cosmos.model_list.append({"name":name,
                                              "type":type_name,
                                              "region":region_name})
                
        ### Scenario
        from cosmos.cosmos_scenario import Scenario

        self.scenario = Scenario(scenario_name)
        self.scenario.path = os.path.join(self.config.main_path,
                                          "scenarios",
                                          scenario_name)
        self.scenario.file_name = os.path.join(self.scenario.path,
                                               scenario_name + ".xml")
        self.scenario.read()


        from cosmos.cosmos_model_loop import ModelLoop
        from cosmos.cosmos_main_loop import MainLoop

        self.model_loop = ModelLoop()
        self.main_loop  = MainLoop()
        
        
        # Temporary path
        self.temp_path = os.path.join(self.config.main_path,
                                      "temp")
        fo.mkdir(self.temp_path)

        fo.mkdir(os.path.join(cosmos.scenario.path,"log_files"))

        # Make sure all paths exist
        # General idiot proofing
                
    def read_configuration_file(self, file_name):
        self.config = CoSMoSConfiguration()
        self.config.file_name = file_name
        self.config.read()

    def run(self,
            cycle=None,
            mode="single",
            run_models=True,
            make_flood_maps=True,
            make_wave_maps=True,
            get_meteo=True,
            make_figures=True,
            upload_data=True,
            ensemble=False,
            username=None,
            password=None,
            sfincs_exe_path=None,
            xbeach_exe_path=None,
            hurrywave_exe_path=None,
            delft3dfm_exe_path=None):
           
        cosmos.config.cycle_mode = mode
        cosmos.config.get_meteo  = get_meteo
        cosmos.config.run_models = run_models
        cosmos.config.make_flood_maps = make_flood_maps
        cosmos.config.make_wave_maps = make_wave_maps
        cosmos.config.upload_data    = upload_data
        cosmos.config.make_figures   = make_figures
        cosmos.config.run_ensemble   = ensemble
        cosmos.config.username       = username
        cosmos.config.password       = password
        if sfincs_exe_path:
            cosmos.config.sfincs_exe_path       = sfincs_exe_path
        if hurrywave_exe_path:    
            cosmos.config.hurrywave_exe_path    = hurrywave_exe_path
        if xbeach_exe_path:    
            cosmos.config.xbeach_exe_path    = xbeach_exe_path
        if delft3dfm_exe_path:    
            cosmos.config.delft3dfm_exe_path    = delft3dfm_exe_path

        if not self.scenario.cycle_time and not cycle:
            # Cycle time not given (must be a forecast)
            delay = 1
            t = datetime.datetime.now(datetime.timezone.utc) - \
                datetime.timedelta(hours=delay)
            h0 = t.hour
            h0 = h0 - np.mod(h0, 6)
            t = t.replace(microsecond=0, second=0, minute=0, hour=h0)
        elif cycle:
            # Cycle is given as input
            t = datetime.datetime.strptime(cycle,"%Y%m%d_%Hz").replace(tzinfo=datetime.timezone.utc)
        else:
            # Cycle defined in scenario
            t = self.scenario.cycle_time.replace(tzinfo=datetime.timezone.utc)
            
        # t is in utc    
        self.main_loop.start(cycle_time=t)

    def stop(self):   
        self.model_loop.scheduler.cancel()
        self.main_loop.scheduler.cancel()

    def collect_timeseries(self,model_name,station_name,parameter,t0=None,t1=None,resample=None):
               
        from cosmos_timeseries import merge_timeseries as merge
        
        v = None
        
        for model in cosmos.scenario.model:
            if model.name == model_name:
                v = merge(model.archive_path, station_name, t0=t0, t1=t1,
                          prefix=parameter,resample=resample)  

        return v

    def log(self, message):
        print(message)
        log_file = os.path.join(cosmos.scenario.path,
                                "log_files",
                                cosmos.cycle_string + ".log")
        with open(log_file, 'a') as f:
            f.write(message + "\n")
            f.close()

class CoSMoSConfiguration:
    
    def __init__(self, main_path):

        self.main_path  = main_path
        self.job_path   = os.path.join(main_path, "jobs")
        self.cycle_mode = "single"
#        self.cycle_mode = "continuous"
        self.run_mode   = "serial"
        self.make_floodmaps = True
        self.get_meteo      = True
        self.make_figures   = True
        self.upload_data    = True
        self.username       = None
        self.password       = None
        self.sfincs_exe_path    = os.path.join(main_path, "exe", "sfincs")
        self.hurrywave_exe_path = os.path.join(main_path, "exe", "hurrywave")
        self.xbeach_exe_path = os.path.join(main_path, "exe", "xbeach")
        self.delft3dfm_exe_path = os.path.join(main_path, "exe", "delft3dfm")
        
        self.stations_path = os.path.join(self.main_path, "stations")
    
    # def read(self):
    #     pass

                    
cosmos = CoSMoS()

