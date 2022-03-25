import numpy as np
import pandas as pd
from typing import Optional, List, Dict
from scipy.optimize import linear_sum_assignment
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture


def feature_correspondence(
        feature_data: pd.DataFrame,
        sample_per_group: Dict[int, int],
        include_groups: Optional[List[int]],
        mz_tolerance: float,
        rt_tolerance: float,
        min_fraction: float,
        min_likelihood: float
):
    X = feature_data.loc[:, ["mz", "rt"]].to_numpy()
    # scale rt to use the same tolerance in both dimensions
    X[:, 1] *= mz_tolerance / rt_tolerance

    # min_samples estimation using the number of samples
    if include_groups is None:
        min_samples = round(sum(sample_per_group.values()) * min_fraction)
        include_groups = list(sample_per_group.keys())
    else:
        min_samples = _get_min_sample(
            sample_per_group, include_groups, min_fraction
        )
    # DBSCAN clustering
    max_size = 100000
    cluster = _make_initial_cluster(X, mz_tolerance, min_samples, max_size)
    feature_data["cluster_"] = cluster

    # estimate the number of chemical species per cluster
    features_per_cluster = _estimate_n_species(
        feature_data.loc[:, ["sample_", "cluster_", "group_"]],
        min_fraction,
        sample_per_group,
        include_groups,
    )


    # refine each cluster using GMMs: split clusters in a way such that there
    # is only one chemical species per cluster
    cluster_count = 0
    refined_cluster = -1 * np.ones(feature_data.shape[0], dtype=int)
    for name, group in feature_data.groupby("cluster_"):
        n_ft = features_per_cluster[name]
        if (n_ft > 0) and (name > -1):
            # refine clusters using GMMs
            refined_cluster[group.index] = _process_cluster() + cluster_count
            cluster_count += n_ft
    return features_per_cluster

def _get_min_sample(
    samples_per_group: Dict[int, int],
    include_groups: List[int],
    min_fraction: float
) -> int:
    min_sample = np.inf
    for k, v in samples_per_group.items():
        if k in include_groups:
            tmp = round(v * min_fraction)
            min_sample = min(tmp, min_sample)
    return min_sample


def _make_initial_cluster(
        X: np.ndarray,
        eps: float,
        min_samples: int,
        max_size: int
) -> np.ndarray:
    """
    First estimation of matched features using the DBSCAN algorithm.
    Data is split to reduce memory usage.

    Auxiliary function to feature_correspondence.

    Parameters
    ----------
    X : array
        m/z and rt values for each feature
    eps : float
        Used to build epsilon parameter of DBSCAN
    min_samples : int
        parameter to pass to DBSCAN
    max_size : int
        maximum number of rows in X. If the number of rows is greater than
        this value, the data is processed in chunks to reduce memory usage.
    Returns
    -------
    cluster : Series
        The assigned cluster by DBSCAN

    """
    n_rows = X.shape[0]

    if n_rows > max_size:
        # sort X based on the values of the columns and find positions to
        # split into smaller chunks of data.
        sorted_index = np.lexsort(tuple(X.T))
        revert_sort_ind = np.arange(X.shape[0])[sorted_index]
        X = X[sorted_index]

        # indices to split X based on max_size
        split_index = np.arange(max_size, n_rows, max_size)

        # find split indices candidates
        min_diff_x = np.min(np.diff(X.T), axis=0)
        split_candidates = np.where(min_diff_x > eps)[0]
        close_index = np.searchsorted(split_candidates, split_index)

        close_index[-1] = min(split_candidates.size - 1, close_index[-1])
        split_index = split_candidates[close_index] + 1
        split_index = np.hstack((0, split_index, n_rows))
    else:
        split_index = np.array([0, n_rows])

    # clusterize using DBSCAN on each chunk
    dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric="chebyshev")
    n_chunks = split_index.size - 1
    cluster = np.zeros(X.shape[0], dtype=int)
    cluster_counter = 0
    for k in range(n_chunks):
        start = split_index[k]
        end = split_index[k + 1]
        dbscan.fit(X[start:end, :])
        labels = dbscan.labels_
        n_cluster = (np.unique(labels) >= 0).sum()
        labels[labels >= 0] += cluster_counter
        cluster_counter += n_cluster
        cluster[start:end] = labels

    # revert sort on cluster and X
    if n_rows > max_size:
        cluster = cluster[revert_sort_ind]
    return cluster


def _estimate_n_species(
        df: pd.DataFrame,
        min_dr: float,
        sample_per_group: Dict[int, int],
        include_groups: Optional[List[int]]):

    # gets a dataframe with four columns: group, sample, cluster and number
    # of features in the cluster.
    n_ft_cluster = (
        df.groupby(["group_"])
        .value_counts()
        .reset_index()
    )

    # computes maximum number of species where the detection rate is greater
    # than min_dr
    n_species_per_cluster = (
        n_ft_cluster.groupby("group_")
        .apply(
            _get_n_species_per_group,
            min_dr,
            sample_per_group,
            include_groups
        )
    )
    if isinstance(n_species_per_cluster.index, pd.MultiIndex):
        # unstack MultiIndex into a DataFrame and get the highest value
        # estimation of the number of species for each cluster
        n_species_per_cluster = n_species_per_cluster.unstack(-1).max()
    elif isinstance(n_species_per_cluster, pd.DataFrame):
        # If multiple groups are used a DataFrame is obtained
        n_species_per_cluster = n_species_per_cluster.max()
    else:
        # DataFrame with only one row is converted to a Series
        n_species_per_cluster = n_species_per_cluster.iloc[0]

    n_species_per_cluster = n_species_per_cluster.astype(int).to_dict()
    return n_species_per_cluster


