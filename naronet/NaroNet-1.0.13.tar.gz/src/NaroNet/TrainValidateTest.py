import random as rand
import torch
import numpy as np
import copy
import torch
from NaroNet.utils import utilz
import torch.nn.functional as F
import math
import NaroNet.NaroNet_model.loss as loss_Op
import gc

def inductiveClustering(self,Indices,index,saveClusters,training,labels,optimizer):
    '''
    Method that loads subject's respective graph, and insert it
    in NaroNet to calculate the phenotypes and neihborhoods
        Indices: (list of ints) that specifies the indices of the subjects.
        index: (int) that specifies the index from the subjects should be obtained in this minibatch step.
        saveClusters: (boolean) if True the Clusters are saved, if False nothing happens.
        trainClustering: (boolean) if True NaroNet is trained end-to-end, if false NaroNet' clustering layers are trained in an unsupervised way.
        training: (boolean) if True NaroNet is trained, if False subjects are inferred.
        labels: (list of ints) that specifies the labels of the subjects
        optimizer: (object) with the specified NaroNet optimizer.
    '''
    
    def clustToTissueGraph(SelectedsubImIndx, chosenLabels, saveClusterPresencePheno, s_iter, saveClusterPresenceComm, total_num_nodes,training):
        for b, subIm in enumerate(SelectedsubImIndx):
            if len(self.data.y)==0:
                self.data.y = torch.tensor(chosenLabels,dtype=torch.float32).to(device=self.device)                
            saveClusterPresencePheno[subIm[1],:] += s_iter[0][b,:self.dataNOW.num_nodes[b],:].sum(-2)
            saveClusterPresenceComm[subIm[1],:] += s_iter[-1][b,:self.dataNOW.num_nodes[b],:].sum(-2)                                                                   
            total_num_nodes[subIm[1]] += self.dataNOW.num_nodes[b]      
        self.data.edge_index = self.dataNOW.edge_index
        self.data.x = self.dataNOW.x
        
        # Save Clustering of patch from a specific patch.
        if saveClusters:
            for b, subIm in enumerate(SelectedsubImIndx):
                self.dataset.saveInductiveClusters(s_iter, Indices[index+subIm[1]],subIm[0][0],b, self.args)      
        return saveClusterPresencePheno, saveClusterPresenceComm, total_num_nodes


    def subgraph_init():
        '''
        Method that initializes the subgraphs list.
        Outputs:
            subgraphs: (list of ints) that specifies the number of subgraphs a single sbject is composed by.
            chosenLabels: (list of ints) that specifies the label of each subgraph for each subject.
        '''

        # Initialize the subgraphs list and the chosenLabels
        subgraphs=[] 
        chosenLabels=[]
        
        # Iterate to obtain the number of subgraphs each subject is composed by.
        for IndicesI in Indices[index:min(index+self.args['batch_size'],len(Indices))]:             
            
            # Obtain the labels of this subject.
            chosenLabels.append(labels[IndicesI])
            
            # If True the subject has a single subgraph, if False obtain the number of subgraphs.
            if self.dataset.findLastIndex(IndicesI)==0:
                subgraphs.append([0]) 
            else:
                subgraphs.append(list(range(0,self.dataset.findLastIndex(IndicesI)))) 
        
        return subgraphs, chosenLabels
    
    def print_losses(cell_ent_loss0,cell_ent_loss1,pat_ent0,pat_ent1,args):
        if args['verbose']==1:
            print('Patient entropy (Phenotypes):'+str(pat_ent0.item())+' Neighborhoods:'+str(pat_ent1.item()))
            print('Patch entropy (Phenotypes):'+str(cell_ent_loss0.item())+' Neighborhoods:'+str(cell_ent_loss1.item()))
    
    # Initialize the subgraphs list
    subgraphs, chosenLabels = subgraph_init()

    # Initialize an empty graph
    self.data = self.dataset.generateEmptyClusteringGraph(len(subgraphs),self.args['clusters'][1]) 
    self.data.x = torch.Tensor(self.data.x).to(self.device)
    self.data.edge_index = torch.Tensor(self.data.edge_index).to(self.device)
            
    # Empty value to save the number of nodes in a slide
    total_num_nodes=np.zeros(self.args['batch_size'])
    
    # Initialize the outputs
    contrast_loss_Ph_total = []
    contrast_loss_Nb_total = []
    PatchEntropy_loss_Ph_total = []
    PatchEntropy_loss_Nb_total = []
    
    # Used to save cluster presence for visualization
    saveClusterPresencePheno = torch.zeros([len(subgraphs),int(self.args['N_Phenotypes'])])
    saveClusterPresenceComm = torch.zeros([len(subgraphs),int(self.args['N_Neighborhoods'])])


    # Initialize the optimizer 
    optimizer.zero_grad()

    # Obtain data from folder.
    self.dataNOW, subgraphs, SelectedsubImIndx=self.dataset.gatherData_parallel(self, Indices[index:index+self.args['batch_size']],subgraphs,training)
    self.dataNOW = self.dataNOW.to(self.device)
    
    # Cluster and embedding from model.
    self.dataNOW, contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb, s_iter = self.model(self.dataNOW,self.device,True,self.args)              
    
    # Unsupervised losses
    contrast_loss_Ph_total.append(contrast_loss_Ph.item()) 
    contrast_loss_Nb_total.append(contrast_loss_Nb.item())
    PatchEntropy_loss_Ph_total.append(PatchEntropy_loss_Ph.item())
    PatchEntropy_loss_Nb_total.append(PatchEntropy_loss_Nb.item())                                          

    # Assign clustering to tissue-graph
    saveClusterPresencePheno, saveClusterPresenceComm, total_num_nodes = clustToTissueGraph(SelectedsubImIndx, chosenLabels, saveClusterPresencePheno, s_iter, saveClusterPresenceComm, total_num_nodes,training)
    self.data.num_nodes = total_num_nodes
      
    return self.data, [saveClusterPresencePheno,saveClusterPresenceComm], contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb

