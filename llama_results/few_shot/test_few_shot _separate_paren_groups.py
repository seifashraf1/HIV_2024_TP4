from poly_llm.to_test.separate_paren_groups import separate_paren_groups

from typing import List
import pytest

# Your original implementation goes here...

@pytest.mark.parametrize("input_data", ["", " ", "(", ")", "()"])
def test_empty_or_incomplete_strings(input_data):
    assert separate_paren_groups(input_data) == []

@pytest.mark.parametrize("input_data", ["(", ")", "()", ")(", "))("])
def test_unbalanced_strings(input_data):
    # Expectation depends on whether you want to handle this gracefully or raise an exception
    pass

@pytest.mark.parametrize(["input_data", "expected"], [
    ("(a)", ["a"]),
    ("(abcd)", ["abcd"]),
    ("(a)(b)", ["a", "b"]),
    ("(a)(b)(c)", ["a", "b", "c"]),
    ("(a b c d e f g h i j k l m n o p q r s t u v w x y z)", ["a b c d e f g h i j k l m n o p q r s t u v w x y z"]),
    ("((a))", ["(a)"]),
    ("((a)(b))", ["(a)(b)"]),
    ("((a)(b)(c))", ["(a)(b)(c)"]),
    ("((a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z))", ["(a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z)"]),
    ("((a)((b)((c)((d)((e)((f)((g)((h)((i)((j)((k)((l)((m)((n)((o)((p)((q)((r)((s)((t)((u)((v)((w)((x)((y)((z))))))))))))))))))))))))", ["(a)((b)((c)((d)((e)((f)((g)((h)((i)((j)((k)((l)((m)((n)((o)((p)((q)((r)((s)((t)((u)((v)((w)((x)((y)((z))))))))))))))))))))))))"]),
])
def test_simple_cases(input_data, expected):
    actual = separate_paren_groups(input_data)
    assert len(actual) == len(expected)
    for item in actual:
        assert item in expected

@pytest.mark.parametrize(["input_data", "expected"], [
    ("((a)(b))", ["(a)", "(b)"]),
    ("((a)(b)(c))", ["(a)", "(b)", "(c)"]),
    ("((a)(b)(c)(d)(e)(f)(g)(h)(i)(j)(k)(l)(m)(n)(o)(p)(q)(r)(s)(t)(u)(v)(w)(x)(y)(z))", ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)", "(i)", "(j)", "(k)", "(l)", "(m)", "(n)", "(o)", "(p)", "(q)", "(r)", "(s)", "(t)", "(u)", "(v)", "(w)", "(x)", "(y)", "(z)"]),
    ("((a)((b)((c)((d)((e)((f)((g)((h)((i)((j)((k)((l)((m)((n)((o)((p)((q)((r)((s)((t)((u)((v)((w)((x)((y)((z))))))))))))))))))))))))", ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)", "(i)", "(j)", "(k)", "(l)", "(m)", "(n)", "(o)", "(p)", "(q)", "(r)", "(s)", "(t)", "(u)", "(v)", "(w)", "(x)", "(y)", "(z)"]),
])
def test_nested_cases(input_data, expected):
    actual = separate_paren_groups(input_data)
    assert len(actual) == len(expected)
    for item in actual:
        assert item in expected