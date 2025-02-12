from funcs import return_att, same_list
import numpy as np
from classes import problem
from random import randint


def func_sol(student_height):
    """Calulates the height of a student in in m and cm
    It takes a list [ft, in] and return a list [m, cm]"""
    
    ft = student_height[0]
    inch = student_height[1]
    
    total_m_height = ft * 0.3048 + inch * 0.0254
    m_height = int(total_m_height)
    cm_height = np.ceil((total_m_height - m_height)*100)
    
    return [m_height, cm_height]


def inputs():
    return [[randint(0, 11) for i in range(2)] for j in range(20)]


class prob2(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variable)
        self.add_prob_grade_and_comment(self.check_function)

        self.n = 2
        self.normalize_grade()

    def check_variable(self):
        student_h = return_att(self.module, 'student_h')
        if type(student_h) != type([]):
            return 0.5, 'Variable student_h is not a list.'

        if student_h == None:
            return 0, 'No variable named student_h'

        if student_h != [[5, 1], [4, 10], [6, 2], [5, 7], [6, 11]]:
            return 0.5, 'Variable student_h is not correct.'

        return 1, ''

    def check_function(self):
        func = return_att(self.module, 'ft_to_m')
        if func == None:
            return 0, 'No function named ft_to_m.'

        inps = inputs()

        try:
            for inp in inps:
                result = same_list(func(inp), func_sol(inp))
                if not result:
                    return 0.5, 'The function did not return the right output.'

            return 1, ''
        except Exception as e:
            return 0, f'The function did not take the right input. Error: {str(e)}'
