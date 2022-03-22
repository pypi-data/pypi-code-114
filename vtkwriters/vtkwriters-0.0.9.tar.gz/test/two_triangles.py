import numpy as np
import vtkwriters as vtkw

vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],], dtype="d")
triangles = np.array([[0, 1, 2], [0, 2, 3],], dtype="i")

vtkw.write_vtu(
    vtkw.vtu_doc(
        vertices,
        triangles,
        celldata={"cell property": np.arange(2)},
        fielddata={"color": (0, 255, 0)},  # green
    ),
    "two_triangles",
)
