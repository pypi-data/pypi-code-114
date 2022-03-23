from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
class scree:
    def __init__(self):
        self.self = self
        
    def scree_plot(x):
        """X=indipendent Attributes (DF)
            """
        cover_matrix=PCA(n_components=len(x.columns))
        cover_matrix.fit(x)
        plt.ylabel("Engine values")
        plt.xlabel("#no of featutes")
        plt.title("PCA Engine values")
        plt.ylim(0,max(cover_matrix.explained_variance_))
        plt.axhline(y=1,color='g',linestyle='--')
        plt.plot(cover_matrix.explained_variance_,'ro-')
        plt.show()