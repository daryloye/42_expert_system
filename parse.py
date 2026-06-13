from utils import *


def create_variables(rules: list, queries: list, facts: list):
    variables = {
        c: {"fact": Fact.FALSE, "verified": False}
        for r in rules
        for c in r["l_string"] + r["r_string"]
        if c in LETTERS
    }

    for c in queries:
        variables[c] = {"fact": Fact.FALSE, "verified": False}

    for c in facts:
        variables[c] = {"fact": Fact.TRUE, "verified": True}
    
    return variables


def parse():
    rules = [{
        "l_string": rule["l_string"],
        "r_string": rule["r_string"],
    } for rule in INPUT_RULES]

    variables = create_variables(INPUT_RULES, INPUT_QUERIES, INPUT_FACTS)

    queries = INPUT_QUERIES

    return rules, variables, queries


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
INPUT_FACTS = ["A"]

INPUT_QUERIES = ["C"]

INPUT_RULES = [
    {"l_string": "AB|", "r_string": "CB&"},
    # {"l_string": "AB|", "r_string": "C!"},
]