import sys

from read import read
from parse import parse
from solve import solve
from utils import *
from pathlib import Path


def get_final_results(filename):
    raw_rules, facts, queries = read(filename)
    rules, variables, queries = parse(raw_rules, facts, queries)

    final_results = {}
    for x in queries:
        result = solve(x, rules, variables)
        final_results[x] = result.name
        print(f"{x}: {result.name}")
    
    return final_results


def get_interactive_temp_file(filename):
    tmp_path = Path(".tmp/" + filename)
    tmp_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filename, "r") as f1, open(tmp_path, "w") as f2:
        facts = input("Enter facts eg. \'ABC\': ")

        lines = f1.readlines()

        for line in lines:
            if line.strip().startswith('='):
                line = "=" + facts + "\n"
            f2.write(line)

    return tmp_path


if __name__ == "__main__":
    try:
        if len(sys.argv) == 3 and sys.argv[2] == '-i':
            temp_file = get_interactive_temp_file(sys.argv[1])
            final_results = get_final_results(temp_file)
            print()
            print_yellow(final_results)


        elif len(sys.argv) == 2:
            final_results = get_final_results(sys.argv[1])
            print()
            print_yellow(final_results)

        else:
            raise Exception("Usage: python main.py <input_file> [-i]")
        

    except Exception as e:
        print_red(f"Error: {e}")
        sys.exit(1)
