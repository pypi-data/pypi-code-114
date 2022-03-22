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


def voxel_size(mrcfile, rounding_precision=6):

    voxel_sizes = mrcfile.voxel_size.tolist()

    rounded_voxel_sizes = [round(v, rounding_precision) for v in voxel_sizes]

    if rounded_voxel_sizes[0] != rounded_voxel_sizes[1] or rounded_voxel_sizes[
            0] != rounded_voxel_sizes[2]:
        raise ValueError("Voxel-sizes cannot differ in different dimensions")

    if rounded_voxel_sizes[0] == 0:
        raise ValueError("Voxel-size cannot be zero")

    return rounded_voxel_sizes[0]


def histogram(density):
    hist, bin_edges = np.histogram(density, bins=200)

pass
