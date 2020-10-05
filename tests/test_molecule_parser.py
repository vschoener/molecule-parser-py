from src.molecule_parser import parse


def test_parse_should_return_empty():
    assert parse("") == {}


def test_parse_should_handle_h2O():
    assert parse("H2O") == {"H": 2, "O": 1}


def test_parse_should_handle_with_simple_sub_molecule_string():
    assert parse("Mg(OH)2") == {"H": 2, "Mg": 1, "O": 2}


def test_parse_should_handle_multiple_sub_molecule_string():
    assert parse("K4[ON(SO3)2]2") == {"K": 4, "N": 2, "O": 14, "S": 4}


def test_parse_should_handle_multiple_sub_molecule_with_close_enclosures_string():
    assert parse("K4[(SO3)]2") == {"K": 4, "O": 6, "S": 2}
