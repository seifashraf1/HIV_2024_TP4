from poly_llm.to_test.find_closest_elements import find_closest_elements

def test_find_closest_elements():# pragma: no cover
    assert find_closest_elements([1.0, 2.2, 3.0, 4.0, 5.0]) == (2.2, 3.0)# pragma: no cover
    assert find_closest_elements([1.0, 2.0, 3.0, 4.4, 5.0, 6.0]) == (4.4, 5.0)# pragma: no cover
    assert find_closest_elements([1.0, 2.0, 3.0, 4.7, 5.0, 7.0]) == (4.7, 5.0)# pragma: no cover