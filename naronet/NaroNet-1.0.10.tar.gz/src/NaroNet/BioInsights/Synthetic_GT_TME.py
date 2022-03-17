import os 
import numpy as np
import copy
import matplotlib.pyplot as plt
import statistics as st

def ObtainMultivariateIntersectInSynthetic(dataset, statisticalTests, clusters, IndexAndClass, num_classes, attentionLayer,isTraining):
    # statisticalTest: List of columns with statistical difference. 1.p-value, 2.Cluster step, 3. column of the heatmap        
    stsTest=statisticalTests[0]
    IntersecIndex=[]
    for nClust, clusterToProcess in enumerate(clusters):      
        IntersecIndex.append([])
        if isTraining and (nClust==0 or nClust==2):
            continue           
           
        # Create directory for this set of images.        
        thisFolder = dataset.bioInsights_dir+'/InterpretabilityQuant/BlueIsCluster_GreenIsGroundTruth_ClusterLevel_{}'.format(clusters[nClust])
        if not os.path.exists(thisFolder):
            os.makedirs(thisFolder)

        # For each image.
        for count, subject_info in enumerate(IndexAndClass): 
            statisticalTest =  statisticalTests[count]
            
            # Apply mask to patch
            for patchIDX in range(dataset.findLastIndex(subject_info[1])+1):                       
                
                # Pixel-to-cluster Matrix
                clust0 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[0]))                 
                if nClust>0:
                    clust1 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[1]))                                    
                if nClust>1:
                    clust2 = np.load(dataset.processed_dir_cell_types+'cluster_assignment_Index_{}_ClustLvl_{}.npy'.format(subject_info[1], clusters[2]))                    
                    clust2 = np.matmul(clust1,clust2)
                clust = clust0 
                clust = clust1 if nClust==1 else clust
                clust = clust2 if nClust==2 else clust                
                
                # Load patch canvas
                Patch_im = np.zeros(np.load(dataset.root+'Raw_Data/Images/'+subject_info[0]+'.npy').shape[:2])

                # Create Patch Label image using the patch size.                         
                division = np.floor(Patch_im.shape[0]/dataset.patch_size)
                lins = np.repeat(list(range(int(division))), dataset.patch_size)
                lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
                for y_indx, y in enumerate(range(int(division))):
                    Patch_im[:int(division*dataset.patch_size),y_indx*dataset.patch_size:(y_indx+1)*dataset.patch_size] = lins+int(y_indx*division)
                Patch_im = Patch_im.astype(int)
                if ('V_H' in dataset.root) or ('V3' in dataset.root) or ('V4' in dataset.root) or ('V2' in dataset.root) or ('V1' in dataset.root):
                    Patch_im = np.transpose(Patch_im)

                #
                cell_type_top1 = np.apply_along_axis(np.argmax, axis=1, arr=clust)                        
                
                # Initialize values
                Thresholds=[0,50,75,95]
                bestintersection=[-1,-1]
                IntersecIndex[nClust].append(0)
                for threshold in Thresholds:
                    AllClusters = copy.deepcopy(cell_type_top1)*0
                    
                    # Iterate through all significant clusters from this ClusterLevel
                    if 'Synthetic' in dataset.root: 
                        if int(statisticalTest[2][0])==clust.shape[1]:
                            AllClusters += statisticalTest[2][1]==cell_type_top1
                            AllClusters[clust[:,statisticalTest[2][1]]<threshold/100]=0
                    Patch_im=AllClusters[Patch_im]

                    # Load Ground-Truth
                    if ('SyntheticV2' in dataset.root) or ('SyntheticV_H2' in dataset.root): # fenotipo 4 y 5 de la region 2
                        Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==2
                    elif ('SyntheticV1' in dataset.root) or ('SyntheticV_H1' in dataset.root): # fenotipo 6 de la region 3
                        Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
                    elif ('SyntheticV3' in dataset.root) or ('SyntheticV_H3' in dataset.root):
                        Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
                    elif ('SyntheticV4' in dataset.root) or ('SyntheticV_H4' in dataset.root):
                        Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')
                        Ground_Truth = np.logical_or(Ground_Truth==2,Ground_Truth==3)
                    
                    # Calculate Intersection Index
                    intersection = np.logical_and(Patch_im, Ground_Truth)                    
                    if intersection.sum():
                        result = intersection.sum() / (1e-16+float(Patch_im.sum()))
                        bestintersection.append(result)
                                                
                        # In case its the best threshold so far.
                        if result>max(bestintersection[:-1]):
                            IntersecIndex[nClust][count] = max(bestintersection)
                            # Save GT and Image
                            RGBImage = np.zeros((Ground_Truth.shape[0],Ground_Truth.shape[1],3))
                            RGBImage[:,:,1] = Ground_Truth
                            RGBImage[:,:,2] = Patch_im
                            if not isTraining:
                                plt.imsave(thisFolder+'/IntersectIdx{}_Slide{}_Patch{}.png'.format(intersection.sum()/float(Patch_im.sum()),subject_info[1],patchIDX), RGBImage) 

                    else:
                        bestintersection.append(0)
                        IntersecIndex[nClust][count] = max(bestintersection)
               
        # Save Statistics Information
        if len(IntersecIndex[-1])==0:
            IntersecIndex[-1]=[-1]
        result_int = np.array(IntersecIndex[-1])
        eval_info = {'Intersect-Index': str(sum(result_int[result_int>0])/len(result_int[result_int>0]))+'+-'+str(st.pstdev(result_int[result_int>0])), ' Stats':statisticalTest}

        # Save epoch information into a log file.
        fn = thisFolder+"/Statistics.txt"                            
        print(str(fn))
        with open(fn, "w") as myfile:
            myfile.write(str(eval_info)+"\n")

    # Save epoch information into a log file.
    Int_Index = np.array(IntersecIndex).max(0)
    eval_info = {'Intersect-Index': str(np.mean(Int_Index[Int_Index>0]))+'+-'+str(np.std(Int_Index[Int_Index>0])), ' Stats':statisticalTest}
    fn = dataset.bioInsights_dir+'InterpretabilityQuant/Interpretability_Acuracy.txt'                
    print(str(fn))
    with open(fn, "w") as myfile:
        myfile.write(str(eval_info)+"\n")

    return np.array(IntersecIndex)


