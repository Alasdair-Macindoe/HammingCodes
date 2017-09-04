"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest


def test_int_0():
    assert '0' == program._get_binary(0,1)

def test_int_5():
    assert '101'== program._get_binary(5,3)

def test_int_1_with_larger_r():
    assert '00001' == program._get_binary(1,5)
