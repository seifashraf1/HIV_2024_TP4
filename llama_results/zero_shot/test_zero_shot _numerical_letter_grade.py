from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
import pytest

GRADES = [(4.0, "A+"), (3.9, "A"), (3.8, "A-"), (3.7, "B+")]

@pytest.mark.parametrize("gpa,expected", GRADES)
def test_single_student(gpa, expected):
    grade = numerical_letter_grade([gpa])
    assert grade == [expected]

MULTIPLE_GPAS = [[4.0, 3.9, 3.8, 3.7]]
EXPECTED_RESULTS = [["A+", "A", "A-", "B+"]]

@pytest.mark.parametrize("multiple_gpas,expected_results", zip(MULTIPLE_GPAS, EXPECTED_RESULTS))
def test_multiple_students(multiple_gpas, expected_results):
    results = numerical_letter_grade(multiple_gpas)
    assert results == expected_results

INVALID_GPAS = [-1, 0, .7, 1.3, 1.7, 2.3, 2.7, 3.3, 3.7, 4.0]

@pytest.mark.parametrize("invalid_gpa", INVALID_GPAS)
def test_invalid_values(invalid_gpa):
    with pytest.raises(Exception):
        numerical_letter_grade([invalid_gpa])

if __name__ == "__main__":
    pytest.main(['-v'])