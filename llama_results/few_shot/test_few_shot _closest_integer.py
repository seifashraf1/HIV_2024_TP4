from poly_llm.to_test.closest_integer import closest_integer
import pytest

# Your existing function definition goes here...

@pytest.mark.parametrize("number, expected", [
    ('10', 10),
    ('987654321', 987654321),
    ('+123', 123),
    ('-456', -456),
    ('0', 0),
])
def test_whole_numbers(number, expected):
    """Tests whole numbers represented as strings."""
    assert closest_integer(number) == expected

@pytest.mark.parametrize("number, expected", [
    ('1.1', 1),
    ('1.5', 2),
    ('1.9', 2),
    ('-1.1', -1),
    ('-1.5', -2),
    ('-1.9', -2),
])
def test_non_integers(number, expected):
    """Tests floating point values represented as strings."""
    assert closest_integer(number) == expected