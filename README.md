# 42 Expert System

This project implements an expert system that reads a set of facts, rules, and queries, then determines the truth value of each query by evaluating the available rules.

## Components

### `read.py`

Reads the input text file and validates that:

- the file format is correct
- only supported characters are used
- input rules are valid

### `parse.py`

Parses the validated input and returns:

- an array of rules, where each rule contains a left-hand side string and a right-hand side string
	- In this array, LHS implies (=>) RHS
	- Hence if the imput has a rule X <=> Y, the array will break it into X => Y and Y => X
- a map of variables storing
	- `fact`: whether the variable is true, false or undetermined
	- `verified`: whether the variable has already been evaluated
- an array of queries


### `solve.py`

Solves each query using the parsed facts and rules.

For each query:

1. If the query has already been verified, return its current fact value.
2. Mark the query as verified.
3. If the query does not appear on the right-hand side of any rule, return its current fact value.
4. For each rule where the query appears on the right-hand side:
   - evaluate all other variables used in the rule;
   - solve the left-hand side of the rule;
   - skip the rule if the left-hand side is false or undetermined;
   - if the left-hand side is true, evaluate the right-hand side;
   - if the query can be either true or false without changing the result of the right-hand side, mark it as undetermined;
   - compare the query conclusion with conclusions from previous rules;
   - if there is a conflict, raise exception.
5. Return the final fact value.

## Testing 
```
pytest -q
```