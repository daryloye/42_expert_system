import pytest
from evaluate import *


def test_evaluate_supports_all_binary_operators():
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False},
        'C': {'fact': Fact.TRUE, 'verified': False}
    }

    assert evaluate_tree(create_tree('AB&'), variables) is Fact.FALSE
    assert evaluate_tree(create_tree('AB|'), variables) is Fact.TRUE
    assert evaluate_tree(create_tree('AB^'), variables) is Fact.TRUE


def test_evaluate_raises_for_malformed_formula():
    variables = {
        'A': {'fact': Fact.TRUE, 'verified': False},
        'B': {'fact': Fact.FALSE, 'verified': False}
    }

    with pytest.raises(Exception):
        evaluate_tree(create_tree('&'), variables)

    with pytest.raises(Exception):
        evaluate_tree(create_tree('AB'), variables)

    with pytest.raises(Exception):
        evaluate_tree(create_tree('AB@'), variables)


def test_evaluate_not():
    assert evaluate_not(Fact.TRUE) is Fact.FALSE
    assert evaluate_not(Fact.FALSE) is Fact.TRUE
    assert evaluate_not(Fact.UNDETERMINED) is Fact.UNDETERMINED


def test_evaluate_or():
    assert evaluate_or(Fact.TRUE, Fact.UNDETERMINED) is Fact.TRUE
    assert evaluate_or(Fact.FALSE, Fact.UNDETERMINED) is Fact.UNDETERMINED
    assert evaluate_or(Fact.UNDETERMINED, Fact.FALSE) is Fact.UNDETERMINED


def test_evaluate_xor():
    assert evaluate_xor(Fact.TRUE, Fact.TRUE) is Fact.FALSE
    assert evaluate_xor(Fact.TRUE, Fact.FALSE) is Fact.TRUE
    assert evaluate_xor(Fact.FALSE, Fact.TRUE) is Fact.TRUE
    assert evaluate_xor(Fact.FALSE, Fact.FALSE) is Fact.FALSE
    assert evaluate_xor(Fact.TRUE, Fact.UNDETERMINED) is Fact.UNDETERMINED
    assert evaluate_xor(Fact.UNDETERMINED, Fact.FALSE) is Fact.UNDETERMINED


def test_evaluate_and():
    assert evaluate_and(Fact.TRUE, Fact.UNDETERMINED) is Fact.UNDETERMINED
    assert evaluate_and(Fact.UNDETERMINED, Fact.TRUE) is Fact.UNDETERMINED
    assert evaluate_and(Fact.FALSE, Fact.UNDETERMINED) is Fact.FALSE
    assert evaluate_and(Fact.UNDETERMINED, Fact.FALSE) is Fact.FALSE
