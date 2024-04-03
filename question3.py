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

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#model_name = "Salesforce/codet5-large-ntp-py"
model_name = "Salesforce/codet5p-770m-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)


#each two examples of each PUT examples list will be used for one prompt
closest_integer_examples = '''
      def test_closet_interger():
        assert closest_integer("10") == 10, "Test 1
        assert closest_integer("14.5") == 15, "Test 2"
    '''

file_name_check_examples = '''
      def test_file_name_check():
        assert file_name_check("example.dll") == 'Yes'
        assert file_name_check("example") == 'No'
    '''

find_closest_elements_examples = '''
      def test_find_closest_elements():
        assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    '''

numerical_letter_grade_examples = '''
      def test_numerical_letter_grade():
        assert numerical_letter_grade([1.2]) == ['D+']
        assert numerical_letter_grade([4.0]) == ['A+']
    '''

separate_paren_groups_examples = '''
      def test_separate_paren_groups():
        assert separate_paren_groups('()()((()))()') == ['()', '()', '((()))', '()']
        assert separate_paren_groups('()()((()))()((()()))') == ['()', '()', '((()))', '()', '((()()))']
    '''

PUTS = [closest_integer, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]
parts = [closest_integer_examples, file_name_check_examples, find_closest_elements_examples, numerical_letter_grade_examples, separate_paren_groups_examples]


for i in range(len(PUTS)):
    executor = AbstractExecutor(PUTS[i])
    prompt_generator = PromptGenerator(PUTS[i])
    llm_generator = LLMTestGenerator(model, tokenizer, PUTS[i])

    prompt = prompt_generator.generate_prompt(few_shot_examples=[parts[i]])

    # inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=512).to(device)

    # outputs = model.generate(input_ids=inputs.input_ids, attention_mask=inputs.attention_mask)
    # print(outputs)
    # break
    # Decode the generated output
    #test = tokenizer.decode(outputs[0], skip_special_tokens=True)

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