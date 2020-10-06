"""
    This module provide some utils
"""


def replicate_pattern(pattern, total):
    """ Concat the pattern by the total provided """
    return pattern * int(total or 1)
