from poly_llm.to_test.separate_paren_groups import separate_paren_groups
from poly_llm.to_test.parse_nested_parens import parse_nested_parens
from poly_llm.to_test.file_name_check import file_name_check
from poly_llm.common.abstract_executor import AbstractExecutor
from poly_llm.common.prompt_generator import PromptGenerator
from poly_llm.generators.llm_test_generator import LLMTestGenerator
from transformers import AutoTokenizer, T5ForConditionalGeneration
import json
from coverage import Coverage

if __name__ == '__main__':
    # Create an instance of the AbstractExecutor class
    #executor = AbstractExecutor(parse_nested_parens)
    executor = AbstractExecutor(file_name_check)
    prompt_generator = PromptGenerator(file_name_check)
    
    model_name = "Salesforce/codet5-large-ntp-py"
    tokenizer = AutoTokenizer.from_pretrained(model_name) #tokenizer#AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-Python-hf")#
    model = T5ForConditionalGeneration.from_pretrained(model_name) 

    llm_generator = LLMTestGenerator(model, tokenizer, file_name_check)
    prompt = prompt_generator.generate_prompt(few_shot_examples=['''def test_file_name_check(): \n # pragma: no cover
    assert file_name_check("example.txt") == 'Yes' # pragma: no cover \n
    assert file_name_check("1example.dll") == 'No' # pragma: no cover\n'''])
    print(prompt)
    test = llm_generator.create_test_function(prompt)

    print(test)
    # Define the inputs to be executed

    '''

    inputs = [
        "example.txt",
        "1example.dll",
        's1sdf3.asd',
        'K.dll',
        'MY16FILE3.exe',
        'His12FILE94.exe',
        '_Y.txt',
        '?aREYA.exe',
        '/this_is_valid.dll',
        'this_is_valid.wow',
    ]

    # Execute the inputs and print the results
    for input in inputs:
        #exceptions, execution_time, coverage = executor._execute_input(input)
        coverage_date = executor._execute_input(input)
        print(coverage_date)
    '''
 