def ObtainMultivariateIntersectInSynthetic_AllClusters(dataset, statisticalTests, clusters, IndexAndClass, num_classes, attentionLayer,isTraining):
    # statisticalTest: List of columns with statistical difference. 1.p-value, 2.Cluster step, 3. column of the heatmap        
    stsTest=statisticalTests[0]
    IntersecIndex=[]
    for nClust, clusterToProcess in enumerate(clusters):      
        IntersecIndex.append([])
        if isTraining and (nClust==0 or nClust==2):
            continue           
           
        # Create directory for this set of images.        
        thisFolder = dataset.bioInsights_dir+'/InterpretabilityQuant/BlueIsCluster_GreenIsGroundTruth_ClusterLevel_{}'.format(clusters[nClust])
        if not os.path.exists(thisFolder):
            os.makedirs(thisFolder)

        # For each image.
        for count, subject_info in enumerate(IndexAndClass): 
            statisticalTest =  statisticalTests[count]
            
            # Apply mask to patch
            for patchIDX in range(dataset.findLastIndex(subject_info[1])+1):                       
                
                # Pixel-to-cluster Matrix
                clust0 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[0]))                 
                if nClust>0:
                    clust1 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[1]))                                    
                if nClust>1:
                    clust2 = np.load(dataset.processed_dir_cell_types+'cluster_assignment_Index_{}_ClustLvl_{}.npy'.format(subject_info[1], clusters[2]))                    
                    clust2 = np.matmul(clust1,clust2)
                clust = clust0 
                clust = clust1 if nClust==1 else clust
                clust = clust2 if nClust==2 else clust                
                
                # Load patch canvas
                Patch_im = np.zeros(np.load(dataset.root+'Raw_Data/Images/'+subject_info[0]+'.npy').shape[:2])

                 # Load Ground-Truth
                if ('SyntheticV2' in dataset.root) or ('SyntheticV_H2' in dataset.root): # fenotipo 4 y 5 de la region 2
                    Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==2
                elif ('SyntheticV1' in dataset.root) or ('SyntheticV_H1' in dataset.root): # fenotipo 6 de la region 3
                    Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
                elif ('SyntheticV3' in dataset.root) or ('SyntheticV_H3' in dataset.root):
                    Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
                elif ('SyntheticV4' in dataset.root) or ('SyntheticV_H4' in dataset.root):
                    Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')
                    Ground_Truth = np.logical_or(Ground_Truth==2,Ground_Truth==3)

                # Create Patch Label image using the patch size.                         
                division = np.floor(Patch_im.shape[0]/dataset.patch_size)
                lins = np.repeat(list(range(int(division))), dataset.patch_size)
                lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
                for y_indx, y in enumerate(range(int(division))):
                    Patch_im[:int(division*dataset.patch_size),y_indx*dataset.patch_size:(y_indx+1)*dataset.patch_size] = lins+int(y_indx*division)
                Patch_im = Patch_im.astype(int)
                if ('V_H' in dataset.root) or ('V3' in dataset.root) or ('V4' in dataset.root) or ('V2' in dataset.root) or ('V1' in dataset.root):
                    Patch_im = np.transpose(Patch_im)

                #
                cell_type_top1 = np.apply_along_axis(np.argmax, axis=1, arr=clust)                        
                
                # Initialize values
                Thresholds=[0,75,95]
                bestintersection=[-1,-1]
                IntersecIndex[nClust].append(0)
                for cluster_idx in range(clusterToProcess):
                    for threshold in Thresholds:
                        AllClusters = copy.deepcopy(cell_type_top1)*0
                        
                        # Iterate through all significant clusters from this ClusterLevel
                        if 'Synthetic' in dataset.root:                         
                            AllClusters += cluster_idx==cell_type_top1
                            AllClusters[clust[:,cluster_idx]<threshold/100]=0
                        Patch_im=AllClusters[Patch_im]                       
                        
                        # Calculate Intersection Index
                        intersection = np.logical_and(Patch_im, Ground_Truth)                    
                        if intersection.sum():
                            result = intersection.sum() / (1e-16+float(Patch_im.sum()))
                            bestintersection.append(result)
                                                    
                            # In case its the best threshold so far.
                            if result>max(bestintersection[:-1]):
                                IntersecIndex[nClust][count] = max(bestintersection)
                                # Save GT and Image
                                RGBImage = np.zeros((Ground_Truth.shape[0],Ground_Truth.shape[1],3))
                                RGBImage[:,:,1] = Ground_Truth
                                RGBImage[:,:,2] = Patch_im
                                if not isTraining:
                                    plt.imsave(thisFolder+'/IntersectIdx{}_Slide{}_Patch{}.png'.format(result,subject_info[1],patchIDX), RGBImage) 

                        else:
                            bestintersection.append(0)
                            IntersecIndex[nClust][count] = max(bestintersection)
                
        # Save Statistics Information
        if len(IntersecIndex[-1])==0:
            IntersecIndex[-1]=[-1]
        result_int = np.array(IntersecIndex[-1])
        eval_info = {'Intersect-Index': str(sum(result_int[result_int>0])/len(result_int[result_int>0]))+'+-'+str(st.pstdev(result_int[result_int>0])), ' Stats':statisticalTest}

        # Save epoch information into a log file.
        fn = thisFolder+"/Statistics.txt"   
        print(str(fn))
        with open(fn, "w") as myfile:
            myfile.write(str(eval_info)+"\n")

    # Save epoch information into a log file.
    Int_Index = np.array(IntersecIndex).max(0)
    eval_info = {'Intersect-Index': str(np.mean(Int_Index[Int_Index>0]))+'+-'+str(np.std(Int_Index[Int_Index>0])), ' Stats':statisticalTest}
    fn = dataset.bioInsights_dir+'InterpretabilityQuant/Interpretability_Acuracy.txt'                
    print(str(fn))
    with open(fn, "w") as myfile:
        myfile.write(str(eval_info)+"\n")

    return np.array(IntersecIndex)


