from typing import List

import os
import shutil
import logging




__all__ = ['remove', 'new_file_name', 'rename_if_exists']

class Char(str):
    """ Single character. """
class FilePath(str):
    """ An absolute or a relative path to a file system resource. """
class FileName(str):
    """ Full file name of a file in a directory. """



def remove(root_dir: FilePath, separator: Char='_') -> None:
    """
    Function for removing all subdirectories of the root_dir. All files located
    in the subdirectories of the root_dir are moved to the root_dir. The files
    are renamed according to the relative path from the root_dir to given file.
    The '\\\\' and '/' in the relative path are replaced by the separator char.
    
    E.g.:
        'root_dir/dir1/dir2/current_dir/file.ext'
        
        old_file_name => file.ext
        
        relative_path => dir1/dir2/current_dir
        
        new_file_name => dir1_dir2_current_dir_file.ext
        
    Parameters
    -------------------------------------------------------------------------
        root_dir : FilePath
            path to the root directory
        separator : Char
            character that will be placed into the new file name instead of '\\\\' and '/'
            
    Returns
    -------------------------------------------------------------------------
        None
    """   
    if not os.path.exists(root_dir):
        raise ValueError("Invalid path to directory.")
    
    # First directory returned by os.walk() is the root_dir
    # => Get immediate subdirs for deletion via shutil.rmtree()
    dirtree_iter = os.walk(root_dir)
    _, subdirs, _ = next(dirtree_iter, None)
    
    for current_dir, _, files in dirtree_iter:
        
        for file_name in files:
            
            source_file_path = os.path.join(current_dir, file_name)
            target_file_path = new_file_name(file_name, current_dir, root_dir, separator)
            
            shutil.move(source_file_path, target_file_path)
            
            logging.debug(f'New name is "{target_file_path}".')

    for dir_name in subdirs:
        shutil.rmtree(os.path.join(root_dir, dir_name))
    
    
def new_file_name(file_name: FileName, current_dir: FilePath, root_dir: FilePath, separator: Char='_'):
    """
    Function returns new file name for a file located in one of the subdirectories
    of the root_dir. The new file name consists of 'prefix' + file_name, where 
    prefix is the relative path between root_dir and current_dir with all
    backslashes and forwardslashes replaced by the separator character.
    
    E.g.:
        'root_dir/dir1/dir2/current_dir/file.ext'
        
        old_file_name => file.ext
        
        relative_path => dir1/dir2/current_dir
        
        new_file_name => dir1_dir2_current_dir_file.ext

    Parameters
    -------------------------------------------------------------------------
        file_name : FileName
            name of the file
        current_dir : FilePath
            path to the current subdirectory
        root_dir : FilePath
            path to the root directory
        separator : Char
            character that will be placed into the new file name instead of '\\\\' and '/'
            
    Returns
    -------------------------------------------------------------------------
        new_file_name with the relative path from root_dir to current_dir as prefix to the input file_name
    """   
    new_file_name = os.path.join(os.path.relpath(current_dir, start=root_dir), file_name)
    new_file_name = _replace_chars(new_file_name, ['\\', '/'], separator)    
    new_file_name = rename_if_exists(os.path.join(root_dir, new_file_name))
    
    return new_file_name

        
def rename_if_exists(target_file_path: FilePath) -> FilePath:
    """
    Function returns a new file path that does not already exist.
    If the target_file_path does not exist then it is unchanged.
    If the target_file_path already exists then the returned file path is
    such that there are no naming conflicts.
    
    E.g.:
    'target/file/path.ext'
    => 'target/file/path' + ' (i)' + .ext'
    => 'target/file/path (i).ext'
    
    Parameters
    -------------------------------------------------------------------------
        target_file_path : FilePath
            path to a new file location
            
    Returns
    -------------------------------------------------------------------------
        potentially a new file path that doesn't already exist
    """   
    if os.path.exists(target_file_path):
        
        # Split off extension from target_file_path and add index (i) to distinguish the file        
        i = 1
        new_file_path = '{1} ({0}){2}'.format(i, *os.path.splitext(target_file_path))
        
        while os.path.exists(new_file_path):
            i += 1
            new_file_path = '{1} ({0}){2}'.format(i, *os.path.splitext(target_file_path))
        
        return new_file_path
                       
    else:
        return target_file_path    
        
        
def _replace_chars(string: str, char_list: List[Char], replacement: Char='_') -> str:
    """
    Function replaces every occurence of characters from char_list in input
    string with the replacement character.
    
    Parameters
    -------------------------------------------------------------------------
        string : str
            input string
        char_list : List[Char]
            list of characters that will be replaced in the input string
        replacement : Char
            character that will replace each occurence of characters from char_list
            
    Returns
    -------------------------------------------------------------------------
        copy of the input string with replaced characters
        
    Raises
    -------------------------------------------------------------------------
        ValueError
            if the char_list is an empty list
        TypeError
            if the input string or characters in char_list are not type of str
    """   
    if not char_list:
        raise ValueError('Argument char_list is an empty list.')
    
    new_string = string
    
    try:
        if _string_contains(string, char_list):
            for ch in char_list:
                new_string = new_string.replace(ch, replacement)
                
    except TypeError as e:
        raise e

    return new_string


def _string_contains(string: str, char_list: List[Char]) -> bool:     
    """ 
    Function checks if the input string contains any characters from char_list.
    
    Parameters
    -------------------------------------------------------------------------
        string : str
            input string
        char_list : List[Char]
            list of characters
            
    Returns
    -------------------------------------------------------------------------
        True if input string contains any characters from char_list, False otherwise
        
    Raises
    -------------------------------------------------------------------------
        TypeError
            if the input string or characters in char_list are not type of str 
    """
    if not isinstance(string, str):
        raise TypeError('String argument is not of type str.')
    
    if not char_list:
        return True
    
    if any([not isinstance(ch, str) for ch in char_list]):
        raise TypeError(('All elements of char_list must be of type str.'))
    
    return any([ch in string for ch in char_list])
