import sys

from read import read
from parse import parse
from solve import solve
from utils import *


def get_final_results(filename):
    raw_rules, facts, queries = read(filename)
    rules, variables, queries = parse(raw_rules, facts, queries)

    final_results = {}
    for x in queries:
        result = solve(x, rules, variables)
        final_results[x] = result.name
        print(f"{x}: {result.name}")
    
    return final_results


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("Usage: python main.py <input_file>")
        
        final_results = get_final_results(sys.argv[1])
        print()
        print_yellow(final_results)

    except Exception as e:
        print_red(f"Error: {e}")
        sys.exit(1)
