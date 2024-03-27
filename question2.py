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
model_name = "Salesforce/codet5-large-ntp-py"
tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

PUTS = [closest_integer]#, file_name_check, find_closest_elements, numerical_letter_grade, separate_paren_groups]

for PUT in PUTS:
    #delete any file that was created by the previous PUT
    try:
        filename = f"{PUT.__name__}_test_generated.py"
        os.remove(filename)
    except:
        pass

    executor = AbstractExecutor(PUT)
    prompt_generator = PromptGenerator(PUT)
    llm_generator = LLMTestGenerator(model, tokenizer, PUT)

    example_tests = []
    with open(f"poly_llm/to_test/{PUT.__name__}.py", "r") as f:
        lines = f.readlines()
        for line in lines:
            if "def test_" in line or "assert" in line:
                example_tests.append(line)
    #turn the list into a string
    example_tests = "".join(example_tests)

    # prompt = prompt_generator.generate_prompt(few_shot_examples=['''def test_closest_integer(): \n
    # assert closest_integer("10") == 10, "Test 1"  \n
    # assert closest_integer("14.5") == 15, "Test 2" \n'''])
    prompt = prompt_generator.generate_prompt(few_shot_examples=[example_tests])
    #print(f"THE PROMPT {prompt}")

    test, test_name = llm_generator.create_test_function(prompt)

    #find the last assert and it remove from the test string the last assert statement and what comes after it
    #remove any starting or trailing whitespace from the string
    test = test.strip()

    #remove the last assert from s
    test = test.split("\n")
    test = test[:-2]
    test = "\n".join(test)+'\n'

    #check if the last character is a  ) and if not add ') == 'NO'
    # if test[-1] != "'" and PUT == file_name_check:
    #     test = test.rstrip()
    #     test += "') == 'Yes'"

    filename = f"{PUT.__name__}_test_generated.py"
    llm_generator.write_test_to_file(test, filename=filename)
    module_name = filename.split(".")[0]
    function_name = test_name


    # Dynamically import the module
    module = importlib.import_module(module_name)

    #refresh the module
    module = importlib.reload(module)


    function = getattr(module, function_name)

    executor2 = AbstractExecutor(function)

    coverage_data = executor2._execute_input(PUT)
    print(PUT.__name__, coverage_data)