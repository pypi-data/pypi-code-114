from NaroNet.NaroNet_dataset import NaroNet_dataset
import NaroNet.utils
import NaroNet.NaroNet_model.NaroNet_model as NaroNet_model
import NaroNet.NaroNet_model.NaroNet_model_simple as NaroNet_model_simple
from NaroNet.architecture_search import architecture_search

# import models.pysurv as pysurv 

from sklearn.model_selection import StratifiedKFold, KFold
from imblearn.over_sampling import RandomOverSampler
import random
import numpy as np

import time
import copy

# from adatune.mu_adam import MuAdam
from torch.optim import Adam, SGD, AdamW
from torch.optim.lr_scheduler import StepLR
import torch

import NaroNet.TrainValidateTest as TrainValidateTest

import NaroNet.utils.utilz as utilz
import random as rand
from NaroNet.NaroNet_model.lossGrad import LossgradOptimizer
from tqdm import tqdm
import os
import pandas as pd

class NaroNet:
    def __init__(self, args, device):
        self.args = utilz.transformToInt(args)
        self.device = device
        
        # Obtain or create dataset.
        self.dataset = NaroNet_dataset(root=self.args['path'],patch_size=self.args['PCL_Patch_Size'],superPatchEmbedding=self.args['PCL_Out_Dimensions'],experiment_label=self.args['experiment_Label'])                              
        
        # Obtain dataset statistics from the last data value.
        self.num_total_nodes, self.edge_index_total, self.num_features, self.mean_STD, self.IndexAndClass, self.percentile, self.num_classes, self.name_labels = self.dataset.getStatistics(self.dataset.__len__())                              
                   
        self.model = NaroNet_model_simple.NaroNet_model_simple(self.num_features, self.name_labels, self.num_total_nodes, self.args["clusters"], self.args)
                  
        # Save Initialization Parameters in an excel file.
        utilz.initialization_params(self.dataset,self.args,self.num_features, self.model)    

    def visualize_results(self):
        self.dataset.visualize_results(self.args['clusters'], self.IndexAndClass)

    def initialize_cross_validation(self):
        '''
        Initialize cross-validation. 
        '''

        # Initialize the number of folds, and the dictionary that holds folds
        self.fold = 0 
        self.dict_fold=None

        # Reorder the list of indexandclass.
        self.IndexAndClass_reorder = copy.deepcopy(self.IndexAndClass)
        self.IndexAndClass_reorder.sort(key = lambda x: x[1])
        self.IndexAndClass = copy.deepcopy(self.IndexAndClass_reorder)

        # Obtain labels for each file.
        self.labels = []
        for i_c in self.IndexAndClass_reorder:
            l_now = []
            for i_l, l in enumerate(i_c[2]):
                if l !='None':
                    l_now.append(self.name_labels[i_l].index(l))
                else:
                    l_now.append(-1)
            self.labels.append(l_now)   


    def train_test_split(self,excel):
        
        def select_subjects(train_test):
            train_subjects = list(excel['Image_Names'][excel['train_test_split']==train_test])
            subjects = [iac[0] for iac in self.IndexAndClass]
            idx = [subjects.index(sub.split('.')[0]) for sub in train_subjects]       
            return idx
        
        train_idx = select_subjects('Train')
        test_idx = select_subjects('Test')
                
        splitter = [(np.array(train_idx),np.array(test_idx))]

        return splitter


    def split_subjects_images(self):
        '''
        split subjects into training and test.
        '''

        # Load excel 
        patient_to_image_excel = pd.read_excel(self.dataset.root+'Raw_Data/Experiment_Information/Image_Labels.xlsx')  

        # In case there is a column named 'Subject_Names' we have to classify subject-wise patients
        if any([p=='Subject_Names' for p in patient_to_image_excel.columns]):
            subject_labels = list(set(patient_to_image_excel['Subject_Names']))
            subjects = [patient_to_image_excel[self.dataset.experiment_label[0]][patient_to_image_excel['Subject_Names']==s] for s in subject_labels]
            subject_level_labels = [i[i!='None'].values[0] if i[i!='None'].values.size!=0 else 'None' for i in subjects]

            # K fold cross validation or leave-one-out
            if min([sum([1 for s in subject_level_labels if s==lbl]) for lbl in set(subject_level_labels)])<rsfk.n_splits and len(set(subject_level_labels))<5:
                # Leave-one-out
                ordered_names = [iac[0] for iac in self.IndexAndClass_reorder]
                splitter = []
                for leave_subject in range(len(subject_level_labels)):                    
                    # Check if subject names contains '.'
                    if any([len(pat.split('.'))>1 for pat in patient_to_image_excel['Image_Names']]): 
                        test_names = ['.'.join(p_name.split('.')[:-1]) for p_name in patient_to_image_excel['Image_Names'][subjects[leave_subject].index]]
                    else:
                        test_names = [p_name for p_name in patient_to_image_excel['Image_Names'][subjects[leave_subject].index]]
                    # Check if image name is in the set of preprocessed images
                    in_set_preprocessed = [t in ordered_names for t in test_names]
                    if any(in_set_preprocessed):                                                
                        test_indices = [ordered_names.index(t) for t in np.array(test_names)[in_set_preprocessed]]
                        train_indices = [iac for iac in range(len(self.IndexAndClass)) if not iac in test_indices]
                        splitter.append((train_indices,test_indices))                    
            else:
                # 10fold cross validation
                ordered_names = [iac[0] for iac in self.IndexAndClass_reorder]
                rsfk = StratifiedKFold(n_splits=self.args['folds'])  
                splitter_of_subjects = list(rsfk.split(subject_labels, np.ones(len(subject_labels))))
                splitter = []
                for sp_fold in splitter_of_subjects: # Each fold
                    sp_tt_fold=[]
                    for sp_train_test in sp_fold: # Each fold
                        sp_tt_ind = []
                        for sp_tt in [subject_labels[s] for s in sp_train_test]: # Each subject
                            # Check if subject names contains '.'
                            if any([len(pat.split('.'))>1 for pat in patient_to_image_excel['Image_Names']]): 
                                name = ['.'.join(p_name.split('.')[:-1]) for p_name in patient_to_image_excel['Image_Names'][patient_to_image_excel['Subject_Names']==sp_tt]]
                            else:
                                name = [p_name for p_name in patient_to_image_excel['Image_Names'][patient_to_image_excel['Subject_Names']==sp_tt]]                            
                            index = [ordered_names.index(t) for t in name if t in ordered_names]
                            for ii in index:
                                sp_tt_ind.append(ii)                                
                        sp_tt_fold.append(sp_tt_ind)
                    splitter.append(tuple(sp_tt_fold))

        elif 'Unsupervised' in str(self.args['experiment_Label']):
            splitter = [(np.array(list(range(len(self.IndexAndClass)))),np.array(list(range(len(self.IndexAndClass)))))]
        else:

            # Whether to perform k-fold CV or Train/Test split
            if any([p=='train_test_split' for p in patient_to_image_excel.columns]):
                
                # Train/test split
                splitter = self.train_test_split(patient_to_image_excel)
                            
            else:

                # Image-wise k-fold cross validation
                if np.unique(np.array(self.labels)).shape[0]<self.args['folds']:
                    splitter = list(rsfk.split(self.IndexAndClass, [i[0] for i in self.labels]))   
                else:
                    
                    # More images than folds
                    aux = list(zip(self.IndexAndClass,self.labels))
                    random.shuffle(aux)
                    self.IndexAndClass,self.labels = zip(*aux)
                    self.IndexAndClass = list(self.IndexAndClass)
                    self.labels = list(self.labels)

                    # Eliminate None values from list
                    for l in range(len(self.labels)-1,-1,-1):
                        if any([ll==-1 for ll in self.labels[l]]):
                            self.labels.pop(l)
                            self.IndexAndClass.pop(l)

                    # K-fold cross validation
                    splitter = list(rsfk.split(self.IndexAndClass,np.ones((len(self.labels)))))
            
        rand.shuffle(splitter)
        return splitter

    def save_train_and_test_subjects_Names_to_excel(self):
        if len(self.IndexAndClass[0][2])==1:
            Train_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0]] for i in self.Train_indices]
            Test_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0]] for i in self.Test_indices]
        elif len(self.IndexAndClass[0][2])==2:
            Train_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1]] for i in self.Train_indices]
            Test_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1]] for i in self.Test_indices]
        elif len(self.IndexAndClass[0][2])==3:
            Train_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1],self.IndexAndClass[i][2][2]] for i in self.Train_indices]
            Test_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1],self.IndexAndClass[i][2][2]] for i in self.Test_indices]
        elif len(self.IndexAndClass[0][2])==4:
            Train_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1],self.IndexAndClass[i][2][2],self.IndexAndClass[i][2][3]] for i in self.Train_indices]
            Test_subjects = [[self.IndexAndClass[i][0],self.IndexAndClass[i][2][0],self.IndexAndClass[i][2][1],self.IndexAndClass[i][2][2],self.IndexAndClass[i][2][3]] for i in self.Test_indices]
        df = pd.DataFrame(Train_subjects)
        writer = pd.ExcelWriter(self.dataset.processed_dir_cross_validation+'Fold_'+str(self.fold+1)+'_Train_subjects.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet_1', index=False)
        writer.save()
        df = pd.DataFrame(Test_subjects)
        writer = pd.ExcelWriter(self.dataset.processed_dir_cross_validation+'Fold_'+str(self.fold+1)+'_Test_subjects.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='sheet_1', index=False)
        writer.save()
    
    def initialize_fold(self):
        '''
        Initialize variable to run a specific fold.
        n_validation_samples: (int) that specifies the number of validation samples used in this experiment.
        '''

        self.dataset.meanSTD_ylabel = []
        for i in range(len(self.IndexAndClass[0][2])):            
            if len(set([iac[2][i] for iac in self.IndexAndClass]))>5 and type(self.IndexAndClass[0][2][i]) is int:
                self.dataset.meanSTD_ylabel.append([np.array([ic[2][i] for ic in self.IndexAndClass if ic[2][i]!='None']).mean(),np.array([ic[2][i] for ic in self.IndexAndClass if ic[2][i]!='None']).std()])
            else:
                self.dataset.meanSTD_ylabel.append([0,1])

        # Start timer for this fold
        self.t_start_fold = time.perf_counter()
        
        # Obtain Train and Test Indices from IndexAndClass
        self.Train_indices = [self.IndexAndClass[i][1] for i in self.Train_indices]
        self.Test_indices = [self.IndexAndClass[i][1] for i in self.Test_indices]

        # Save training and testing images
        self.save_train_and_test_subjects_Names_to_excel()
        rand.shuffle(self.Train_indices)

        # Balance train dataset with the same number of classes.
        ros = RandomOverSampler()
        self.Train_indices, _ = ros.fit_resample(np.expand_dims(np.array(self.Train_indices),1), [self.labels[i][0] for i in self.Train_indices])
        self.Train_indices = list(self.Train_indices.squeeze())

        # Eliminate those subjects that are not included in the experiment.
        for n in range(len(self.labels[0])):
            self.Train_indices = [i for i in self.Train_indices if not self.labels[i][n]==-1]                        
            self.Test_indices = [i for i in self.Test_indices if not self.labels[i][n]==-1]

        # From the training dataset get a number of subjects to conform the validation dataset.
        self.Validation_indices = [] #self.Train_indices[:n_validation_samples]
        # self.Train_indices = self.Train_indices[n_validation_samples:]

        # Choose NaroNet's Optimizer
        self.optimizer = Adam(self.model.parameters(), lr=self.args['lr'],weight_decay=self.args['weight_decay'],amsgrad=True,eps=1e-4) # Set Optimizer
        
        # Choose NaroNet's scheduler
        self.scheduler = StepLR(self.optimizer, step_size=self.args['lr_decay_step_size'], gamma=self.args['lr_decay_factor'])
        
        # Assign the fold step.
        self.fold += 1
        
        # Initialize dictionary that save the learning history
        self.dict_epoch=None
        self.saveClusters=False
            
    def runONEepoch(self,epoch):
        '''
        Run one epoch with all the specified parameters.
        epoch: (int) that specifies which epoch we are training.
        '''

        # Start timer to count epoch time.
        t_start_epoch = time.perf_counter()                 
                
        # Train model        
        training=True                 
        train_results = TrainValidateTest.train(self,self.Train_indices,self.optimizer,training,self.saveClusters,self.labels)                       
        
        # Validate model
        training=False
        validation_results = TrainValidateTest.train(self,self.Test_indices,self.optimizer,training,self.saveClusters,self.labels)
        
        # Scheduler step
        self.scheduler.step()      

        # Show epoch information and save it into a file
        self.dict_epoch = utilz.showAndSaveEpoch(self,train_results,validation_results,self.fold,epoch,time.perf_counter(),t_start_epoch)      

    def runONEepoch_onlyTrain(self,epoch):
        '''
        Run one epoch with all the specified parameters.
        epoch: (int) that specifies which epoch we are training.
        '''

        # Start timer to count epoch time.
        t_start_epoch = time.perf_counter()                 
                
        # Train model        
        training=True                 
        train_results = TrainValidateTest.train(self,self.Train_indices,self.optimizer,training,self.saveClusters,self.labels)                       

        # Scheduler step
        self.scheduler.step()      

        # Show epoch information and save it into a file
        self.dict_epoch = utilz.showAndSaveEpoch(self,train_results,train_results,self.fold,epoch,time.perf_counter(),t_start_epoch)      
        
    
    def test(self):
        # Once the epochs finished evaluate the model and save the clusters for this fold.
        training=False
        trainClustering=False
        saveClusters=True
        train_results = TrainValidateTest.train(self,self.Train_indices,self.optimizer,training,saveClusters,self.labels)
        validation_results = TrainValidateTest.train(self,self.Test_indices,self.optimizer,training,saveClusters,self.labels)
        test_results = TrainValidateTest.train(self,self.Test_indices,self.optimizer,training,saveClusters,self.labels) # Used to save the clusters
        self.dict_fold=utilz.showAndSaveFold(self,train_results,validation_results,test_results,time.perf_counter(),self.t_start_fold)
    
    def cross_validation(self,n_validation_samples):
        '''
        Perform a K-fold cross-validation with NaroNet.
        '''

        # Initialize K-fold Cross-Validation
        self.initialize_cross_validation()
                 
        # Run the K-fold training   
        with tqdm(total=self.args['folds'], ascii=True, desc="NaroNet: Train/Test (folds)") as bar_folds:
            with tqdm(total= self.args['epochs'],ascii=True, desc="NaroNet: Train (epochs)") as bar_epochs:                 
                with tqdm(total=100,ascii=True, desc="NaroNet: Train accuracy (%)") as bar_train_acc:   
                    with tqdm(total=100,ascii=True, desc="NaroNet: Top-1 contrast accuracy (%)") as bar_contrast_acc:   
                        with tqdm(total=100,ascii=True, desc="NaroNet: Patch entropy (%)") as patch_entropy_acc:     
                    
                            # Check if the model was already trained.
                            if len([i for i in os.listdir(self.dataset.processed_dir_cross_validation) if 'ROC_AUC_' in i])>0:
                                bar_folds.update(self.args['folds']) 
                                bar_epochs.update(self.args['epochs'])                        
                                return

                            # Split 
                            splitter = NaroNet.split_subjects_images(self)
                            
                            for self.Train_indices, self.Test_indices in splitter:                        
                                
                                # Initialize Model            
                                self.model.reset_parameters()
                                self.model.to(self.device)                        
                                self.dict_fold_now = None
                                
                                # Initialize Fold iteration.
                                self.initialize_fold()                        
                                
                                bar_epochs.update(-bar_epochs.last_print_n)
                                bar_train_acc.update(-bar_train_acc.last_print_n)

                                # Train Model
                                for epoch in range(1, self.args['epochs'] + 1):            
                                    
                                    # Train 1 epoch
                                    self.runONEepoch(epoch)                

                                    # Save stats
                                    bar_epochs.update(1)
                                    bar_train_acc.update(-bar_train_acc.last_print_n+100*self.dict_epoch['train_acc'][-1][-1])
                                    cont_loss = (100*self.dict_epoch['train_contrast_loss_Ph_loss'][-1][-1]+100*self.dict_epoch['train_contrast_loss_Nb_loss'][-1][-1]+100*self.dict_epoch['train_contrast_loss_Ph_loss'][-1][-1])/3
                                    ent_loss = (100*self.dict_epoch['train_patch_entropy_Ph_loss'][-1][-1]+100*self.dict_epoch['train_patch_entropy_Nb_loss'][-1][-1]+100*self.dict_epoch['train_patch_entropy_Ar_loss'][-1][-1])/3
                                    bar_contrast_acc.update(-bar_contrast_acc.last_print_n-cont_loss)
                                    patch_entropy_acc.update(-patch_entropy_acc.last_print_n+ent_loss)                                                                        
                                
                                # Test Model
                                self.test()
                                self.dict_fold_now = self.dict_fold
                                
                                # Save Training history and print statistic graphs
                                dict_fold = utilz.showAndSaveEndOfTraining(self)
                                                        
                                bar_folds.update(1)               
                                    
        # Eliminate model from GPU        
        self.model.to("cpu") 
        return dict_fold

    def train_all(self):
        '''
        Perform a K-fold cross-validation with NaroNet.
        '''

        # Initialize K-fold Cross-Validation
        rsfk = self.initialize_cross_validation()
                 
        # Run the K-fold training   
        with tqdm(total=self.args['folds'], ascii=True, desc="NaroNet: Train/Test (folds)") as bar_folds:
            with tqdm(total= self.args['epochs'],ascii=True, desc="NaroNet: Train (epochs)") as bar_epochs:                 
                with tqdm(total=100,ascii=True, desc="NaroNet: Train accuracy (%)") as bar_train_acc:   
                    with tqdm(total=100,ascii=True, desc="NaroNet: Top-1 contrast accuracy (%)") as bar_contrast_acc:   
                        with tqdm(total=100,ascii=True, desc="NaroNet: Patch entropy (%)") as patch_entropy_acc:     
                    
                            # Check if the model was already trained.
                            if len([i for i in os.listdir(self.dataset.processed_dir_cross_validation) if 'ROC_AUC_' in i])>0:
                                bar_folds.update(self.args['folds']) 
                                bar_epochs.update(self.args['epochs'])                        
                                return

                            # Split                             
                            splitter = [(np.array(list(range(len(self.IndexAndClass)))),np.array(list(range(len(self.IndexAndClass)))))]
                            

                            for self.Train_indices, self.Test_indices in splitter:                        
                                
                                # Initialize Model            
                                self.model.reset_parameters()
                                self.model.to(self.device)                        
                                self.dict_fold_now = None
                                
                                # Initialize Fold iteration.
                                self.initialize_fold()                        
                                
                                bar_epochs.update(-bar_epochs.last_print_n)
                                bar_train_acc.update(-bar_train_acc.last_print_n)

                                # Train Model
                                for epoch in range(1, self.args['epochs'] + 1):            
                                    
                                    # Train 1 epoch
                                    self.runONEepoch_onlyTrain(epoch)                

                                    # Save stats
                                    bar_epochs.update(1)
                                    bar_train_acc.update(-bar_train_acc.last_print_n+100*self.dict_epoch['train_acc'][-1][-1])
                                    cont_loss = (100*self.dict_epoch['train_contrast_loss_Ph_loss'][-1][-1]+100*self.dict_epoch['train_contrast_loss_Nb_loss'][-1][-1]+100*self.dict_epoch['train_contrast_loss_Ph_loss'][-1][-1])/3
                                    ent_loss = (100*self.dict_epoch['train_patch_entropy_Ph_loss'][-1][-1]+100*self.dict_epoch['train_patch_entropy_Nb_loss'][-1][-1]+100*self.dict_epoch['train_patch_entropy_Ar_loss'][-1][-1])/3
                                    bar_contrast_acc.update(-bar_contrast_acc.last_print_n-cont_loss)
                                    patch_entropy_acc.update(-patch_entropy_acc.last_print_n+ent_loss)                                                                        
                                
                                # Test Model
                                self.test()
                                self.dict_fold_now = self.dict_fold
                                
                                # Save Training history and print statistic graphs
                                dict_fold = utilz.showAndSaveEndOfTraining(self)
                                                        
                                bar_folds.update(1)               
                                    
        # Eliminate model from GPU        
        self.model.to("cpu") 
        return dict_fold


    def nested_cross_validation(self,n_validation_samples,parameters,possible_params,best_params):
        '''
        Perform a K-fold cross-validation with NaroNet.
        '''

        # Initialize K-fold Cross-Validation
        self.initialize_cross_validation()
        
        # Run the K-fold training   
        with tqdm(total=self.args['folds'], ascii=True, desc="NaroNet: Train/Test (folds)") as bar_folds:
            with tqdm(total= self.args['epochs'],ascii=True, desc="NaroNet: Train (epochs)") as bar_epochs:                 
                with tqdm(total=100,ascii=True, desc="NaroNet: Train accuracy (%)") as bar_train_acc:    
                    
                    # Check if the model was already trained.
                    if len([i for i in os.listdir(self.dataset.processed_dir_cross_validation) if 'ROC_AUC_' in i])>0:
                        bar_folds.update(self.args['folds']) 
                        bar_epochs.update(self.args['epochs'])                        
                        return

                    # Split 
                    splitter = NaroNet.split_subjects_images(self)

                    for self.Train_indices, self.Test_indices in splitter:

                        # Architecture search
                        fold_path = self.args['path']+'Nested_CV_Arch/cv_'+str(bar_folds.n)+'/'
                        if not os.path.exists(self.args['path']+'Nested_CV_Arch/'):
                            os.mkdir(self.args['path']+'Nested_CV_Arch/')
                        if not os.path.exists(fold_path):                            
                            os.mkdir(fold_path)
                        parametrs = architecture_search.architecture_search(fold_path,best_params,possible_params,self.Test_indices)
                        parameters['Phenotype_Learning'] = False
                        parameters['Neighborhood_Learning'] = True
                        parameters['Area_Learning'] = True
                        parameters['experiment_Label'] = ['POLE Mutation woPheno','Copy number variation','MSI Status','Tumour Type']
                        self.args = utilz.transformToInt(parameters)    
                        self.model = NaroNet_model.NaroNet_model(self.num_features, self.name_labels, self.args["hiddens"], self.num_total_nodes, self.args["clusters"], self.args)

                        # Initialize Model            
                        self.model.reset_parameters()
                        self.model.to(self.device)                        
                        self.dict_fold_now = None
                        
                        # Initialize Fold iteration.
                        self.initialize_fold()                        
                        
                        bar_epochs.update(-bar_epochs.last_print_n)
                        bar_train_acc.update(-bar_train_acc.last_print_n)

                        # Train Model.
                        for epoch in range(1, self.args['epochs'] + 1):            

                            # Let's generate a GIF showing how the network is being learned
                            if self.args['showHowNetworkIsTraining']:
                                self.dataset.args = {'epochs':epoch}                                
                                self.Train_indicesALL = copy.deepcopy(self.Train_indices) if epoch==1 else self.Train_indicesALL
                                rand.shuffle(self.Train_indicesALL)
                                self.Train_indices = self.Train_indicesALL[:self.args['batch_size']]
                                self.runONEepoch(epoch)   
                                self.dict_fold=None
                                self.test()                                                            
                                self.dataset.visualize_results(self.model,self.args['clusters'], [self.IndexAndClass[i] for i in self.Test_indices], self.args['num_classes'],self.mean_STD, self.args)                                  
                                dict_fold = utilz.showAndSaveEndOfTraining(self)

                            else:
                                # Train 1 epoch
                                self.runONEepoch(epoch)                

                            bar_epochs.update(1)
                            bar_train_acc.update(-bar_train_acc.last_print_n+100*self.dict_epoch['train_acc'][-1][-1])
                        
                        # Test Model
                        self.test()
                        self.dict_fold_now = self.dict_fold
                        
                        # Save Training history and print statistic graphs
                        dict_fold = utilz.showAndSaveEndOfTraining(self)
                                                
                        bar_folds.update(1)               
                                
        # Eliminate model from GPU        
        self.model.to("cpu") 
        return dict_fold

    def epoch_validation(self):
        # torch.set_anomaly_enabled(True)        
        # Put Model in GPU
        torch.cuda.empty_cache()
        # torch.autograd.set_detect_anomaly(True)
        n_validation_samples=1 # self.args['batch_size']
        
        # Start the model
        if self.epoch==0:
            # Initialize Parameters
            self.model.reset_parameters()       
            self.model.to(self.device)   
            # Initialize Cross-Validation
            self.initialize_cross_validation()
            # Split 
            splitter = NaroNet.split_subjects_images(self)            
            # Run the k-fold training    
            for self.Train_indices, self.Test_indices in splitter:#[i[1] for i in IndexAndClass], [round(i) for i in labels]):                  
                # Initialize Fold iteration.
                self.initialize_fold()
                break 

            # Eliminate Test Indices in case nested cross validation is used 
            if 'AvoidSet' in self.args:
                self.Train_indices = [i for i in self.Train_indices if not i in self.args['AvoidSet']]
                self.Test_indices = [i for i in self.Test_indices if not i in self.args['AvoidSet']]
                
        else:
            self.model.to(self.device)
            self.dict_epoch = None
            self.dict_fold = None
        
        # Run one epoch
        for _ in range(int(self.args['epochs']/3)):
            self.runONEepoch(self.epoch)
            self.epoch += 1
        
        # Obtain Intersection accuracy
        self.dict_epoch['epoch'] = self.epoch
        if 'Synthetic' in self.dataset.root or False:
            self.test()   
            intersec_acc = self.dataset.obtain_intersec_acc(self.model,self.args['clusters'], self.IndexAndClass, self.args['num_classes'],self.mean_STD, self.args,self.epoch)  
            #intersec_acc = max([i[0] for i in intersec_acc])
            # Assign a intersection acc and test acc
            self.dict_epoch['maximize_acc_interpretability'] = self.dict_fold['test_Cross_entropy'][-1] -intersec_acc
            self.dict_epoch['loss_test'] = self.dict_fold['loss_test'][-1]
            self.dict_epoch['acc_test'] = self.dict_fold['acc_test'][-1]
            self.dict_epoch['test_Cross_entropy'] = [self.dict_fold['test_Cross_entropy']]
            self.dict_epoch['interpretability'] = intersec_acc
        else:
            self.test() 
            self.dict_epoch['interpretability'] = 0
            self.dict_epoch['cross_ent_test'] = self.dict_fold['cross_ent_test'][-1]
        

        # # Let's generate a GIF showing how the network is being learned        
        # self.test()                            
        # self.dataset.visualize_results_epoch(self.model,self.args['clusters'], self.IndexAndClass, self.args['num_classes'],self.mean_STD, self.args,epoch)  
        
        # Eliminate space from memory
        self.model.to('cpu')
        self.data.to('cpu')
        self.dataNOW.to('cpu')
        self.model.s[0] = self.model.s[0].to('cpu')
        self.model.s[1] = self.model.s[1].to('cpu')
        self.model.s[2] = self.model.s[2].to('cpu')                
        self.model.S[0] = self.model.S[0].to('cpu')
        self.model.S[1] = self.model.S[1].to('cpu')
        self.model.S[2] = self.model.S[2].to('cpu')  

        self.dict_res = copy.deepcopy(self.dict_epoch)
        for key in self.dict_res.keys():
            if "list" in str(type(self.dict_res[key])):
                self.dict_res[key]= [10 if self.dict_res[key][-1][-1]!=self.dict_res[key][-1][-1] else self.dict_res[key][-1][-1]][0]
        return self.dict_res

def run_NaroNet(path,parameters,possible_params,best_params):
    '''
    Code to run NaroNet using the enriched graph.  
    '''

    # Set the device to run the Neural Network.
    device =  torch.device(parameters["device"] if torch.cuda.is_available() else "cpu")

    # Load the model.
    N = NaroNet(parameters, device)
    N.epoch = 0

    # Execute k-fold cross-validation
    n_validation_samples = parameters['batch_size']
    n_validation_samples = 1

    if parameters['training_MODE']=='NestedCrossValidation':    
        N.nested_cross_validation(n_validation_samples,parameters,possible_params,best_params)   
    
    elif parameters['training_MODE']=='CrossValidation':    
        N.cross_validation(n_validation_samples)   
    
    elif parameters['training_MODE']=='TrainALL':    
        N.train_all()   