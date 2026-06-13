from utils import *


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


def evaluate_formula(formula, variables) -> bool:
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


def infer_x_from_rule(x, rule, variables):
    lhs_result = evaluate_formula(rule["l_string"], variables)
    print_blue(f"- LHS result: {lhs_result}")
    
    # If LHS is false, then RHS cannot be inferred. Skip the rule
    if lhs_result is False:
        return Fact.NO_CONCLUSION

    # If LHS is true, then infer x from RHS
    original_fact = variables[x]["fact"]
    
    variables[x]["fact"] = Fact.TRUE
    rhs_result_with_x_true = evaluate_formula(rule["r_string"], variables)

    variables[x]["fact"] = Fact.FALSE
    rhs_result_with_x_false = evaluate_formula(rule["r_string"], variables)

    variables[x]["fact"] = original_fact

    match (rhs_result_with_x_true, rhs_result_with_x_false):
        case (True, False):
            print_blue(f"RHS is True when {x} is True")
            return Fact.TRUE
        case (False, True):
            print_blue(f"RHS is True when {x} is False")
            return Fact.FALSE
        case (True, True):
            print_blue(f"RHS is True when {x} is either True or False")
            return Fact.NO_CONCLUSION
        case (False, False):
            print_blue(f"Impossible for RHS to be True")
            return Fact.NO_CONCLUSION


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
        print_blue(f"{x} has already been verified as {variables[x]["fact"]}")
        return variables[x]["fact"]

	# Mark the query as verified
    variables[x]["verified"] = True

    # If x is not in RHS of any rule, then return the current fact
    if not any(x in r["r_string"] for r in rules):
        print_blue(f"Cannot find {x} in RHS of any rule, returning current fact")
        return variables[x]["fact"]

    # Check rules where x is in RHS
    current_fact = variables[x]["fact"]
    variables[x]["fact"] = Fact.NO_CONCLUSION
    
    for rule in rules:
        if x not in rule["r_string"]:
            continue
        
        print_blue(f"- Found {x} on RHS of rule: {rule["l_string"]} => {rule["r_string"]}")

        solve_dependencies(x, rule, rules, variables)

        inferred = infer_x_from_rule(x, rule, variables)
        if inferred is Fact.NO_CONCLUSION:
            print_blue(f"Cannot infer {x} from this rule")
            continue
        
        # Check if any conflict with previous rules
        if variables[x]["fact"] is not Fact.NO_CONCLUSION and variables[x]["fact"] is not inferred:
            print_blue(f"Conflict with previous rule, setting {x} to Undetermined")
            variables[x]["fact"] = Fact.UNDETERMINED
            return Fact.UNDETERMINED

        print_blue(f"Setting {x} to be {inferred}\n")
        variables[x]["fact"] = inferred
        current_fact = inferred
    
    print_blue(f"Returning current fact")
    variables[x]["fact"] = current_fact
    return current_fact