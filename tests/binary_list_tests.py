"""
Lines 5 and 6 were adapted from SO code:
http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
"""
import sys
sys.path.insert(0, '..')
""" END """

import main as program
import pytest

#Note: All tests must begin with test_<name>
####
""" Test the creation and manipulation of binary_matrix class"""
####
def test_binary_matrix():
    """
    Ensures that the create_binary_list method is actually returning a binary
    matrix and not a regular list
    """
    assert (
            type(program.create_binary_matrix([1,2])) ==
            type(program.binary_matrix([1,2]))
            )

def test_binary_matrix_for_small_values():
    """
    Tests the binary_list type for single integers
    """
    assert (
            type(program.create_binary_matrix([1])) ==
            type(program.binary_matrix([1]))
            )
def test_binary_matrix_for_non_lists():
    """
    Tests the binary_list type for single integers.
    Should raise an error.
    """
    with pytest.raises(TypeError):
        assert (
                type(program.create_binary_matrix(1)) ==
                type(program.binary_matrix(1))
                )
