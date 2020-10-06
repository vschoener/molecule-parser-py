from pytest import raises

from src.molecule import flatten, flatten_all, flatten_sub_molecule
from src.exceptions.enclosure_exception import EnclosureException


def test_flatten_should_return_same_if_nothing_changed():
    assert flatten("MgO") == "MgO"


def test_flatten_should_convert_simple_molecule():
    assert flatten("H2O") == "HHO"


def test_flatten_should_convert_complex_molecule():
    assert flatten("Mg3H2OCi4") == "MgMgMgHHOCiCiCiCi"


def test_flatten_should_convert_inside_sub_molecule():
    assert flatten("K4[ON(SO3)2]2") == "KKKK[ON(SOOO)2]2"


def test_flatten_sub_molecule_should_convert_simple_flatten_molecule():
    assert flatten_sub_molecule("Mg(OH)2") == "MgOHOH"


def test_flatten_sub_molecule_should_convert_with_no_number():
    assert flatten_sub_molecule("Mg(OH)") == "MgOH"


def test_flatten_sub_molecule_should_convert_flatten_molecule():
    assert flatten_sub_molecule("KKKK[ON(SOOO)2]2") == "KKKKONSOOOSOOOONSOOOSOOO"


def test_flatten_sub_molecule_should_return_same_if_nothing_changed():
    assert flatten_sub_molecule("Mg2OH") == "Mg2OH"


def test_flatten_sub_molecule_should_throw_with_bad_encloser():
    with raises(EnclosureException) as exception:
        flatten_sub_molecule("Mg(OH}2")

    assert exception.value.message == "Parsing error"
    assert exception.value.match.group(0) == "(OH}2"


def test_flatten_all_should_convert_all_molecules_with_easier():
    assert flatten_all("Mg(OH)2") == "MgOHOH"


def test_flatten_all_should_convert_all_molecules_with_simple():
    assert flatten_all("Mg2OH") == "MgMgOH"


def test_flatten_all_should_convert_all_molecules_with_complex():
    assert flatten_all("K4[ON(SO3)2]2") == "KKKKONSOOOSOOOONSOOOSOOO"
