def test_closest_integer(closest_integer):
    assert closest_integer("10") == 10
    assert closest_integer("15.3") == 15
    assert closest_integer("14.5") == 15
    assert closest_integer("-14.5") == -15

#check if the last character is a  ) and if not add ') == 'NO'
if test[-1] != "'":
    #remove any trailing spaces or '\n'
    test = test.rstrip()
    test += "') == 'NO'"
print(test)