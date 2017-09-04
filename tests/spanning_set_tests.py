"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_span_creation():
    assert program.span_from_identity(2) == program.binary_matrix([
                                                                [1,1],
                                                                [1,0],
                                                                [0,1]
                                                                ])
def test_larger_span_creation():
    assert program.span_from_identity(3) == program.binary_matrix([
                                                                [1,1,0],
                                                                [1,0,1],
                                                                [0,1,1],
                                                                [1,1,1],
                                                                [1,0,0],
                                                                [0,1,0],
                                                                [0,0,1]
                                                                ])
