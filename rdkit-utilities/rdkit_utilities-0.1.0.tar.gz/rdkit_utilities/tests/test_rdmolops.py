import pytest

import numpy as np
from numpy.testing import assert_allclose

from rdkit_utilities import rdmolfiles, rdmolops


def test_OrderByMapNumber():
    mol = rdmolfiles.MolFromSmiles("[C:3][C:2][O:1]")
    assert mol.GetAtomWithIdx(0).GetSymbol() == "C"

    reordered = rdmolops.OrderByMapNumber(mol, clearAtomMapNumbers=False)
    first = reordered.GetAtomWithIdx(0)
    assert first.GetSymbol() == "O"
    assert first.GetAtomMapNum() == 1

    reordered = rdmolops.OrderByMapNumber(mol, clearAtomMapNumbers=True)
    first = reordered.GetAtomWithIdx(0)
    assert first.GetSymbol() == "O"
    assert first.GetAtomMapNum() == 0


@pytest.mark.parametrize(
    "core_indices, include_central_atoms, n_neighbors, expected_indices",
    [
        ({14}, True, -1, set(range(25))),
        ({14}, False, -1, set(range(14)) | set(range(15, 25))),
        ({14}, True, 0, {14}),
        ({14}, False, 0, set()),
        ({14}, True, 1, {12, 14, 15}),
        ({14}, False, 1, {12, 15}),
        ({14}, True, 2, {7, 13, 12, 14, 15, 16, 17, 18}),
        ({14}, False, 2, {7, 13, 12, 15, 16, 17, 18}),
        ({14}, True, 3, {5, 8, 7, 13, 12, 14, 15, 16, 17, 18, 19, 20, 21}),
        ({14}, False, 3, {5, 8, 7, 13, 12, 15, 16, 17, 18, 19, 20, 21}),
        ({2, 12, 21}, True, -1, set(range(25))),
        ({2, 12, 21}, True, 0, {2, 12, 21}),
        ({2, 12, 21}, False, 0, set()),
        ({2, 12, 21}, False, 1, {1, 3, 10, 7, 13, 14, 18, 22, 23, 24}),
        ({2, 12}, False, 2, {0, 1, 3, 4, 5, 10, 8, 11, 7, 13, 14, 5, 8, 15})
    ]
)
def test_GetAtomNeighborIndices(
    propylparaben,
    core_indices,
    include_central_atoms,
    n_neighbors,
    expected_indices
):
    indices = rdmolops.GetAtomNeighborIndices(
        propylparaben,
        centralAtomIndices=core_indices,
        includeCentralAtoms=include_central_atoms,
        numAtomNeighbors=n_neighbors
    )
    assert indices == expected_indices


@pytest.fixture()
def mol_with_conformers():
    from rdkit_utilities.rdchem import AddConformerWithCoordinates
    mol = rdmolfiles.MolFromSmarts("[O]=[C]=[O]")
    coords = np.zeros((3, 3), dtype=float)
    for i in range(10):
        AddConformerWithCoordinates(mol, coords + i)
    return mol


def test_ReorderConformers(mol_with_conformers):
    conf = mol_with_conformers.GetConformer(0)
    assert_allclose(np.array(conf.GetPositions())[0], [0, 0, 0])
    assert conf.GetId() == 0

    order = [4, 2, 1, 0, 3, 5, 6, 7, 8, 9]
    rdmolops.ReorderConformers(mol_with_conformers, order)
    conf = mol_with_conformers.GetConformer(0)
    assert_allclose(np.array(conf.GetPositions())[0], [4, 4, 4])
    assert conf.GetId() == 0


def test_KeepConformerIds(mol_with_conformers):
    rdmolops.KeepConformerIds(mol_with_conformers, [1, 0, 3, 5, 6, 7])
    conformer_ids = [
        conf.GetId()
        for conf in mol_with_conformers.GetConformers()
    ]
    assert conformer_ids == [0, 1, 3, 5, 6, 7]