def _get_n_species_per_group(
        df: pd.DataFrame,
        min_dr: float,
        samples_per_group: Dict[int, int],
        include_groups: List[int]
) -> pd.DataFrame:
    if df.name in include_groups:
        n_samples = samples_per_group[df.name]
        res = (
            # pivot table where the values are the number of features
            # contributed by a sample
            df.pivot(index="sample_", columns="cluster_", values=0)
            .fillna(0)
            # count how many times a given number of features was obtained
            .apply(lambda x: x.value_counts())
            .div(n_samples)  # convert values to detection rates
            .fillna(0)
            .iloc[::-1]
            .cumsum()
            .iloc[::-1]
            # these three previous steps are a trick to pass detection rates
            # values from higher to lower values.
            .ge(min_dr)     # find values where above the min_dr
            .apply(lambda x: x.iloc[::-1].idxmax() if x.any() else 0)
            # get the maximum number of species above the min_dr
        )
    else:
        c = df.cluster_.unique()
        res = pd.Series(data=np.zeros(c.size), index=c)
    return res


def _process_cluster(df: pd.DataFrame, min_likelihood: float, n_species: int):
    """
    Process each cluster obtained from DBSCAN. Auxiliary function to
    `feature_correspondence`.

    Parameters
    ----------
    df : DataFrame
        feature_data values for a given cluster
    min_likelihood : float
    n_species: int
        Number of features in the cluster, estimated with
        `estimate_features_per_cluster`.

    Returns
    -------
    subcluster : Series
        The subcluster values.
    """

    X = df.loc[:, ["mz", "rt"]].to_numpy()
    # fit a Gaussian mixture model using the cluster data
    gmm = GaussianMixture(n_components=n_species, covariance_type="diag")
    labels = gmm.fit_predict(X)
    likelihood = gmm.score_samples(X)
    df["cluster"] = labels
    df.loc[likelihood < min_likelihood, "cluster"] = -1
    # ft_per_cluster =



def _make_gmm(ft_data: pd.DataFrame, n_feature: int, cluster_name: str):
    """
    fit a gaussian model and set subcluster names for each feature. Auxiliary
    function to process cluster.

    Parameters
    ----------
    ft_data : DataFrame
        The mz and rt columns of the cluster DataFrame
    n_feature : int
        Number of features estimated in the cluster.
    cluster_name: str

    Returns
    -------
    gmm : GaussianMixtureModel fitted with cluster data
    score: The log-likelihood of each feature.
    subcluster : pd.Series with subcluster labels.
    """
    gmm = GaussianMixture(n_components=n_feature, covariance_type="diag")
    gmm.fit(ft_data.loc[:, ["mz", "rt"]].values)
    # scores = pd.Series(data=gmm.score_samples(ft_data), index=ft_data.index)
    ft_data["score"] = gmm.score_samples(ft_data.loc[:, ["mz", "rt"]].values)

    # get index of features in the cases where the number of features is greater
    # than the number of components in the gmm
    noise_index = (ft_data
                   .groupby("sample")
                   .filter(lambda x: x.shape[0] > n_feature))

    if not noise_index.empty:
        noise_index = (noise_index
                       .groupby("sample")
                       .apply(lambda x: _noise_ind(x, n_feature))
                       .droplevel(0)
                       .index)
    else:
        noise_index = noise_index.index

    noise = pd.Series(data="-1", index=noise_index)

    # if the number of features is equal to the number of components in the
    # gmm, each feature is assigned to a cluster using the Hungarian algorithm
    # on the posterior probabilities on each component
    subcluster = (ft_data.loc[ft_data.index.difference(noise_index)]
                  .groupby("sample")
                  .filter(lambda x: x.shape[0] <= n_feature)
                  .groupby("sample")
                  .apply(lambda x: _get_best_cluster(x, gmm))
                  .droplevel(0)
                  .astype(str))
    subcluster = subcluster.apply(lambda x: str(cluster_name) + "-" + x)
    subcluster = pd.concat([noise, subcluster])
    subcluster = subcluster.sort_index()
    # TODO: add here the case where n_features < n_components

    # subcluster = pd.Series(data=gmm.predict(ft_data), index=ft_data.index,
    #                        dtype=str)
    scores = 1
    return gmm, scores, subcluster


def _noise_ind(x, n):
    """
    search the index of samples that are going to be considered as noise.
    Reduces the number of features from a sample in a cluster until the size is
    equal to n
    """
    ind = x["score"].sort_values().index[:(x.shape[0] - n)]
    return x.loc[ind, :]


def _get_best_cluster(x, gmm):
    """
    Assigns a feature to a cluster the posterior probability to each cluster.
    """
    proba = gmm.predict_proba(x.loc[:, ["mz", "rt"]].values)
    rows, cols = proba.shape
    if rows != cols:
        fill = np.zeros(shape=(cols - rows, cols))
        proba = np.vstack((proba, fill))
    _, best_cluster = linear_sum_assignment(proba)
    best_cluster = best_cluster[:rows]
    best_cluster = pd.Series(data=best_cluster, index=x.index)
    return best_cluster
