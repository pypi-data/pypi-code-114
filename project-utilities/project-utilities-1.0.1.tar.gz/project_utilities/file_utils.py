import glob 
import os
import sys 

def find_files(directory:str, file:str, exit:bool()=False, recursive:bool()=True):

    error_message = "ERROR " + file + " not found !"
    files = []

    if recursive:

        files.append(glob.glob(os.path.join(directory, '**', file), recursive=recursive))

    else: 
        files.append(glob.glob(os.path.join(directory, file), recursive=recursive))

    if len(files) == 0:
        if exit:
            sys.exit(error_message)
        else: 
            return error_message
    
    if len(files) == 1: 
        return files[0]
    
    else: 
        return files

if __name__ == 'main':
    print(find_files("C:/Users/horga/project-utilities", "LICENSE"))
