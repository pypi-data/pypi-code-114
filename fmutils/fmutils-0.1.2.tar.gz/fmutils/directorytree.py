# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:23:37 2022

@author: talha

Adopted from : https://realpython.com/directory-tree-generator-python/#step-5-saving-the-directory-tree-diagram-to-a-file
"""
import os
import pathlib
import sys

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTree:
    '''
        Parameters
        ----------
        root_dir : absolute/relative path to root directory containing all files.
        dir_only : TYPE, optional
            wether to only show sub-dirs in the dir-tree. The default is False.
        write_tree : TYPE, optional
            write the full dir-tree in a txt file in current working dir. The default is True.
            
        Returns
        -------
        None.
        
        '''
    def __init__(self, root_dir, dir_only=False, write_tree = True):
        self._generator = _TreeGenerator(root_dir, dir_only)
        self.write_tree = write_tree
    def generate(self):
        tree = self._generator.build_tree()
        if self.write_tree:
            file = os.getcwd()+'/dir_tree.txt'
            with open(file, 'w', encoding="utf-8") as f:
                for entry in tree:
                    f.write("%s\n" % entry)
            f.close()
            print(f'directory tree file saved at \n {file}')
        if not self.write_tree:
            for entry in tree:
                print(entry)
        return


class _TreeGenerator:
    def __init__(self, root_dir, dir_only=False):
        self._root_dir = pathlib.Path(root_dir)
        self._dir_only = dir_only
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = self._prepare_entries(directory)
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir():
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            else:
                self._add_file(entry, prefix, connector)

    def _prepare_entries(self, directory):
        entries = directory.iterdir()
        if self._dir_only:
            entries = [entry for entry in entries if entry.is_dir()]
            return entries
        entries = sorted(entries, key=lambda entry: entry.is_file())
        return entries

    def _add_directory(
        self, directory, index, entries_count, prefix, connector
    ):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(
            directory=directory,
            prefix=prefix,
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")