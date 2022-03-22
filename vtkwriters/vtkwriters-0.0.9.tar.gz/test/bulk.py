import itertools
from vtkwriters import *


vtu_doc([(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0)], [(0, 1, 2), (0, 1, 2, 3)])

delta = 1.0, 1.5
shape = 2, 3
B = np.arange(np.prod(shape))
B.shape = shape
write_vti(block_as_vti_doc(B, location="cell", name="B"), "image2D")
delta = 1.0, 1.5, 2.0
shape = 2, 3, 4
B1 = np.arange(np.prod(shape))
B1.shape = shape
write_vti(vti_doc(shape, delta, celldata={"B1": B1}), "image1")
write_vti(block_as_vti_doc(B1, location="point", name="B1"), "image2")
for shape in itertools.permutations((3, 5, 7)):
    size = np.prod(shape)
    block = np.zeros(shape, dtype="i")
    dim = len(shape)
    for axis in range(dim):
        axisname = ["Ox", "Oy", "Oz"][axis]
        filename = "test-block_%dx%dx%d-along_" % (shape) + axisname
        pos = [slice(None),] * dim
        for k in range(shape[axis]):
            pos[axis] = k
            block[tuple(pos)] = k
        doc = block_as_vti_doc(block, location="cell", name="foo")
        write_vti(doc, filename)
B2 = 2 * B1
doc = blocks_as_vti_doc(celldata={"B1": B1, "B2": B2})
write_vti(doc, "image3")
doc = blocks_as_vti_doc(
    pointdata={"B1": B1, "B2": B2},
    celldata={"B1bis": B1[1:, 1:, 1:], "B2bis": B2[1:, 1:, 1:]},
)
write_vti(doc, "image4")
# %% dummy 2D unstructured grid
vertices = np.array([[[i, j] for i in range(3)] for j in range(3)])
vertices.shape = (-1, 2)
connectivity = np.array([[0, 1, 3], [1, 3, 4], [1, 2, 4], [3, 4, 6]])
write_vtu(vtu_doc(vertices, connectivity), "grid")
# %% block snapthots
times = np.arange(10)
blocks = [B1 + t for t in times]
write_block_snapshots(times, blocks, "foo", proppath="values")
# %% unstructured snapshots
C = np.arange(len(connectivity))
datas = [C + t for t in times]
write_unstructured_snapshots(
    times, "ufoo", vertices, connectivity, datas, "cell", proppath="values",
)
points = points_as_vtu_doc(np.array([[0, 0, 0]], dtype=np.double))
