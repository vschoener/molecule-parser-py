from pytest import mark

from src.molecule_parser import parse


def describe_parse():
    @mark.parametrize(
        "molecule, expected",
        [
            ("", {}),  # Empty case
            ("H2O", {"H": 2, "O": 1}),  # Simple case
            ("Mg(OH)2", {"H": 2, "Mg": 1, "O": 2}),  # With sub case
            ("K4[ON(SO3)2]2", {"K": 4, "N": 2, "O": 14, "S": 4}),  # With complex case
            (
                "K4[(SO3)]2",
                {"K": 4, "O": 6, "S": 2},
            ),  # With complex case without multiplier after encloser
        ],
    )
    def test_fixtures(molecule, expected):
        assert parse(molecule) == expected
