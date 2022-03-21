import torch
import torch.nn.functional as F
import NaroNet.NaroNet_model.pooling as pooling
import NaroNet.NaroNet_model.loss as loss
import NaroNet.NaroNet_model.GNN as GNN
import NaroNet.utils.utilz
import numpy as np
import copy

class NaroNet_model_simple(torch.nn.Module):
    def __init__(self, num_features, labels, num_nodes, clusts, args):
        super(NaroNet_model_simple, self).__init__()
        self.features = num_features        
        self.args = args                                 

        # Learning local phenotypes 
        self.pheno_clust = GNN.pheno(self.features,clusts[0], args)
                        
        # Learning cellular neighborhoods
        self.neigh_clust = GNN.neigh(self.features, clusts[1], args,True)  
        self.neigh_emb = GNN.neigh(self.features, clusts[1], args, False)            
        
        # Learning tissue areas
        self.area_clust = GNN.area(self.features, clusts[2], args,True)   
        self.area_emb = GNN.area(self.features, clusts[2], args,False)                        

        # Final layer
        self.lin_pat_1 = torch.nn.Linear(clusts[0] + clusts[1] + clusts[2], len(set(labels[0])), bias=True)

        if len(args['experiment_Label'])>1:
            self.lin_pat_2 = torch.nn.Linear(clusts[0] + clusts[1] + clusts[2], int(max(labels[1])) if len(labels[1])>5 else len(labels[1]), bias=True)          
        if len(args['experiment_Label'])>2:
            self.lin_pat_3 = torch.nn.Linear(clusts[0] + clusts[1] + clusts[2], int(max(labels[2])) if len(labels[2])>5 else len(labels[2]), bias=True)          
        if len(args['experiment_Label'])>3:
            self.lin_pat_4 = torch.nn.Linear(clusts[0] + clusts[1] + clusts[2], int(max(labels[3])) if len(labels[3])>5 else len(labels[3]), bias=True)          
    
    def reset_parameters(self):        
                
        # Phenotypes
        self.pheno_clust.reset_parameters()
                
        # Cellular neighborhoods
        self.neigh_clust.reset_parameters()

        # Tissue areas
        self.area_clust.reset_parameters()

        # Final layer    
        self.lin_pat_1.reset_parameters()                
        if len(self.args['experiment_Label'])>1:
            self.lin_pat_2.reset_parameters()
        if len(self.args['experiment_Label'])>2:
            self.lin_pat_3.reset_parameters()
        if len(self.args['experiment_Label'])>3:
            self.lin_pat_4.reset_parameters()
                    
    def softmaxToClst(self,s,args,device):
        s=F.softmax(s,dim=-1)
        if args['1Patch1Cluster']:
            s = torch.where(s>=s.max(-1).values.unsqueeze(-1).repeat(1,1,s.shape[2]), s, torch.tensor([0],dtype=torch.float32).to(device))
        s = torch.where(s>=args['attntnThreshold'], s, s*0)
        return s
    
    def poolingToClst(self,s,device,num_nodes):
        Spatient = torch.zeros(s.shape[0],s.shape[-1],dtype=torch.float32).to(device)
        for i in range(s.shape[0]):
            Spatient[i,:] = (s[i,:num_nodes[i],:].sum(0)/num_nodes[i])   
        return Spatient

    def ObtainPhenotypesClustering(self, x, data, device, args):          
        self.s=[self.pheno_clust(x, data.edge_index, device, data.num_nodes,args)]        
        return self.s

    def ClassifyPatients(self, args):
        x = []
        
        # Fully connected Layer               
        x.append(self.lin_pat_1(torch.cat(self.S,dim=-1)))                         
        if len(self.args['experiment_Label'])>1:
            x.append(self.lin_pat_2(torch.cat(self.S,dim=-1)))
        if len(self.args['experiment_Label'])>2:
            x.append(self.lin_pat_3(torch.cat(self.S,dim=-1)))
        if len(self.args['experiment_Label'])>3:
            x.append(self.lin_pat_4(torch.cat(self.S,dim=-1)))
                
        return x

    def Areas_forward(self, data, device, args):
        
        # GNN Forward to obtain clusters.
        self.s.append(self.area_clust(data.x, data.edge_index, device, data.num_nodes,args))                            
        
        # Obtain Cell Entropy Loss
        contrast_loss_Ar, PatchEntropy_loss_Ar = loss.patch_contrast_entropy(self.area_emb(data.x, data.edge_index, device, data.num_nodes,args),F.softmax(self.s[-1],dim=2), [self.s[-1].shape[1]]*self.s[-1].shape[0],device)

        # Apply Softmax to cluster assignment             
        self.s[-1] = self.softmaxToClst(self.s[-1],args,device)
                
        # Obtain Patient Concentration for each cluster
        self.S.append(self.poolingToClst(self.s[-1],device,[self.s[-1].shape[1]]*self.s[-1].shape[0]))                           
        self.s[-1] = self.s[-1].to('cpu') 
        return data.x, data.edge_index, contrast_loss_Ar, PatchEntropy_loss_Ar

    def Neighborhoods_forward(self, data, device, args):

        # Neighborhood assignment
        self.s.append(self.neigh_clust(data.x, data.edge_index, device, data.num_nodes,args))  

        # Obtain patch
        contrast_loss_Nb, PatchEntropy_loss_Nb = loss.patch_contrast_entropy(self.neigh_emb(data.x, data.edge_index, device, data.num_nodes,args),F.softmax(self.s[-1],dim=2), data.num_nodes,device)
                
        # Apply Softmax to cluster assignment       
        self.s[-1] = self.softmaxToClst(self.s[-1],args,device)

        # Node-Pooling     
        data.x, data.edge_index = pooling.Dense_Pooling(data.x, data.edge_index, self.s[-1], device, data.num_nodes, True)  # Tissue-Communities                                             

        # Obtain Patient Concentration for each cluster
        self.S.append(self.poolingToClst(self.s[-1],device,data.num_nodes)) 
        self.s[-1] = self.s[-1].to('cpu')           

        return data.x, data.edge_index, contrast_loss_Nb, PatchEntropy_loss_Nb

    def Phenotypes_forward(self, data, device, args):
        
        # Assign patches to phenotypes
        self.s = self.ObtainPhenotypesClustering(data.x,data, device, args)                                          

        # Calculate patch entropy and contrast loss
        contrast_loss_Ph, PatchEntropy_loss_Ph = loss.patch_contrast_entropy(data.x,F.softmax(self.s[0],dim=2), data.num_nodes,device)
                        
        # Apply Softmax to cluster assignment
        self.s[-1] = self.softmaxToClst(self.s[-1],args,device)        
        
        # Calculate subject abundance
        self.S = [self.poolingToClst(self.s[-1],device,data.num_nodes)]    
        self.s[-1] = self.s[-1].to('cpu')                   

        return contrast_loss_Ph, PatchEntropy_loss_Ph

    def forward(self, data, device, doClustering,args):
        
        if doClustering:                                
            # Calculate phenotypes            
            contrast_loss_Ph, PatchEntropy_loss_Ph = self.Phenotypes_forward(data, device, args)            
            
            # Calculate neighborhoods                      
            data.x, data.edge_index, contrast_loss_Nb, PatchEntropy_loss_Nb = self.Neighborhoods_forward(data, device, args)
                                  
            return data, contrast_loss_Ph, PatchEntropy_loss_Ph, contrast_loss_Nb, PatchEntropy_loss_Nb, self.s                    
        
        else:        
            # Obtain Tissue-Communities Interactions
            data.x, data.edge_index, contrast_loss_Ar, PatchEntropy_loss_Ar = self.Areas_forward(data, device, args)

        # Classify subjects from microenvironment abundances        
        x = self.ClassifyPatients(args)                       
                
        return x, self.s[2:], contrast_loss_Ar, PatchEntropy_loss_Ar