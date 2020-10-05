"""
    This module provide access to Molecule manipulation
"""

from re import compile as compile_regex
from utils import replicate_pattern
from src.exceptions.enclosure_exception import EnclosureException

MOLECULE_REGEX = r"([A-Z]{1}[a-z]*)(\d*)"
SUB_FLATTEN_MOLECULE_REGEX = r"([([{])([a-zA-Z]*)([\])}])(\d*)"

enclosures = {"{": "}", "[": "]", "(": ")"}

molecule_regex = compile_regex(MOLECULE_REGEX)
sub_regex = compile_regex(SUB_FLATTEN_MOLECULE_REGEX)


def __assert_and_replicate_flatten_molecule(match):
    begin_enclosure, flatten_molecule, end_enclosure, multiplier = match.groups()

    if enclosures[begin_enclosure] != end_enclosure:
        raise EnclosureException("Parsing error", match)

    return replicate_pattern(flatten_molecule, multiplier)


def flatten_sub_molecule(flatten_molecule):
    # Flatten sub molecule works as close as the flatten but it needs
    # to deal with the enclosures
    # ex: K4(SO3) => K4(SOOO)
    last_flatten_molecule = ""
    new_flatten_molecule = flatten_molecule

    while last_flatten_molecule != new_flatten_molecule:
        last_flatten_molecule = new_flatten_molecule
        new_flatten_molecule = sub_regex.sub(
            lambda matched: __assert_and_replicate_flatten_molecule(matched),
            last_flatten_molecule,
        )

    return new_flatten_molecule


def flatten(molecule):
    # Flatten molecule means we want to replace the atoms and associated number
    # by each times they exists
    # ex: K4O2 => KKKKOO
    flatten_molecule = molecule_regex.sub(
        lambda matched: replicate_pattern(matched[1], matched[2]), molecule
    )

    return flatten_molecule


def flatten_all(molecule):
    return flatten_sub_molecule(flatten(molecule))
