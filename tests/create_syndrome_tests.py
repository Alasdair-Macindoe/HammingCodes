"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest


def test_r_3():
    """ This example is taken from Lecture 7 - 01 """
    results = program.create_syndrome_dict(7,3)
    syndromes = {
                0: 0,
                1: 1,
                2: 2,
                4: 4,
                7: 8,
                3: 16,
                5: 32,
                6: 64
                }
    assert results == syndromes
