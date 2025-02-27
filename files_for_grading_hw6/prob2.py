from funcs import return_att, add_comment
import numpy as np
from classes import problem
from random import randint
import os


def func_sol(x, x0, y0, r):
    y_positive = np.sqrt(r**2 - (x - x0)**2) + y0
    y_negative = -np.sqrt(r**2 - (x - x0)**2) + y0
    return y_positive, y_negative


def inputs():
    x0, y0, r, x = 2, 2, 10, np.linspace(-8, 12, 201)
    return [x, x0, y0, r]


class prob2(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variables)
        self.add_prob_grade_and_comment(self.check_function)
        self.add_prob_grade_and_comment(self.check_extra_py_file)

        self.n = 3
        self.normalize_grade()

    def check_extra_py_file(self):
        og_py_files = ['prob1.py', 'funcs.py', 'prob3.py', 'prob2.py', 'prob4.py', 'classes.py', 'main.py', 'module_for_grading.py']
        files = os.listdir()
        for file in files:
            if file.endswith('.py') and file not in og_py_files:
                return 1, ''
        return 0, 'No separate .py file.'

    def check_variables(self):
        def check_single_variable(var_name, var_value):
            var = return_att(self.module, var_name)
            if var_name == None:
                return 0, f'No variable named {var_name}.'

            if type(var_value) != type(np.array([])):
                if var != var_value:
                    return 0.5, f'Variable {var_name} is not correct.'
            else:
                if not np.array_equal(var, var_value):
                    return 0.5, f'Variable {var_name} is not correct.'

            return 1, ''

        def check_multiple_variables(var_names, var_values):
            grade, comment = 0, ''
            for v_name, v_val in zip(var_names, var_values):
                g, c = check_single_variable(v_name, v_val)
                grade += g
                comment = add_comment(comment, c)

            return grade/len(var_names), comment

        inps = inputs()
        var_list = ['x', 'x0', 'y0', 'r']
        return check_multiple_variables(var_list, inps)

    def check_function(self):
        def check_outputs(out, sol):
            o1, o2 = out
            s1, s2 = sol

            arrs = [o1, o2, s1, s2]
            for arr in arrs:
                arr = np.round(arr, 3)

            for i in range(2):
                if not any(np.array_equal(arrs[i], arrs[j]) for j in range(2, 4)): return False

            return True
            
        func_name = 'circle'
        func = return_att(self.module, func_name)
        if func == None:
            return 0, f'No function named {func_name}.'

        inp = inputs()

        try:
            if not check_outputs(func(*inp), func_sol(*inp)):
                return 0.5, f'The function {func_name} did not return the right values'
        except Exception as e:
            return 0, f'The function {func_name} did not take the right input or did not return the output in the right format.\n{str(e)}'

        return 1, ''
