from poly_llm.to_test.closest_integer import closest_integer

from pytest import raises

# Defining our testing functions
def test_positive_integers():
    assert closest_integer('1') == 1
    assert closest_integer('987654321') == 987654321
    assert closest_integer('+123') == 123

def test_negative_integers():
    assert closest_integer('-456') == -456

def test_floats():
    assert closest_integer('1.0') == 1
    assert closest_integer('1.1') == 1
    assert closest_integer('1.4999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999') == 2

def test_halfway_cases():
    assert closest_integer('14.5') == 15
    assert closest_integer('-14.5') == -15

def test_invalid_inputs():
    with raises(ValueError):
        closest_integer('abc')
    with raises(TypeError):
        closest_integer([])
    with raises(AttributeError):
        closest_integer({})