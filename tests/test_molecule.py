from pytest import raises, mark

from src.molecule import flatten, flatten_all, flatten_sub_molecule
from src.exceptions.enclosure_exception import EnclosureException


def describe_flatten():
    @mark.parametrize(
        "molecule, expected",
        [
            ("MgO", "MgO"),  # Nothing to change
            ("H2O", "HHO"),  # Simple case
            ("Mg3H2OCi4", "MgMgMgHHOCiCiCiCi"),  # More longer
            ("K4[ON(SO3)2]2", "KKKK[ON(SOOO)2]2"),  # Complex inside encloser
        ],
    )
    def test_fixtures(molecule, expected):
        assert flatten(molecule) == expected


def describe_flatten_sub():
    @mark.parametrize(
        "molecule, expected",
        [
            ("Mg2OH", "Mg2OH"),  # Nothing to change
            ("Mg(OH)2", "MgOHOH"),  # Simple case
            ("Mg(OH)", "MgOH"),  # Simple case without a number
            ("KKKK[ON(SOOO)2]2", "KKKKONSOOOSOOOONSOOOSOOO"),
            (
                "K4[ON(SO3)2]2",
                "K4[ON(SO3)2]2",
            ),  # To show we need to flatten before, otherwise it does nothing
        ],
    )
    def test_fixtures(molecule, expected):
        assert flatten_sub_molecule(molecule) == expected

    def test_flatten_sub_molecule_bad_encloser():
        with raises(EnclosureException) as exception:
            flatten_sub_molecule("Mg(OH}2")

        assert exception.value.message == "Parsing error"
        assert exception.value.match.group(0) == "(OH}2"


def describe_flatten_all():
    @mark.parametrize(
        "molecule, expected",
        [
            ("H2O", "HHO"),  # Simple case
            ("Mg(OH)2", "MgOHOH"),  # With sub molecule
            ("K4[ON(SO3)2]2", "KKKKONSOOOSOOOONSOOOSOOO"),  # Complex case
        ],
    )
    def test_fixtures(molecule, expected):
        assert flatten_all(molecule) == expected
