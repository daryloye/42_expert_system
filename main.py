import sys

from read import read
from parse import parse
from solve import solve
from utils import Fact


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("Usage: python main.py <input_file>")

        raw_rules, facts, queries = read(sys.argv[1])
        rules, variables, queries = parse(raw_rules, facts, queries)

        for x in queries:
            result = solve(x, rules, variables)
            print(f"{x}: {result.name}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
