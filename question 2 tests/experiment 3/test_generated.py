def test_closest_integer(closest_integer):
    assert closest_integer("15.5") == 16, "Test 5"
    assert closest_integer("1.326") == 1, "Test 6"
def test_closest_integer(closest_integer):
    assert closest_integer("15.5") == 16, "Test 5"
    assert closest_integer("1.326") == 1, "Test 6"
def test_file_name_check(file_name_check):
    assert file_name_check("example.dll") == 'Yes'
    assert file_name_check("example") == 'No'
def test_find_closest_elements(find_closest_elements):
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.1]) == (2.0, 2.1)
def test_separate_paren_groups(separate_paren_groups):
    assert separate_paren_groups('()()((()))()') == ['()', '()', '((()))', '()']
    assert separate_paren_groups('()()((()))()((()())))') == ['()', '()', '((()))', '()', '((()())))']
