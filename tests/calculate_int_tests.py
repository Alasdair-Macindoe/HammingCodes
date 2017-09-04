"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_for_0():
    assert program.calculate_int([0]) == 0

def test_for_1():
    assert program.calculate_int([1]) == 1

def test_for_non_zero():
    assert program.calculate_int([1,1,1,0]) == 14
