import pandas as pd
import pandas_plink
import numpy as np
from pandas_plink import read_plink1_bin

genetic_data_path = "/ocean/projects/asc170022p/tighu/UKB_Genetic_Data/"


class genetic_data_handler:
    """
    A class to represent family of methods that can fetch pandas object based on subject id

    ...

    Attributes
    ----------
    number_of_subjects : int
        number of subjects to fetch genetic data for

    Methods
    -------
    get_genetic_data_batch(number_of_subjects,chromosome_number_list):
        get pandas object having genetic data corresponding to the specified chromosome for specified number of subjects

    """

    def __init__(self):


        self.location = np.ndarray
        self.chromosome= None

        genetic_df = read_plink1_bin(genetic_data_path + "bed_files/" + "ukb22418_c" + "1" + "_b0_v2.bed",
                                     genetic_data_path + "bim_files/" + "ukb_snp_chr" + "1" + "_v2.bim",
                                     genetic_data_path + "fam_files/" + "ukb22418_c" + "1" + "_b0_v2_s488176.fam",
                                     verbose=True)
        genetic_df = genetic_df.set_index({"variant": "snp"})
        self.subjects_list= genetic_df.sample.values




    def get_subject_ids(self):
        """
        A utility function which lets user fetch numpy array containing the list of all subject ids

        Parameters:
        No parameter required

        Returns:
        categories list: A numpy array object
        :rtype: np.ndarray
        """
        if self.subjects_list is None:
            print("Please initialize Module")
            return None

        else:
            return self.subjects_list

    def get_all_genetic_data_storage_location(self):
        """
        A utility function which lets user see all the genetic data locations

        Parameters:
        No parameter required

        Returns:
        categories list: A string
        :rtype: str
        """

        return genetic_data_path


    def get_genetic_locations(self):
        """
        A utility function which lets user fetch numpy array containing the locations of genetic data

        Parameters:
        No parameter required

        Returns:
        categories list: A numpy array object
        :rtype: np.ndarray
        """

        if self.location is None:
            print("Please initialize with a chromosome and read the binary data first")
            return None

        else:
            return self.location



    def set_chromosome_number(self,chr_num):

        self.chromosome=chr_num
        print("Genetic handler object initialized with chromosome")

    def get_binary_data(self,num_subjects= 10):
        genetic_data_output = []
        for chr_num in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]:

            genetic_df = read_plink1_bin(genetic_data_path + "bed_files/" + "ukb22418_c" + chr_num + "_b0_v2.bed",
                                         genetic_data_path + "bim_files/" + "ukb_snp_chr" + chr_num + "_v2.bim",
                                         genetic_data_path + "fam_files/" + "ukb22418_c" + chr_num + "_b0_v2_s488176.fam",verbose=True)
            genetic_df = genetic_df.set_index({"variant": "snp"})
            temp_output = temp_output=genetic_df.head(num_subjects)
            genetic_data_output.append(temp_output)

            del genetic_df
            del temp_output

        return genetic_data_output
