#!/usr/bin/env python3
#
# GlobalChemExtensions - Partial SMILES
#
# --------------------------------------

# Imports
# -------

import partialsmiles as ps

class PartialSmilesValidation(object):

    __version__ = '0.0.1'


    def __init__(self,
                 partial=False
                 ):

        self.partial = partial

    def validate(self, smiles_list):

        '''

        Validate the SMILES

        Arguments:
            smiles_list (List): List of SMILES that the user would like to put

        Returns:
            successes (List): List of SMILES that worked
            failures (List): List of failed smiles that didn't work.

        '''

        successes = []
        failures = []

        for smiles in smiles_list:
            try:
                mol = ps.ParseSmiles(smiles, partial=self.partial)
                successes.append(smiles)
            except:
                failures.append(smiles)

        return successes, failures