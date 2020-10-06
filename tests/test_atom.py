from pytest import mark

from src.atom import reduce_atoms


def describe_reduce_atoms():
    @mark.parametrize(
        "molecule, expected",
        [
            ("HO", {"H": 1, "O": 1}),
            (
                "KKKKKOOOOMgMgCiCiNNNNN",
                {
                    "Ci": 2,
                    "K": 5,
                    "Mg": 2,
                    "N": 5,
                    "O": 4,
                },
            ),
        ],
    )
    def test_fixtures(molecule, expected):
        assert reduce_atoms(molecule) == expected
