"""
This module provides a molecule parser over complex molecule string
"""

from src.molecule import flatten_all
from src.atom import reduce_atoms


def parse(molecule):
    """ Entry point of the module to parse molecule """
    flatten_molecule = flatten_all(molecule)
    atoms = reduce_atoms(flatten_molecule)

    return atoms
