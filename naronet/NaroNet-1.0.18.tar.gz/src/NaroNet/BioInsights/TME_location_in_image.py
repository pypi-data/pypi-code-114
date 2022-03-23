import statistics as st
import os
import numpy as np
import copy
import matplotlib.pyplot as plt
from matplotlib import cm
from tifffile.tifffile import imwrite
import matplotlib.patches as mpatches
from PIL import Image
from NaroNet.utils.parallel_process import parallel_process
from NaroNet.BioInsights.Pheno_Neigh_Info import load_cell_types_assignments, load_patch_image
import gc
import cv2

def TME_location_in_image_(dataset,thisfolder,idxclster,patchIDX, clusters,nClust,sts,statisticalTests_PerPatient,statisticalTests,unrestrictedLoss,count,Patindx):
    '''
    '''

    if not os.path.exists(dataset.bioInsights_dir_TME_in_image+thisfolder+idxclster[2][0]+'/'):
        os.mkdir(dataset.bioInsights_dir_TME_in_image+thisfolder+idxclster[2][0]+'/')

    # Pixel-to-cluster Matrix
    clust0 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(idxclster[1], 0, clusters[0]))                    
    if nClust>0:
        clust1 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(idxclster[1], 0, clusters[1]))                                     
    if nClust>1:
        clust2 = np.load(dataset.processed_dir_cell_types+'cluster_assignment_Index_{}_ClustLvl_{}.npy'.format(idxclster[1], clusters[2]))                    
        clust2 = np.matmul(clust1,clust2)
    clust = clust0 
    clust = clust1 if nClust==1 else clust
    clust = clust2 if nClust==2 else clust                
    
    # Open Raw Image.
    im, imList = dataset.open_Raw_Image(idxclster,1)

    # Assign significant cluster as 1 to SuperPatch Image             
    if ('Endometrial_LowGrade' in dataset.raw_dir):
        for imList_n ,imList_i in enumerate(imList[::-1]):
            Patch_im_i = np.zeros(imList_i.shape[:2])                        
            # Create superPatch Label image using the Superpatch size. 
            division_rows = np.floor(Patch_im_i.shape[0]/dataset.patch_size)
            division_cols = np.floor(Patch_im_i.shape[1]/dataset.patch_size)
            lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for row_indx, row in enumerate(range(int(division_rows))):
                Patch_im_i[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
            Patch_im_i = Patch_im_i.astype(int) 
            if imList_n==0:
                Patch_im = Patch_im_i
            else:                
                Patch_im = np.concatenate((Patch_im, Patch_im_i+Patch_im.max()+1),1)
    elif 'ZuriBasel' in dataset.raw_dir:
        for imList_n ,imList_i in enumerate(imList[::-1]):
            Patch_im_i = np.zeros(imList_i.shape[:2])                        
            # Create superPatch Label image using the Superpatch size. 
            division_rows = np.floor(Patch_im_i.shape[0]/dataset.patch_size)
            division_cols = np.floor(Patch_im_i.shape[1]/dataset.patch_size)
            lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for row_indx, row in enumerate(range(int(division_rows))):
                Patch_im_i[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
            Patch_im_i = Patch_im_i.astype(int) 
            if imList_n==0:
                Patch_im = Patch_im_i
            else:                
                Patch_im = np.concatenate((Patch_im, Patch_im_i+Patch_im.max()+1),1)
    else:
        Patch_im = np.zeros(im.shape[:2])                        
        # Create superPatch Label image using the Superpatch size. 
        division_rows = np.floor(Patch_im.shape[0]/dataset.patch_size)
        division_cols = np.floor(Patch_im.shape[1]/dataset.patch_size)
        lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
        lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
        for row_indx, row in enumerate(range(int(division_rows))):
            Patch_im[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
        # suprpxlIm = np.transpose(suprpxlIm)
        Patch_im = Patch_im.astype(int)
        if ('V_H' in dataset.root) or ('V3' in dataset.root) or ('V1' in dataset.root) or ('V4' in dataset.root):
            Patch_im = np.transpose(Patch_im)                        

    # Assign significant clusters to pixels.
    cell_type_top1 = np.apply_along_axis(np.argmax, axis=1, arr=clust)       

    # Obtain Image in RGB
    # imRGB = dataset.nPlex2RGB(im)                                   
    # for c in range(imRGB.shape[2]):
    #     imRGB[:,:,c] = imRGB[:,:,c]/imRGB[:,:,c].max()                 
                            
    # For each threshold value
    #for thrs in ClusteringThreshold:
    # Mask selecting top PIR values.
    AllClusters = (copy.deepcopy(cell_type_top1)*0).astype('float32')
    AllClusters[sts[2][1]==cell_type_top1] = clust[sts[2][1]==cell_type_top1,sts[2][1]]
    # Apply Threshold to select cells with high confidence.
    # AllClusters[np.percentile(clust.max(-1),thrs)>clust.max(-1)] = 0 
    AllClusters_2=AllClusters[Patch_im] # Superpatches of significant clusters.
    # Number of SuperPatches present in this one    
    # Save Certainty of this Phenotype-TissueCommunity     
    plt.figure()
    n, bins, patches = plt.hist(clust.max(-1)[sts[2][1]==cell_type_top1], 100, color=cm.jet_r(int(sts[2][1]*(255/int(sts[2][0])))), alpha=0.5)

    if int(sts[2][0])==clusters[0]:
        plt.xlabel('Level of Phenotype Certainty')
        plt.title('Histogram of Phenotype '+str(sts[2][1])+' Certainty')
    elif int(sts[2][0])==clusters[1]:
        plt.xlabel('Level of Neighborhood Certainty')
        plt.title('Histogram of Neighborhood '+str(sts[2][1])+' Certainty')
    elif int(sts[2][0])==clusters[2]:
        plt.xlabel('Level of Area Certainty')
        plt.title('Histogram of Area '+str(sts[1])+' Certainty')
    plt.ylabel('Number of patches')
    plt.savefig(dataset.bioInsights_dir_TME_in_image+thisfolder+idxclster[2][0]+'/Label{}_Slide{}_Patch{}_Clstrs{}_Thrs{}_Acc{}_PIR{}_Hist.png'.format(
        idxclster[2][0],idxclster[0],patchIDX,statisticalTests['TME -h'][count],100,unrestrictedLoss[count],str(round(statisticalTests_PerPatient[Patindx][1],2))), format="PNG",dpi=200) 
    plt.close()
    # Save GT and Image                           
    # imwrite(dataset.bioInsights_dir_TME_in_image+thisfolder+idxclster[2][0]+'/Label{}_Slide{}_Patch{}_Clstrs{}_Acc{}_PIR{}_Images.tiff'.format(idxclster[2][0],idxclster[0],patchIDX,statisticalTests['TME -h'][count],unrestrictedLoss[count],str(round(statisticalTests_PerPatient[Patindx][1],2))),np.moveaxis(im,2,0))                                        
    imtosave = Image.fromarray(np.uint8(AllClusters_2*255))
    imtosave.save(dataset.bioInsights_dir_TME_in_image+thisfolder+idxclster[2][0]+'/Label{}_Slide{}_Patch{}_Clstrs{}_Acc{}_PIR{}_Label.tiff'.format(idxclster[2][0],idxclster[0],patchIDX,statisticalTests['TME -h'][count],unrestrictedLoss[count],str(round(statisticalTests_PerPatient[Patindx][1],2))))                
    
    return 'done'

def TME_location_in_image(dataset, statisticalTests, clusters, IndexAndClass,unrestrictedLoss,statisticalTests_PerPatient, num_classes, attentionLayer,ClusteringThreshold):
    '''
        docstring
    '''
    
    # statisticalTests = sorted(statisticalTests, key=lambda k: k[0]) # 1.p-value, 2.Cluster step, 3. column of the heatmap        
    # stsTest=statisticalTests[0]
    IntersecIndex=[]
    patchIDX = dataset.args['epochs']
    dict_subjects = []
    for nClust, clusterToProcess in enumerate(clusters):            
        IntersecIndex.append([])
        # For each image...
        for count, Patindx in enumerate(statisticalTests['Patient index']):      
            idxclster = IndexAndClass[Patindx]                   
            thisfolder = statisticalTests['TME -h'][count]+'/'
            if not os.path.exists(dataset.bioInsights_dir_TME_in_image+thisfolder):
                os.mkdir(dataset.bioInsights_dir_TME_in_image+thisfolder)            
            # One Phenotype or Tissue Community to one image
            for sts in statisticalTests['TME'][count]:
                if int(sts[2][0])==clusterToProcess: 
                    dict_subjects.append({'dataset':dataset,'thisfolder':thisfolder,'idxclster':idxclster,'patchIDX':patchIDX, 
                                        'clusters':clusters,'nClust':nClust,'sts':sts,'statisticalTests_PerPatient':statisticalTests_PerPatient,
                                        'statisticalTests':statisticalTests,'unrestrictedLoss':unrestrictedLoss,'count':count,'Patindx':Patindx})
    
    # select_patches_from_cohort
    result = parallel_process(dict_subjects,TME_location_in_image_,use_kwargs=True,front_num=1,desc='BioInsights: Save TOP-k PIRs for each TME') 
    return 1

def TissueArea_in_image_(dataset, thisfolder, subject,Area_conf):
    # Open Raw Image.
    im, imList = dataset.open_Raw_Image(subject,1)
    
    # Assign significant cluster as 1 to SuperPatch Image             
    if ('Endometrial_LowGrade' in dataset.raw_dir):
        for imList_n ,imList_i in enumerate(imList[::-1]):
            Patch_im_i = np.zeros(imList_i.shape[:2])                        
            # Create superPatch Label image using the Superpatch size. 
            division_rows = np.floor(Patch_im_i.shape[0]/dataset.patch_size)
            division_cols = np.floor(Patch_im_i.shape[1]/dataset.patch_size)
            lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for row_indx, row in enumerate(range(int(division_rows))):
                Patch_im_i[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
            Patch_im_i = Patch_im_i.astype(int) 
            if imList_n==0:
                Patch_im = Patch_im_i
            else:                
                Patch_im = np.concatenate((Patch_im, Patch_im_i+Patch_im.max()+1),1)
    elif ('Synthetic' in dataset.raw_dir):
        for imList_n ,imList_i in enumerate(imList[::-1]):
            Patch_im_i = np.zeros(imList_i.shape[:2])                        
            # Create superPatch Label image using the Superpatch size. 
            division_rows = np.floor(Patch_im_i.shape[0]/dataset.patch_size)
            division_cols = np.floor(Patch_im_i.shape[1]/dataset.patch_size)
            lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for row_indx, row in enumerate(range(int(division_rows))):
                Patch_im_i[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
            Patch_im_i = Patch_im_i.astype(int) 
            if imList_n==0:
                Patch_im = Patch_im_i
            else:                
                Patch_im = np.concatenate((Patch_im, Patch_im_i+Patch_im.max()+1),1)
    elif 'Endometrial_POLE' in dataset.root:
        Patch_im = np.zeros(im.shape[:2])                        
        # Create superPatch Label image using the Superpatch size. 
        division_rows = np.floor(Patch_im.shape[0]/dataset.patch_size)
        division_cols = np.floor(Patch_im.shape[1]/dataset.patch_size)
        lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
        lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
        for row_indx, row in enumerate(range(int(division_rows))):
            Patch_im[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
        # Patch_im = np.transpose(Patch_im)
        Patch_im = Patch_im.astype(int)
    else: 
        Patch_im = np.zeros(im.shape[:2])                        
        # Create superPatch Label image using the Superpatch size. 
        division_rows = np.floor(Patch_im.shape[0]/dataset.patch_size)
        division_cols = np.floor(Patch_im.shape[1]/dataset.patch_size)
        lins = np.repeat(list(range(int(division_cols))), dataset.patch_size)
        lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
        for row_indx, row in enumerate(range(int(division_rows))):
            Patch_im[row_indx*dataset.patch_size:(row_indx+1)*dataset.patch_size,:int(division_cols*dataset.patch_size)] = np.transpose(lins+int(row_indx*division_cols))
        # Patch_im = np.transpose(Patch_im)
        Patch_im = Patch_im.astype(int)
    
    # Superpatches of significant clusters.
    Area_conf_im = Area_conf[Patch_im] 
    Area_conf_im = Area_conf_im/Area_conf_im.max()
    # Save tissue area confidence
    imtosave = Image.fromarray(np.uint8(Area_conf_im*255))
    imtosave.save(dataset.bioInsights_dir_TME_in_image+thisfolder+'{}_conf{}_Label.tiff'.format(subject[0],round(Area_conf.max(),3)))                
    # Save image original.
    imwrite(dataset.bioInsights_dir_TME_in_image+thisfolder+'{}_conf{}_Images.tiff'.format(subject[0],round(Area_conf.max(),3)),np.moveaxis(im,2,0))                                        


def TissueArea_in_image(dataset,TissueArea_Conf,subjects,top_k):
    '''
        docstring
    '''   
    dict_subjects = []

    # choose highest confidence tissue areas.
    for n_ar, tissue_area in enumerate(TissueArea_Conf):
        thisfolder = 'A{}/'.format(str(n_ar+1))
        if not os.path.exists(dataset.bioInsights_dir_TME_in_image+thisfolder):
            os.mkdir(dataset.bioInsights_dir_TME_in_image+thisfolder)            

        max_conf_for_area = [t[0].max() for t in tissue_area] 
        hi_conf_subjcts = sorted(range(len(max_conf_for_area)), key=lambda i: max_conf_for_area[i])[:top_k]                    
        for hi_conf_s in hi_conf_subjcts:
            dict_subjects.append({'dataset':dataset, 'subject':subjects[hi_conf_s],'Area_conf':tissue_area[hi_conf_s]})                
                         
    # select_patches_from_cohort
    result = parallel_process(dict_subjects,TissueArea_in_image_,use_kwargs=True,front_num=1,desc='BioInsights: Save examples of tissue areas') 
    return 1

def All_TMEs_in_Image_(clusters,dataset,subject_info):
    
    # Crops,Confidence,and Phenotype Vector.    
    prev_cell_type_assignment=[]
        
    # Apply mask to patch
    for subgraph_idx in range(dataset.findLastIndex(subject_info[1])+1):                
        
        # Open Raw Image.        
        im, imList = dataset.open_Raw_Image(subject_info,1)                

        # Load image of patches
        Patch_im,Patch_IMS = load_patch_image(dataset,imList)                    
        
        # Load Patch Contrastive Learning Information
        PCL_reprsntions = np.load(dataset.raw_dir+'/{}.npy'.format(subject_info[0])) 

        for cell_type_idx, n_cell_types in enumerate(clusters):    
            # load cell_types_assignments
            prev_cell_type_assignment, cell_type_assignment = load_cell_types_assignments(
                                                                    dataset,cell_type_idx,subject_info,subgraph_idx,
                                                                    n_cell_types,prev_cell_type_assignment)                                    
            
            # Initialize labels
            Labels = np.zeros((im.shape[0],im.shape[1],n_cell_types),dtype=np.uint8)

            # For each cell type
            for cell_type in range(n_cell_types):
                
                # Create image with probabilities with the size of the original image
                aux = (cell_type_assignment[:Patch_im.max()+1,cell_type]*255).astype(np.uint8)                
                last_patch = 0
                aux_2 = []
                for im_i in Patch_IMS:
                    aux_2.append(np.reshape(aux[last_patch:last_patch+im_i.max()+1],(im_i.shape[1],im_i.shape[0])))                    
                    last_patch = last_patch+im_i.max()+1
                aux = np.concatenate(aux_2,1)                

                # Interpolate aux image to match size with the original one.
                Labels[:,:,cell_type] = cv2.resize(aux, (im.shape[1],im.shape[0]), 0, 0, interpolation = cv2.INTER_NEAREST)        

            # Save image of labels as a multitiff.
            if cell_type_idx==0:
                imwrite(dataset.bioInsights_dir_TME_in_image+'{}_Phenotypesss.tif'.format(subject_info[0]),np.moveaxis(Labels,2,0),photometric='minisblack')                
            elif cell_type_idx==1:
                imwrite(dataset.bioInsights_dir_TME_in_image+'{}_Neighborhoods.tif'.format(subject_info[0]), np.moveaxis(Labels,2,0), photometric='minisblack')        
            else:
                imwrite(dataset.bioInsights_dir_TME_in_image+'{}_Areas.tif'.format(subject_info[0]), np.moveaxis(Labels,2,0), photometric='minisblack')       

            # Save original image
            if dataset.args['Bio_save_Orig_im']:                
                imwrite(dataset.bioInsights_dir_TME_in_image+'{}.tif'.format(subject_info[0]), np.moveaxis(np.concatenate(imList,1),2,0), photometric='minisblack')  


        del im, imList, PCL_reprsntions, Patch_im
        gc.collect(0)
        gc.collect(1)
        gc.collect(2)


def All_TMEs_in_Image(dataset,clusters, IndexAndClass):
    # Apply mask to slide
    dict_subjects = []
    for count, subject_info in enumerate(IndexAndClass):
        dict_subjects.append({'clusters':clusters,'dataset':dataset,'subject_info':subject_info})
    
    result = parallel_process(dict_subjects,All_TMEs_in_Image_,use_kwargs=True,front_num=5,desc='BioInsights: Save TMEs for each patient') 
