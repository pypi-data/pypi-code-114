import os
import sys
import json
import time
import tempfile
import importlib
from copy import deepcopy
from typing import Optional, Dict, List, Callable, Union
from datetime import datetime

import numpy as np

from hpogrid.core.defaults import *
from hpogrid.core import config_manager
from hpogrid.utils import helper
import hpogrid.core.environment_settings as es

from .abstract_object import AbstractObject

class HPOTask(AbstractObject):
    
    @property
    def algorithm(self) -> str:
        return self._algorithm
    
    @algorithm.setter
    def algorithm(self, name):
        if name and (name not in kSearchAlgorithms):
            raise ValueError('unrecognized search algorithm: {}'.format(name))
        self._algorithm = kAlgoMap.get(name, name)
    
    @property
    def scheduler(self) -> str:
        return self._scheduler
    
    @scheduler.setter
    def scheduler(self, name):
        if name and (name not in kSchedulers):
            raise ValueError('unrecognized trial scheduler: {}'.format(name))
        self._scheduler = name

    @property
    def mode(self) -> str:
        return self._mode
    
    @mode.setter
    def mode(self, value):
        if value not in kMetricMode:
            raise ValueError('metric mode must be either "min" or "max"')
        self._mode = value
    
    @property
    def resource(self):
        return self._resource
    
    @property
    def resource_per_trial(self):
        return self._resource_per_trial
    
    @resource_per_trial.setter
    def resource_per_trial(self, value):
        if not self.resource:
            self._resource = self.get_resource_info()
        resource_per_trial = {}
        num_trials = self.num_trials if self.num_trials != -1 else max(self.resource['gpu'], 1)
        max_concurrent = min(num_trials, self.max_concurrent)
        for device in ['cpu', 'gpu']:
            n_device = self.resource[device]
            if n_device >= max_concurrent:
                resource_per_trial[device] = int(n_device/max_concurrent)  
            elif n_device > 0:
                resource_per_trial[device] = n_device / max_concurrent
            else:
                resource_per_trial[device] = 0
        # for now only use 1 GPU per trial
        if self.num_trials == -1:
            resource_per_trial['gpu'] = 1
            
        if isinstance(value, dict):
            for device in ['cpu', 'gpu']:
                if device in value and value[device]:
                    resource_per_trial[device] = min(value[device], resource_per_trial[device])
        self._resource_per_trial = resource_per_trial
    
    @property
    def algorithm_param(self):
        return self._algorithm_param
    
    @property
    def scheduler_param(self):
        return self._scheduler_param
    
    @algorithm_param.setter
    def algorithm_param(self, val):
        self._algorithm_param = val if val is not None else {}
            
    @scheduler_param.setter
    def scheduler_param(self, val):
        self._scheduler_param = val if val is not None else {}
        
    @property
    def model(self):
        return self._model
    
    @property
    def search_space(self):
        return self._search_space   
        
    @property
    def stop(self):
        return self._stop
    
    @stop.setter
    def stop(self, val):
        self._stop = val if val is not None else {}    
        
    @property
    def df(self) -> 'pandas.DataFrame':
        return self._df
    
    @property
    def start_datetime(self) -> str:
        return self._start_datetime
    
    @property
    def end_datetime(self) -> str:
        return self._end_datetime
    
    @property
    def start_timestamp(self) -> float:
        return self._start_timestamp
    
    @property
    def total_time(self) -> float:
        return self._total_time
    
    @property
    def best_config(self) -> Dict:
        return self._best_config

    @property
    def hyperparameters(self):
        return self._hyperparameters
    
    @property
    def log_dir(self) -> str:
        return self._log_dir

    @log_dir.setter
    def log_dir(self, val):
        """
        self._log_dir = val
        if hpogrid.is_local_job() and (not os.path.isabs(val)):
            project_path = helper.get_project_path(self.project_name)
            if os.path.exists(project_path):
                self._log_dir = os.path.join(project_path, val)
        self._log_dir = helper.pretty_path(self._log_dir)
        """
        self._log_dir = val    
    
    def __init__(self, model:Optional[Callable]=None, search_space:Optional[Dict]=None,
                 verbosity:str="INFO"):
        super().__init__(verbosity=verbosity)
        self._resource = None
        self.reset()
        self.set_model(model)
        self.set_search_space(search_space)
        
    def setup(self, project_name:Optional[str]=None, algorithm:str=kDefaultSearchAlgorithm,
              metric:str=kDefaultMetric, mode:str=kDefaultMetricMode, num_trials:int=kDefaultTrials,
              max_concurrent:int=kDefaultMaxConcurrent, stop:Optional[Dict]=None,
              scheduler:str=kDefaultScheduler, resource_per_trial:Optional[Dict]=None,
              verbose:int=kDefaultVerbosity, log_dir:Optional[str]=kDefaultLogDir,
              extra_metrics:Optional[Dict]=None, algorithm_param:Optional[Dict]=None,
              scheduler_param:Optional[Dict]=None, model_script:Optional[str]=None,
              model_name:Optional[str]=None, model_param:Optional[Dict]=None,
              scripts_path:Optional[str]=None):
        
        # set default values for dict type arguments
        if stop is None:
            stop = deepcopy(kDefaultStopping)
        if algorithm_param is None:
            algorithm_param = deepcopy(kDefaultAlgorithmParam)
        if scheduler_param is None:
            scheduler_param = deepcopy(kDefaultSchedulerParam)
        if resource_per_trial is None:
            resource_per_trial = deepcopy(kDefaultResource)
        if model_param is None:
            model_param = {}
        if scripts_path is None:
            scripts_path = os.getcwd()
            
        self.project_name       = project_name
        self.algorithm          = algorithm
        self.metric             = metric
        self.mode               = mode
        self.num_trials         = num_trials
        self.max_concurrent     = max_concurrent
        self.stop               = stop
        self.scheduler          = scheduler
        self.resource_per_trial = resource_per_trial
        self.verbose            = verbose
        self.log_dir            = log_dir
        self.extra_metrics      = extra_metrics
        self.scheduler_param    = scheduler_param
        self.algorithm_param    = algorithm_param
        self.model_script       = model_script
        self.model_name         = model_name
        self.model_param        = model_param
        self.scripts_path       = scripts_path
        
    def export_setup(self):
        attributes = ["project_name", "algorithm", "metric", "mode",
                      "num_trials", "max_concurrent", "stop", "scheduler",
                      "resource_per_trial", "verbose", "log_dir", "extra_metrics",
                      "scheduler_param", "algorithm_param", "model_script",
                      "model_name", "model_param", "scripts_path"]
        result = {}
        for attribute in attributes:
            result[attribute] = self.__getattribute__(attribute)
        return result

    def reset(self):
        self.set_model()
        # hpo configuration
        self.setup()
        # search space
        self.set_search_space()
        # parameters for logging
        self._df = None
        self._start_datetime = None
        self._end_datetime = None
        self._total_time = None
        self._best_config = None
        self._start_timestamp = None
        self.idds_job = False
        self.search_points = None
        self.summary_fname = kGridSiteMetadataFileName
        
    def set_model(self, model:Optional[Callable]=None):
        self._model = model
        
    def set_search_space(self, search_space:Optional[Dict]=None):
        if search_space is None:
            self._search_space = None
            self._hyperparameters = {}
        elif isinstance(search_space, dict):
            self._search_space = deepcopy(search_space)
            self._hyperparameters = list(self.search_space.keys())
        else:
            raise ValueError("search space must be of type \"dict\"")
            
    def set_search_points(self, search_points:Union[str, List]):
        if isinstance(search_points, str):
            with open(search_points, 'r') as f:
                search_points = json.load(f)
        self.search_points = search_points
        from hpogrid.search_space import SkOptSpace
        skopt_search_points = SkOptSpace.transform(search_points, reference=self.search_space)
        self.algorithm = 'skopt'
        self.scheduler = None
        self.scheduler_param = {}
        self.algorithm_param = {'points_to_evaluate': skopt_search_points}
        self.num_trials = len(skopt_search_points)
        self.stdout.info("INFO: Using explicit search points for execution. "
                         "Search algorithm is set to \"skopt\" and trial "
                         "scheduler is set to None. Parameters for scheduler "
                         "and search algorithm is reset. Number of trials is changed "
                         "according to the number of search points provided")            
            
    @staticmethod
    def get_scheduler(name:str, metric:str, mode:str, search_space=None, **args):
        if (name == None) or (name == 'None'):
            return None
        _name = SchedulerType.parse(name)
        if _name == SchedulerType.ASYNCHYPERBAND:
            from hpogrid.schedulers import AsyncHyperBandScheduler
            return AsyncHyperBandScheduler().create(metric, mode, **args)
        elif _name == SchedulerType.BOHBHYPERBAND:
            from hpogrid.schedulers import BOHBHyperBandScheduler
            return BOHBHyperBandScheduler().create(metric, mode, **args)
        elif _name == SchedulerType.PBT:
            from hpogrid.schedulers import PBTScheduler
            if search_space is None:
                raise ValueError('missing search space definition for pbt scheduler')
            return PBTScheduler().create(metric, mode, search_space, **args)
        else:
            raise ValueError(f'Unrecognized scheduler method: {name}')

    @staticmethod
    def get_search_space(base_search_space:Dict, algorithm:str):
        if base_search_space is None:
            raise ValueError('search space can not be empty')
        _algorithm = SearchSpaceType.parse(algorithm)
        if _algorithm == SearchSpaceType.AX:
            from hpogrid.search_space import AxSpace
            return AxSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.BOHB:
            from hpogrid.search_space import BOHBSpace
            return BOHBSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.HYPEROPT:
            from hpogrid.search_space import HyperOptSpace
            return HyperOptSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.SKOPT:
            from hpogrid.search_space import SkOptSpace
            return SkOptSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.TUNE:
            from hpogrid.search_space import TuneSpace
            return TuneSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.NEVERGRAD:
            from hpogrid.search_space import NeverGradSpace
            return NeverGradSpace(base_search_space).get_search_space()
        elif _algorithm == SearchSpaceType.OPTUNA:
            from hpogrid.search_space import OptunaSpace
            return OptunaSpace(base_search_space).get_search_space()         
        else:
            raise ValueError(f'Unrecognized search algorithm: {algorithm}')

    @staticmethod
    def get_algorithm(name:str, metric:str, mode:str, base_search_space:Dict,
                      max_concurrent=None, **args):
        _name = AlgorithmType.parse(name)
        if _name == AlgorithmType.AX:
            from hpogrid.algorithms import AxAlgorithm
            algorithm = AxAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.BOHB:
            from hpogrid.algorithms import BOHBAlgorithm
            algorithm = BOHBAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.HYPEROPT:
            from hpogrid.algorithms import HyperOptAlgorithm
            algorithm = HyperOptAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.SKOPT:
            from hpogrid.algorithms import SkOptAlgorithm
            algorithm = SkOptAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.NEVERGRAD:
            from hpogrid.algorithms import NeverGradAlgorithm
            algorithm = NeverGradAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.OPTUNA:
            from hpogrid.algorithms import OptunaAlgorithm
            algorithm = OptunaAlgorithm().create(metric, mode, base_search_space, **args)
        elif _name == AlgorithmType.TUNE:
            algorithm = None
        else:
            raise ValueError(f'Unrecognized search algorithm: {name}')
        # limit max concurrency
        if algorithm and max_concurrent:
            from ray.tune.suggest import ConcurrencyLimiter
            algorithm = ConcurrencyLimiter(algorithm, max_concurrent=max_concurrent) 
        return algorithm

    def load_model(self, script_name:str, model_name:str, scripts_path:Optional[str]=None):
        scripts_path = os.getcwd() if scripts_path is None else scripts_path
        model = None
        script_name_noext = os.path.splitext(script_name)[0]
        try: 
            es.set_scripts_path(scripts_path)
            module = importlib.import_module(script_name_noext)
            model = getattr(module, model_name)
        except: 
            raise ImportError(f'Unable to import function/class {model_name} '
                              'from training script: {script_name_noext}.py')
        finally:
            es.set_scripts_path(scripts_path, undo=True)
        self.stdout.info('INFO: Loaded module {}'.format(model.__name__))
        return model

    def create_metadata(self, df) -> Dict:

        summary = {
            'project_name' : self.project_name,
            'start_datetime': self.start_datetime,
            'end_datetime': self.end_datetime,
            'start_timestamp': self.start_timestamp,
            'task_time_s' : self.total_time,
            'hyperparameters': self.hyperparameters,
            'metric': self.metric,
            'mode' : self.mode,
            'best_config' : self.best_config, 
        }
        
        rename_cols = { 'config/{}'.format(hp): hp for hp in self.hyperparameters}
        rename_cols['time_total_s'] = 'time_s'
        
        df = df.rename(columns=rename_cols)
        cols_to_save = ['time_s'] + self.hyperparameters
        if 'metric' in summary:
            cols_to_save.append(summary['metric'])
        if self.extra_metrics:
            cols_to_save += self.extra_metrics
        df = df.filter(cols_to_save, axis=1).transpose()
        summary['result'] = df.to_dict()
        
        return summary

    def get_resource_info(self) -> Dict:
        resource = {}
        n_gpu = helper.get_n_gpu()
        n_cpu = helper.get_n_cpu()
        resource['gpu'] = n_gpu
        resource['cpu'] = n_cpu
        return resource
    
    def print_resource_info(self):
        self.stdout.info('INFO: Number of GPUs detected: {}'.format(self.resource['gpu']))
        self.stdout.info('INFO: Number of CPUs detected: {}'.format(self.resource['cpu']))
        self.stdout.info('INFO: Each trial will use {} GPU(s) resource'.format(self.resource_per_trial['gpu']))
        self.stdout.info('INFO: Each trial will use {} CPU(s) resource'.format(self.resource_per_trial['cpu']))
    
    def print_setup(self):
        from hpogrid.utils.stylus import create_formatted_dict
        text = create_formatted_dict(self.export_setup(), indexed=False, columns=["Attribute","Value"])
        self.stdout.info(text)
    
    def run(self) -> None:
            
        self._start_timestamp = start = time.time()
        self._start_datetime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        # get model parameters
        if self.algorithm == 'tune':
            tune_config_space = self.get_search_space(self.search_space, algorithm='tune')
        else:
            tune_config_space = {}

        tune_config_space.update(self.model_param)

        # get search algorithm
        algorithm = self.get_algorithm(
            self.algorithm,
            self.metric,
            self.mode,
            self.search_space,
            self.max_concurrent,
            **self.algorithm_param)
        
        # get trial scheduler
        scheduler = self.get_scheduler(
            self.scheduler,
            self.metric,
            self.mode,
            self.search_space,
            **self.scheduler_param)
        
        # load model from path
        if (not self.model):
            model = self.load_model(self.model_script, self.model_name, self.scripts_path)
        else:
            model = self.model
            
        self.print_resource_info()
        
        callbacks = None
        #loggers = self.get_loggers()
        
        # save something to prevent looping job
        with open(kGridSiteMetadataFileName,'w') as output:
            json.dump({}, output)
        
        temp_dir = tempfile.TemporaryDirectory()
        
        import ray
        from ray import tune

        # HPO starts
        try:
            # extract input dataset if it is a tar file
            # (for grid jobs only)
            extracted_files = []
            if es.is_grid_job():
                datadir = es.get_datadir()
                extracted_files = helper.extract_tarball(datadir, datadir)
            ray.init(include_dashboard=False)
            # lru_evict=True      
            if not self.log_dir:
                local_dir = os.path.join(temp_dir.name, 'log')
            else:
                local_dir = self.log_dir
            if self.num_trials == -1:
                num_samples = max(self.resource.get('gpu'), 1)
            else:
                num_samples = self.num_trials
                
            if AlgorithmType.parse(self.algorithm) == AlgorithmType.NEVERGRAD:
                try:
                    algo_str = f"{self.algorithm} ({algorithm.searcher._nevergrad_opt.name})"
                except:
                    algo_str = f"{self.algorithm}"
            else:
                algo_str = f"{self.algorithm}"
                
            self.stdout.info("--------------------------------------------------------------------------------")
            self.stdout.info(f"INFO: Begin hyperparameter optimization with the following settings")
            self.stdout.info(f"Project Name            : {self.project_name}")
            self.stdout.info(f"Search Algorithm        : {algo_str}")
            self.stdout.info(f"Trial Scheduler         : {self.scheduler}")
            self.stdout.info(f"Number of Search Points : {num_samples}")
            self.stdout.info("--------------------------------------------------------------------------------")
            analysis = tune.run(
                model,
                name=self.project_name,
                scheduler=scheduler,
                search_alg=algorithm,
                config=tune_config_space,
                num_samples=num_samples,
                resources_per_trial=self.resource_per_trial,
                verbose=self.verbose,
                local_dir=local_dir,
                callbacks=callbacks,
                stop=self.stop)
        finally:
            ray.shutdown()
            # remove the extracted tar files
            helper.remove_files(extracted_files)
        end = time.time()
        self._total_time = float(end - start)
        self._end_datetime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

        self._best_config = analysis.get_best_config(metric=self.metric, mode=self.mode)
        
        self.stdout.info(f"Best config: {self.best_config}")
        self.stdout.info(f"Time taken in seconds: {self.total_time}")
        
        if self.log_dir:
            self.stdout.info(f"INFO: Ray Tune log files are saved at {self.log_dir}")

        df = analysis.dataframe(metric=self.metric, mode=self.mode)

        metadata = self.create_metadata(df)
        
        summary_output_path = helper.pretty_path(self.summary_fname)
        # save metadata
        with open(summary_output_path, 'w') as output:            
            json.dump(metadata, output, cls=helper.NpEncoder, indent=2)
            self.stdout.info(f'INFO: Job metadata is saved at {summary_output_path}')
        
        # save idds output
        if es.is_idds_job():
            from hpogrid.interface.idds.main import save_idds_output_from_metadata
            save_idds_output_from_metadata(metadata)

        # reset environment
        es.reset()
        temp_dir.cleanup()
    
    def get_loggers(self):
        from ray.tune.logger import NoopLogger, MLFLowLogger
        return [NoopLogger, MLFLowLogger]
    
    def set_run_mode(self, mode:str='local'):
        es.setup(mode)

    def parse_project_config(self, source:[Dict, str]):
        
        is_saved_project = config_manager.is_project(source)
        
        config = config_manager.load_configuration(source)
        from hpogrid.configuration import ProjectConfiguration
        config = ProjectConfiguration._validate(config)
        
        # if input is a project name, set scripts path to 
        # where the scripts are stored in the project directory
        # if input is a configuration file, set scripts path to
        # the scripts path stated in configuration file
        if is_saved_project:
            project_name = source
            scripts_path = config_manager.get_project_script_dir(project_name)
        else:
            scripts_path = helper.pretty_dirname(config['scripts_path'])
            
        # Load search space
        self.set_search_space(config['search_space'])
        
        setup_kwargs = {
            "project_name"       : config['project_name'],
            "algorithm"          : config['hpo_config']['algorithm'],
            "metric"             : config['hpo_config']['metric'],
            "mode"               : config['hpo_config']['mode'],
            "scheduler"          : config['hpo_config']['scheduler'],
            "scheduler_param"    : config['hpo_config']['scheduler_param'],
            "algorithm_param"    : config['hpo_config']['algorithm_param'],
            "num_trials"         : config['hpo_config']['num_trials'],
            "max_concurrent"     : config['hpo_config']['max_concurrent'],
            "verbose"            : config['hpo_config']['verbose'],
            "log_dir"            : config['hpo_config'].get('log_dir', None),
            "stop"               : config['hpo_config'].get('log_dir', None),
            "resource_per_trial" : config['hpo_config'].get('resource', None),
            "extra_metrics"      : config['hpo_config'].get('extra_metrics', None),
            "scripts_path"       : scripts_path,
            "model_script"       : config['model_config']['script'],
            "model_name"         : config['model_config']['model'],
            "model_param"        : config['model_config']['param']
        }

        # Load hpo configuration
        self.setup(**setup_kwargs)

    @classmethod
    def load(cls, source:[Dict, str], search_points=None, mode='local'):
        """
        Arguments:
            source: str or dict
                dict: a dict representing the project configuration
                str: path to the json file storing the project configuration, or
                     name of the project saved under hpogrid
        """

        task = cls()
        task.set_run_mode(mode)
        
        task.parse_project_config(source)

        # configuration for idds
        if (not search_points) and es.is_idds_job():
            from hpogrid.interface.idds.main import get_search_points
            search_points = get_search_points()

        if search_points:
            task.set_search_points(search_points)
        
        return task