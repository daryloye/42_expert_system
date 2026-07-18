from utils import *
from evaluate import *


def infer_x_from_rule(x, rule, variables):
    lhs_result = evaluate(rule["l_string"], variables)
    print_blue(f"- LHS result: {lhs_result}")
    
    # If LHS is false, then RHS cannot be inferred. Skip the rule
    if lhs_result in (Fact.FALSE, Fact.UNDETERMINED):
        print_blue(f"Cannot infer {x} from this rule")
        return None

    # If LHS is true, then infer x from RHS
    original_fact = variables[x]["fact"]
    
    # Compare RHS result with x being true / false
    variables[x]["fact"] = Fact.TRUE
    rhs_result_with_x_true = evaluate(rule["r_string"], variables)

    variables[x]["fact"] = Fact.FALSE
    rhs_result_with_x_false = evaluate(rule["r_string"], variables)

    variables[x]["fact"] = original_fact

    print_blue(f"RHS if {x} is true: {rhs_result_with_x_true} | RHS if {x} is false: {rhs_result_with_x_false}")
    match (rhs_result_with_x_true, rhs_result_with_x_false):
        case (Fact.TRUE, Fact.FALSE):
            return Fact.TRUE
        case (Fact.TRUE, Fact.UNDETERMINED):
            return Fact.TRUE
        case (Fact.FALSE, Fact.TRUE):
            return Fact.FALSE
        case (Fact.UNDETERMINED, Fact.TRUE):
            return Fact.FALSE
        case (Fact.FALSE, Fact.FALSE):
            print_red(f"Impossible for RHS to be True")
            return Fact.UNDETERMINED
        case _:
            return Fact.UNDETERMINED
    

def solve_dependencies(x, rule, rules, variables):
    dependents = set(rule["l_string"] + rule["r_string"]) - set(SYMBOLS) - set(x)
    print_blue(f"Dependent variables: {dependents}\n")
        
    for v in dependents:
        print_blue(f"-- Solving for: {v}")
        result = solve(v, rules, variables)
        print_green(f"{v} is {result}\n")


def solve(x, rules, variables):
    # If x has already been verified, then return the fact
    if variables[x]["verified"] is True:
        print_blue(f"{x} has already been verified as {variables[x]['fact']}")
        return variables[x]["fact"]

    # Mark cyclic dependencies as undetermined
    if variables[x]["fact"] is None:
        print_blue(f"{x} is cyclic dependency, marking as undetermined")
        variables[x]["fact"] = Fact.UNDETERMINED
        return variables[x]["fact"]

    # If x is not in RHS of any rule, then return the current fact
    if not any(x in r["r_string"] for r in rules):
        print_blue(f"Cannot find {x} in RHS of any rule, returning current fact")
        variables[x]["verified"] = True
        return variables[x]["fact"]

    # Check rules where x is in RHS
    current_fact = variables[x]["fact"]
    variables[x]["fact"] = None
    
    for rule in rules:
        if x not in rule["r_string"]:
            continue
        
        print_blue(f"- Found {x} on RHS of rule: {rule['l_string']} => {rule['r_string']}")

        solve_dependencies(x, rule, rules, variables)

        inferred = infer_x_from_rule(x, rule, variables)
        if inferred is None:
            continue
        
        # Check if any conflict with previous rules
        if variables[x]["fact"] not in (None, Fact.UNDETERMINED, inferred):
            raise Exception(f"Conflict with previous rule")

        print_blue(f"Setting {x} to be {inferred}\n")
        variables[x]["fact"] = inferred
        current_fact = inferred
    
    print_blue(f"Returning current fact: {current_fact}")
    variables[x]["fact"] = current_fact
    variables[x]["verified"] = True
    return current_fact