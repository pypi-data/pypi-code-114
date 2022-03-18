import numpy as np
import random
import torch
from torch.utils.data.sampler import Sampler

class ImbalanceSamplerV1(Sampler):
    def __init__(self, dataset, batch_size=None, labels=None, shuffle=True, num_pos=None, sampling_rate=None):
        '''
        sampling_rate: Sampling rate refers to rate of number of positive samples of all samples. 
        num_pos: Number of postive samples in a mini-batch
        shuffle: Random shuffle data pool every epoch
        labels: labels in list for the given dataset. If none, get labels from dataset
        '''
        assert batch_size is not None, 'Batch size need to be specified!'
        assert (num_pos is None) or (sampling_rate is None), 'You can only use one of {pos_num} and {sampling_rate}!'
  
        if sampling_rate:
           assert sampling_rate>0.0 and sampling_rate<1.0, 'Sampling rate is out of range!'
        if labels is None:
           labels = self._get_labels(dataset)
        
        self.labels = labels
        self.sampling_rate = sampling_rate
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.class_labels = np.unique(labels)
        self.num_classes = len(self.class_labels)

        # create data pool for each class
        self.dataDict = {}
        for cls in self.class_labels:
            self.dataDict[int(cls)] = []
        for i in range(len(self.labels)):
            self.dataDict[int(self.labels[i])].append(i)
        self.value_counts = self._value_counts(self.labels)

        # TODO: multi-class; auto policy
        if self.sampling_rate:
           self.num_pos = int(self.sampling_rate*batch_size)
           if self.num_pos < 1:
              self.num_pos = 1
           self.num_neg = batch_size - self.num_pos
        elif num_pos:
            self.num_pos = num_pos if num_pos < 1 else 1
            self.num_neg = batch_size - self.num_pos
        else:
            NotImplementedError

        # TODO: multi-class; auto policy
        # statstics
        self.pos_indices = self.dataDict[1]
        self.neg_indices = self.dataDict[0]
        self.pos_len = self.value_counts[1]
        self.neg_len  = self.value_counts[0]
        
        # sampling params
        self.num_batches = max(self.pos_len//self.num_pos, self.neg_len//self.num_neg)
        self.sampled = np.empty(self.num_batches*self.batch_size, dtype=np.int64)
        self.posPtr, self.negPtr = 0, 0

    def _get_labels(self, dataset):
      # TODO: isinstance(dataset, torchvision.datasets.ImageFolder)
      if isinstance(dataset, torch.utils.data.Dataset):
          return dataset.targets
      else:
          raise NotImplementedError
        
    def _value_counts(self, targets):
       if len(targets.shape) >= 2: # x one-hot
          targets = targets.flatten().astype(int)
       dict = {}
       for val in np.unique(targets):
           dict[val] = np.count_nonzero(targets == val)
       return dict

    def __iter__(self):
        
        for i in range(self.num_batches):
            start_index = i*self.batch_size
            if self.posPtr+self.num_pos > self.pos_len:
                temp = self.pos_indices[self.posPtr:]
                np.random.shuffle(self.pos_indices)
                self.posPtr = (self.posPtr+self.num_pos)%self.pos_len
                self.sampled[start_index:start_index+self.num_pos]= np.concatenate((temp,self.pos_indices[:self.posPtr]))
            else:
                self.sampled[start_index:start_index+self.num_pos]= self.pos_indices[self.posPtr: self.posPtr+self.num_pos]
                self.posPtr += self.num_pos

            start_index += self.num_pos
            if self.negPtr+self.num_neg > self.neg_len:
                temp = self.neg_indices[self.negPtr:]
                np.random.shuffle(self.neg_indices)
                self.negPtr = (self.negPtr+self.num_neg)%self.neg_len
                self.sampled[start_index:start_index+self.num_neg]= np.concatenate((temp,self.neg_indices[:self.negPtr]))
            else:
                self.sampled[start_index:start_index+self.num_neg]= self.neg_indices[self.negPtr: self.negPtr+self.num_neg]
                self.negPtr += self.num_neg

        return iter(self.sampled)

    def __len__ (self):
        return len(self.sampled)
    
# alias name
ImbalanceSampler = ImbalanceSamplerV1
    
    
