""" This file establishes and maintains the state so we can run experiments """
import random
from enum import Enum, unique

@unique
class state(Enum):
    """ Declare all the possible states we can be in """
    good = 0,
    bad = 1

#TODO: Unit test?
def _chance_test(chance):
    """
    Tests whether or not we should switch for a given chance percentage
    0 <= chance <= 1
    """
    return True if random.random() < chance else False

#TODO: Refactor and unit testing?
def switch_state(current_state, pgb, pbg):
    """ Returns what the state should become with these parameters """
    if current_state == state.good:
        if _chance_test(pgb):
            return state.bad
        else:
            return state.good
    else:
        if _chance_test(pbg):
            return state.good
        else:
            return state.bad

def switch_bit(current_state, p):
    """ Returns whether a bit should be flipped for this state and chance """
    if current_state == state.bad:
        return _chance_test(p)
    return False

#TODO: Review enumerate choice?
def add_errors(message, current_state, p, pgb, pbg):
    """ Adds errors to simulate burst errors in ONE vector """
    for i,bit in enumerate(message):
        #First see if we switch state
        current_state = switch_state(current_state, pgb, pbg)
        #Then see if we switch any bits
        if switch_bit(current_state, p):
            #Python inverts integers strangely so we need this ternary
            message[i] = 0 if bit else 1
    return message

def add_errors_matrix(matrix, p, pgb, pbg, current_state=state.good):
    """ Adds errors into a matrix """
    res = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            #First see if we switch state
            current_state = switch_state(current_state, pgb, pbg)
            #Then see if we switch any bits
            if switch_bit(current_state, p):
                #Python inverts integers strangely so we need this ternary
                row.append(0 if matrix[i][j] else 1)
            else:
                row.append(matrix[i][j])
        res.append(row)
    return res

def generate_vectors(length, amount):
    """
    Generates amount vectors of length.
    For a (n,k,d) code this is the k parameter """
    return [\
            [random.randint(0,1) for i in range(length)] \
            for j in range(amount)
            ]

#TODO: Documentation, unit testing and refactoring
def calculate_percentage_same(original, recent):
    total = len(original)
    identical = 0
    for a,b in zip(original, recent):
        if a == b:
            identical = identical + 1
    return (float((100/total))*identical)
