# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 18:36:54 2022

@author: talha

directories, files & paths management utilities. 'dfpu'
"""
import re, os, glob, shutil
import numpy as np
from tqdm import tqdm, trange
from utils.directorytree import DirectoryTree

numbers = re.compile(r'(\d+)')


def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def get_all_files(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    sort : wether to sort the output lost in Alphabetical order.
    
    Returns
    -------
    file_list : list containing full paths of all files.
    
    '''

    file_list = []
    for root, dirs, files in os.walk(main_dir):
        for file in files:
            file_list.append(os.path.join(root, file))
    if sort:
        file_list = sorted(file_list, key=numericalSort)

    return file_list


def get_all_dirs(main_dir, sort=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    sort : wether to sort the output lost in Alphabetical order. 
    
    Returns
    -------
    dir_list : list containing full paths of all sub directories in root.
    
    '''

    dir_list = []
    for root, dirs, files in os.walk(main_dir):
        for dr in dirs:
            dir_list.append(os.path.join(root, dr))
    if sort:
        dir_list = sorted(dir_list, key=numericalSort)

    return dir_list


def get_num_of_files(main_dir):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    
    Returns
    -------
    num_per_class : an array containing number of file in all sub dirs of root.
    name_classes : name of all the sub-dirs/classes inside the root.
    total_files : total number of files in all the sub-dir/classes.
    
    '''
    
    file_count = []
    for root, dirs, files in os.walk(main_dir):
        file_count.append((os.path.basename(os.path.normpath(root)), len(files)))
        
    file_count = file_count[1:]
    
    name_classes = np.asarray(file_count)[:,0].astype(str)
    num_per_class = np.asarray(file_count)[:,1].astype(int)
    
    total_files = sum(num_per_class)
    
    return num_per_class, name_classes, total_files


def get_basename(full_path, include_extension=True):
    '''
    Parameters
    ----------
    full_path : absolute/relative path of file or dir.
    include_extension : if the input full_path leads to file the by default the
                        the file's extension in included in output string.
                        
    Returns
    -------
    name : name of the file with/without extension or the base dir
    
    '''
    
    name = os.path.basename(os.path.normpath(full_path))
    if include_extension== False:
        name = name.split('.')[0]
    return name


def get_random_files(main_dir, count=1):
    '''
    Parameters
    ----------
    main_dir :  absolute/relative path to root directory containing all files.
    count : TYPE, optional
        the number of files to get from the root dir. The default is 1.
        
    Returns
    -------
    file_path : absolute path to the file/files.
    
    '''
    
    file_list = get_all_files(main_dir, sort=True)
    file_path = np.random.choice(file_list, size=count, replace=False)
    
    return file_path


def del_all_files(main_dir, confirmation=True):
    '''
    Parameters
    ----------
    main_dir : absolute/relative path to root directory containing all files.
    confirmation : TYPE, optional
        confirm before deleting the files. The default is True.
        
    Returns
    -------
    None.
    
    '''
    
    file_list = get_all_files(main_dir, sort=True)
    if confirmation:
        ans = input(f'do you wnat to continue deleting {len(file_list)} files? [yes[y]/no[n]] \n')
    else:
        ans = 'y'
    if ans == 'y':
        for i in file_list:
            os.remove(i)
        n = len(file_list)
        print(f'{n} files deleted.')
    else:
        print('Operation stopped.')
    return

