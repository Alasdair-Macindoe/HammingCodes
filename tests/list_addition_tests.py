"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_normal_additon():
    assert program.list([1,0]) + program.list([0,1]) == program.list([1,1])

def test_ensure_xor_addition():
    assert program.list([1,1]) + program.list([1,1]) == program.list([0,0])
