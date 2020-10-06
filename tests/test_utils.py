from pytest import mark

from src.utils import replicate_pattern


def describe_replicate_pattern():
    @mark.parametrize(
        "pattern, total, expected",
        [
            ("p", 3, "ppp"),
            ("OH", 3, "OHOHOH"),
            ("OH", "", "OH"),
        ],
    )
    def test_fixtures(pattern, total, expected):
        assert replicate_pattern(pattern, total) == expected
