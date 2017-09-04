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
    """ Example from Lecture 7 - 01 """
    v = program.binary_matrix([[1,1,0,0,0,0,0]])
    H = program.get_parity_check(3)
    syndromes = program.create_syndrome_dict(7,3)
    res = program.decode_syndrome(v, syndromes, H)
    assert res == [1,1,1,0,0,0,0]

def test_larger_example():
    start = program.binary_matrix([[1,1,0,1,0,0,1,0,1,0,0]])
    G = program.create_generator_matrix(4, 11)
    v = program.binary_matrix([program.get_encoding(start,G)])
    H = program.get_parity_check(4)
    syndromes = program.create_syndrome_dict(15, 4)
    res = program.decode_syndrome(v, syndromes, H)
    assert res == v[0]

#Test fails, please review. 
def test_small_example():
    s = program.binary_matrix([[1,1,1]])
    G = program.create_generator_matrix(2,1)
    v = program.binary_matrix([program.get_encoding(s,G)])
    H = program.get_parity_check(2)
    syndromes = program.create_syndrome_dict(3,2)
    res = program.decode_syndrome(v, syndromes, H)
    assert res == v[0]
