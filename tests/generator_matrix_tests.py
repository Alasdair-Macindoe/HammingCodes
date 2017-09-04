"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_743_code():
    G = program.binary_matrix([
                        [1,0,0,0,1,1,0],
                        [0,1,0,0,1,0,1],
                        [0,0,1,0,0,1,1],
                        [0,0,0,1,1,1,1]
                        ])
    assert program.create_generator_matrix(3,4) == G

def test_313_code():
    G = program.binary_matrix([[1,1,1]])
    assert program.create_generator_matrix(2,1) == G
