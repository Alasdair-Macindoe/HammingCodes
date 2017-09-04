"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_i_0():
    """ Ensure I_0 is the empty matrix"""
    assert program.identity(0) == program.binary_matrix()

def test_i_1():
    """ Ensure I_1 is just [1] """
    assert program.identity(1) == program.binary_matrix([[1]])

def test_i_2():
    """ Ensure I_2 is [[1,0],[0,1]] """
    i_2 = program.create_binary_matrix([
                                    [1,0],
                                    [0,1]
                                    ])
    for a,b in zip(program.identity(2), i_2):
        assert a == b

def test_type():
    """ Ensure types returned are correct """
    assert (
        type(program.identity(3)) ==
        type(program.binary_matrix([1]))
        )
