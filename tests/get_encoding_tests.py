"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest


def test_normal_encoding():
    a = program.binary_matrix([[1,1,1,0]])
    G = program.create_generator_matrix(3,4)
    assert program.get_encoding(a,G) == [1,1,1,0,0,0,0]

def test_for_zero():
    a = program.binary_matrix([[0,0,0,0]])
    G = program.create_generator_matrix(3,4)
    assert program.get_encoding(a,G) == [0,0,0,0,0,0,0]

def test_for_one():
    a = program.binary_matrix([[1,1,1,1]])
    G = program.create_generator_matrix(3,4)
    assert program.get_encoding(a,G) == [1,1,1,1,1,1,1]
