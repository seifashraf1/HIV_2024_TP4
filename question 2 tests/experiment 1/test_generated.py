def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("10") == 10, "Test 1"

def test_file_name_check(file_name_check):
    assert file_name_check("example.txt") == 'Yes'
    assert file_name_check("example.dll") == 'Yes'

def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)

def test_separate_paren_groups(numerical_letter_grade):
    assert numerical_letter_grade([4.0]) == ['A+']
    assert numerical_letter_grade([3.0, 2.0, 1.0]) == ['A', 'B', 'C']
    assert numerical_letter_grade([3.0, 2.0, 1.0, 0.0]) == ['A', 'B', 'C', 'D']
    assert numerical_letter_grade([3.0, 2.0, 1.0, 0.0, 4.0]) == ['A', 'B', 'C', 'D', 'E']
    assert numerical_letter_grade([3.0, 2.0, 1.0, 0.0, 4.0, 5.0]) == ['A', 'B', 'C', 'D', 'E', 'F']
    assert numerical_letter_grade([3.0, 2.0, 1.0, 0.0, 4.0, 5.0, 6.0]) == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    assert numerical_letter_grade([3.0, 2.0, 1.0, 0.0, 4.0, 5.0, 6.0, 7.0]) == ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def test_separate_paren_groups(separate_paren_groups):
    assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
    assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']


