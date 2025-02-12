from funcs import return_att, same_list
import numpy as np
from classes import problem
from random import randint


def inputs():
    roots = [[randint(1, 100) for i in range(4)] for j in range(20)] # Creates 20 different quadratic equations in the form (ax - b)(cx-d)
    return [[a*c, -a*d - b*c, b*d] for a, b, c, d in roots] # Returns a list with the coefficients a, b, c for ax^2 + bx + c


def func_sol(a, b, c):
    """Solves the quadratic formula and returns the roots given the coefficients a, b, c"""
    
    # Solves for delta (the square root)
    delta = np.sqrt(b**2 - 4*a*c)
    
    # Solves for the two roots
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    
    return [x1, x2]


class prob1(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variables)
        self.add_prob_grade_and_comment(self.check_function)

        self.n = 2
        self.normalize_grade()

    def check_variables(self):
        roots = ['x1', 'x2']
        if any(return_att(self.module, root) == None for root in roots):
            return 0, 'No variable named "x1" or "x2"'

        return 1, ''

    def check_function(self):
        func = return_att(self.module, 'quadratic')
        if func == None:
            return 0, 'No function named quadratic.'

        inps = inputs()

        try:
            for inp in inps:
                result = same_list(func(*inp), func_sol(*inp))
                if not result:
                    return 0.5, 'The function did not return the right output.'

            return 1, ''
        except Exception as e:
            return 0, f'The function did not take the right input. Error: {str(e)}'
