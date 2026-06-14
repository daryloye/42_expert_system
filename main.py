from read import *
from parse import *
from solve import *
from utils import *


if __name__ == "__main__":
    try:
        read()
        rules, variables, queries = parse()

        print_yellow(f"RULES: {rules}\n")
        print_yellow(f"VARIABLES: {variables}\n")
        print_yellow(f"QUERIES: {queries}\n")

        for x in queries:
            print_red(f"Solving for: {x}")
            result = solve(x, rules, variables)
            print_red(f"{x} is {result}\n")

    except Exception as e:
        print(f"Error: {e}")