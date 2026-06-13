from enum import Enum

SYMBOLS = '!&|^>='
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Fact(Enum):
    TRUE = 1
    FALSE = 2
    NONE = 3
    UNDETERMINED = 4

def print_red(s):
    print(f"\033[31m{s}\033[0m")

def print_green(s):
    print(f"\033[32m{s}\033[0m")

def print_yellow(s):
    print(f"\033[33m{s}\033[0m") 

def print_blue(s):
    print(f"\033[34m{s}\033[0m") 