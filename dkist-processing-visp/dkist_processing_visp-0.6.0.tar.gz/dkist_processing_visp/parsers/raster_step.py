"""Copies of UniqueBud and SingleValueSingleKeyFlower from common that only activate if the frames are "observe" task."""
from dkist_processing_common.models.flower_pot import SpilledDirt
from dkist_processing_common.parsers.single_value_single_key_flower import (
    SingleValueSingleKeyFlower,
)
from dkist_processing_common.parsers.unique_bud import UniqueBud

from dkist_processing_visp.models.constants import VispBudName
from dkist_processing_visp.models.tags import VispStemName
from dkist_processing_visp.parsers.visp_l0_fits_access import VispL0FitsAccess


class TotalRasterStepsBud(UniqueBud):
    """Bud for finding the total number of raster steps."""

    def __init__(self):
        super().__init__(
            constant_name=VispBudName.num_raster_steps.value, metadata_key="total_raster_steps"
        )

    def setter(self, fits_obj: VispL0FitsAccess):
        """
        Setter for the bud.

        Parameters
        ----------
        fits_obj:
            A single FitsAccess object
        """
        if fits_obj.ip_task_type != "observe":
            return SpilledDirt
        return super().setter(fits_obj)


class RasterScanStepFlower(SingleValueSingleKeyFlower):
    """Flower for a raster scan step."""

    def __init__(self):
        super().__init__(
            tag_stem_name=VispStemName.raster_step.value, metadata_key="raster_scan_step"
        )

    def setter(self, fits_obj: VispL0FitsAccess):
        """
        Setter for a flower.

        Parameters
        ----------
        fits_obj:
            A single FitsAccess object
        """
        if fits_obj.ip_task_type != "observe":
            return SpilledDirt
        return super().setter(fits_obj)
