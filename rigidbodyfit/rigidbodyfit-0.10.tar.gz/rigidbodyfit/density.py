import mrcfile
import numpy as np

def read(densityfilename):
    density = mrcfile.open(densityfilename)
    return density


def origin_vector(density):

    origin = np.array(density.header.origin.tolist())

    if np.all(origin == 0):
        origin[0] = density.header.nxstart * density.voxel_size['x']
        origin[1] = density.header.nystart * density.voxel_size['y']
        origin[2] = density.header.nzstart * density.voxel_size['z']

    return origin

def histogram(density):
    hist, bin_edges = np.histogram(density, bins=200)

pass
