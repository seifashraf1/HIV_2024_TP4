from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade


def test_numerical_letter_grade():
    # Test case with valid inputs
    assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']

    # Test case with invalid input
    assert numerical_letter_grade([1.2]) == ['D+']