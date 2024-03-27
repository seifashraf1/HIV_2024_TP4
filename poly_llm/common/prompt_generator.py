
from typing import Callable, Optional, List
import inspect
import re

class PromptGenerator:
    def __init__(self, function_to_test: Callable):
        self._function_to_test = function_to_test
        self._func_name = self._function_to_test.__name__
        self._lines, _ = inspect.getsourcelines(self._function_to_test)
        self._lines = "".join(self._lines)

    def generate_prompt(self, few_shot_examples: Optional[List[str]] = None):
        """Generate a prompt for the given function."""
        self._few_shot_examples = few_shot_examples
        #prompt = f"Generate tests for the function {self._func_name} \n "
        #prompt = f"Write tests for the function {self._func_name} and follow the example tests provided \n"
        prompt = f"Generate tests for the function {self._func_name} and follow the example tests provided to maximize coverage \n"
        #prompt = f"Write tests for the function {self._func_name} and follow the example tests provided to maximize coverage and use the description of the function to generate valid tests\n"
        if self._few_shot_examples:

            for example in self._few_shot_examples:

                prompt += "Code \n"
                prompt += f"{self._lines}\n"
                prompt += "Test \n"
                prompt += f"{example}\n"

        #print(f"Lines {self._lines}")
        prompt += "Code \n"
        prompt += f"{self._lines}\n"
        prompt += "Test \n"
        prompt += f"def test_{self._func_name}():\n"

        final_prompt = ''.join(prompt)
        comment_regex = r'""".*?"""'
        final_prompt = re.sub(comment_regex, '', final_prompt, flags=re.DOTALL)

        return final_prompt
