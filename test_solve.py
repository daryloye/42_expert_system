from solve import *
import pytest


def test_if_query_is_verified_then_return_current_fact():
    rules = [
        {'l_string': 'A', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.TRUE, 'verified': True}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE


def test_if_query_is_not_in_RHS_of_any_rule_then_return_current_fact():
    rules = [
        {'l_string': 'A', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False},
        'D': {'fact': Fact.TRUE, 'verified': False}
    }
    x = 'D'

    assert solve(x, rules, variables) == Fact.TRUE


def test_if_LHS_is_false_then_skip_rule():
    rules = [
        {'l_string': 'A', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.FALSE


def test_if_RHS_requires_query_to_be_true_then_infer_true():
    rules = [
        {'l_string': 'A', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE
    

def test_if_RHS_requires_query_to_be_false_then_infer_false():
    rules = [
        {'l_string': 'A', 'r_string': 'C!'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.TRUE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.FALSE


def test_if_RHS_is_ambiguous_then_infer_undetermined():
    rules = [
        {'l_string': 'A', 'r_string': 'CB|'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.UNDETERMINED


def test_if_fact_is_ambiguous_then_infer_undetermined():
    rules = [
        {'l_string': 'A', 'r_string': 'CB&'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.UNDETERMINED, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.UNDETERMINED


def test_if_conflicting_rules_then_raise_error():
    rules = [
        {'l_string': 'A', 'r_string': 'B'},
        {'l_string': 'A', 'r_string': 'B!'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'B'

    with pytest.raises(Exception):
        solve(x, rules, variables)


def test_if_RHS_is_impossible_for_query_true_or_false_then_query_is_undetermined():
    rules = [
        {'l_string': 'A', 'r_string': 'CC!&'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.UNDETERMINED


def test_if_query_depends_on_another_rule_then_solve_dependency_first():
    rules = [
        {'l_string': 'A', 'r_string': 'B'},
        {'l_string': 'B', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE


def test_if_multiple_rules_infer_same_fact_then_query_is_not_conflicting():
    rules = [
        {'l_string': 'A', 'r_string': 'C'},
        {'l_string': 'B', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE


def test_cylic_dependencies_does_not_recurse_forever():
    rules = [
        {'l_string': 'A', 'r_string': 'B'},
        {'l_string': 'B', 'r_string': 'A'},
        {'l_string': 'AC&', 'r_string': 'D'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.TRUE, 'verified': True},
        'D': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'D'

    assert solve(x, rules, variables) == Fact.FALSE


def test_if_inference_from_first_rule_is_ambiguous_and_second_is_deterministic_then_override():
    rules = [
        {'l_string': 'A', 'r_string': 'CB|'},
        {'l_string': 'A', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE
