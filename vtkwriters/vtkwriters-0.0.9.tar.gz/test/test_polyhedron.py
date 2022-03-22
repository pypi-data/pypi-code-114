import numpy as np

import vtkwriters as vtkw

vtkw.write_vtu(
    vtkw.polyhedra_vtu_doc(
        vertices=np.array(
            [(-1, -1, 0), (1, -1, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0),], dtype="d",
        ),
        cells_faces=[[(0, 4, 1, 2), (0, 1, 3), (1, 2, 3), (2, 0, 3),]],
    ),
    "tet_as_polyhedron",
)
