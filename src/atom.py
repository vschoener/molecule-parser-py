from re import compile
from functools import reduce

EXTRACT_ATOMS_REGEX = r"[A-Z][a-z]*"
extract_atoms_regex = compile(EXTRACT_ATOMS_REGEX)

# Lambda does not allow to assign value, so this act as an helper
def __acc_reduce_atoms(acc, atom):
    acc[atom] = (acc.get(atom) or 0) + 1
    return acc


def reduce_atoms(molecule):
    atoms = extract_atoms_regex.findall(molecule)
    return reduce(__acc_reduce_atoms, atoms, {})
