import pytest
from main import get_final_results
from pathlib import Path


def e2e_test(filename, facts):
    tmp_path = Path(".tmp/" + filename)
    tmp_path.parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "r") as f1, open(tmp_path, "w") as f2:
        lines = f1.readlines()
        for line in lines:
            if line.strip().startswith('='):
                line = "=" + facts + "\n"
            f2.write(line)
    
    return get_final_results(tmp_path)


def test_AND_input():
    input_file = "./inputs/AND_input.txt"
    
    facts = "DEIJOP"
    expected_results = {
        'A': 'TRUE',
        'F': 'TRUE',
        'K': 'TRUE',
        'P': 'TRUE'
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "DEIJP"
    expected_results = {
        'A': 'TRUE',
        'F': 'TRUE',
        'K': 'FALSE',
        'P': 'TRUE'
    }
    assert e2e_test(input_file, facts) == expected_results


def test_OR_input():
    input_file = "./inputs/OR_input.txt"
    
    facts = ""
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "D"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "E"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "DE"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results


def test_XOR_input():
    input_file = "./inputs/XOR_input.txt"
    
    facts = ""
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "D"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "E"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "DE"
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results


def test_NOT_input():
    input_file = "./inputs/NOT_input.txt"
    
    facts = ""
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "B"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "C"
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "BC"
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results


def test_same_conclusion_input():
    input_file = "./inputs/same_conclusion_input.txt"
    
    facts = ""
    expected_results = {
        'A': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "B"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "C"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "BC"
    expected_results = {
        'A': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results


def test_parentheses_input():
    input_file = "./inputs/parentheses_input.txt"
    
    facts = ""
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "A"
    expected_results = {
        'E': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "B"
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "C"
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "AC"
    expected_results = {
        'E': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "BC"
    expected_results = {
        'E': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "F"
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "G"
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "H"
    expected_results = {
        'E': 'FALSE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "FH"
    expected_results = {
        'E': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results

    facts = "GH"
    expected_results = {
        'E': 'TRUE',
    }
    assert e2e_test(input_file, facts) == expected_results


def test_conflict_input():
    input_file = "./inputs/conflict_input.txt"
    
    with pytest.raises(Exception):
        get_final_results(input_file)
