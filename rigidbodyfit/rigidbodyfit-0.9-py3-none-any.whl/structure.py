import biopandas.pdb
import sklearn.cluster

import scipy.spatial.transform


def heavy_atom_dataframe(pdb):
    """Read structure from filename

    Args:
        filename (str): filename of pdb file to be read

    Returns:
        dataframe with all heavy atoms and without ions
    """

    # atom name may not contain : H, W, CL, CLA, NA, SOD, K
    excluded_atoms = 'H|W|CL|CLA|NA|SOD|K'
    rows_with_excluded_atoms = pdb.df['ATOM']['atom_name'].str.contains(
        excluded_atoms, na=False)

    return pdb.df['ATOM'][~rows_with_excluded_atoms]


def to_coordinates(atoms):

    return atoms[['x_coord', 'y_coord', 'z_coord']].to_numpy()


def reduce_coordinates(coordinates, n_points=1000):
    k_means = sklearn.cluster.MiniBatchKMeans(n_clusters=n_points)
    points = k_means.fit(coordinates)

    return k_means.cluster_centers_


def set_coordinates(atoms, coordinates):

    atoms['x_coord'] = coordinates.T[0]
    atoms['y_coord'] = coordinates.T[1]
    atoms['z_coord'] = coordinates.T[2]

    return atoms


pass
