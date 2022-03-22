""" Run the command line interface """
import logging
import sys

import biopandas.pdb

import importlib.metadata

import matplotlib.pyplot as plt

import numpy as np

import scipy.interpolate
import scipy.optimize
import scipy.spatial.transform
import scipy.stats.qmc

import rich.console
import rich.logging
import rich.progress

import rigidbodyfit.arguments
import rigidbodyfit.structure
import rigidbodyfit.density


def create_rich_logger():
    FORMAT = "%(message)s"
    logging.basicConfig(level="INFO",
                        format=FORMAT,
                        datefmt="[%X]",
                        handlers=[rich.logging.RichHandler()])
    return logging.getLogger("rich")


class ShiftAndOrientation:
    def __init__(self, combined_vector):
        self.shift = combined_vector[:3]
        self.orientation = combined_vector[3:]


class Transformator:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.coordinates_center = np.average(self.coordinates, axis=0)

    def apply(self, shift, quaternion):
        rotation = scipy.spatial.transform.Rotation.from_quat(quaternion)
        return rotation.apply(self.coordinates - self.coordinates_center
                              ) + self.coordinates_center + shift

    def apply_to_other(self, shift, quaternion, other_coordinates):
        rotation = scipy.spatial.transform.Rotation.from_quat(quaternion)
        return rotation.apply(other_coordinates - self.coordinates_center
                              ) + self.coordinates_center + shift


def gridpoints(voxel_size, extend, density_origin):
    return (voxel_size * np.arange(extend[0]) + density_origin[0],
            voxel_size * np.arange(extend[1]) + density_origin[1],
            voxel_size * np.arange(extend[2]) + density_origin[2])


class OverlapOptimiser:
    def __init__(self, gridpoints, voxels, coordinate_transformator):
        self.coordinate_transformator = coordinate_transformator
        self.interpolator = scipy.interpolate.RegularGridInterpolator(
            gridpoints, voxels, bounds_error=False, fill_value=0.)

    # def calculate_with_shift(self, shift):

    #     return -np.log(np.average(self.interpolator(self.mobile + shift)))

    def calculate_with_shift_and_rotation(self, shift_rotation):
        """Evaluate point cloud overlap applying shift and rotation

        Args:
            shift_rotation : combined shift and quaternion array, first three
                             entries shift, other four quaternion

        Returns:
            pointcloud overlap
        """

        shift_and_orientation = ShiftAndOrientation(shift_rotation)

        mobile_rotated_shifted = self.coordinate_transformator.apply(
            shift_and_orientation.shift, shift_and_orientation.orientation)

        return -np.average(self.interpolator(mobile_rotated_shifted))


def initialValues(origin, extend, numberOfElements):

    lower_bound_orientation = [-1, -1, -1, 0]
    lower_bound = np.hstack([origin, lower_bound_orientation])

    upper_bound_orientation = [1, 1, 1, 1]
    upper_bound = np.hstack([origin + extend, upper_bound_orientation])

    sampler = scipy.stats.qmc.Sobol(d=len(lower_bound), scramble=False)

    for _ in range(numberOfElements):
        yield scipy.stats.qmc.scale(sampler.random(), lower_bound,
                                    upper_bound)[0]


def run():
    """ run the command line interface """

    # set up the console for printing
    console = rich.console.Console()

    # derive the program version via git
    try:
        version = importlib.metadata.version("rigidbodyfit")
    except importlib.metadata.PackageNotFoundError:
        version = "Unknown"

    command_line_arguments = (
        rigidbodyfit.arguments.get_command_line_arguments(version))

    # read density data and determine voxel size and shift vector from it

    log = create_rich_logger()

    log.info("Reading density ...")

    density = rigidbodyfit.density.read(command_line_arguments.density)
    voxel_size = rigidbodyfit.density.voxel_size(density)
    density_origin_vector = rigidbodyfit.density.origin_vector(density)
    voxels = np.copy(density.data.T)
    voxels[voxels < command_line_arguments.threshold * np.max(voxels)] = 0
    density_grid = gridpoints(voxel_size, voxels.shape, density_origin_vector)
    density_extend = np.array(density.voxel_size.tolist()) * voxels.shape

    log.info("done")

    log.info("Reading structure file ...")

    full_structure = biopandas.pdb.PandasPdb().read_pdb(
        command_line_arguments.structure)
    heavy_atoms = rigidbodyfit.structure.heavy_atom_dataframe(full_structure)
    coordinates = rigidbodyfit.structure.to_coordinates(heavy_atoms)
    log.info(f"Selected {coordinates.size // 3} atoms for fitting.")

    log.info("done")

    log.info("Optimising shift and rotatation ...")

    mobile_coordinates = Transformator(coordinates)
    overlap = OverlapOptimiser(voxels=voxels,
                               coordinate_transformator=mobile_coordinates,
                               gridpoints=density_grid)

    unit_quaternion_constraint = scipy.optimize.NonlinearConstraint(
        lambda x: np.dot(x[3:], x[3:]), 1, 1)
    number_initial_configurations = pow(2,
                                        command_line_arguments.sampling_depth)

    center_structure_density_origin = density_origin_vector - np.average(
        coordinates, axis=0)

    bestResult = 0
    for initial_shift_rotation in rich.progress.track(
            initialValues(center_structure_density_origin, density_extend,
                          number_initial_configurations),
            f"Optimising {number_initial_configurations} initial configurations",
            total=number_initial_configurations):
        result = scipy.optimize.minimize(
            overlap.calculate_with_shift_and_rotation,
            initial_shift_rotation,
            constraints=unit_quaternion_constraint)

        if result.fun < bestResult:
            bestResult = result.fun
            log.info(
                f"Best average voxel value at structure coordintates : {-bestResult:.4f} ."
            )
            bestFit = ShiftAndOrientation(result.x)

    all_coordinates = rigidbodyfit.structure.to_coordinates(
        full_structure.df['ATOM'])

    full_structure.df['ATOM'] = rigidbodyfit.structure.set_coordinates(
        full_structure.df['ATOM'],
        mobile_coordinates.apply_to_other(bestFit.shift, bestFit.orientation,
                                          all_coordinates))

    # use input structure as template for output
    full_structure.to_pdb(command_line_arguments.output_structure)

    log.info(f"Best shift       : {bestFit.shift} ")
    log.info(f"Best orientation : {bestFit.orientation} ")
