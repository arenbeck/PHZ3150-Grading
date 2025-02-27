from funcs import return_att, same_list
from classes import problem
from random import randint
import numpy as np
import os


def func_sol(arr):
    return np.sort(arr)


def inputs():
    ret = []
    for i in range(10):
        num_items = randint(1, 100)
        ret.append(np.random.rand(num_items))
    return ret


class prob3(problem):
    def __init__(self, module):
        super().__init__(module)

        #self.add_prob_grade_and_comment(self.check_variables)
        self.add_prob_grade_and_comment(self.check_function)
        self.add_prob_grade_and_comment(self.check_extra_py_file)

        self.n = 2
        self.normalize_grade()

    def check_variables(self):
        var_sol = np.array([4,5,2,10,42,22,8,12])

        var_name = 'array'
        array = return_att(self.module, var_name)
        if array is None:
            return 0, f'No variable named {var_name}.'

        if not np.array_equal(var_sol, array):
            return 0.5, f'Variable {var_name} does not have the correct value.'

        return 1, ''

    def check_extra_py_file(self):
        og_py_files = ['prob1.py', 'funcs.py', 'prob3.py', 'prob2.py', 'prob4.py', 'classes.py', 'main.py', 'module_for_grading.py']
        files = os.listdir()
        for file in files:
            if file.endswith('.py') and file not in og_py_files:
                return 1, ''
        return 0, 'No separate .py file.'

    def check_function(self):
        func_name = 'order_array'
        func = return_att(self.module, func_name)
        if func == None:
            return 0, f'No function named {func_name}.'

        inps = inputs()

        try:
            for inp in inps:
                result = np.array_equal(func(inp),func_sol(inp))
                if not result:
                    return 0.5, f'The function {func_name} did not return the right output.'
        except Exception as e:
            return 0, f'The function {func_name} did not take the right input.\n{str(e)}'

        return 1, ''
