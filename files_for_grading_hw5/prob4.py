from funcs import return_att, same_list
from classes import problem
from random import randint
import numpy as np
import os


def inputs():
    return "one two three four five six six six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen".split()


def func_sol(your_number):
    """Takes an english numerical word and gives you the corresponding number (1-20).
    Input: english name of number
    Output: number """

    word_to_num = {}  # dict()

    word_to_num['zero'] = 0
    word_to_num['one'] = 1
    word_to_num['two'] = 2
    word_to_num['three'] = 3
    word_to_num['four'] = 4
    word_to_num['five'] = 5
    word_to_num['six'] = 6
    word_to_num['seven'] = 7
    word_to_num['eight'] = 8
    word_to_num['nine'] = 9
    word_to_num['ten'] = 10
    word_to_num['eleven'] = 11
    word_to_num['twelve'] = 12
    word_to_num['thirteen'] = 13
    word_to_num['fourteen'] = 14
    word_to_num['fifteen'] = 15
    word_to_num['sixteen'] = 16
    word_to_num['seventeen'] = 17
    word_to_num['eightteen'] = 18
    word_to_num['nineteen'] = 19
    word_to_num['twenty'] = 20

    return word_to_num[your_number.lower()]


class prob4(problem):

    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_function)

    def check_function(self):
        grade = 15
        comment = ""

        func_name = 'word_to_number'
        func = return_att(self.module, func_name)
        if func != None:
            if func.__doc__ is None:
                comment += f'Function {func_name} has no docstring.'
                grade -= 1

            #not checking if function has a dictionary in it: (5 points)

            #check func returns against func_sol

            # generate inputs
            inps = inputs()

            try:
                gr = 2
                for inp in inps:
                    result = func(inp) == func_sol(inp)
                    if not result:
                        comment += 'The function did not return the right number.\n'
                        gr = 1
                grade -= gr

            except:
                comment += 'The function did not run without errors.\n'
                grade -= 2

            # not checking for function call: (2 points)
            # not checking code for comments: (1 point)

        else:
            grade -= 15
            comment += f'No function named {func_name}.\n'

        return grade, comment
