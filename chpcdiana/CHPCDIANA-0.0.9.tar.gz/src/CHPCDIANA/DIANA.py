from click import pass_obj
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean as dis
from scipy.cluster.hierarchy import dendrogram, linkage


class DivisiveAnalysis:
    """
    Divisive Analysis Implements the DIANA (Divisive Analysis) algorithm and provides an interface for using the
    implementation.

    Parameters:
        no_clusters (int) : numbers of clusters.
    """

    def __init__(self, no_clusters):
        self.no_clusters = no_clusters
        self.labels = []
        self.clusters = [0]

    def initialize_to_zero(self, x):
        """
        :param x: dataframe
        :return: list of zeros which are the initial labels
        """
        return [0 for i in range(x.shape[0])]

    def cluster_list(self, x, c):
        """
        :param x: dataframe
        :param c: label
        :return: a list of points which have label 'c' and their respective index
        """
        # Given a dataframe, their respective labels and a single label
        # Returns a list of points which have label 'c' and their respective index
        l = []
        for i, p in enumerate(x):
            if self.labels[i] == c:
                l.append([p[k] for k in range(len(p))] + [i])
        return np.array(l)

    def cluster_diameter(self, x):
        """
        :param x: dataframe
        :return: the maximum distance between two points in it
        """

        distances = [0]  # Initialized with a zero for clusters of 1 point that won´t enter the loop below
        for i in range(x.shape[0]):
            for j in range(i + 1, x.shape[0]):
                distances.append(dis(x[i], x[j]))
        return max(distances)

    def largest_cluster(self, x):
        """
        :param x: dataframe
        :return: Returns the label of the biggest cluster (the one with the biggest diameter)
        """
        # Given a dataframe, its labels, and a list of unique labels contained in labels
        # Returns the label of the biggest cluster (the one with the biggest diameter)
        max_val = 0
        max_cluster = 0
        for c in self.clusters:
            diam = self.cluster_diameter(self.cluster_list(x, c))
            if diam > max_val:
                max_val = diam
                max_cluster = c
        return max_cluster

    def get_clusters(self):
        """
        :return: all the clusters.
        """
        return self.clusters

    def average_point(self, p, x):
        """
        :param p: point
        :param x: dataframe
        :return: Returns the mean distance between the point and each point in the dataframe
        """
        # Given a point and a dataframe
        # Returns the mean distance between the point and each point in the dataframe
        point_in_cluster = False

        sum_distances = 0
        for point in x:
            for i in range(len(p)):
                if point[i] == p[i]:
                    point_in_cluster = True
            sum_distances += dis(p, point)

        if point_in_cluster:
            if len(x) == 1:
                return 0
            else:
                return sum_distances / (len(x) - 1)  # we subtract 1 p is part of x
        else:
            return sum_distances / (len(x))

    def splinter(self, x_i):
        """
        :param x_i: Given a dataframe with (x,y,z...,i) where i is the index.
        :return: The index of the point in the dataframe which in average is furthest apart from the rest
        """
        # Given a dataframe with (x,y,z...,i) where i is the index
        # Returns the index of the point in the dataframe which in average is furthest apart from the rest
        splinter = 0
        max_avg = 0

        for point in x_i:
            The_average = self.average_point(point[:-1], x_i[:, :-1])
            if The_average > max_avg:
                max_avg = The_average
                splinter = point[len(point) - 1]
        return int(splinter)

    def a_splinter(self, p, father_dataframe, x):
        """
        :param p: point
        :param father_dataframe: the father dataframe
        :param x: the splinter dataframe
        :return: True if the point should be in the splinter dataframe using the average distance
        """
        # Given a point, the father dataframe and the splinter dataframe
        # Returns True if the point should be in the splinter dataframe using the average distance
        if self.average_point(p, x) < self.average_point(p, father_dataframe):
            return True
        else:
            return False

    def create_dendrogram(self, X):
        # Function to create the dendrogram using the linkage matrix and save it to a file.
        fig = plt.figure(figsize=(18, 8))
        plt.title("Dendrogram - Divisive Clustering")
        Z = linkage(X, 'ward')
        dendrogram(Z, orientation='top', labels=self.labels)
        fig.savefig('DIANA\dendrograms\dendrogram.png')
        plt.show()

    def fit(self, x):
        if x.shape[0] < self.no_clusters:
            import warnings
            warnings.warn("The number of clusters can't be larger than number of points in the dataframe")
            return None

        x = np.array(x)

        self.labels = self.initialize_to_zero(x)

        for z in range(self.no_clusters - 1):

            # Get the largest cluster
            majorClusterLabel = self.largest_cluster(x)
            majorClusterList = self.cluster_list(x, majorClusterLabel)

            # Get the splinter that makes your new cluster
            disi = self.splinter(majorClusterList)
            self.clusters.append(self.clusters[-1] + 1)
            self.labels[disi] = self.clusters[-1]
            newClusterList = self.cluster_list(x, self.clusters[-1])
            m = newClusterList.copy()
            M = majorClusterList.copy()

            # pass the points to the splinter cluster
            changed = True
            max_changes = x.shape[0] * 4
            changes = 0
            while changed == True and changes != max_changes:
                changed = False
                for i in range(len(majorClusterList)):
                    if self.labels[int(majorClusterList[i][-1])] == majorClusterLabel:
                        if self.a_splinter(majorClusterList[i][:-1], M[:, :-1], m[:, :-1]):
                            changed = True
                            self.labels[int(majorClusterList[i][-1])] = self.clusters[-1]
                            M = self.cluster_list(x, majorClusterLabel)
                            m = self.cluster_list(x, self.clusters[-1])
                    else:
                        if not self.a_splinter(majorClusterList[i][:-1], M[:, :-1], m[:, :-1]):
                            changed = True
                            self.labels[int(majorClusterList[i][-1])] = majorClusterLabel
                            M = self.cluster_list(x, majorClusterLabel)
                            m = self.cluster_list(x, self.clusters[-1])
                            changes += 1

        return (list(self.labels))


if __name__ == '__main__':
    pass
