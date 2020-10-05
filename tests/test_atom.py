from src.atom import reduce_atoms


def test_reduce_atoms_simple():
    assert reduce_atoms("HO") == {"H": 1, "O": 1}


def test_reduce_atoms_longer():
    assert reduce_atoms("KKKKKOOOOMgMgCiCiNNNNN") == {
        "Ci": 2,
        "K": 5,
        "Mg": 2,
        "N": 5,
        "O": 4,
    }