def InterpretabilityAccuracy_CohortWiseRelevantTME_PerPatch(dataset, MostRelevantTME, clusters, IndexAndClass, num_classes, attentionLayer,isTraining):
    # statisticalTest: List of columns with statistical difference. 1.p-value, 2.Cluster step, 3. column of the heatmap        
    IntersecIndex=[]

    # Interpretability metrics per patch
    Interp_Metrics = {'n_Patches':[], 'Correct_patches':[]}

    # N clusters, and cluster.
    RelTME = MostRelevantTME[4][0][1]
    if 'P' in RelTME:
        nClust = 0
    elif 'N' in RelTME:
        nClust = 1
    elif 'A' in RelTME:
        nClust = 2
    clusterToProcess = int(RelTME[1:])-1
            
    # Create directory for this set of images.        
    thisFolder = dataset.bioInsights_dir+'/InterpretabilityQuant/BlueIsCluster_GreenIsGroundTruth_ClusterLevel_{}'.format(clusters[0])
    if not os.path.exists(thisFolder):
        os.makedirs(thisFolder)

    # For each image.
    for count, subject_info in enumerate(IndexAndClass): 
        
        # Apply mask to patch
        for patchIDX in range(dataset.findLastIndex(subject_info[1])+1):                       
            
            # Pixel-to-cluster Matrix
            clust0 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[0]))                 
            if nClust>0:
                clust1 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[1]))                                    
            if nClust>1:
                clust2 = np.load(dataset.processed_dir_cell_types+'cluster_assignment_Index_{}_ClustLvl_{}.npy'.format(subject_info[1], clusters[2]))                    
                clust2 = np.matmul(clust1,clust2)
            clust = clust0 
            clust = clust1 if nClust==1 else clust
            clust = clust2 if nClust==2 else clust                
            
            # Load patch canvas
            Patch_im = np.zeros(np.load(dataset.root+'Raw_Data/Images/'+subject_info[0]+'.npy').shape[:2])

                # Load Ground-Truth
            if ('SyntheticV2' in dataset.root) or ('SyntheticV_H2' in dataset.root): # fenotipo 4 y 5 de la region 2
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==2
            elif ('SyntheticV1' in dataset.root) or ('SyntheticV_H1' in dataset.root): # fenotipo 6 de la region 3
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
            elif ('SyntheticV3' in dataset.root) or ('SyntheticV_H3' in dataset.root):
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
            elif ('SyntheticV4' in dataset.root) or ('SyntheticV_H4' in dataset.root):
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')
                Ground_Truth = np.logical_or(Ground_Truth==2,Ground_Truth==3)

            # Create Patch Label image using the patch size.                         
            division = np.floor(Patch_im.shape[0]/dataset.patch_size)
            lins = np.repeat(list(range(int(division))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for y_indx, y in enumerate(range(int(division))):
                Patch_im[:int(division*dataset.patch_size),y_indx*dataset.patch_size:(y_indx+1)*dataset.patch_size] = lins+int(y_indx*division)
            Patch_im = Patch_im.astype(int)
            if ('V_H' in dataset.root) or ('V3' in dataset.root) or ('V4' in dataset.root) or ('V2' in dataset.root) or ('V1' in dataset.root):
                Patch_im = np.transpose(Patch_im)

            #
            cell_type_top1 = np.apply_along_axis(np.argmax, axis=1, arr=clust)                        
            
            # Initialize values
            Thresholds=[0,25,75,95,96,97,98,99]
            bestintersection=[-1,-1]    
            Interp_Metrics['n_Patches'].append(0)        
            Interp_Metrics['Correct_patches'].append(0)        
            # for cluster_idx in range(clusterToProcess):
            for threshold in Thresholds:
                AllClusters = copy.deepcopy(cell_type_top1)*0
                Patch_im_Int = copy.deepcopy(Patch_im)

                # Iterate through all significant clusters from this ClusterLevel
                if 'Synthetic' in dataset.root:                         
                    AllClusters += clusterToProcess==cell_type_top1
                    AllClusters[clust[:,clusterToProcess]<threshold/100]=0
                Patch_im_Int=AllClusters[Patch_im_Int]                       
                
                # Calculate Intersection Index
                intersection = np.logical_and(Patch_im_Int, Ground_Truth)                    
                if intersection.sum():
                    result = intersection.sum() / (1e-16+float(Patch_im_Int.sum()))
                    bestintersection.append(result)
                                            
                    # In case its the best threshold so far.
                    if result>max(bestintersection[:-1]):
                        # Extract interpretability
                        Interp_Metrics['n_Patches'][-1]=Patch_im_Int.sum()
                        Interp_Metrics['Correct_patches'][-1]=intersection.sum()
                        # Save GT and Image
                        RGBImage = np.zeros((Ground_Truth.shape[0],Ground_Truth.shape[1],3))
                        RGBImage[:,:,1] = Ground_Truth
                        RGBImage[:,:,2] = Patch_im_Int
                        if not isTraining:
                            plt.imsave(thisFolder+'/IntersectIdx{}_Slide{}_Patch{}.png'.format(result,subject_info[1],patchIDX), RGBImage) 

                else:
                    bestintersection.append(0)
            
    # Save Statistics Information    
    print(['Num Patches: ',str(sum(Interp_Metrics['n_Patches'])+1)])
    result = sum(Interp_Metrics['Correct_patches'])/(sum(Interp_Metrics['n_Patches'])+1)
    eval_info = {'Intersect-Index': str(result), ' Stats':MostRelevantTME}

    # Save epoch information into a log file.
    fn = thisFolder+"/Statistics.txt"   
    print(str(fn))
    with open(fn, "w") as myfile:
        myfile.write(str(eval_info)+"\n")

    return result


def InterpretabilityAccuracy_ImageWiseRelevantTME_PerPatch(dataset, MostRelevantTME, clusters, IndexAndClass, num_classes, attentionLayer,isTraining):
    # statisticalTest: List of columns with statistical difference. 1.p-value, 2.Cluster step, 3. column of the heatmap        
    IntersecIndex=[]

    # Interpretability metrics per patch
    Interp_Metrics = {'n_Patches':[], 'Correct_patches':[]}
            
    # For each image.
    for count, subject_info in enumerate(IndexAndClass): 
        
        nClust = clusters.index(int(MostRelevantTME[count][2][0]))
        clusterToProcess = MostRelevantTME[count][2][1]
        # Create directory for this set of images.        
        thisFolder = dataset.bioInsights_dir+'/InterpretabilityQuant/BlueIsCluster_GreenIsGroundTruth_ClusterLevel_{}'.format(clusters[nClust])
        if not os.path.exists(thisFolder):
            os.makedirs(thisFolder)

        # Apply mask to patch
        for patchIDX in range(dataset.findLastIndex(subject_info[1])+1):                       
            
            # Pixel-to-cluster Matrix
            clust0 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[0]))                 
            if nClust>0:
                clust1 = np.load(dataset.processed_dir_cell_types+'cluster_assignmentPerPatch_Index_{}_{}_ClustLvl_{}.npy'.format(subject_info[1], patchIDX, clusters[1]))                                    
            if nClust>1:
                clust2 = np.load(dataset.processed_dir_cell_types+'cluster_assignment_Index_{}_ClustLvl_{}.npy'.format(subject_info[1], clusters[2]))                    
                clust2 = np.matmul(clust1,clust2)
            clust = clust0 
            clust = clust1 if nClust==1 else clust
            clust = clust2 if nClust==2 else clust                
            
            # Load patch canvas
            Patch_im = np.zeros(np.load(dataset.root+'Raw_Data/Images/'+subject_info[0]+'.npy').shape[:2])

                # Load Ground-Truth
            if ('SyntheticV2' in dataset.root) or ('SyntheticV_H2' in dataset.root): # fenotipo 4 y 5 de la region 2
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==2
            elif ('SyntheticV1' in dataset.root) or ('SyntheticV_H1' in dataset.root): # fenotipo 6 de la region 3
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
            elif ('SyntheticV3' in dataset.root) or ('SyntheticV_H3' in dataset.root):
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')==3
            elif ('SyntheticV4' in dataset.root) or ('SyntheticV_H4' in dataset.root):
                Ground_Truth = np.load(dataset.root+'Raw_Data/Experiment_Information/Synthetic_Ground_Truth/Ground_Truth_'+subject_info[0][6:]+'.npy')
                Ground_Truth = np.logical_or(Ground_Truth==2,Ground_Truth==3)

            # Create Patch Label image using the patch size.                         
            division = np.floor(Patch_im.shape[0]/dataset.patch_size)
            lins = np.repeat(list(range(int(division))), dataset.patch_size)
            lins = np.repeat(np.expand_dims(lins,axis=1), dataset.patch_size, axis=1)
            for y_indx, y in enumerate(range(int(division))):
                Patch_im[:int(division*dataset.patch_size),y_indx*dataset.patch_size:(y_indx+1)*dataset.patch_size] = lins+int(y_indx*division)
            Patch_im = Patch_im.astype(int)
            if ('V_H' in dataset.root) or ('V3' in dataset.root) or ('V4' in dataset.root) or ('V2' in dataset.root) or ('V1' in dataset.root):
                Patch_im = np.transpose(Patch_im)

            #
            cell_type_top1 = np.apply_along_axis(np.argmax, axis=1, arr=clust)                        
            
            # Initialize values
            Thresholds=[95,96,97,98,99]
            bestintersection=[-1,-1]    
            Interp_Metrics['n_Patches'].append(0)        
            Interp_Metrics['Correct_patches'].append(0)        
            # for cluster_idx in range(clusterToProcess):
            for threshold in Thresholds:
                AllClusters = copy.deepcopy(cell_type_top1)*0
                Patch_im_Int = copy.deepcopy(Patch_im)

                # Iterate through all significant clusters from this ClusterLevel
                if 'Synthetic' in dataset.root:                         
                    AllClusters += clusterToProcess==cell_type_top1
                    AllClusters[clust[:,clusterToProcess]<threshold/100]=0
                Patch_im_Int=AllClusters[Patch_im_Int]                       
                
                # Calculate Intersection Index
                intersection = np.logical_and(Patch_im_Int, Ground_Truth)                    
                if intersection.sum():
                    result = intersection.sum() / (1e-16+float(Patch_im_Int.sum()))
                    bestintersection.append(result)
                                            
                    # In case its the best threshold so far.
                    if result>max(bestintersection[:-1]):
                        # Extract interpretability
                        Interp_Metrics['n_Patches'][-1]=Patch_im_Int.sum()
                        Interp_Metrics['Correct_patches'][-1]=intersection.sum()
                        # Save GT and Image
                        RGBImage = np.zeros((Ground_Truth.shape[0],Ground_Truth.shape[1],3))
                        RGBImage[:,:,1] = Ground_Truth
                        RGBImage[:,:,2] = Patch_im_Int
                        if not isTraining:
                            plt.imsave(thisFolder+'/IntersectIdx{}_Slide{}_Patch{}.png'.format(result,subject_info[1],patchIDX), RGBImage) 

                else:
                    bestintersection.append(0)
        
    # Save Statistics Information    
    result = sum(Interp_Metrics['Correct_patches'])/(sum(Interp_Metrics['n_Patches'])+1)
    eval_info = {'Intersect-Index': str(result), ' Stats':MostRelevantTME}

    # Save epoch information into a log file.
    fn = thisFolder+"/Statistics.txt"   
    print(str(fn))
    with open(fn, "w") as myfile:
        myfile.write(str(eval_info)+"\n")

    return result