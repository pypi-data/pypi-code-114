"""
Stores the Image class, and its subclasses.
"""

from typing import List, Tuple

import numpy as np
import pywt
from scipy.ndimage import uniform_filter, gaussian_filter
from sklearn.cluster import DBSCAN

from .cluster import Cluster


def _wavelet_freqs_below_length_scale(length_scale: int, wavelet_type: str):
    """
    Calculates the number of wavelet frequency scales that exist below the
    given length scale.
    """
    if wavelet_type != "sym4":
        raise NotImplementedError(
            "The only implemented wavelet choice is 'sym4'. If you would " +
            "like a different wavelet type, please raise an issue on the " +
            "local_stats github page.")
    # Wavelet length scales increase by powers of 2.
    return np.floor(np.log2(length_scale))


class Image:
    """
    The base class for all images.

    Attrs:
        image_array:
            Numpy array representing the image.
    """

    def __init__(self, image_array: np.ndarray) -> None:
        self.image_array = image_array

    def subtract_background(self, background_array: np.ndarray,
                            zero_clip=True) -> None:
        """
        Carried out a simple background subtraction on self.image_array. If
        zero_clip is true, then any pixels in image_array that are decreased
        below zero by the background subtraction will be clipped to zero. This
        is particularly useful if there's a hot pixel in your background array.

        Args:
            background_array:
                A numpy array representing the background to be subtracted.
            zero_clip:
                Boolean determining if the background subtracted image_array
                should be clipped at 0.
        """
        self.image_array -= background_array
        if zero_clip:
            self.image_array = np.clip(self.image_array, 0, np.inf)

    def wavelet_denoise(self,
                        signal_length_scale: 20,
                        cutoff_factor: float = 0.2,
                        max_cutoff_factor: float = 0.8,
                        wavelet_choice: str = "sym4") -> None:
        """
        Runs some wavelet denoising on the image. Without arguments, will run
        default denoising.

        Args:
            signal_length_scale:
                We would like to preferentially rotate our image away from
                wavelets whose length-scales are decently smaller than our
                signal length scale. This is the most important parameter for
                decimating noise wavelets. A value of 20 will kill most typical
                noise wavelets, but if your signal length scale is significantly
                larger than 20 pixels then it may be productive to increase this
                number.
            cutoff_factor:
                If any wavelet coefficient is less than cutoff_factor*(maximum
                wavelet coefficient), then set it to zero. The idea is that
                small coefficients are required to represent noise; meaningful
                data, as long as it is large compared to background, will
                require large coefficients to be constructed in the wavelet
                representation.
            max_cutoff_factor:
                The cutoff factor to be applied to signal occuring on length
                scales much smaller than signal_length_scale.
            wavelet_choice:
                Fairly arbitrary. Sym4 is the only currently supported wavelet.
                Look at http://wavelets.pybytes.com/ for more info. If you want
                a new wavelet supported, please feel free to raise an issue on
                the github page.
        """
        # Work out how many high frequency levels will have the max_cutoff
        # applied to them.
        max_noise_length = signal_length_scale/2
        max_cutoff_levels = _wavelet_freqs_below_length_scale(max_noise_length,
                                                              wavelet_choice)

        # Get the wavelet coefficients; cast them to a mutable type.
        coeffs = list(pywt.wavedec(self.image_array, wavelet_choice))
        # Work out the largest wavelet coefficient.
        max_coeff = 0
        for arr in coeffs:
            max_coeff = np.max(arr) if np.max(arr) > max_coeff else max_coeff

        # Get min_coeff from the arguments to this method.
        min_coeff = max_coeff*cutoff_factor
        high_freq_min_coeff = max_coeff*max_cutoff_factor

        for i in range(max_cutoff_levels):
            idx = -(i+1)
            coeffs[idx] = np.where(
                ((coeffs[idx] > high_freq_min_coeff).any() or
                 (coeffs[idx] < -high_freq_min_coeff).any()).any(),
                coeffs[idx], 0)

        # Apply the decimation.
        coeffs = [np.where(
            ((arr > min_coeff).any() or (arr < -min_coeff).any()).any(), arr, 0
        ) for arr in coeffs]

        # Invert the wavelet transformation.
        self.image_array = pywt.waverec(coeffs, wavelet_choice)

    def _significance_levels(self, signal_length_scale: int,
                             bkg_length_scale: int) -> np.ndarray:
        """
        Returns an image of the local significance level of every pixel in the
        image.

        TODO: this should be replaced by optimized numpy extension function.

        Args:
            signal_length_scale:
                The length scale over which signal is present. This is usually
                just a few pixels for typical magnetic diffraction data.
            bkg_length_scale:
                The length scale over which background level varies in a CCD
                image. If your CCD is perfect, you can set this to the number
                of pixels in a detector, but larger numbers will run more
                slowly. Typically something like 1/10th of the number of pixels
                in your detector is probably sensible.

        Returns:
            Array of standard deviations between the mean and each pixel.
        """
        # Compute local statistics.
        local_signal = gaussian_filter(
            self.image_array, int(signal_length_scale/3))
        local_bkg_levels = uniform_filter(local_signal, bkg_length_scale)
        local_deviation = np.std(local_signal)

        return np.abs((local_signal - local_bkg_levels)/local_deviation)

    def _significant_pixels(self, signal_length_scale: int,
                            bkg_length_scale: int,
                            n_sigma: float = 4,
                            significance_mask: np.ndarray = None) -> None:
        """
        Returns a significance map of the pixels in self.data.

        Args:
            signal_length_scale:
                The length scale over which signal is present. This is usually
                just a few pixels for typical magnetic diffraction data.
            bkg_length_scale:
                The length scale over which background level varies in a CCD
                image. If your CCD is perfect, you can set this to the number
                of pixels in a detector, but larger numbers will run more
                slowly. Typically something like 1/10th of the number of pixels
                in your detector is probably sensible.
            n_sigma:
                The number of standard deviations above the mean that a pixel
                needs to be to be considered significant.
        """
        # Compute significance; return masked significance. Significant iff
        # pixel is more than 4stddevs larger than the local average.
        significant_pixels = np.where(self._significance_levels(
            signal_length_scale, bkg_length_scale) > n_sigma, 1, 0)

        # If a mask was provided, use it.
        if significance_mask is not None:
            return significant_pixels*significance_mask
        return significant_pixels

    def mask_from_clusters(self, clusters: List[Cluster]) -> np.ndarray:
        """
        Generates a mask array from clusters.

        Args:
            clusters:
                A list of the cluster objects that we'll use to generate our
                mask.

        Returns:
            A boolean numpy mask array.
        """
        # Make an array of zeros of the correct size for this image; every
        # pixel is a mask by default.
        mask = np.zeros_like(self.image_array)

        for cluster in clusters:
            mask[cluster.pixel_indices[1], cluster.pixel_indices[0]] = 1
        return mask

    def cluster(self,
                signal_length_scale: int,
                bkg_length_scale: int,
                n_sigma: float = 4,
                significance_mask: np.ndarray = None) -> List[Cluster]:
        """
        Returns the clustered significant pixels. Does significance calculations
        here under the hood.

        Args:
            signal_length_scale:
                The length scale over which signal is present. This is usually
                just a few pixels for typical magnetic diffraction data.
            bkg_length_scale:
                The length scale over which background level varies in a CCD
                image. If your CCD is perfect, you can set this to the number
                of pixels in a detector, but larger numbers will run more
                slowly. Typically something like 1/10th of the number of pixels
                in your detector is probably sensible.
            n_sigma:
                The number of standard deviations above the mean that a pixel
                needs to be to be considered significant.
            significance_mask:
                Pixels that should never be considered to be statistically
                significant (useful if, for example, stats are biased in this
                region due to a physical barrier like a beamstop).
        """
        # Do the significance calculation.
        significant_pixels = self._significant_pixels(
            signal_length_scale, bkg_length_scale, n_sigma, significance_mask)
        # Get the significant pixels.
        pixels_y, pixels_x = np.where(significant_pixels == 1)

        # Massage these pixels into the form that sklearn wants to see.
        pixel_coords = np.zeros((len(pixels_x), 2))
        pixel_coords[:, 0] = pixels_x
        pixel_coords[:, 1] = pixels_y

        # If there are no significant pixels, return an empty list.
        if len(pixel_coords) == 0:
            return []

        # Run the DBSCAN algorithm, setting eps and min_samples according to our
        # expected signal_length_scale.
        dbscan = DBSCAN(
            eps=signal_length_scale, min_samples=signal_length_scale**2
        ).fit(pixel_coords)

        return Cluster.from_DBSCAN(pixel_coords, dbscan.labels_)


