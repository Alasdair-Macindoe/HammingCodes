"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_normal():
    assert program._get_row([1,0,1,0]) == [1,0,1,0]

def test_string():
    assert program._get_row('10001') == [1,0,0,0,1]
