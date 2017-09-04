"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_zero():
    assert program._get_binary(0,1) == '0'

def test_normal():
    assert program._get_binary(10,4) == '1010'

def test_added_zeros():
    assert program._get_binary(3,5) == '00011'
