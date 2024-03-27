from poly_llm.to_test.separate_paren_groups import separate_paren_groups

import pytest

PAREN_STRINGS = [
    ("((()))", ["((()))"]),
    ("(()())", ["(()())"]),
    ("()()()", ["()", "()", "()"]),
    ("((()()))", ["((()()))"]),
    ("()(()())", ["()", "(()())"]),
    ("()((()))", ["()", "((()))"]),
    ("()()((()))", ["()", "()", "((()))"]),
    ("()()((()))()", ["()", "()", "((()))", "()"]),
    ("()()((()))()((()()))", ["()", "()", "((()))", "()", "((()()))"]),
]

@pytest.mark.parametrize("paren_string,expected", PAREN_STRINGS)
def test_separated_strings(paren_string, expected):
    result = separate_paren_groups(paren_string)
    assert result == expected

NESTING_ERRORS = [
    ('(', IndexError),
    (')', IndexError),
    (')))', IndexError),
    ('((((', IndexError),
    ('()))))', IndexError),
    ('()()()((()))()', IndexError),
]

@pytest.mark.parametrize("nesting_error", NESTING_ERRORS)
def test_nesting_errors(nesting_error):
    paren_string, error = nesting_error
    with pytest.raises(error):
        separate_paren_groups(paren_string)
