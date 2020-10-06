"""
    This module provide access to Atom manipulation
"""

from re import compile as compile_regex
from functools import reduce

EXTRACT_ATOMS_REGEX = r"[A-Z][a-z]*"
extract_atoms_regex = compile_regex(EXTRACT_ATOMS_REGEX)


def __acc_reduce_atoms(acc, atom):
    """ Lambda does not allow to assign value, so this act as an helper to create dict"""

    acc[atom] = (acc.get(atom) or 0) + 1
    return acc


def reduce_atoms(molecule):
    """ Create dict using reduce method over the molecule """

    atoms = extract_atoms_regex.findall(molecule)
    return reduce(__acc_reduce_atoms, atoms, {})
