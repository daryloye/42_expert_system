from classes import *


def create_stack(formula: str) -> Op:
    stack = []
    for c in formula:
        if c in LETTERS:
            stack.append( Op(c, c) )
        
        elif c == '!':
            if len(stack) < 1:
                raise Exception('not enough operands in input:', formula)
            stack.append( Op(c, stack.pop()) )

        elif c in '&|^>=':
            if len(stack) < 2:
                raise Exception('not enough operands in input:', formula)
            right = stack.pop()
            left = stack.pop()
            stack.append( Op(c, left, right) )

        else:
            raise Exception('invalid character in input:', formula)
        
    if len(stack) > 1:
        raise Exception('too many operands in input:', formula)
    
    return stack.pop()


def create_variables(input_rules: list, facts: list):
    variables = {
        c: {"fact": Fact.FALSE, "visited": False}
        for r in input_rules
        for c in r["l_string"] + r["r_string"]
        if c in LETTERS
    }

    for c in facts:
        variables[c] = {"fact": Fact.TRUE, "visited": False}
    
    return variables


# process_input creates a map of the rules and facts from the inputs
def process_input(input_rules: list, input_facts: list):
    rules = [{
        "l_string": rule["l_string"],
        "l_stack": create_stack( rule["l_string"] ),
        "r_string": rule["r_string"],
        "r_stack": create_stack( rule["r_string"] )
    } for rule in input_rules]

    variables = create_variables(input_rules, input_facts)

    return rules, variables
