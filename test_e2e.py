from read import read
from parse import parse
from solve import solve
from utils import *
from main import get_final_results


def test_AND_input_1():
    input_file = "./inputs/AND_input_1.txt"
    expected_results = {
        'A': 'TRUE',
        'F': 'TRUE',
        'K': 'TRUE',
        'P': 'TRUE'
    }

    test_results = get_final_results(input_file)
    assert test_results == expected_results


def test_AND_input_2():
    input_file = "./inputs/AND_input_2.txt"
    expected_results = {
        'A': 'TRUE',
        'F': 'TRUE',
        'K': 'FALSE',
        'P': 'TRUE'
    }

    test_results = get_final_results(input_file)
    assert test_results == expected_results

