from tkinter import N
from torchvision.transforms import transforms
from NaroNet.Patch_Contrastive_Learning.data_aug.gaussian_blur import GaussianBlur
from torchvision import transforms, datasets
from NaroNet.Patch_Contrastive_Learning.data_aug.view_generator import ContrastiveLearningViewGenerator
from NaroNet.Patch_Contrastive_Learning.exceptions.exceptions import InvalidDatasetSelection
from NaroNet.utils import utilz
from imgaug import augmenters as iaa
from torch.utils.data import Dataset, DataLoader 
import pandas as pd
import torch
import os
import numpy as np
from skimage import io
from skimage import filters
import random
import gc
import csv
from NaroNet.Patch_Contrastive_Learning.preprocess_images import Mean_std_experiment

class ContrastiveLearningDataset_PCL(Dataset):
    def __init__(self, args,training, mean=None, std=None):
        self.training = training

        # Root folder
        self.root_folder = args['path']+'Raw_Data/Images/'

        # Image list
        self.image_list = os.listdir(self.root_folder)
        random.shuffle(self.image_list)

        # Open Channels.txt
        self.Channels, _ = utilz.load_channels(args['path']+'Raw_Data/')
        self.in_channels = len(self.Channels)        

        # Parameters
        self.args = args    
        self.patch_size = args['PCL_Patch_Size']
        self.stride = args['PCL_Stride']
        self.alpha_L = args['PCL_Alpha_L']
        self.n_crops_per_image = args['PCL_N_Crops_per_Image']    

        # Preprocessing
        if os.path.exists(self.root_folder[:-7]+'Experiment_Stats.csv'):
            f = csv.reader(open(self.root_folder[:-7]+'Experiment_Stats.csv'))
            self.mean = np.array(next(f),dtype=np.float32)
            self.std = np.array(next(f),dtype=np.float32)            
        else: 
            self.mean, self.std = Mean_std_experiment(obj=self, base_path=self.root_folder,image_paths=self.image_list[:10],Channels=self.Channels)     
    
    def __len__(self):        
        return len(self.image_list)

    def load_image(self,idx):

        # Load CZI file
        if self.image_list[idx].endswith('.czi'):
            from aicspylibczi import CziFile
            import pathlib
            import cv2
            
            # Obtain header info from the czi
            factor = 5
            file = pathlib.Path(self.root_folder+self.image_list[idx])
            czi = CziFile(file)
            self.czidimensions = czi.get_mosaic_scene_bounding_box(0)    
            dims = czi.get_dims_shape()        
            
            # Obtain crop or the full image
            if self.training:
                xIn,yIn = np.random.randint(0,self.czidimensions.w-int(self.patch_size*factor*self.alpha_L)-1), np.random.randint(0,self.czidimensions.h-int(self.patch_size*factor*self.alpha_L)-1)
                image = czi.read_mosaic(C=0,region=(self.czidimensions.x+xIn,self.czidimensions.y+yIn,int(self.patch_size*factor*self.alpha_L),int(self.patch_size*factor*self.alpha_L)))
                new_size_x, new_size_y  = int(self.patch_size*self.alpha_L), int(self.patch_size*self.alpha_L)
            else:    
                image = czi.read_mosaic(C=0,region=(self.czidimensions.x,self.czidimensions.y,self.czidimensions.w,self.czidimensions.h))
                new_size_x, new_size_y  = int(self.czidimensions.w/factor), int(self.czidimensions.h/factor)
            
            # Postprocessing and image resizing
            image = image.squeeze()
            image = cv2.resize(image, dsize=(new_size_x, new_size_y), interpolation=cv2.INTER_CUBIC)
            self.wsiIm = czi

        elif self.image_list[idx].endswith('.ome.tif'): 
            image = io.imread(self.root_folder+self.image_list[idx])              
            image = image[:,:,self.Channels]
            if self.args['PCL_Z_Score'] and hasattr(self, 'mean'):
                image -= np.expand_dims(np.expand_dims(self.mean,0),0)
                image /= np.expand_dims(np.expand_dims(self.std,0),0)

        # Load TIFF file
        elif self.image_list[idx].endswith('.tif') or self.image_list[idx].endswith('.tiff'): 
            image = io.imread(self.root_folder+self.image_list[idx])                
            
            if np.argmin(image.shape)==0:
                image = image.swapaxes(0,2)                            
            
            image = image[:,:,self.Channels]
            if self.args['PCL_Z_Score'] and hasattr(self, 'mean'):
                image = image-np.expand_dims(np.expand_dims(self.mean,0),0)
                image = image/np.expand_dims(np.expand_dims(self.std,0),0)
        else:
            image =  np.load(self.root_folder+self.image_list[idx],allow_pickle=True)  
            from PIL import Image            
        return image

    def get_crops(self, data,idx):

        # Don´t train using 
        thr = filters.threshold_multiotsu(data.sum((2)),classes=3)
        
        images=[]
        for _ in range(int(self.n_crops_per_image)):
            
            if self.image_list[idx].endswith('.czi'):                
                images.append(self.load_image(idx))
            else:                                
                while True:
                
                    # Get random x,y positions within the image and append the local phenotype crop
                    xIn,yIn = np.random.randint(0,data.shape[0]-int(self.patch_size*self.alpha_L)-1), np.random.randint(0,data.shape[1]-int(self.patch_size*self.alpha_L)-1)
                    
                    if data[xIn:xIn+int(self.patch_size*self.alpha_L),yIn:yIn+int(self.patch_size*self.alpha_L),:].sum((2)).max()>=thr[0] and self.args['PCL_eliminate_Black_Background']:                                        
                        images.append(data[xIn:xIn+int(self.patch_size*self.alpha_L),yIn:yIn+int(self.patch_size*self.alpha_L),:])
                        break
                    elif data[xIn:xIn+int(self.patch_size*self.alpha_L),yIn:yIn+int(self.patch_size*self.alpha_L),:].sum((2)).max()<=thr[0] and self.args['PCL_eliminate_White_Background']:                                        
                        images.append(data[xIn:xIn+int(self.patch_size*self.alpha_L),yIn:yIn+int(self.patch_size*self.alpha_L),:])
                        break
                    elif self.args['PCL_eliminate_Black_Background']==False and self.args['PCL_eliminate_Black_Background']==False: 
                        images.append(data[xIn:xIn+int(self.patch_size*self.alpha_L),yIn:yIn+int(self.patch_size*self.alpha_L),:])
                        break        
        return images  

    def get_all_crops(self, data):
        
        # Obtain indices considering patch size and stride
        patches=[]  
        patch_pos = []     
        x_steps = range(int(np.floor(self.patch_size/2)), int(np.floor(data.shape[0]/(self.patch_size-self.stride))*(self.patch_size-self.stride)), (self.patch_size-self.stride))
        y_steps = range(int(np.floor(self.patch_size/2)), int(np.floor(data.shape[1]/(self.patch_size-self.stride))*(self.patch_size-self.stride)), (self.patch_size-self.stride))      

        # Iterate to obtain patches
        for x in x_steps:
            for y in y_steps:
                patches.append(data[int(np.ceil(x-self.patch_size/2)):int(np.ceil(x+self.patch_size/2)),
                                    int(np.ceil(y-self.patch_size/2)):int(np.ceil(y+self.patch_size/2)),:])            
                patch_pos.append([x,y])
        
        return patches, np.array(patch_pos)

    def perform_augmentation(self, crop):

        # Obtain image patch from image crop.
        x, y =np.random.randint(0,crop[0].shape[0]-self.patch_size+1), np.random.randint(0,crop[0].shape[0]-self.patch_size+1)        
        aug = crop[x:self.patch_size+x,y:self.patch_size+y,:]

        # Add color perturbation
        if self.args['PCL_Color_perturbation_Augmentation']:
            # To install the following library: pip install histomicstk --find-links https://girder.github.io/large_image_wheels
            from histomicstk.preprocessing.augmentation.color_augmentation import rgb_perturb_stain_concentration
            min_im = aug.min((0,1))
            aug = aug-min_im
            max_im = aug.max((0,1))
            max_im[max_im<=0] = 1e-16
            aug = aug/max_im*255     
            try:
                aug = rgb_perturb_stain_concentration(aug.astype(np.uint8))
                aug = (((aug*max_im)/255)+min_im)
            except:
                aug = (((aug*max_im)/255)+min_im)
        
        # Define sequence of augmentations
        seq_easy = iaa.Sequential([
            iaa.CoarseDropout(0.04, size_percent=0.05, per_channel=0.5), # Drop 2% of all pixels, 15% of the original size,in 50% of all patches channeld
            iaa.Add((-0.15, 0.15), per_channel=0.5), # Add noise per channel...
            iaa.GaussianBlur(sigma=(0, 1)) # blur patches with a sigma of 0 to 3.0
        ])                
        
        # Flip lr
        if random.random()<0.5:
            for c in range(aug.shape[2]):
                aug[:,:,c] = np.flip(aug[:,:,c],0)
    
        # Flip ud
        if random.random()<0.5:
            for c in range(aug.shape[2]):
                aug[:,:,c] = np.flip(aug[:,:,c],1)

        # RGB
        if aug.shape[2]==3:
            return seq_easy(image=aug.astype(np.float32))    
        
        # Multiplex
        else:
            return seq_easy(images=aug.astype(np.float32))    

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()

        # Load image
        image = self.load_image(idx)    
        # image = image.astype(np.float32)    

        if self.training:

            # Obtain a crop of size Patch_size*alpha_L
            crops = self.get_crops(image,idx)
            
            # Perform sequential image transformations
            augs_1 = []
            augs_2 = []
            for crop in crops:
                augs_1.append(self.perform_augmentation(crop))
                augs_2.append(self.perform_augmentation(crop))
            del image, crops
            gc.collect(0)
            gc.collect(1)
            gc.collect(2)
            return torch.tensor(np.array(augs_1)), torch.tensor(np.array(augs_2))

        else:
            crops, patch_pos = self.get_all_crops(image)
            del image
            gc.collect(0)
            gc.collect(1)
            gc.collect(2)
            return crops, patch_pos, self.image_list[idx]


        