def train(self,Indices,optimizer,training,saveClusters,labels):
    '''
    We train/test the specified subjects using NaroNet
    Indices: (list of ints) that specifies the indices of the images.
    optimizer: (object) with the specified NaroNet optimizer.
    training: (boolean) if True NaroNet is trained, if False subjects are inferred.
    trainClustering: (boolean) if True NaroNet is trained end-to-end, if false NaroNet' clustering layers are trained in an unsupervised way.
    saveClusters: (boolean) if True the Clusters are saved, if False nothing happens.
    labels: (list of ints) that specifies the labels of the subjects
    '''

    # Initialize the outputs
    total_contrast_loss_Ph = 0
    total_PatchEntropy_loss_Ph = 0 
    total_contrast_loss_Nb = 0
    total_PatchEntropy_loss_Nb = 0 
    total_contrast_loss_Ar = 0 
    total_PatchEntropy_loss_Ar = 0 
    total_Cross_entropy_loss = 0
    accuracy = 0
        
    # Shuffle Indices if we are training the model
    rand.shuffle(Indices)
    
    # Start minibatch to train/test the model
    for index in range(0,len(Indices),self.args['batch_size']):   

        # index = max(len(Indices)-self.args['batch_size'],0) if abs(index-len(Indices))<self.args['batch_size'] else index
        # print(str(index) + '-' + str(len(Indices)))
        torch.cuda.empty_cache()
        # If True NaroNet is trained, if False subjects are inferred
        if training:  
            
            # Train NaroNet
            self.model.train()

            # Obtain phenotypes and neighborhoods.            
            data, save_Inductivecluster_presence, contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb = inductiveClustering(self,Indices,index,saveClusters,training,labels,optimizer)

            # Obtain neighborhood interactions, and classify the subjects.
            out, cluster_assignment, contrast_loss_Ar, PatchEntropy_loss_Ar = self.model(data,self.device,False,self.args)                        

        else:
            
            # Subjects are inferred. 
            self.model.eval()    

            # Specify that NaroNet does not calculate the graph of gradients.
            with torch.no_grad():
                
                # Obtain phenotypes and neighborhoods.            
                data, save_Inductivecluster_presence, contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb = inductiveClustering(self,Indices,index,saveClusters,training,labels,optimizer)

                # Obtain neighborhood interactions, and classify the subjects.
                out, cluster_assignment, contrast_loss_Ar, PatchEntropy_loss_Ar = self.model(data,self.device,False,self.args)                      
        
        Cross_entropy_loss, pred_Cross_entropy, PredictedLabels_Cross_entropy = utilz.cross_entropy_loss(training, self.args, out, data.y, self.dataset, self.device, self.model)                        

        # Apply loss to update NaroNet´s parameters
        utilz.gather_apply_loss(training, contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb, contrast_loss_Ar, PatchEntropy_loss_Ar, Cross_entropy_loss, self.optimizer,self.model,self.args)    


        pred, PredictedLabels = pred_Cross_entropy, PredictedLabels_Cross_entropy
        # if self.args['NearestNeighborClassification']:
        #     pred, PredictedLabels = pred_Nearesteighbor, PredictedLabels_NearestNeighbor
        GroundTruthLabels=data.y.cpu().numpy()
        if 'PredictedLabelsAll' in locals():
            for pred_all_i in range(len(PredictedLabelsAll)):
                PredictedLabelsAll[pred_all_i] = np.concatenate((PredictedLabelsAll[pred_all_i],PredictedLabels[pred_all_i]))            
            GroundTruthLabelsAll = np.concatenate((GroundTruthLabelsAll,GroundTruthLabels))
        else:
            PredictedLabelsAll = PredictedLabels
            GroundTruthLabelsAll = GroundTruthLabels        
        for i in range(len(pred)):            
            accuracy += np.equal(pred[i],data.y[:,i].cpu().numpy()).sum()        

        # Save supervised/unsupervised loss
        total_Cross_entropy_loss += Cross_entropy_loss[0].item()
        total_contrast_loss_Ph += contrast_loss_Ph.item()
        total_PatchEntropy_loss_Ph += PatchEntropy_loss_Ph.item() 
        total_contrast_loss_Nb += contrast_loss_Nb.item()
        total_PatchEntropy_loss_Nb += PatchEntropy_loss_Nb.item() 
        total_contrast_loss_Ar += contrast_loss_Ar.item() 
        total_PatchEntropy_loss_Ar += PatchEntropy_loss_Ar.item()          
        
        # Eliminate usage of tensors in cuda.
        del data
        gc.collect()
        
        # When testing, save the clusters for visualization purposes
        if saveClusters:            
            indexes = Indices[index:min(index+self.args['batch_size'],len(Indices))]
            for idx, val in enumerate(indexes):
                self.dataset.save_cluster_and_attention(idx, val, save_Inductivecluster_presence, cluster_assignment)

    n_iter = len(list(range(0,len(Indices),self.args['batch_size'])))

    return GroundTruthLabelsAll, PredictedLabelsAll, (accuracy / PredictedLabelsAll[0].shape[0])/len(pred), total_Cross_entropy_loss/n_iter, total_contrast_loss_Ph/n_iter, total_PatchEntropy_loss_Ph/n_iter, total_contrast_loss_Nb/n_iter, total_PatchEntropy_loss_Nb/n_iter, total_contrast_loss_Ar/n_iter, total_PatchEntropy_loss_Ar/n_iter, Indices
