"""
This module contains some convenience I/O functions for working with image and
diffraction data, particularly for constructing Point Of Normal Incidence
(.poni) files.
"""


def write_poni(
        path: str, pixel_size: float, detector_distance: float,
        beam_centre_x: int, beam_centre_y: int, wavelength: float) -> None:
    """
    Makes a Point Of Normal Incidence (.poni) file at path from the input
    arguments.

    Args:
        path:
            Path to where the .poni file should be saved.
        pixel_size:
            Size of each pixel, in metres.
        detector_distance:
            Distance from the sample to the detector, in metres.
        beam_centre_x:
            The pixel index of the beam centre along the fast axis.
        beam_centre_y:
            The pixel index of the beam centre along the slow axis.
        wavelength:
            The wavelength of the incident light, in metres.
    """
    if not path.endswith('.poni'):
        path += '.poni'

    with open(path, 'w+', encoding='utf-8') as f:
        lines = [
            "poni_version: 1\n",
            f"pixelsize1: {pixel_size}\n",
            f"pixelsize2: {pixel_size}\n",
            f"Distance: {detector_distance}\n",
            f"Poni1: {beam_centre_y*pixel_size}\n",
            f"Poni2: {beam_centre_x*pixel_size}\n",
            "Rot1: 0.0\n",
            "Rot2: 0.0\n",
            "Rot3: 0.0\n",
            f"Wavelength: {wavelength}\n"
        ]
        f.writelines(lines)
