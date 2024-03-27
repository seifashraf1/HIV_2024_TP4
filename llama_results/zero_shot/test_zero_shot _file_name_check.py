from poly_llm.to_test.file_name_check import file_name_check
import pytest

@pytest.mark.parametrize("filename", [".txt", "..txt"])
def test_empty_prefix(filename):
    """Check filenames without prefix."""
    result = file_name_check(filename)
    expected = "No"
    assert result == expected

@pytest.mark.parametrize("suffix", ["png", ".jpg", ""])
def test_wrong_extension(suffix):
    """Check filenames with wrong extensions."""
    filename = f"hello{suffix}"
    result = file_name_check(filename)
    expected = "No"
    assert result == expected

@pytest.mark.parametrize("filename", ["a.txt", "abcd.exe", "myfile.dll"])
def test_valid_filenames(filename):
    """Check valid filenames."""
    result = file_name_check(filename)
    expected = "Yes"
    assert result == expected

@pytest.mark.parametrize("filename", ["123.txt", "a1b2c3d4e5.exe"])
def test_too_many_digits(filename):
    """Check filenames with too many digits."""
    result = file_name_check(filename)
    expected = "No"
    assert result == expected

@pytest.mark.parametrize("filename", ["$%^&*().txt", "-=[]{}();'.exe"])
def test_special_characters(filename):
    """Check filenames with special characters."""
    result = file_name_check(filename)
    expected = "No"
    assert result == expected

if __name__ == "__main__":
    pytest.main(['-v'])