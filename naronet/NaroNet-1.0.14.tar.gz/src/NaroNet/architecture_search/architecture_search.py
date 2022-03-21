import os
from ray import tune
from ray.tune import Trainable
from ray.tune.schedulers import ASHAScheduler
from ray.tune.suggest.hyperopt import HyperOptSearch
from ray.tune.suggest import ConcurrencyLimiter
from NaroNet.architecture_search.extract_info_architectureSearch import extract_best_result
from NaroNet.architecture_search.extract_info_architectureSearch import save_architecture_search_stats
import torch
import ray
from NaroNet import NaroNet
from NaroNet.NaroNet_simple import NaroNet_simple

class NaroNet_Search(Trainable):


    def _setup(self, parameters):  
        self.device = torch.device(parameters["device"] if torch.cuda.is_available() else "cpu")
        # Initialize 
        self.N = NaroNet.NaroNet(parameters, self.device)        
        self.N.epoch = 0
              
    def _train(self):
        try:
            result = self.N.epoch_validation()
        except Exception as exc:
            del self.N                                   
            result = {"val_acc":0.1,"epoch": 1000,"maximize_acc_interpretability":0,"acc_test":0,"interpretability":0,"train_Cell_ent":0,"train_Cross_entropy":10,"train_Pat_ent":0,"train_UnsupContrast_acc":0,"train_acc":0,"train_loss":0,"val_Cell_ent":0,"val_Pat_ent":0,"val_UnsupContrast_acc":0,"val_loss":10,'val_Cross_entropy':10,'test_Cross_entropy':10}             
            pass            
        return result

    def _save(self, checkpoint_dir):        
        return

class NaroNet_Search_simple(Trainable):
    def _setup(self, parameters):  
        self.device = torch.device(parameters["device"] if torch.cuda.is_available() else "cpu")
        # Initialize 
        self.N = NaroNet_simple(parameters, self.device)
        self.N.epoch = 0
              
    def _train(self):
        try:
            result = self.N.epoch_validation()
        except Exception as exc:
            del self.N                                   
            result = {"val_acc":0.1,"epoch": 1000,"cross_ent_test":1000,"acc_test":0,"interpretability":0,"train_Cell_ent":0,"train_Cross_entropy":10,"train_Pat_ent":0,"train_UnsupContrast_acc":0,"train_acc":0,"train_loss":0,"val_Cell_ent":0,"val_Pat_ent":0,"val_UnsupContrast_acc":0,"val_loss":10,'val_Cross_entropy':10,'test_Cross_entropy':10}             
            pass            
        return result

    def _save(self, checkpoint_dir):        
        return


def architecture_search(path,best_parameters,possible_parameters,AvoidSet=None):
    
    # In case NestedCrossvalidation, add AvoidSet to the parameters.
    if AvoidSet is not None:
        possible_parameters['AvoidSet'] = AvoidSet

    # Metric to optimize
    metric = 'cross_ent_test' #  "loss_test"
    num_gpus = 1
    best_parameters['device'] = best_parameters['device'] if 'Synthetic' in path else 'cuda'
    possible_parameters['device'] = possible_parameters['device'] if 'Synthetic' in path else 'cuda'

    # Whether to search architecture or load previous ones.
    architecture_search_path = path+'Architecture_Search/'
    architecture_search_path_save = architecture_search_path+'Results/'
    if (not os.path.exists(architecture_search_path)) or (not os.path.exists(architecture_search_path+'NaroNet_Search/')) or (not os.path.exists(architecture_search_path_save)):        
        os.mkdir(architecture_search_path)
        os.mkdir(architecture_search_path+'NaroNet_Search/')
        os.mkdir(architecture_search_path_save)
    else:
        best_result, n_runs = extract_best_result(architecture_search_path+'NaroNet_Search/',metric,best_parameters)
        if (n_runs>10 and len(os.listdir(architecture_search_path_save))==0):
            save_architecture_search_stats(architecture_search_path_save,architecture_search_path+'NaroNet_Search/',10)
        if n_runs>best_parameters['num_samples_architecture_search']*0.9:
            return best_result

    # Restart Ray defensively in case the ray connection is lost. 
    # ray start --head --node-ip-address=127.0.0.1 --port=34009
    # ray start --address='128.3.60.116:34009' --redis-password='5241590000000000'
    # ray.shutdown()  
    ray.init(local_mode=True)#,_redis_password='sadfh*&H^&T^&TU')#address='127.0.0.1:34009', _redis_password='5241590000000000')#) # Local address #,address='127.0.0.1:6379'
    
    # Set Scheduler
    scheduler=ASHAScheduler(time_attr="epoch",max_t=best_parameters['epochs']-2, metric=metric, mode="min")        
    
    # Set algorithm
    search_algo = HyperOptSearch(possible_parameters, metric=metric, mode="min",n_initial_points=int(best_parameters['num_samples_architecture_search']*0.8), points_to_evaluate=[best_parameters])    
    search_algo = ConcurrencyLimiter(search_algo, max_concurrent=1)

    # Running parameters
    runIt = {"num_samples": best_parameters['num_samples_architecture_search'], 
    "resources_per_trial":{"gpu": 0, "cpu":1}, "checkpoint_freq":0, "local_dir":architecture_search_path} 
    sync_config = tune.SyncConfig()
        
    # Obtain the best hyperparametersWWW
    analysis = tune.run(NaroNet_Search,scheduler=scheduler,search_alg=search_algo,sync_config=sync_config,**runIt)

    # Obtain best result parameters
    best_result, n_runs = extract_best_result(architecture_search_path+'NaroNet_Search/',metric,best_parameters)
    return best_result
