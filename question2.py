from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.to_test.closest_integer import closest_integer
from poly_llm.to_test.find_closest_elements import find_closest_elements
from poly_llm.to_test.numerical_letter_grade import numerical_letter_grade
from poly_llm.to_test.separate_paren_groups import separate_paren_groups
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
import torch
import importlib
import os
from tqdm import tqdm


#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
device = torch.device("cpu")
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)


def divide_list(lst):
    n = len(lst)
    size = n // 3  # Calculate the size of each part
    parts = [lst[i * size:(i + 1) * size] for i in range(3)]  # Divide the list into three parts
    return parts

#each two examples of each PUT examples list will be used for one prompt
closest_integer_examples =[
    '''
        assert closest_integer("10") == 10, "Test 1
        assert closest_integer("14.5") == 15, "Test 2"
    ''',
    '''
        assert closest_integer("-14.5") == -15, "Test 3"
        assert closest_integer("15.3") == 15, "Test 4"
    ''',
    '''
        assert closest_integer("15.5") == 16, "Test 5"
        assrt closest_integer("1.326") == 1, "Test 6"
    '''
]

file_name_check_examples = [
    '''
        assert file_name_check("example.txt") == 'Yes'
        assert file_name_check("example.dll") == 'Yes'
    ''',
    '''
        assert file_name_check('.txt') == 'No'
        assert file_name_check('example.') == 'No'
    ''',
    '''
        assert file_name_check("example.dll") == 'Yes'
        assert file_name_check("example") == 'No'
    '''
]

find_closest_elements_examples = [
    '''
        assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    ''',
    '''
        assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    ''',
    '''
        assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
        assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.1]) == (2.0, 2.1)
    '''
]

numerical_letter_grade_examples = [
    '''
        assert numerical_letter_grade([4.0]) == ['A']
    ''',
    '''
        assert numerical_letter_grade([4.0, 3, 1.7, 2, 3.5]) == ['A+', 'B', 'C-', 'C', 'A-']
    ''',
    '''
        assert numerical_letter_grade([1.2]) == ['D+']
        assert numerical_letter_grade([4.0]) == ['A+']
    '''
]

separate_paren_groups_examples = [
    '''
        assert separate_paren_groups('(()()) ((())) () ((())()())') == ['(()())', '((()))', '()', '((())()())']
        assert separate_paren_groups('() (()) ((())) (((())))') == ['()', '(())', '((()))', '(((())))']
    ''',
    '''
        assert separate_paren_groups('((()()))') == ['((()))']
    ''',
    '''
        assert separate_paren_groups('()()((()))()') == ['()', '()', '((()))', '()']
        assert separate_paren_groups('()()((()))()((()()))') == ['()', '()', '((()))', '()', '((()()))']
    '''
]

closest_integer_parts = divide_list(closest_integer_examples)
file_name_check_parts = divide_list(file_name_check_examples)
find_closest_elements_parts = divide_list(find_closest_elements_examples)
numerical_letter_grade_parts = divide_list(numerical_letter_grade_examples)
separate_paren_groups_parts = divide_list(separate_paren_groups_examples)

PUTS = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
parts = [closest_integer_parts, file_name_check_parts, find_closest_elements_parts, numerical_letter_grade_parts, separate_paren_groups_parts]
# PUTS = [PUTS[4]]
# parts = [parts[4]]

for i in range(len(PUTS)):
    #delete any file that was created by the previous PUT
    # try:
    #     filename = f"{PUT.__name__}_test_generated.py"
    #     os.remove(filename)
    # except:
    #     pass

    executor = AbstractExecutor(PUTS[i])
    prompt_generator = PromptGenerator(PUTS[i])
    llm_generator = LLMTestGenerator(model, tokenizer, PUTS[i])

    # example_tests = []
    # with open(f"poly_llm/to_test/{PUT.__name__}.py", "r") as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         if "def test_" in line or "assert" in line:
    #             example_tests.append(line)
    # #turn the list into a string
    # example_tests = "".join(example_tests)

    prompt = prompt_generator.generate_prompt(few_shot_examples=parts[i][2])

    test, test_name = llm_generator.create_test_function(prompt)

    #find the last assert and it remove from the test string the last assert statement and what comes after it
    #remove any starting or trailing whitespace from the string
    test = test.strip()

    #remove the last assert from s
    test = test.split("\n")
    #test = test[:-2]
    test = "\n".join(test)+'\n'

    #check if the last character is a  ) and if not add ') == 'NO'
    # if test[-1] != "'" and PUT == file_name_check:
    #     test = test.rstrip()
    #     test += "') == 'Yes'"

    #filename = f"{PUTS[i].__name__}_test_generated.py"
    filename = "test_generated.py"
    llm_generator.write_test_to_file(test, filename=filename)
    module_name = filename.split(".")[0]
    function_name = test_name


    module = importlib.import_module(module_name)

    module = importlib.reload(module)


    function = getattr(module, function_name)

    executor2 = AbstractExecutor(function)

    coverage_data = executor2._execute_input(PUTS[i])
    if coverage_data is None:
        print("Coverage data is None")
        continue
    line_coverage = coverage_data['coverage']['percent_covered_display']
    print(PUTS[i].__name__, " Line Coverage: ", line_coverage)
    branch_coverage = coverage_data['coverage']['covered_branches']/coverage_data['coverage']['num_branches']
    print(PUTS[i].__name__, " Branch Coverage: ", branch_coverage)