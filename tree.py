from utils import *

LETTER = 'LETTER'

class Op:
    def __init__(self, symbol, e1, e2=''):
        self.symbol = symbol
        self.e1 = e1
        self.e2 = e2
    
    def to_string(self) -> str:
        match self.symbol:
            case '!':
                return self.e1.to_string() + '!'
            case '&' | '|' | '^' :
                return self.e1.to_string() + self.e2.to_string() + self.symbol      
            case LETTER:
                return self.e1
    
    def has_elem(self, e: str) -> bool:
        if self.symbol == LETTER:
            return (self.e1 == e)
        else:
            return (self.e1 and self.e1.has_elem(e)) or (self.e2 and self.e2.has_elem(e))


def create_tree(formula: str) -> Op:
    stack = []
    for c in formula:
        if c in LETTERS:
            stack.append( Op(LETTER, c) )
        
        elif c == '!':
            if len(stack) < 1:
                raise Exception('not enough operands')
            stack.append( Op(c, stack.pop()) )

        elif c in '&|^':
            if len(stack) < 2:
                raise Exception('not enough operands')
            right = stack.pop()
            left = stack.pop()
            stack.append( Op(c, left, right) )

        else:
            raise Exception('invalid character')
        
    if len(stack) > 1:
        raise Exception('too many operands')
    
    return stack.pop()
