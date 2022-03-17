import logging
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, Union

import numpy as np
import pydicom
from plotly import graph_objects as go
from pydicom import FileDataset

from ..helpers.check_path_is_valid import check_path_is_valid_path
from ..helpers.pixel_data import get_pixel_array
from ..helpers.rotate_image import rotate_image
from ..helpers.voxel_data import VoxelData
from ..helpers.window import get_default_window_settings
from ..plotting.plotly import show_image
from ..roi.roi import Roi
from .dicom_series import DicomSeries

logger = logging.getLogger(__name__)


class ProjectionSeries(DicomSeries):
    """A class to manage 2D DICOM images, e.g., from conventional X-rays, mammography, panoramic, intraoral etc.

    This class only handles one image per series, as is usually the case for this kind of images.

    Args:
        file: Path object for the file that is to be imported
        dcm: A pydicom FileDataset object containing the file

    Attributes:
        kV: Tube voltage used in the image acquisition in kV
        mA: Tube current used in the image acquisition in mA
        Modality: The modality of the image, e.g., IO, PX, MG, DX, CR, etc.
        Manufacturer: The name of the manufacturer as specified in the DICOM file
        ManufacturersModelName: The model name specified by the manufacturer as given in the DICOM file

    """

    def __init__(self, file: Path, dcm: Optional[FileDataset] = None):
        if dcm is None:
            dcm = pydicom.dcmread(fp=str(file.absolute()), stop_before_pixels=True)

        if "SeriesInstanceUID" not in dcm:
            raise ValueError("The DICOM file does not contain a series instance UID")

        super().__init__(series_instance_uid=dcm.SeriesInstanceUID)

        self.Modality = dcm.Modality
        self.Manufacturer: Optional[str] = None
        if "Manufacturer" in dcm:
            self.Manufacturer = dcm.Manufacturer

        self.ManufacturersModelName: Optional[str] = None
        if "ManufacturerModelName" in dcm:
            self.ManufacturersModelName = dcm.ManufacturerModelName
        if self.Modality == "IO" and "DetectorManufacturerModelName" in dcm:
            self.ManufacturersModelName = dcm.DetectorManufacturerModelName

        self.kV: Optional[List[Optional[float]]] = []
        self.mA: Optional[List[Optional[float]]] = []
        self.ms: Optional[List[Optional[float]]] = []
        self.ImageVolume: Optional[List[np.ndarray]] = []

        self.add_file(file=file, dcm=dcm)

    def add_file(self, file: Union[Path, str], dcm: Optional[FileDataset] = None):
        """Add a file to the objects list of files

        First performs a check that the file path is of a path object and that it has the same series instance UID as
        the class object

        Args:
            file: Path to where the file to be added is stored on disc
            dcm: The DICOM-file imported to a FileDataset object

        Raises:
            InvalidDicomError: If the given file is not a valid DICOM file
            ValueError: If the file does not have the same study instance UID as the StudyInstanceUID of the object

        """
        file = check_path_is_valid_path(path_to_check=file)

        super().add_file(file=file, dcm=dcm)

        if len(self.CompleteMetadata) == len(self.FilePaths):
            # Skip out because the file has already been added
            return

        if dcm is None:
            dcm = pydicom.dcmread(fp=str(file.absolute()), stop_before_pixels=True)

        if "PixelSpacing" in dcm:
            self.VoxelData.append(VoxelData(x=float(dcm.PixelSpacing[1]), y=float(dcm.PixelSpacing[0]), z=None))
        else:
            # Assume pixel size is set in Detector Element Spacing tag (0018, 7022)
            self.VoxelData.append(
                VoxelData(x=float(dcm.DetectorElementSpacing[1]), y=float(dcm.DetectorElementSpacing[0]), z=None)
            )

        self.kV.append(self._get_tag_value_as_float_or_none("KVP", ds=dcm))

        if "XRayTubeCurrent" in dcm:
            self.mA.append(float(dcm.XRayTubeCurrent))
        elif "XRayTubeCurrentInmA" in dcm:
            self.mA.append(float(dcm.XRayTubeCurrentInmA))
        elif "XRayTubeCurrentInuA" in dcm:
            self.mA.append(float(dcm.XRayTubeCurrentInuA) / 1000)
        else:
            self.mA.append(None)

        self.ms.append(self._get_tag_value_as_float_or_none("ExposureTime", ds=dcm))

        # Remove pixel data part of dcm to decrease memory used for the object
        if "PixelData" in dcm:
            try:
                del dcm[0x7FE00010]
            except Exception:
                logger.debug(
                    "Failed to remove pixel data from file before appending to CompleteMetadata", exc_info=True
                )
                pass

        self.CompleteMetadata.append(dcm)

    @staticmethod
    def _get_tag_value_as_float_or_none(tag_name: str, ds: FileDataset) -> Optional[float]:
        tag_value = ds.get(tag_name)

        if tag_value is None:
            return None

        return float(tag_value)

    def import_image(self, rotate_to_0_degerees: Optional[bool] = False) -> None:
        """Import the pixel data into the ImageVolume property"""
        self.ImageVolume = []
        for ind, fp in enumerate(self.FilePaths):
            dcm = pydicom.dcmread(str(fp.absolute()))
            pixel_array = get_pixel_array(dcm=dcm)

            if rotate_to_0_degerees:
                pixel_array = rotate_image(image=pixel_array, metadata=self.CompleteMetadata[ind])

            self.ImageVolume.append(pixel_array)

        if self.PixelIntensityNormalized:
            self.normalize_pixel_intensity_relationship()

    def sort_images_on_acquisition_time(self) -> None:
        """Reorder the images in the series based on the acquisition time"""
        file_order = [
            ind for ind in list(np.argsort(np.array([self._get_acquisition_time(ds) for ds in self.CompleteMetadata])))
        ]

        self.kV = self._reorder_list_by_index_order_list(order_list=file_order, list_to_order=self.kV)
        self.mA = self._reorder_list_by_index_order_list(order_list=file_order, list_to_order=self.mA)
        self.ms = self._reorder_list_by_index_order_list(order_list=file_order, list_to_order=self.ms)
        self.CompleteMetadata = self._reorder_list_by_index_order_list(
            order_list=file_order, list_to_order=self.CompleteMetadata
        )
        self.FilePaths = self._reorder_list_by_index_order_list(order_list=file_order, list_to_order=self.FilePaths)
        self.ImageVolume = self._reorder_list_by_index_order_list(order_list=file_order, list_to_order=self.ImageVolume)

    @staticmethod
    def _get_acquisition_time(dataset: FileDataset) -> Optional[datetime]:
        acquisition_date = dataset.AcquisitionDate
        acquisition_time = dataset.AcquisitionTime

        acquisition_datetime = f"{acquisition_date} {acquisition_time}"
        datetime_format = "%Y%m%d %H%M%S"

        if "." in acquisition_time:
            datetime_format += ".%f"

        return datetime.strptime(acquisition_datetime, datetime_format)

    @staticmethod
    def _reorder_list_by_index_order_list(order_list: List[int], list_to_order: List[Any]):
        if len(list_to_order) == 0:
            return list_to_order
        return [list_to_order[ind] for ind in order_list]

    def show_image(
        self,
        index: int = 0,
        rois: Optional[Roi] = None,
        colour_map: str = "bone",
        window: Optional[tuple[float, float]] = None,
        roi_only_borders: Optional[bool] = True,
        roi_colour: str = "#33a652",
        roi_border_width: int = 2,
    ) -> go.Figure:
        super().show_image(index=index, rois=rois, colour_map=colour_map, window=window)

        if self.ImageVolume is None:
            self.import_image()

        if window is None:
            window = self._get_default_window_settings(index=index)

        return show_image(
            image=self.ImageVolume[index],
            x_scale=self.VoxelData[index].x,
            y_scale=self.VoxelData[index].y,
            window=window,
            rois=rois,
            roi_colour=roi_colour,
            roi_only_border=roi_only_borders,
            roi_border_width=roi_border_width,
            colour_map=colour_map,
        )

    def _get_default_window_settings(self, index: int) -> tuple[float, float]:
        return get_default_window_settings(metadata=self.CompleteMetadata[index], image_slice=self.ImageVolume[index])
