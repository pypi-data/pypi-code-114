
from scipy.spatial.distance import squareform, pdist
import numpy as np
import pandas as pd



def distance_matrix(df, metric='euclidean'):
    dist_m = pd.DataFrame(squareform(pdist(df.iloc[:, :-1],metric)))
    diam = dist_m.max().max()
    dist_m['mean'] = dist_m.mean(axis=1)
    max_dist_avr = dist_m['mean'].max()
    return dist_m, max_dist_avr , diam


def fill_group(parent,splinter,metric='euclidean'):
    i = 0 
    while ( i < len(parent)):
    
      splinter = splinter.append(parent.loc[parent.index == i])
      splinter = splinter.reset_index(drop=True)

      s_m , s_max_av , s_d = distance_matrix(splinter,metric)
      p_m , p_max_av ,p_d = distance_matrix(parent,metric)
      d1 = p_m['mean'][i]
      d2 = s_m['mean'].iloc[-1]
      if (d1 >= d2):
        parent = parent.drop(i)
        parent = parent.reset_index(drop=True)
        i -= 1
      else:
        splinter = splinter.drop(splinter.index[len(splinter)-1])
        splinter = splinter.reset_index(drop=True)
      i += 1
    return parent , splinter


def splinter_df(data,metric='euclidean'):
    m , max_av,diam = distance_matrix(data,metric)
    index = m.loc[m['mean'] ==  max_av].index[0]
    new_group = m.loc[m['mean'] ==  max_av]
    splinter = data.loc[data.index == index]
    data = data.drop(index)
    data = data.reset_index(drop=True)
    splinter = splinter.reset_index(drop=True)
    return data, splinter

class Diana:
  def __init__(self,DataFrame, n_cluster= 2,metric = 'euclidean'):
      self.DataFrame = DataFrame
      self.distance_matrix = (distance_matrix(DataFrame,metric)[0]).iloc[:,:-1] 
      DataFrame['idx'] = DataFrame.index 
      self.n_cluster = n_cluster
      self.clusters = {'0': [DataFrame]}
      self.clusters_idx = []
      self.metric = metric
      self.labels = [i for i in range(n_cluster)]

  
  def fit(self):

    while(int(list(self.clusters.keys())[0]) < (self.n_cluster - 1) and int(list(self.clusters.keys())[0]) < len(self.DataFrame)):

      max_diam = -np.inf
      max_diam_idx = -np.inf
      dfs = list(self.clusters.values())[0]

      for idx,df in enumerate(dfs):
        dist_info = distance_matrix(df,self.metric)
        if (dist_info[2] > max_diam):
          max_diam = dist_info[2]
          max_diam_idx = idx

      data , splinter = splinter_df(dfs[max_diam_idx],self.metric)
      data , splinter = fill_group(data,splinter,self.metric)
      del dfs[max_diam_idx]
      dfs.append(data)
      dfs.append(splinter)
      self.clusters[str(int(list(self.clusters.keys())[0]) + 1)] = dfs
      del self.clusters[str(list(self.clusters.keys())[0])]


    dfs = list(self.clusters.values())[0]
    for idx,df in enumerate(dfs):
      self.clusters_idx.append(df['idx'].tolist())


  def predict(self,arr):
    predictions = []
    for idx in arr:
      for c_idx , cluster in enumerate(self.clusters_idx):
        if idx in cluster:
          predictions.append(c_idx)
    return predictions

  def get_clusters_diam(self):
    dfs = list(self.clusters.values())[0]
    diameters  = []
    for df in dfs:
      dist_m = pd.DataFrame(squareform(pdist(df.iloc[:, :-1],self.metric)))
      diam = dist_m.max().max()
      diameters.append(diam)
    return diameters
