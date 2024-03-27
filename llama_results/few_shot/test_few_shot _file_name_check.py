from poly_llm.to_test.file_name_check import file_name_check

def test_file_name_check():
    assert file_name_check('my.file.txt') == 'No'
    assert file_name_check('test.py') == 'No'
    assert file_name_check('5exampl3.txt') == 'No'
    assert file_name_check('') == 'No'