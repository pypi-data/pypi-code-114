import re
import pytest

import numpy as np
from numpy.testing import assert_allclose

from rdkit import Chem as rdChem
from rdkit_utilities import rdchem, rdmolfiles


@pytest.mark.parametrize("smarts, indices", [
    ("[C](=[O])-[O-]", [(1, 2)]),
    (
        "[N:1](-[H:2])(-[H:3])-[C:4](-[O:5]-[H:6])(-[O:7]-[H:8])-[O:9]-[H:10]",
        [(1, 2), (4, 6, 8), (5, 7, 9)]
    ),
    (
        "[N-2:1]-[C:2](-[O:3]-[H:4])(-[O:5]-[H:6])-[O:7]-[H:8]",
        [(2, 4, 6), (3, 5, 7)]
    ),
])
def test_GetSymmetricAtomIndices(smarts, indices):
    mol = rdmolfiles.MolFromSmarts(smarts, orderByMapNumber=True,
                                   clearAtomMapNumbers=True)
    rdChem.SanitizeMol(mol)
    assert rdchem.GetSymmetricAtomIndices(mol) == indices


def test_AddConformerWithCoordinates(propylparaben):
    assert propylparaben.GetNumConformers() == 0
    coordinates = np.ones((25, 3))
    rdchem.AddConformerWithCoordinates(propylparaben, coordinates)
    assert propylparaben.GetNumConformers() == 1
    rdcoords = propylparaben.GetConformer(0).GetPositions()
    assert_allclose(np.array(rdcoords), coordinates)


def test_AddConformerWithCoordinates_error(propylparaben):
    assert propylparaben.GetNumConformers() == 0
    coordinates = np.ones((24, 3))

    err = (
        "Shape of coordinates must be (25, 3). "
        "Given array with shape (24, 3)"
    )

    with pytest.raises(ValueError, match=re.escape(err)):
        rdchem.AddConformerWithCoordinates(propylparaben, coordinates)
    assert propylparaben.GetNumConformers() == 0
