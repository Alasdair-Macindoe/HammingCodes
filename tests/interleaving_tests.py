"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

def test_one_row():
    assert program.interleave([[1,0,1]]) == [[1],[0],[1]]

def test_two_rows():
    assert program.interleave([[1,0,1],[0,0,0]]) == [[1,0],[0,0],[1,0]]

def test_interleave_for_one():
    a = program.binary_matrix([[0,0,0,0,0,0,0]])
    a_T = program.interleave(a)
    assert a_T == [[0],[0],[0],[0],[0],[0],[0]]

def test_interleave_for_multiple():
    a = program.binary_matrix([[0,0,0,0,0,0,0],[1,1,1,1,1,1,1]])
    a_T = program.interleave(a)
    assert a_T == [[0,1],[0,1],[0,1],[0,1],[0,1],[0,1],[0,1]]

def test_interleave_for_n():
    a = [[1,1,1],[0,0,0],[1,1,1],[0,0,0]]
    assert program.interleave_for_size(a, 2) == [
                                                [
                                                    [1,0],
                                                    [1,0],
                                                    [1,0]
                                                ],[
                                                    [1,0],
                                                    [1,0],
                                                    [1,0]
                                                ]]
def test_repeat():
    assert program.interleave(program.interleave([[1,0,1]])) == [[1,0,1]]

def test_long():
    assert program.interleave([[1,0],[1,0],[1,0],[1,0]]) == [[1,1,1,1],[0,0,0,0]]
