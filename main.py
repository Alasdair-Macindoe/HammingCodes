import argparse
import state as st

"""
===============================================================================
This section overrides some of the built in types, for example we create
a new integer object called int which will be called over the default int
===============================================================================
"""

#Redefined the default int implementation (sort-of)
class int(int):
    """
    This class is a subclass of the built in int type.
    It redefines addition from the real field to the binary field ({0,1})
    """
    def __add__(self, other):
        """
        Redefine integer addition to be over the field {0,1}
        Which is just a logical XOR. This works so long as both
        parameters are either 1 or 0.
         """
        return self ^ other


class list(list):
    """
    This class is a subclass of the built in list type.
    It redefines addition of two lists to be elementwise.
    """
    def __add__(self, other):
        """
        Defines elementwise addition for two lists
        """
        for row in self:
            return [int(self[i]) + int(other[i]) for i in range(len(self))]


#Refactor, pythonic etc.
#TODO: This probably need redeveloped
class binary_matrix(list):
    """
    A list implementation for a n-dimension list over the binary field, with
    addition defined as XOR (and therefore multiplication defined as AND).
    """
    def __matmul__(self, other):
        """ Allows us to use the '@' operator on our lists over our field """
        res = [0 for i in range(len(other[0]))]
        for i in range(len(self[0])):
            if self[0][i] == 1:
                res = list(res) + list(other[i])
        return res


    def __mul__(self, other):
        """
        Allows you to use both the multiplication sign and PEP-465 defined
        matrix multiplication sign for our matrix multiplications.
        """
        return binary_matrix.__matmul__(self, other)


"""
===============================================================================
Helper (Internal) methods.
===============================================================================
"""


def _get_row(row):
    """
    Takes a (binary) string (without spaces) and converts it in a row with
    those values
    """
    return [int(v) for v in row]

def _get_binary(v,r):
    """
    Returns the binary representation of a given number with spaces between
    each character
    """
    return bin(v) \
                .lstrip('0b') \
                .zfill(r)

def pretty_print(a):
    """
    Print out a n-dimensional structure on rows.
    """
    for row in a:
        print(row)

def create_binary_matrix(a):
    """
    Takes a list and converts it to a new binary matrix
    """
    return binary_matrix(a)

def _convert_to_code(input, k):
    """ Converts a binary string into words of k length """
    current = 0
    res = []
    #Need it to round downwards
    for i in range(int(len(input)/k)):
        row = [int(e) for e in list(input[current:current+k])]
        res.append(row)
        current = current + k
    return res

"""
===============================================================================
This section is where we implement the actual Hamming code implementation.
===============================================================================
"""


def identity(r):
    """
    Returns the standard identity matrix Ir.
    NOTE: This is the identity matrix over the REAL field.
    Not the binary field.
    This means e * Ir != e for some e from a group within the binary field.
    """
    return binary_matrix([ \
            [int(1) if i == j else int(0) for j in range(r)] \
            for i in range(r)])

def span_from_identity(r):
    """
    Creates the finite spanning set of the identity matrix of size r of the
    reals. This is equivalent to the basis of the group of code words.
    Always has the identity at the bottom.
    """
    #We can do this efficiently by realising that in this field we are just
    #generating the integers from 1 to 2^r -1
    max = (2 ** r) - 1
    #We then want the values that will form the identity values and handle them
    #differently so they are at the bottom
    identity_values = list([2 ** i for i in range(0,r)])
    #Find the values that are not the identity values and get their binary
    values = list([i for i in range(1, max+1) if i not in identity_values])
    values = [reversed(_get_binary(i,r)) for i in values]
    #Generate the top of our binary matrix with those values
    spanning_set = [_get_row(row) for row in values]
    #Get the the binary of the identity values in reverse order
    identity_values = [_get_binary(i,r) for i in reversed(identity_values)]
    #Append those to the bottom and return our span
    [spanning_set.append(_get_row(row)) for row in identity_values]
    return binary_matrix(spanning_set)

def get_parity_check(r):
    """
    Returns the parity check matrix for our given r parameter
    """
    return span_from_identity(r)

def span_without_basis(r):
    """
    Returns the span created by the identity matrix over the reals without
    the basis (ie without I_r itself)
    """
    span_I_r = span_from_identity(r)
    I_r = identity(r)
    [span_I_r.remove(row) for row in I_r]
    return span_I_r

def create_generator_matrix(r,k):
    """
    Creates a generator matrix for our code
    """
    I_k = identity(k)
    span_I_r = span_without_basis(r)
    [[e.append(value) for value in s] for e,s in zip(I_k, span_I_r)]
    return binary_matrix(I_k)

def get_encoding(a,b):
    """
    Encodes the multiplication of two matrices.
    One should be the binary to encode, and the other a generator matrix.
    """
    return a@b

def do_parity_check(a,H):
    """
    Returns True if an element a is in the set checked by H, and
    false otherwise
    """
    zero_matrix = [0 for i in range(len(H[0]))]
    return True if get_encoding(a, H) == zero_matrix else False

def interleave(messages):
    """ Interleaves a set of code words """
    return [[row[i] for row in messages] for i in range(len(messages[0]))]

#TODO: Documentation - and what if len(messages) % n != 0
def interleave_for_size(messages, n):
    current = 0
    length = len(messages)
    res = []
    while current < length:
        res.append(interleave(messages[current:current+n]))
        current = current + n
    return res;


#TODO: Refactor, pythonic.
def calculate_int(row):
    """ Calculates the integer value of a binary String """
    #Special case, if we are just given an integer
    if (type(row) == type(1)):
         return row
    res = 0
    row = list(reversed(row))
    for r in range(len(row)):
        if row[r] == 1:
            res = res + 2**r
    return res

#TODO: Refactoring, pythonic
def create_syndrome_dict(n,r,t=1):
    """ Creates the syndrome dictionary """
    H = get_parity_check(r)
    s_values = [2 ** i for i in range(n)]
    res = {}
    for s in s_values:
        binary = binary_matrix([_get_row(_get_binary(s,n))])*H
        res[calculate_int(binary)] = s
    res[0] = 0
    return res

def calculate_syndrome(v,H):
    """ Calculates the value of a syndrome """
    return binary_matrix(v*H)

#TODO: Review this logic
def decode_syndrome(v, syndromes, H):
    """
    Decodes the value a syndrome would be.
    v is the value recieved,
    syndromes is the dictionary of syndromes,
    H is the parity check matrix
    """
    vH = calculate_syndrome(v, H)
    row = _get_row(_get_binary(syndromes[calculate_int(vH)], len(v[0])))
    return list(v[0]) + list(row)


"""
===============================================================================
Parse arguments
===============================================================================
"""

def parse():
    """
    Manages command line parsing.
    Variable names are not imemediately clear:

    r = number of parity bits in our Hamming code,
    n = number of bits in the Hamming code (2 ^ r - 1)
    k = number of "information" bits (2 ^ r - r -1)
    d = minimum distance corrected (Hamming codes can only correct 1 error)
    p = probability of a bit being flipped whilst in the bad state
    q = probability of a bit NOT being flipped whilst in the bad state (1 - p)
    pgb = probability of jumping to the bad state from the good state
    pgg = probability of staying in good state (1 - pgb)
    pbg = probability of jumping to the good state from the bad state
    pbb = probability of staying in the bad state (1 - pbg)
    i = input string
    b = optional interleaving
    ni = number to interleave to
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', type=int, default=3,
                        help='Number of parity bits for a Hamming code. \
                        Note: This value determines n and k')
    parser.add_argument('-p', type=float, default=0.0, help="Probability of \
                        a bit being flipped whilst in the bad state")
    parser.add_argument('-pgb', type=float, default=0.0, help="Probability of \
                        jumping from the good state to the bad state")
    parser.add_argument('-pbg', type=float, default=1.0, help="Probability of \
                        jumping from the bad state to the good state")
    parser.add_argument('-i', type=str, default="1011", help="A binary string \
                        to be input")
    parser.add_argument('-b', type=bool, default=False, help="To interleave \
                        or not to interleave")
    parser.add_argument('-ni', type=int, default=0, help="Number of interleave")
    args = vars(parser.parse_args()) #Convert our argparse object to a dict
    #Calculate the rest of the values
    args['pgg'] = 1.0 - args['pgb']
    args['pbb'] = 1.0 - args['pbg']
    args['q'] = 1.0 - args['p']
    args['n'] = 2 ** args['r'] - 1
    args['k'] = args['n'] - args['r']
    args['d'] = 1
    #By default this looks something like:
    #{'pgb': 0.0, 'p': 0.0, 'pgg': 1.0, 'pbb': 0.0, 'pbg': 1.0, 'q': 1.0,
    #                                           'd': 1, 'r': 3, 'n': 7, 'k': 4}
    #Step 1: Convert the input into a matrix of element of size k
    args['i'] = _convert_to_code(args['i'], args['k'])
    print("Split into: {}".format(args['i']))
    #Step 2: Generate code words
    G = create_generator_matrix(args['r'],args['k'])
    code_words = []
    for e in args['i']:
        code_words.append(get_encoding(binary_matrix([e]),G))
    print("Code words: {}".format(code_words))
    #Step 3: Test for interleaving
    if(args['b']):
        if(args['ni']):
            code_words = interleave_for_size(code_words,args['ni'])
        else:
            code_words = interleave(code_words)
        print("Interleaved code words: {}".format(code_words))
    #Step 4: Add errors
    if(args['b']):
        code_words = st.add_errors_matrix(code_words,args['p'],args['pgb'],\
                                            args['pbb'])
        if(args['ni']):
            code_words = interleave_for_size(code_words,args['ni'])
        else:
            code_words = interleave(code_words)
    else:
        code_words = st.add_errors_matrix(code_words,args['p'],args['pgb'],\
                                            args['pbb'])
    print("With errors: {}".format(code_words))
    #Step 5: Find syndromes
    syndromes = create_syndrome_dict(args['n'], args['r'])
    H = get_parity_check(args['r'])
    print(code_words[0])
    syn_list = [decode_syndrome(binary_matrix([c]), syndromes, H) for c in code_words]
    print("Results: {}".format(syn_list))

#Always invoke parse
if __name__=="__main__":
    parse()
