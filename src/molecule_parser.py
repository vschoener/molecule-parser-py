"""
This module provides a molecule parser over complex molecule string
"""

from re import compile
from src.molecule import flatten_all
from src.atom import reduce_atoms
from src.utils import replicate_pattern


def parse(molecule):
    flatten_molecule = flatten_all(molecule)
    atoms = reduce_atoms(flatten_molecule)

    return atoms
