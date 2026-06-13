from read import *
from parse import *
from solve import *
from utils import *

# def apply_operator(stack: list, operator: str):
#     right = stack.pop()
#     left = stack.pop()

#     match operator:
#         case '&':
#             stack.append(left & right)
#         case '|':
#             stack.append(left | right)
#         case '^':
#             stack.append(left ^ right)
#         case '>':
#             stack.append((not left) | right)
#         case '=':
#             stack.append(left == right)
#         case _:
#             raise Exception('invalid character: ', operator)


# def solve(formula, variables) -> bool:
#     validate_args(formula)

#     stack = []
#     for c in formula:
#         if c in LETTERS:
#             stack.append(variables[c]["fact"] == Fact.TRUE)
        
#         elif c == '!':
#             if len(stack) < 1:
#                 raise Exception('not enough operands')
#             stack.append(not stack.pop())
        
#         else:
#             if len(stack) < 2:
#                 raise Exception('not enough operands')
#             apply_operator(stack, c)
        
#     if len(stack) > 1:
#         raise Exception('too many operands')
    
#     return stack.pop()


if __name__ == "__main__":
    try:
        read()
        rules, variables, queries = parse()

        print_yellow("RULES:")
        print_yellow(rules)
        print()
        print_yellow("VARIABLES:")
        print_yellow(variables)
        print()
        print_yellow("QUERIES:")
        print_yellow(queries)
        print()

        for x in queries:
            print_red(f"Solving for: {x}")
            result = solve(x, rules, variables)
            print_green(f"{x} is {result}\n")

    except Exception as e:
        print(f"Error: {e}")