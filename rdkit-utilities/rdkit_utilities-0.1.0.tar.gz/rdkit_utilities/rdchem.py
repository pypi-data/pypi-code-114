"""
Functions to do with molecules that are analogous to rdkit.Chem.rdchem.
"""

from typing import List, Tuple

from rdkit import Chem as rdChem
import numpy as np


def AddConformerWithCoordinates(
    mol: rdChem.Mol,
    coordinates: np.ndarray,
) -> int:
    """Add conformer to molecule with coordinates in angstrom"""
    from rdkit import Geometry
    n_atoms = mol.GetNumAtoms()
    coord_type = np.asarray(coordinates)
    if coord_type.shape != (n_atoms, 3):
        raise ValueError(
            f"Shape of coordinates must be ({n_atoms}, 3). "
            f"Given array with shape {coord_type.shape}"
        )
    conformer = rdChem.Conformer(n_atoms)
    for i, xyz in enumerate(coordinates):
        x, y, z = map(float, xyz)
        conformer.SetAtomPosition(i, Geometry.Point3D(x, y, z))
    conformer.SetId(mol.GetNumConformers())
    return mol.AddConformer(conformer)


def GetSymmetricAtomIndices(
    mol: rdChem.Mol,
    maxMatches: int = 10000,
) -> List[Tuple[int, ...]]:
    """Get atom indices of symmetric atoms

    Returns
    -------
    symmetric_indices: List[Tuple[int, ...]]
        In this list, one item is a sorted tuple of indices,
        where each index indicates an atom that is symmetric
        to all the other indices in the tuple.
    """
    # take care of resonance
    matches = [
        match
        for resMol in rdChem.ResonanceMolSupplier(mol)
        for match in resMol.GetSubstructMatches(mol, uniquify=False,
                                                maxMatches=maxMatches)
    ]
    atom_symmetries = set(tuple(sorted(set(x))) for x in zip(*matches))
    return sorted([x for x in atom_symmetries if len(x) > 1])
