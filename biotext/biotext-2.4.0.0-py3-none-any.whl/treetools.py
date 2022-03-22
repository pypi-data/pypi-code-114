from skbio import DistanceMatrix
from skbio.tree import nj
import skbio
from scipy.spatial.distance import pdist
from scipy.cluster import hierarchy
import re

def mat2tree(vect, ids, method='complete'):
    dist = pdist(vect, metric='euclidean')
    if method == 'complete':
        Z = hierarchy.linkage(dist,method='complete')
        tree=skbio.tree.TreeNode.from_linkage_matrix(Z,ids)
        tree = tree.__str__()
    elif method == 'nj':
        ids = [re.sub('\'','\'\'',i) for i in ids]
        ids = [("'%s'"%i) for i in ids]
        dm = DistanceMatrix(dist, ids)
        tree = nj(dm,result_constructor=str)
    return tree
vect2tree=mat2tree