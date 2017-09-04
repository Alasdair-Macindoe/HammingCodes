"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_zeros():
    a = program.binary_matrix([[0,0,0,0,0,0,0]])
    H = program.get_parity_check(3)
    assert program.do_parity_check(a,H) == True

def test_ones():
    a = program.binary_matrix([[1,1,1,1,1,1,1]])
    H = program.get_parity_check(3)
    assert program.do_parity_check(a,H) == True

def test_normal():
    a = program.binary_matrix([[1,1,1,0,0,0,0]])
    H = program.get_parity_check(3)
    assert program.do_parity_check(a,H) == True

def test_failure():
    a = program.binary_matrix([[0,1,1,1,0,1,1]])
    H = program.get_parity_check(3)
    assert program.do_parity_check(a,H) == False
