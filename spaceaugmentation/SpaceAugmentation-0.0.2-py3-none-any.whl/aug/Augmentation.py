import copy
import numpy as np
import random


class Augmentation():
    def __init__(self):
        pass


    def delta_S(self,embed_list, label_list,target = None, lambda_ = None):
        """
        Paper found here: https://arxiv.org/abs/1910.04176

        Sample a pair of sentences (Xi, Xj) from the target category.
        DELTAS applies deltas from the same target category.

        X_hat =( Xi − Xj ) + Xk
        Xi is sample 1, Xj is sample 2, Xk is sample 3

        if lambda_ is used then we use the lambda_ value times the delta
        X_hat =( Xi − Xj ) * λ + Xk

        :param embed_list: Pass in the embedding list
        :param label_list: Pass in the label list
        :param target:which target category to use
        :param lambda_: The lambda value to use
        :return:
        """
        # Checks
        self.list_exceptions(embed_list)
        self.list_exceptions(label_list)
        if target is None:
            return Exception("Target is not specified!")

        #Now we do the actual things
        cpy_embed_list = copy.copy(embed_list) #slightly redundant but should be too much of a problem
        cpy_label_list = copy.copy(label_list) #slightly redundant but should be too much of a problem
        #-------------------------------------


        # Find the target category
        target_list, target_categories = self.find_category(cpy_embed_list,cpy_label_list, target)


        #copy over the original data to the augmented sample list
        augmented_sample = cpy_embed_list.copy()
        augmented_sample_label = cpy_label_list.copy()

        if len(target_list) < 3:
            return Exception(" Extrapolation Not Possible. Target list is less than 3,")

        #print(f"Target list for {target} is of size {len(target_list)}, Size will increase by {len(target_list)*2}")

        for i in range(len(target_list)):

            X_i = target_list[i]

            X_j_idx = self.get_rand_index_from_list(target_list,i)
            X_j = target_list[X_j_idx]

            X_k_idx = self.get_rand_index_from_list(target_list,X_j_idx)
            X_k = target_list[X_k_idx]

            # X_hat =( X_i − X_j ) + X_k
            if lambda_ == None:

                X_hat = (X_i - X_j)  + X_k

            else:
                #X_hat =( Xi − Xj ) * λ + Xk
                X_hat = (X_i - X_j) * lambda_ + X_k

            augmented_sample.append(X_hat)
            augmented_sample_label.append(target)


        return augmented_sample, augmented_sample_label


    def get_rand_index_from_list(self,list_,no_idx):
        """
        Get a random index from the list
        That is not no_idx
        :param list:
        :param no_idx:
        :return: random index
        """
        while True:

            rand_idx = random.randint(0,len(list_)-1)

            if rand_idx == no_idx:

                continue
            else:

                break

        return rand_idx

    def find_category(self,list_, list_label, target):
        """
        Find the target category in the list
        :param list_: The list to search
        :param target: The target category to search for
        :return:
        """

        new_sample = []
        new_sample_label = []

        for i in range(len(list_)):
            if list_label[i] == target:
                new_sample.append(list_[i])
                new_sample_label.append(list_label[i])

        return new_sample, new_sample_label


    def add_noise(self, embed_list, label_list, noise_low= 0.0, nose_high= 0.1):
        """
        Add noise to the embedding
        :param embed_list: Pass in the embedding list
        :param label_list: Pass in the label list
        :param noise_low: The lower bound of the noise
        :param nose_high: The higher bound of the noise
        :return: extended list of embeddings and labels with added noise.
        :rtype: list, list
        """
        # Check if the list is empty
        self.list_exceptions(embed_list)
        self.list_exceptions(label_list)

        #Now we do the actual things
        cpy_embed_list = copy.copy(embed_list)
        cpy_label_list = copy.copy(label_list)
        noise =  np.random.uniform(noise_low, nose_high, size=(cpy_embed_list[0].shape[0],))

        augmented_samples = []
        augmented_labels = []

        for i in range(len(cpy_embed_list)):
            augmented_samples.append(cpy_embed_list[i])
            augmented_labels.append(cpy_label_list[i])

            sample = cpy_embed_list[i] + noise
            augmented_samples.append(sample)
            augmented_labels.append(cpy_label_list[i])

        return augmented_samples, augmented_labels

    def list_exceptions(self,list):
        if len(list) == 0:
            return Exception("List is empty")
        else:
            return None