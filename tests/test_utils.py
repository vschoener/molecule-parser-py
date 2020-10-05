from src.utils import replicate_pattern


def test_replicate_pattern_should_replicate_3_times():
    assert replicate_pattern("p", 3) == "ppp"


def test_replicate_pattern_should_replicate_longer_3_times():
    assert replicate_pattern("OH", 3) == "OHOHOH"


def test_replicate_pattern_should_replicate_once_if_total_not_provided():
    assert replicate_pattern("OH", "") == "OH"
