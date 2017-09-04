"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_example():
    """ From Lecture 7 - 01 """
    v = program.binary_matrix([[1,1,0,0,0,0,0]])
    H = program.get_parity_check(3)
    syndromes = program.create_syndrome_dict(7,3)
    vH = program.calculate_syndrome(v,H)
    assert vH == [0,1,1]
