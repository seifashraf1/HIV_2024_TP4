import inspect
import time
import sys
from coverage import Coverage
import json
class AbstractExecutor:
    '''
    The `AbstractExecutor` class is a Python class that provides functionality for executing a program
    module and tracking code coverage.
    '''

    def __init__(self, program_module):
        self.program_module = program_module
        self.execution_data = {}
    
    def _execute_input(self, input):
        exceptions = 0
        try:
            cov = Coverage(branch=True)
            cov.start()
            #.. call your code ..
            start_time = time.time()
            self.program_module(input)
            end_time = time.time()
            cov.stop()
            cov.json_report()
            with open("coverage.json", "r") as f:
                f = json.load(f)
            coverage_data = f["totals"]
            execution_time = end_time - start_time
        except Exception as e:
            exceptions += 1
            end_time = time.time()
            execution_time = end_time - start_time

        self.execution_data = {"input": input, "exceptions": exceptions, "execution_time": execution_time, "coverage": coverage_data}

        return self.execution_data