class DiffractionImage(Image):
    """
    A container for images obtained as a result of a diffraction experiment.
    """

    def __init__(self, image_array: np.ndarray,
                 beam_centre: Tuple[int]) -> None:
        super().__init__(image_array)
        self.beam_centre = beam_centre

    @property
    def _pixel_dx(self):
        """
        Returns the horizontal distance between each pixel and the beamstop.
        """
        horizontal_x = np.arange(0, self.image_array.shape[1])
        horizontal_dx = horizontal_x - self.beam_centre[0]
        pixel_dx = np.zeros_like(self.image_array)
        for col in range(self.image_array.shape[1]):
            pixel_dx[:, col] = horizontal_dx[col]

        return pixel_dx

    @property
    def _pixel_dy(self):
        """
        Returns the vertical distance between each pixel and the beamstop.
        """
        vertical_y = np.arange(self.image_array.shape[0]-1, -1, -1)
        vertical_dy = vertical_y - (
            self.image_array.shape[0] - 1 - self.beam_centre[1]
        )
        pixel_dy = np.zeros_like(self.image_array)
        for row in range(self.image_array.shape[0]):
            pixel_dy[row, :] = vertical_dy[row]

        return pixel_dy

    @property
    def pixel_radius(self):
        """
        Returns each pixel's radial distance from the beam centre, in units of
        pixels.
        """
        return np.sqrt(np.square(self._pixel_dx) + np.square(self._pixel_dy))

    @property
    def pixel_chi(self):
        """
        Returns each pixel's azimuthal rotation for a polar coordinate mapping.
        This is equivalent to the typical diffraction motor chi.
        """
        return np.arctan2(self._pixel_dx, self._pixel_dy)
