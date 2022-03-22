from collections import namedtuple
import numpy as np
import vtkwriters as vtkw


TShape = namedtuple("Tshape", ["lower_left_corner", "extent"])

texture = TShape((2, 14), (4, 4))

zmap = np.arange(12)
zmap.shape = 4, 3

doc = vtkw.elevation_map_as_vtp_doc(
    zmap, upper_left_center=(0, 20), steps=(2, 2), texture=texture, ofmt="ascii",
)
