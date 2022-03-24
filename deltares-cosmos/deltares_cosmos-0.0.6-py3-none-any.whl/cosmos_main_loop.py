# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:28:48 2021

@author: ormondt
"""

import time
import datetime
import sched
import os

from .cosmos_main import cosmos
from .cosmos_meteo import read_meteo_sources
from .cosmos_meteo import download_and_collect_meteo
#import cosmos_stations

# from cht.meteo import MeteoSource
# from cht.meteo import MeteoGrid
import cht.fileops as fo


class MainLoop:
    
    def __init__(self):
        # Try to kill all instances of main loop and model loop
        pass
    
    def start(self, cycle_time=None):

        cosmos.cycle_time = cycle_time
        cosmos.cycle_string = cosmos.cycle_time.strftime("%Y%m%d_%Hz")
        delay = datetime.timedelta(hours=0) # Delay in hours

        cosmos.log("Starting main loop ...")
        
        ### Meteo sources
        read_meteo_sources()

        cosmos.next_cycle_time = cosmos.cycle_time + datetime.timedelta(hours=cosmos.scenario.run_interval)

        if cosmos.scenario.cycle_stop_time:
            if cosmos.cycle_time>cosmos.scenario.cycle_stop_time:
                cosmos.next_cycle_time = None

        tnow = datetime.datetime.now(datetime.timezone.utc)
        if tnow > cosmos.cycle_time + delay:
            # start now
            start_time = tnow + datetime.timedelta(seconds=1)
        else:
            # start after delay
            start_time = cosmos.cycle_time + delay
        self.scheduler = sched.scheduler(time.time, time.sleep)
        dt = start_time - tnow
        
        cosmos.log("Next forecast cycle " + cosmos.cycle_string + " will start at " + start_time.strftime("%Y-%m-%d %H:%M:%S") + " UTC")
        
        self.scheduler.enter(dt.seconds, 1, self.run, ())
        self.scheduler.run()

    def run(self):
                
        # Read scenario
        cosmos.scenario.read()
        
        # Prepare models and determine which models are nested in which
        for model in cosmos.scenario.model:

            model.prepare()
            
            if model.flow_nested_name:
                # Look up model from which it gets it boundary conditions
                for model2 in cosmos.scenario.model:
                    if model2.name == model.flow_nested_name:
                        model.flow_nested = model2
                        model2.nested_flow_models.append(model)
                        break
            if model.wave_nested_name:
                # Look up model from which it gets it boundary conditions
                for model2 in cosmos.scenario.model:
                    if model2.name == model.wave_nested_name:
                        model.wave_nested = model2
                        model2.nested_wave_models.append(model)
                        break

#         # Read cycle info
#         cycle_path = os.path.join(cosmos.scenario.path,
#                                   "cycle_list")

#         if not os.path.exists(cycle_path):
#             os.mkdir(cycle_path)

#         cycle_file = os.path.join(cycle_path,
#                                   cosmos.cycle_string + ".txt")

#         if os.path.exists(cycle_file):

#             # This cycle has already been started before
#             # Read cycle text file to determine catchup cycle and next cycle
#             # Read catch-up cycle and next cycle from cycle file
#             fid = open(cycle_file, 'r')
#             lines = fid.readlines()
#             fid.close()
#             cosmos.catchup_cycle_time = datetime.datetime.strptime(lines[0].rstrip(),
#                                                          '%Y%m%d %H%M%S')
#             cosmos.next_cycle_time    = datetime.datetime.strptime(lines[1].rstrip(),
#                                                          '%Y%m%d %H%M%S')
#         else:
            
#             # First time this cycle is run
#             # Determine catchup cycle and next cycle and write to file
#             # Check if we're playing catch-up
#             if cosmos.catchup:
# #                cosmos.catchup_cycle_time = rounddown(now-hm.delay/24,hm.runInterval/24);
#                 cosmos.catchup_cycle_time = cosmos.cycle_time
#                 cosmos.next_cycle_time    = cosmos.catchup_cycle_time + \
#                     datetime.timedelta(hours=cosmos.scenario.run_interval)
#             else:
#                 cosmos.catchup_cycle_time = cosmos.cycle_time
#                 cosmos.next_cycle_time    = cosmos.catchup_cycle_time + \
#                     datetime.timedelta(hours=cosmos.scenario.run_interval)
                
#             # Write new cycle file
#             fid = open(cycle_file, "w")
#             fid.write(cosmos.catchup_cycle_time.strftime("%Y%m%d %H%M%S") + "\n")
#             fid.write(cosmos.next_cycle_time.strftime("%Y%m%d %H%M%S") + "\n")
#             # fprintf(fid,'%s\n',datestr(hm.catchupCycle,'yyyymmdd HHMMSS'));
#             # fprintf(fid,'%s\n',datestr(hm.nextCycle,'yyyymmdd HHMMSS'));
#             fid.close()

#             # Reading data
#             # (models are already read with the scenario)

#             # hm=cosmos_readMeteo(hm);
#             # hm=cosmos_readOceanModels(hm);
#             # hm=cosmos_readParameters(hm);
#             # hm=cosmos_readContinents(hm);

# # %% Time Management
# # hm.NCyc=hm.NCyc+1;

        # Prepare job_list folder
        job_list_path = os.path.join(cosmos.scenario.path,
                                     "job_list",
                                     cosmos.cycle_string)
        if not os.path.exists(job_list_path):        
            if not os.path.exists(os.path.join(cosmos.scenario.path,"job_list")):
                os.mkdir(os.path.join(cosmos.scenario.path,"job_list"))
            os.mkdir(job_list_path)
        finished_list = os.listdir(job_list_path)
        cosmos.job_list_path = job_list_path

        # Set initial durations and what needs to be done for each model
        for model in cosmos.scenario.model:

            model.status = "waiting"

            # Check finished models
            for file_name in finished_list:
                model_name = file_name.split('.')[0]
                if model.name.lower() == model_name.lower():
                    model.status = "finished"
                    model.run_simulation = False
                    break
            
            if model.priority == 0:
                model.run_simulation = False
                
            # Find matching meteo subset
            if model.meteo_dataset:
               for subset in cosmos.meteo_subset:
                   if subset.name == model.meteo_dataset:
                       model.meteo_subset = subset
                       break

        # Start and stop times
        cosmos.log('Getting start and stop times ...')
        get_start_and_stop_times()
        
        # Set reference date to minimum of all start times
        rfdate = datetime.datetime(2200, 1, 1, 0, 0, 0)
        for model in cosmos.scenario.model:
            if model.flow:
                rfdate = min(rfdate, model.flow_start_time)
            if model.wave:
                rfdate = min(rfdate, model.wave_start_time)                
        cosmos.scenario.ref_date = datetime.datetime(rfdate.year,
                                                     rfdate.month,
                                                     rfdate.day,
                                                     0, 0, 0)
        
        # Write start and stop times to log file
        for model in cosmos.scenario.model:
            if model.flow:
                cosmos.log(model.long_name + " : " + \
                           model.flow_start_time.strftime("%Y%m%d %H%M%S") + " - " + \
                           model.flow_stop_time.strftime("%Y%m%d %H%M%S"))
            else:    
                cosmos.log(model.long_name + " : " + \
                           model.wave_start_time.strftime("%Y%m%d %H%M%S") + " - " + \
                           model.wave_stop_time.strftime("%Y%m%d %H%M%S"))
        
        # Get meteo data
        download_and_collect_meteo()
                
        # # Now determine which stations need to be uploaded  
        # # Only upload stations from high-res models
        # cosmos_stations.set_stations_to_upload()

        # Delete the old png tiles from the previous cycle
        tile_path = os.path.join(cosmos.scenario.path, "tiles", "*")
        pths = fo.list_folders(tile_path)
        for pth in pths:
            fo.delete_folder(pth)

        # And now start the model loop
        cosmos.model_loop.start()

def get_start_and_stop_times():
        
    y = cosmos.cycle_time.year
    cosmos.reference_time = datetime.datetime(y, 1, 1)
    
    start_time  = cosmos.cycle_time
        
    stop_time = cosmos.cycle_time + \
        datetime.timedelta(hours=cosmos.scenario.run_duration)    
        
    start_time = start_time.replace(tzinfo=None)    
    stop_time  = stop_time.replace(tzinfo=None)    

    # Find all the models that do not have any models nested in them

    # First waves

    for model in cosmos.scenario.model:        
        if model.wave:
            model.wave_start_time = start_time
            model.wave_stop_time  = stop_time
    
    not_nested_models = []
    for model in cosmos.scenario.model:
        if model.wave:
            # This is a wave model
            if not model.nested_wave_models:
                # And it does not have any model nested in it
                not_nested_models.append(model)

    # Now for each of these models, loop up in the model tree until
    # not nested in any other model            
    for not_nested_model in not_nested_models:
        
        nested = True        
        model = not_nested_model
        nested_wave_start_time = start_time
        
        while nested:
            
            model.wave_start_time = min(model.wave_start_time,
                                        nested_wave_start_time)
            
            # Check for restart files
            restart_time, restart_file = check_for_wave_restart_files(model)
            if not restart_time:
                # No restart file available, so subtract spin-up time
                tok = nested_wave_start_time - datetime.timedelta(hours=model.wave_spinup_time)
                model.wave_start_time = min(model.wave_start_time, tok)
#                model.wave_start_time -= datetime.timedelta(hours=model.wave_spinup_time)
                model.wave_restart_file = None
            else:    
                model.wave_start_time   = restart_time
                model.wave_restart_file = restart_file
                        
            if model.wave_nested:
                
                # This model gets it's wave boundary conditions from another model                
                nested_wave_start_time = model.wave_start_time
                model = model.wave_nested
                
            else:

                # Done looping through the tree
                nested = False

    # And now flow
    
    for model in cosmos.scenario.model:
        if model.flow:
            if model.wave:
                model.flow_start_time = model.wave_start_time
                model.flow_stop_time  = model.wave_stop_time
            else:
                model.flow_start_time = start_time
                model.flow_stop_time  = stop_time
    
    not_nested_models = []
    for model in cosmos.scenario.model:
        if model.flow:
            # This is a flow model
            if not model.nested_flow_models:
                # And it does not have any model nested in it
                not_nested_models.append(model)

    # Now for each of these models, loop up in the model tree until
    # not nested in any other model            
    for not_nested_model in not_nested_models:
        
        nested = True        
        model = not_nested_model
        nested_flow_start_time = start_time
        
        while nested:
            
            model.flow_start_time = min(model.flow_start_time,
                                        nested_flow_start_time)
            
            # Check for restart files
            restart_time, restart_file = check_for_flow_restart_files(model)
            if not restart_time:
                # No restart file available, so subtract spin-up time
                tok = nested_flow_start_time - datetime.timedelta(hours=model.flow_spinup_time)
                model.flow_start_time = min(model.flow_start_time, tok)
#                model.flow_start_time -= datetime.timedelta(hours=model.flow_spinup_time)
                model.flow_restart_file = None
            else:    
                model.flow_start_time   = restart_time
                model.flow_restart_file = restart_file
                        
            if model.flow_nested:
                
                # This model gets it's flow boundary conditions from another model                
                nested_flow_start_time = model.flow_start_time
                # On to the next model in the chain
                model = model.flow_nested
                
            else:

                # Done looping through the tree
                nested = False

    # For only wave model, also add flow start and stop time (used for meteo)
    for model in cosmos.scenario.model:        
        if model.wave:
            if not model.flow_start_time:
                model.flow_start_time = model.wave_start_time
            if not model.flow_stop_time:
                model.flow_stop_time = model.wave_stop_time

def check_for_wave_restart_files(model):
    
    restart_time = None
    restart_file = None
    
    path = os.path.join(model.restart_path,
                        "wave")

    if os.path.exists(path): 
        restart_list = os.listdir(path)
        times = []
        files = []
        for file_name in restart_list:
            tstr = file_name[-19:-4]
            t    = datetime.datetime.strptime(tstr,
                                              '%Y%m%d.%H%M%S')
            times.append(t)
            files.append(file_name)
        
        # Now find the last time that is greater than the start time
        # and smaller than 
        for it, t in enumerate(times):
            if t>model.wave_start_time - datetime.timedelta(hours=model.wave_spinup_time) and t<=model.wave_start_time:
                restart_time = t
                restart_file = files[it]
    else:
        fo.mkdir(path)
    
    return restart_time, restart_file

def check_for_flow_restart_files(model):
    
    restart_time = None
    restart_file = None
    
    path = os.path.join(model.restart_path,
                        "flow")

    if os.path.exists(path): 
        restart_list = os.listdir(path)
        times = []
        files = []
        for file_name in restart_list:
            tstr = file_name[-19:-4]
            t    = datetime.datetime.strptime(tstr,
                                              '%Y%m%d.%H%M%S')
            times.append(t)
            files.append(file_name)
        
        # Now find the last time that is greater than the start time
        # and smaller than 
        for it, t in enumerate(times):
            if t>=model.flow_start_time - datetime.timedelta(hours=model.flow_spinup_time) and t<=model.flow_start_time:
                restart_time = t
                restart_file = files[it]
    else:
        fo.mkdir(path)
                
    return restart_time, restart_file

