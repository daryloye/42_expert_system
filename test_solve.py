import pytest
from solve import *


def test_if_query_is_verified_then_return_current_fact():
    rules = [
        {'l_string': 'AB&', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.TRUE, 'verified': True}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE


def test_if_query_is_not_in_RHS_of_any_rule_then_return_current_fact():
    rules = [
        {'l_string': 'AB&', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False},
        'D': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'D'

    assert solve(x, rules, variables) == Fact.FALSE


def test_if_LHS_is_false_then_skip_rule():
    rules = [
        {'l_string': 'AB&', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.FALSE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.FALSE


def test_if_LHS_is_true_then_infer_query():
    rules = [
        {'l_string': 'AB&', 'r_string': 'C'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.TRUE


def test_if_conflicting_rules_then_x_is_unknown():
    rules = [
        {'l_string': 'AB&', 'r_string': 'C'},
        {'l_string': 'AB&', 'r_string': 'C!'}
    ]
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.TRUE, 'verified': False},
        'C': {'fact': Fact.FALSE, 'verified': False}
    }
    x = 'C'

    assert solve(x, rules, variables) == Fact.UNDETERMINED
