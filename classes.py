from enum import Enum

SYMBOLS = '!&|^>='
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Op:
    def __init__(self, symbol, e1, e2=''):
        self.symbol = symbol
        self.e1 = e1
        self.e2 = e2


class Fact(Enum):
    TRUE = 1
    FALSE = 2
    UNDETERMINED = 3


# Example Input:

# INPUT_RULES = [
#     {"l_string": "C", "r_string": "E"},
#     {"l_string": "ABC&&", "r_string": "D"},
#     {"l_string": "AB|", "r_string": "C"},
#     {"l_string": "AB!|", "r_string": "F"},
#     {"l_string": "CG!|", "r_string": "H"},
#     {"l_string": "VW^", "r_string": "X"},
#     {"l_string": "AB&", "r_string": "YZ&"},
#     {"l_string": "CD|", "r_string": "XV|"},
#     {"l_string": "EF&", "r_string": "V!"},
#     {"l_string": "AB&", "r_string": "C"},
#     {"l_string": "C", "r_string": "AB&"},
#     {"l_string": "AB&", "r_string": "C!"},
#     {"l_string": "C!", "r_string": "AB&"}
# ]

# INPUT_FACTS = ["A", "B", "G"]
INPUT_FACTS = []

# INPUT_QUERIES = ["G", "V", "X"]

INPUT_RULES = [
    {"l_string": "AB&", "r_string": "C"}
]