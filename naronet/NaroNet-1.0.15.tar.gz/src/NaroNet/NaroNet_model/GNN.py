import torch
import torch.nn.functional as F
from NaroNet.NaroNet_model.torch_geometric_rusty import JumpingKnowledge, uniform


def batchNorm(x,num_nodes,device):
    mean = torch.zeros((1,x.shape[2]),device=device)
    std = torch.zeros((1,x.shape[2]),device=device)
    for i in range(x.shape[0]):
        mean += x[i,:num_nodes[i],:].sum((0),keepdims=True)
    mean /= sum(num_nodes)
    for i in range(x.shape[0]):
        std += ((x[i,:num_nodes[i],:]-mean)**2).sum(0,keepdims=True)
    std /= sum(num_nodes)-1
    std = std**0.5
    std[std==0] = 1e-15
    return mean, std

class Dense_SAGEConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels,paramApply):
        super(Dense_SAGEConv, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.paramApply = paramApply
        self.weight = torch.nn.Parameter(torch.Tensor(self.in_channels, out_channels))        
        self.bias = torch.nn.Parameter(torch.Tensor(out_channels))

    def reset_parameters(self):
        uniform(self.in_channels, self.weight)        
        uniform(self.in_channels, self.bias)

    def forward(self, x, edge_index, device, num_nodes=None):        
        
        if self.paramApply:
            x = torch.matmul(x, self.weight)                    
            x = x + self.bias 
            
        out = torch.zeros((x.shape),device=device)
        for i in range(len(edge_index)):
            out[i,:,:] = torch.matmul(edge_index[i], x[i,:,:])
                    
        # Apply mask to nodes that are present
        if num_nodes is not None:
            for i in range(x.shape[0]):
                out[i,num_nodes[i]:,:] = 0
        return out

class Sparse_SAGEConv(torch.nn.Module):
    def __init__(self, in_channels, out_channels,paramApply):
        super(Sparse_SAGEConv, self).__init__()
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.paramApply = paramApply
        self.weight = torch.nn.Parameter(torch.Tensor(self.in_channels, out_channels))
        self.bias = torch.nn.Parameter(torch.Tensor(out_channels))            
        self.reset_parameters()

    def reset_parameters(self):
        uniform(self.in_channels, self.weight)        
        uniform(self.in_channels, self.bias)        

    def forward(self, x, adj):                
        
        if self.paramApply:
            x = torch.matmul(x, self.weight)        
            x = x + self.bias            

        x = torch.matmul(adj, x)        
        x = x / adj.sum(dim=-1, keepdim=True).clamp(min=1)        
        
        return x


class neigh(torch.nn.Module):
    def __init__(self, in_channels, out_channels, args, paramApply):
        super(neigh, self).__init__()
        self.in_channels = in_channels
        self.args = args
        self.out_channels = out_channels       
        self.conv1 = Dense_SAGEConv(in_channels, in_channels,paramApply)
        self.conv2 = Dense_SAGEConv(in_channels, in_channels,paramApply)
        self.conv3 = Dense_SAGEConv(in_channels, out_channels,paramApply)
       
    def reset_parameters(self):
        # First MLP into the features
        self.conv1.reset_parameters()
        self.conv2.reset_parameters()
        self.conv3.reset_parameters()

    def forward(self, x, edge_index, device, num_nodes,args):        
        x = F.dropout(x, p=args['dropoutRate'], training=self.training)
        x = self.conv1(x, edge_index, device, num_nodes)
        x = self.conv2(x, edge_index, device, num_nodes)
        x = self.conv3(x, edge_index, device, num_nodes)  

        # Calculate mean and std
        if self.training:
            self.mean, self.std = batchNorm(x,num_nodes,device)
         
        # Apply normalization
        if args['Batch_Normalization']:
            x = (x-self.mean)/self.std    

        return x                            


class area(torch.nn.Module):
    def __init__(self, in_channels, out_channels, args,paramApply):
        super(area, self).__init__()
        self.in_channels = in_channels
        self.args = args
        self.out_channels = out_channels
        
        self.conv1 = Sparse_SAGEConv(in_channels, out_channels, paramApply)        

    def reset_parameters(self):
        self.conv1.reset_parameters()

    def forward(self, x, edge_index, device, num_nodes,args):        
        x = F.dropout(x, p=args['dropoutRate'], training=self.training)
        x = self.conv1(x, edge_index) 

        # Calculate mean and std
        if self.training:
            self.mean, self.std = batchNorm(x,[x.shape[1]]*x.shape[0],device)
         
        # Apply normalization
        if args['Batch_Normalization']:
            x = (x-self.mean)/self.std    

        return x                            

class pheno(torch.nn.Module):
    def __init__(self, in_channels, out_channels, args):
        super(pheno, self).__init__()
        self.in_channels = in_channels
        self.args = args
        self.out_channels = out_channels

        # Initialize linear model
        self.lin = torch.nn.Linear(in_channels, out_channels)
        self.BN = torch.nn.BatchNorm1d(out_channels)#,track_running_stats=False)                

    def reset_parameters(self):
        # Reset parameters of linear model.
        self.lin.reset_parameters()     
        self.BN = torch.nn.BatchNorm1d(self.out_channels)#,track_running_stats=False)                                           
  
    def forward(self, x, edge_index, device, num_nodes,args):    
        # Linear layer
        x = F.dropout(x, p=args['dropoutRate'], training=self.training)   
        x = self.lin(x)  
        
        # Calculate mean and std
        if self.training:
            self.mean, self.std = batchNorm(x,num_nodes,device)
         
        # Apply normalization
        if args['Batch_Normalization']:
            x = (x-self.mean)/self.std                    
        return x