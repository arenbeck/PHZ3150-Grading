from funcs import return_att, same_list
from classes import problem
from random import randint
import numpy as np
import os


def func_sol(v0, t, a):
    """Calculates the displacement of a body based on the basic kinematic equation for constant 
    acceleration, given the initial displacement v0, time t, and the acceleration a"""
    
    return v0*t + 0.5*a*t**2


def inputs():
    return [[randint(-10, 10) for i in range(3)] for j in range(20)]


class prob3(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_function)
        self.add_prob_grade_and_comment(self.check_extra_py_file)

        self.n = 2
        self.normalize_grade()

    def check_extra_py_file(self):
        og_py_files = ['prob1.py', 'funcs.py', 'prob3.py', 'prob2.py', 'classes.py', 'main.py', 'module_for_grading.py']
        files = os.listdir()
        for file in files:
            if file.endswith('.py') and file not in og_py_files:
                return 1, ''
        return 0, 'No separate .py file.'

    def check_function(self):
        func_name = 'displacement'
        func = return_att(self.module, func_name)
        if func == None:
            return 0, f'No function named {func_name}.'

        inps = inputs()

        try:
            for inp in inps:
                result = func(*inp) == func_sol(*inp)
                if not result:
                    return 0.5, 'The function did not return the right output.'
            return 1, ''
        except Exception as e:
            return 0, f'The function did not take the right input. Error: {str(e)}'
