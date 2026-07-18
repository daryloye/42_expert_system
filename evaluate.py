from utils import *
from tree import *


def evaluate_not(x):
    if x is Fact.TRUE:
        return Fact.FALSE
    elif x is Fact.FALSE:
        return Fact.TRUE
    else:
        return Fact.UNDETERMINED


def evaluate_and(left, right):
    if left is Fact.FALSE or right is Fact.FALSE:
        return Fact.FALSE
    elif left is Fact.UNDETERMINED or right is Fact.UNDETERMINED:
        return Fact.UNDETERMINED
    elif left is Fact.TRUE and right is Fact.TRUE:
        return Fact.TRUE
    else:
        return Fact.FALSE


def evaluate_or(left, right):
    if left is Fact.TRUE or right is Fact.TRUE:
        return Fact.TRUE
    elif left is Fact.UNDETERMINED or right is Fact.UNDETERMINED:
        return Fact.UNDETERMINED
    else:
        return Fact.FALSE


def evaluate_xor(left, right):
    if left is Fact.TRUE and right is Fact.FALSE:
        return Fact.TRUE
    elif left is Fact.FALSE and right is Fact.TRUE:
        return Fact.TRUE
    elif left is Fact.UNDETERMINED or right is Fact.UNDETERMINED:
        return Fact.UNDETERMINED
    else:
        return Fact.FALSE

    
def apply_operator(stack: list, operator: str):
    right = stack.pop()
    left = stack.pop()

    match operator:
        case '&':
            stack.append( evaluate_and(left, right) )
        case '|':
            stack.append( evaluate_or(left, right) )
        case '^':
            stack.append( evaluate_xor(left, right) )
        case _:
            raise Exception('invalid character: ', operator)


def evaluate_tree(op, variables) -> bool:
    match op.symbol:
        case '!':
            return evaluate_not(
                evaluate_tree(op.e1, variables)
            )
        case '&':
            return evaluate_and(
                evaluate_tree(op.e1, variables),
                evaluate_tree(op.e2, variables)
            )
        case '|':
            return evaluate_or(
                evaluate_tree(op.e1, variables),
                evaluate_tree(op.e2, variables)
            )
        case '^':
            return evaluate_xor(
                evaluate_tree(op.e1, variables),
                evaluate_tree(op.e2, variables)
            )
        case _:
            return variables[op.e1]["fact"]

