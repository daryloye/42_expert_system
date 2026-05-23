from classes import *
from process_input import *
from utils import *

def validate_args(formula: str):
    if len(formula) == 0:
        raise Exception("empty formula")
    if not all(c in SYMBOLS or c in LETTERS for c in formula):
        raise Exception("invalid character:", formula)


def apply_operator(stack: list, operator: str):
    right = stack.pop()
    left = stack.pop()

    match operator:
        case '&':
            stack.append(left & right)
        case '|':
            stack.append(left | right)
        case '^':
            stack.append(left ^ right)
        case '>':
            stack.append((not left) | right)
        case '=':
            stack.append(left == right)
        case _:
            raise Exception('invalid character: ', operator)


def solve(formula, variables) -> bool:
    validate_args(formula)

    stack = []
    for c in formula:
        if c in LETTERS:
            stack.append(variables[c]["fact"] == Fact.TRUE)
        
        elif c == '!':
            if len(stack) < 1:
                raise Exception('not enough operands')
            stack.append(not stack.pop())
        
        else:
            if len(stack) < 2:
                raise Exception('not enough operands')
            apply_operator(stack, c)
        
    if len(stack) > 1:
        raise Exception('too many operands')
    
    return stack.pop()


def fact_check(x, rules, variables):
    print()
    print_green(f"Solving for: {x}")

    # If x has already been visited, then return the fact
    if variables[x]["visited"] is True:
        return variables[x]["fact"]

    # If x is not in RHS of any rule, then return the initial fact
    if not any(x in r["r_string"] for r in rules):
        print_yellow(f"Cannot find {x} in RHS of any rule, returning initial fact")
        variables[x]["visited"] = True
        return variables[x]["fact"]

    # Check if x is in r_string of any rule
    for rule in rules:
        if x not in rule["r_string"]:
            continue
        
        print(f"Found {x} on RHS of rule: {rule["l_string"]} => {rule["r_string"]}")

        # solve other variables
        other_variables = set(rule["l_string"] + rule["r_string"]) - set(SYMBOLS) - set(x)
        print("Other variables:", other_variables)
        
        for v in other_variables:
            result = fact_check(v, rules, variables)
            print_green(f"{v} is {result}")

        lhs_result = solve(rule["l_string"], variables)
        print("LHS result:", lhs_result)
        

    variables[x]["visited"] = True
    return variables[x]["fact"]


if __name__ == "__main__":
    rules, variables = process_input(INPUT_RULES, INPUT_FACTS)

    print_blue("RULES:")
    print_blue(rules)
    print()
    print_yellow("VARIABLES:")
    print_yellow(variables)
    print()

    query = ["C"]
    for x in query:
        result = fact_check(x, rules, variables)
        print_green(f"{x} is {result}")